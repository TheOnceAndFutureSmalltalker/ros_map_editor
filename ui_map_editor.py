# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MapEditor_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapEditor(object):
    def setupUi(self, MapEditor):
        MapEditor.setObjectName("MapEditor")
        MapEditor.resize(939, 747)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MapEditor.sizePolicy().hasHeightForWidth())
        MapEditor.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MapEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(200, 200))
        self.label_2.setBaseSize(QtCore.QSize(100, 100))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setText("")
        
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)



        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.filename_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filename_lbl.sizePolicy().hasHeightForWidth())
        self.filename_lbl.setSizePolicy(sizePolicy)
        self.filename_lbl.setObjectName("filename_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.filename_lbl)
        self.width_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width_lbl.sizePolicy().hasHeightForWidth())
        self.width_lbl.setSizePolicy(sizePolicy)
        self.width_lbl.setObjectName("width_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.width_lbl)
        self.height_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_lbl.sizePolicy().hasHeightForWidth())
        self.height_lbl.setSizePolicy(sizePolicy)
        self.height_lbl.setObjectName("height_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.height_lbl)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.cell_lbl = QtWidgets.QLabel(self.centralwidget)
        self.cell_lbl.setObjectName("cell_lbl")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cell_lbl)
        self.horizontalLayout.addLayout(self.formLayout)

        # color box label
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)

        # color box
        self.colorBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorBox.sizePolicy().hasHeightForWidth())
        self.colorBox.setSizePolicy(sizePolicy)
        self.colorBox.setObjectName("colorBox")
        self.horizontalLayout.addWidget(self.colorBox)

        # zoom box label
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        # zoom box
        self.zoomBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomBox.sizePolicy().hasHeightForWidth())
        self.zoomBox.setSizePolicy(sizePolicy)
        self.zoomBox.setObjectName("zoomBox")
        self.horizontalLayout.addWidget(self.zoomBox)

        # close button
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
       
        # save button
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # menu bar
        MapEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MapEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 939, 21))
        self.menubar.setObjectName("menubar")
        MapEditor.setMenuBar(self.menubar)

        # status bar
        self.statusbar = QtWidgets.QStatusBar(MapEditor)
        self.statusbar.setObjectName("statusbar")
        MapEditor.setStatusBar(self.statusbar)

        self.retranslateUi(MapEditor)
        QtCore.QMetaObject.connectSlotsByName(MapEditor)

    def retranslateUi(self, MapEditor):
        _translate = QtCore.QCoreApplication.translate
        MapEditor.setWindowTitle(_translate("MapEditor", "MainWindow"))
        self.label.setText(_translate("MapEditor", "Zoom"))
        self.closeButton.setText(_translate("MapEditor", "Close"))
        
        self.saveButton.setText(_translate("MapEditor", "Save"))
        self.label_3.setText(_translate("MapEditor", "File"))
        self.label_4.setText(_translate("MapEditor", "Width"))
        self.label_5.setText(_translate("MapEditor", "Height"))
        self.filename_lbl.setText(_translate("MapEditor", "TextLabel"))
        self.width_lbl.setText(_translate("MapEditor", "TextLabel"))
        self.height_lbl.setText(_translate("MapEditor", "TextLabel"))
        self.label_9.setText(_translate("MapEditor", "Cell"))
        self.cell_lbl.setText(_translate("MapEditor", "TextLabel"))
        self.label_11.setText(_translate("MapEditor", "Color"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MapEditor = QtWidgets.QMainWindow()
    ui = Ui_MapEditor()
    ui.setupUi(MapEditor)
    MapEditor.show()
    sys.exit(app.exec_())

