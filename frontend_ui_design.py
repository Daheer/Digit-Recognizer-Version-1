        # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Neural_Final.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import datetime
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPainterPath, QPainter, QPen
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog
from backend_neural_network import callpre, callpredict

# saved = False
saved_d = ''
defualt = "Capture.PNG"

class Drawer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # self.setAttribute(WA_StaticContents)
        h = 280
        w = 280
        self.myPenWidth = 45
        self.myPenColor = Qt.white
        self.image = QImage(w, h, QImage.Format_RGB32)
        # self.image.fill(Qt.black)
        self.path = QPainterPath()
        self.clearImage()

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.path = QPainterPath()
        self.image.fill(Qt.black)  ## switch it to else
        self.update()

    def saveImage(self, fileName, fileFormat):
        self.image.save(fileName, fileFormat)
        self.predict()

    def predict(self):
        # print(x)
        prediction = callpredict()
        dlg = QMessageBox(self)
        dlg = QMessageBox()
        dlg.setWindowTitle('Prediction')
        dlg.setText(f'You drew a {int(prediction)}')
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print('Prediction Complete')

    def predictSaved(self):
        prediction = callpredict()
        dlg = QMessageBox(self)
        dlg = QMessageBox()
        dlg.setWindowTitle('Prediction')
        dlg.setText(f'You drew a {int(prediction)}')
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print('Prediction Complete')


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image, self.rect())

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        p = QPainter(self.image)
        p.setPen(QPen(self.myPenColor,
                      self.myPenWidth, Qt.SolidLine, Qt.RoundCap,
                      Qt.RoundJoin))
        p.drawPath(self.path)
        p.end()
        self.update()

    def sizeHint(self):
        return QSize(300, 300)


def saveImage():
    # selecting file path
    filePath, _ = QFileDialog.getOpenFileName(Drawer(), "Open Image", "",
                                              "JPEG(*.jpg *.jpeg);;PNG(*.png);;All Files(*.*) ")

    # if file path is blank return back
    if filePath == "":
        return

    saved = True
    saved_d = filePath

    if saved:
        global defualt
        defualt = f"{saved_d}"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QtCore.QSize(400, 510))
        MainWindow.setStyleSheet("background-color: rgb(125, 125, 125);")

        # widgets
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tab Widgets
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 511))
        self.tabWidget.setStyleSheet("font: 75 14pt \"Consolas\";\n"
                                     "\n"
                                     "")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab.setAutoFillBackground(False)
        self.tab.setStyleSheet("QTabWidget{background-color: rgb(74, 76, 92);}")
        self.tab.setObjectName("tab")

        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 20, 321, 351))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")


        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 394, 121, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    font: 12pt \"Consolas\";\n"
                                        "    background-color: rgb(74, 76, 92);\n"
                                        "    border: 2px solid;\n"
                                        "    border-color: rgb(255, 255, 255);\n"
                                        "    color:rgb(255, 255, 255);\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:rgb(182, 137, 73)\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(40, 394, 121, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    font: 12pt \"Consolas\";\n"

                                      "    background-color: rgb(74, 76, 92);\n"
                                      "    border: 2px solid;\n"
                                      "    border-color: rgb(255, 255, 255);\n"
                                      "    color:rgb(255, 255, 255);\n"
                                      "    border-radius: 10px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: rgb(0, 0, 0);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color:rgb(182, 137, 73)\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "Import Image")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 400, 121, 41))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    font: 12pt \"Consolas\";\n"
                                        "    background-color: rgb(74, 76, 92);\n"
                                        "    border: 2px solid;\n"
                                        "    border-color: rgb(255, 255, 255);\n"
                                        "    color:rgb(255, 255, 255);\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:rgb(182, 137, 73)\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 400, 121, 41))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    font: 12pt \"Consolas\";\n"
                                        "    background-color: rgb(74, 76, 92);\n"
                                        "    border: 2px solid;\n"
                                        "    border-color: rgb(255, 255, 255);\n"
                                        "    color:rgb(255, 255, 255);\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(0, 0, 0);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:rgb(182, 137, 73)\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.draw = Drawer(self.widget)

        self.widget.setGeometry(QtCore.QRect(70, 70, 280, 280))
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(lambda: saveImage())
        self.pushButton_2.clicked.connect(lambda: self.draw.predictSaved())
        self.pushButton_3.clicked.connect(lambda: self.draw.clearImage())
        self.pushButton_4.clicked.connect(lambda: self.draw.saveImage("image.jpg","JPEG"))


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def changePx(self):
        self.label.setPixmap(QtGui.QPixmap(defualt))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "0/1 Recognizer"))
        self.pushButton_2.setText(_translate("MainWindow", "Predict"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.pushButton_4.setText(_translate("MainWindow", "Predict"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Draw Image"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    def update_label():
        current_time = str(datetime.datetime.now().time())
        ui.label.setPixmap(QtGui.QPixmap(defualt))


    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(1000)  # every 1000 milliseconds

    sys.exit(app.exec_())
