# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sobre.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_Voltar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_Voltar.setGeometry(QtCore.QRect(310, 310, 101, 51))
        self.bt_Voltar.setObjectName("bt_Voltar")
        self.lb_Fundo = QtWidgets.QLabel(self.centralwidget)
        self.lb_Fundo.setGeometry(QtCore.QRect(390, 320, 51, 31))
        self.lb_Fundo.setObjectName("lb_Fundo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 310, 54, 54))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imagens/python_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 310, 54, 54))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagens/spyder_logo.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 310, 54, 54))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("imagens/qt_logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 310, 54, 54))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("imagens/arduino_logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 310, 54, 54))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("imagens/ufu_logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 81, 81))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("imagens/icone.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(123, 20, 251, 24))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 60, 301, 52))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(120, 240, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(120, 200, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.lbEmail = QtWidgets.QLabel(self.centralwidget)
        self.lbEmail.setGeometry(QtCore.QRect(200, 275, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.lbEmail.setFont(font)
        self.lbEmail.setAutoFillBackground(False)
        self.lbEmail.setScaledContents(False)
        self.lbEmail.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lbEmail.setWordWrap(True)
        self.lbEmail.setObjectName("lbEmail")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 130, 301, 48))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(200, 250, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.lb_Fundo.raise_()
        self.bt_Voltar.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.lbEmail.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sobre"))
        self.bt_Voltar.setText(_translate("MainWindow", "Voltar"))
        self.lb_Fundo.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Sobre Sistema de Relatórios"))
        self.label_8.setText(_translate("MainWindow", "Sistema envolvendo hardware para aquisição de sinais elétricos e software para tratamento de dados e auxílio na tomada de decisões."))
        self.label_9.setText(_translate("MainWindow", "Created by: Leonardo Pedrassoli Silva"))
        self.label_10.setText(_translate("MainWindow", "Última modificação: 08/08/2018"))
        self.lbEmail.setText(_translate("MainWindow", "leopedrassoli@ufu.br"))
        self.label_11.setText(_translate("MainWindow", "Software para visualização de gráficos e geração de relatórios baseados nos dados coletados e em períodos de tempo especificados."))
        self.label_12.setText(_translate("MainWindow", "Engenharia de Computação"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

