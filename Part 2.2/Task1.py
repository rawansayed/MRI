# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.All = QtWidgets.QFrame(self.centralwidget)
        self.All.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.All.setFrameShadow(QtWidgets.QFrame.Raised)
        self.All.setObjectName("All")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.All)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Widgets = QtWidgets.QFrame(self.All)
        self.Widgets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Widgets.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Widgets.setObjectName("Widgets")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Widgets)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Widget1 = QtWidgets.QFrame(self.Widgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(150)
        sizePolicy.setHeightForWidth(self.Widget1.sizePolicy().hasHeightForWidth())
        self.Widget1.setSizePolicy(sizePolicy)
        self.Widget1.setMinimumSize(QtCore.QSize(0, 150))
        self.Widget1.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.Widget1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Widget1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Widget1.setObjectName("Widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.Widget1)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = ImageView(self.Widget1)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_1 = ImageView(self.Widget1)
        self.widget_1.setAutoFillBackground(True)
        self.widget_1.setObjectName("widget_1")
        self.gridLayout.addWidget(self.widget_1, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.Widget1, 0, 0, 1, 1)
        self.Widget2 = QtWidgets.QFrame(self.Widgets)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(150)
        sizePolicy.setHeightForWidth(self.Widget2.sizePolicy().hasHeightForWidth())
        self.Widget2.setSizePolicy(sizePolicy)
        self.Widget2.setMinimumSize(QtCore.QSize(0, 150))
        self.Widget2.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.Widget2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Widget2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Widget2.setObjectName("Widget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Widget2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = PlotWidget(self.Widget2)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.Widget2, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.Widgets, 0, 0, 1, 1)
        self.control = QtWidgets.QFrame(self.All)
        self.control.setMaximumSize(QtCore.QSize(500, 16777215))
        self.control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.control.setObjectName("control")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.control)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.control)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.control)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.control, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.All, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 587, 26))
        self.menubar.setObjectName("menubar")
        self.Open = QtWidgets.QMenu(self.menubar)
        self.Open.setObjectName("Open")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Image = QtWidgets.QAction(MainWindow)
        self.Image.setObjectName("Image")
        self.Open.addAction(self.Image)
        self.menubar.addAction(self.Open.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Phase"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Real"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.pushButton.setText(_translate("MainWindow", "Graph"))
        self.Open.setTitle(_translate("MainWindow", "Open"))
        self.Image.setText(_translate("MainWindow", "Image"))
from pyqtgraph import ImageView, PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
