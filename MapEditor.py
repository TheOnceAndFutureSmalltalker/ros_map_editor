from PyQt5 import QtCore, QtGui, QtWidgets, uic

from ui_map_editor import Ui_MapEditor

from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

import math
import yaml
from PIL import Image
import sys
import os


class MapEditor(QtWidgets.QMainWindow):
    def __init__(self, fn):
        super(MapEditor, self).__init__()

        # two approaches to integrating tool generated ui file shown below
        
        # setup user interface directly from ui file
        #uic.loadUi('UI_MapEditor.ui', self)

        # setup user interface from py module converted from ui file
        self.ui = Ui_MapEditor()
        self.ui.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.setMinimumSize(600, 600)

        self.ui.zoomBox.addItem("100 %", 1)
        self.ui.zoomBox.addItem("200 %", 2)
        self.ui.zoomBox.addItem("400 %", 4)
        self.ui.zoomBox.addItem("800 %", 8)
        self.ui.zoomBox.addItem("1600 %", 16)
        self.ui.zoomBox.currentIndexChanged.connect(self.handleZoom)

        self.read(fn)

        view_width = self.frameGeometry().width()
        #view_height = self.frameGeometry.height()

        self.min_multiplier = math.ceil(view_width / self.map_width_cells)
        self.zoom = 1
        self.pixels_per_cell = self.min_multiplier * self.zoom 

        self.draw_map()
        
        self.scene.mousePressEvent = self.mapClick
        self.ui.closeButton.clicked.connect(self.closeEvent)
        self.ui.saveButton.clicked.connect(self.saveEvent)


    def handleZoom(self, index):
        self.zoom = self.ui.zoomBox.currentData()
        self.pixels_per_cell = self.min_multiplier * self.zoom 
        self.draw_map()
        pass


    def read(self, fn):
        # try to open as fn or fn.pgm
        try:
            self.im = Image.open(fn, mode='rw')
            self.fn = fn
        except:
            fnpgm = fn + '.pgm'
            try:
                self.im = Image.open(fnpgm)
                self.fn = fnpgm
            except:
                print(f"ERROR:  Cannot open file {fn} or {fnpgm}.")
                sys.exit(1)

        if self.im.format != 'PPM':
            print("ERROR:  This is not a PGM formatted file.")
            sys.exit(1)

        if self.im.mode != 'L':
            print("ERROR:  This PGM file is not of mode L.")
            sys.exit(1)           

        self.map_width_cells = self.im.size[0]
        self.map_height_cells = self.im.size[1]

        fn_yaml = os.path.splitext(fn)[0] + '.yaml'
        try:
            stream = open(fn_yaml, "r")
            docs = yaml.load_all(stream)
            for doc in docs:
                self.occupied_thresh = doc['occupied_thresh']  # probability its occupied
                self.free_thresh = doc['free_thresh']  # probability its uncertain or occupied
                self.resolution = doc['resolution']    # in meters per cell
                self.origin_x = doc['origin'][0]
                self.origin_y = doc['origin'][1]
        except:
            print(f"ERROR:  Corresponding YAML file {fn_yaml} is missing or incorrectly formatted.")
            sys.exit(1) 


    def mapClick(self, event):
        # get current model value
        x = math.floor(event.scenePos().x() / self.pixels_per_cell)
        y = math.floor(event.scenePos().y() / self.pixels_per_cell)
        val = self.im.getpixel((x,y))

        # determine next value in sequence white->black->gray
        if val <= (255.0 * (1.0 - self.occupied_thresh)):  # if black, become gray
            val = 200
        elif val <= (255.0 * (1.0 - self.free_thresh)):  # else if gray, become white
            val = 255
        else:  # else its white, become black
            val = 0    

        # update model with new value
        self.im.putpixel((x,y), val)    

        # redraw cell in new color
        color = self.value2color(val)
        self.color_cell(x, y, color)


    def value2color(self, val):
        if val > (255.0 * (1.0 - self.free_thresh)):
            return Qt.white
        elif val > (255.0 * (1.0 - self.occupied_thresh)):
            return Qt.gray
        else:
            return Qt.black

        
    def color_cell(self, x, y, color):
        pen = QPen(color)
        pen.setWidth(1)
        if self.pixels_per_cell > 10:
            pen = QPen(Qt.lightGray)
        brush = QBrush(color)
        x = x * self.pixels_per_cell
        y = y * self.pixels_per_cell
        self.scene.addRect(x, y, self.pixels_per_cell, self.pixels_per_cell, pen, brush)


    def draw_map(self):
        
        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        # draw the cells
        self.scene.clear()
        for x in range(0,self.map_width_cells):
            for y in range(0, self.map_height_cells):
                val = self.im.getpixel((x,y))
                color = self.value2color(val)
                self.color_cell(x,y,color)

        # draw the grid lines
        if self.pixels_per_cell > 10:
            pen = QPen(Qt.lightGray)
            pen.setWidth(1)
            pixel_width = self.map_width_cells * self.pixels_per_cell
            pixel_height =self. map_height_cells * self.pixels_per_cell
            for x in range(0, pixel_width, self.pixels_per_cell):
                self.scene.addLine(x, 0, x, pixel_height, pen)
            for y in range(0, pixel_height, self.pixels_per_cell):
                self.scene.addLine(0, y, pixel_width, y, pen)
        

    def closeEvent(self, event):
        self.close()


    def saveEvent(self, event):
        self.im.save("map_old.pgm")
        #self.im.save(self.fn)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('ERROR:  Must provide map file name - with or without .pgm extension.')
        print()
        print('     $ python MapEditor.py map_file_name')
        print()
    app = QtWidgets.QApplication(sys.argv)
    window = MapEditor(sys.argv[1])
    window.show()
    sys.exit(app.exec_())
