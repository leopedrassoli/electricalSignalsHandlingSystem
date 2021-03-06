# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(502, 635)
        icon = QtGui.QIcon.fromTheme("icon")
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gbGrafico = QtWidgets.QGroupBox(self.centralwidget)
        self.gbGrafico.setGeometry(QtCore.QRect(30, 360, 211, 131))
        self.gbGrafico.setObjectName("gbGrafico")
        self.rb_Separado = QtWidgets.QRadioButton(self.gbGrafico)
        self.rb_Separado.setGeometry(QtCore.QRect(20, 16, 69, 31))
        self.rb_Separado.setChecked(True)
        self.rb_Separado.setObjectName("rb_Separado")
        self.rb_Juntos = QtWidgets.QRadioButton(self.gbGrafico)
        self.rb_Juntos.setGeometry(QtCore.QRect(110, 16, 49, 31))
        self.rb_Juntos.setChecked(False)
        self.rb_Juntos.setObjectName("rb_Juntos")
        self.bt_Grafico = QtWidgets.QPushButton(self.gbGrafico)
        self.bt_Grafico.setGeometry(QtCore.QRect(20, 90, 171, 23))
        self.bt_Grafico.setObjectName("bt_Grafico")
        self.cb_Potencia = QtWidgets.QCheckBox(self.gbGrafico)
        self.cb_Potencia.setGeometry(QtCore.QRect(110, 60, 70, 31))
        self.cb_Potencia.setObjectName("cb_Potencia")
        self.cb_Corrente = QtWidgets.QCheckBox(self.gbGrafico)
        self.cb_Corrente.setGeometry(QtCore.QRect(20, 40, 70, 31))
        self.cb_Corrente.setObjectName("cb_Corrente")
        self.cb_Tensao = QtWidgets.QCheckBox(self.gbGrafico)
        self.cb_Tensao.setGeometry(QtCore.QRect(20, 60, 70, 31))
        self.cb_Tensao.setObjectName("cb_Tensao")
        self.cb_Temperatura = QtWidgets.QCheckBox(self.gbGrafico)
        self.cb_Temperatura.setGeometry(QtCore.QRect(110, 40, 91, 31))
        self.cb_Temperatura.setObjectName("cb_Temperatura")
        self.gbTipo = QtWidgets.QGroupBox(self.centralwidget)
        self.gbTipo.setEnabled(True)
        self.gbTipo.setGeometry(QtCore.QRect(260, 220, 211, 131))
        self.gbTipo.setObjectName("gbTipo")
        self.rb_Completo = QtWidgets.QRadioButton(self.gbTipo)
        self.rb_Completo.setGeometry(QtCore.QRect(20, 20, 82, 31))
        self.rb_Completo.setChecked(True)
        self.rb_Completo.setObjectName("rb_Completo")
        self.rb_Periodo = QtWidgets.QRadioButton(self.gbTipo)
        self.rb_Periodo.setGeometry(QtCore.QRect(20, 40, 82, 31))
        self.rb_Periodo.setObjectName("rb_Periodo")
        self.dt_Final = QtWidgets.QDateTimeEdit(self.gbTipo)
        self.dt_Final.setEnabled(False)
        self.dt_Final.setGeometry(QtCore.QRect(50, 100, 128, 20))
        self.dt_Final.setObjectName("dt_Final")
        self.label_6 = QtWidgets.QLabel(self.gbTipo)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 26, 20))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.gbTipo)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 29, 21))
        self.label_5.setObjectName("label_5")
        self.dt_Inicio = QtWidgets.QDateTimeEdit(self.gbTipo)
        self.dt_Inicio.setEnabled(False)
        self.dt_Inicio.setGeometry(QtCore.QRect(50, 70, 128, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.dt_Inicio.setFont(font)
        self.dt_Inicio.setProperty("showGroupSeparator", False)
        self.dt_Inicio.setObjectName("dt_Inicio")
        self.gbArquivo = QtWidgets.QGroupBox(self.centralwidget)
        self.gbArquivo.setGeometry(QtCore.QRect(30, 220, 211, 131))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.gbArquivo.setFont(font)
        self.gbArquivo.setObjectName("gbArquivo")
        self.bt_Abrir = QtWidgets.QPushButton(self.gbArquivo)
        self.bt_Abrir.setGeometry(QtCore.QRect(20, 30, 171, 41))
        self.bt_Abrir.setObjectName("bt_Abrir")
        self.labelFinal = QtWidgets.QLabel(self.gbArquivo)
        self.labelFinal.setGeometry(QtCore.QRect(20, 100, 171, 16))
        self.labelFinal.setObjectName("labelFinal")
        self.labelInicio = QtWidgets.QLabel(self.gbArquivo)
        self.labelInicio.setGeometry(QtCore.QRect(20, 80, 171, 16))
        self.labelInicio.setObjectName("labelInicio")
        self.gbRelatorio = QtWidgets.QGroupBox(self.centralwidget)
        self.gbRelatorio.setGeometry(QtCore.QRect(260, 360, 211, 131))
        self.gbRelatorio.setObjectName("gbRelatorio")
        self.bt_GerarRelatorio = QtWidgets.QPushButton(self.gbRelatorio)
        self.bt_GerarRelatorio.setGeometry(QtCore.QRect(20, 30, 171, 41))
        self.bt_GerarRelatorio.setAutoDefault(False)
        self.bt_GerarRelatorio.setDefault(False)
        self.bt_GerarRelatorio.setFlat(False)
        self.bt_GerarRelatorio.setObjectName("bt_GerarRelatorio")
        self.bt_Sair = QtWidgets.QPushButton(self.gbRelatorio)
        self.bt_Sair.setGeometry(QtCore.QRect(20, 82, 171, 31))
        self.bt_Sair.setObjectName("bt_Sair")
        self.progressBarLeitura = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarLeitura.setGeometry(QtCore.QRect(140, 500, 331, 41))
        self.progressBarLeitura.setProperty("value", 0)
        self.progressBarLeitura.setObjectName("progressBarLeitura")
        self.progressBarProcessamento = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarProcessamento.setGeometry(QtCore.QRect(140, 550, 331, 41))
        self.progressBarProcessamento.setProperty("value", 0)
        self.progressBarProcessamento.setObjectName("progressBarProcessamento")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 510, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 560, 77, 21))
        self.label_2.setObjectName("label_2")
        self.lb_image = QtWidgets.QLabel(self.centralwidget)
        self.lb_image.setGeometry(QtCore.QRect(0, 20, 501, 191))
        self.lb_image.setText("")
        self.lb_image.setPixmap(QtGui.QPixmap("./src/img/logo.png"))
        self.lb_image.setScaledContents(True)
        self.lb_image.setObjectName("lb_image")
        self.lbFundo = QtWidgets.QLabel(self.centralwidget)
        self.lbFundo.setGeometry(QtCore.QRect(0, 200, 501, 391))
        self.lbFundo.setText("")
        self.lbFundo.setPixmap(QtGui.QPixmap("./src/img/fundo.png"))
        self.lbFundo.setScaledContents(True)
        self.lbFundo.setObjectName("lbFundo")
        self.lbFundo.raise_()
        self.gbGrafico.raise_()
        self.gbTipo.raise_()
        self.gbArquivo.raise_()
        self.gbRelatorio.raise_()
        self.progressBarLeitura.raise_()
        self.progressBarProcessamento.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lb_image.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 21))
        self.menubar.setObjectName("menubar")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionSobre = QtWidgets.QAction(mainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.menuSobre.addSeparator()
        self.menuSobre.addAction(self.actionSobre)
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.bt_Abrir, self.rb_Completo)
        mainWindow.setTabOrder(self.rb_Completo, self.rb_Periodo)
        mainWindow.setTabOrder(self.rb_Periodo, self.dt_Inicio)
        mainWindow.setTabOrder(self.dt_Inicio, self.dt_Final)
        mainWindow.setTabOrder(self.dt_Final, self.rb_Separado)
        mainWindow.setTabOrder(self.rb_Separado, self.rb_Juntos)
        mainWindow.setTabOrder(self.rb_Juntos, self.cb_Corrente)
        mainWindow.setTabOrder(self.cb_Corrente, self.cb_Tensao)
        mainWindow.setTabOrder(self.cb_Tensao, self.cb_Potencia)
        mainWindow.setTabOrder(self.cb_Potencia, self.bt_Grafico)
        mainWindow.setTabOrder(self.bt_Grafico, self.bt_GerarRelatorio)
        mainWindow.setTabOrder(self.bt_GerarRelatorio, self.bt_Sair)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Sistema de Relatórios"))
        self.gbGrafico.setTitle(_translate("mainWindow", "Gráfico(s):"))
        self.rb_Separado.setText(_translate("mainWindow", "Separado"))
        self.rb_Juntos.setText(_translate("mainWindow", "Único"))
        self.bt_Grafico.setText(_translate("mainWindow", "Visualizar"))
        self.cb_Potencia.setText(_translate("mainWindow", "Potência"))
        self.cb_Corrente.setText(_translate("mainWindow", "Corrente"))
        self.cb_Tensao.setText(_translate("mainWindow", "Tensão"))
        self.cb_Temperatura.setText(_translate("mainWindow", "Temperatura"))
        self.gbTipo.setTitle(_translate("mainWindow", "Tipo de relatório:"))
        self.rb_Completo.setText(_translate("mainWindow", "Completo"))
        self.rb_Periodo.setText(_translate("mainWindow", "Período:"))
        self.dt_Final.setDisplayFormat(_translate("mainWindow", "dd/MM/yyyy HH:mm:ss"))
        self.label_6.setText(_translate("mainWindow", "Final:"))
        self.label_5.setText(_translate("mainWindow", "Início:"))
        self.dt_Inicio.setDisplayFormat(_translate("mainWindow", "dd/MM/yyyy HH:mm:ss"))
        self.gbArquivo.setTitle(_translate("mainWindow", "Arquivo:"))
        self.bt_Abrir.setText(_translate("mainWindow", "Abrir"))
        self.labelFinal.setText(_translate("mainWindow", "Final: "))
        self.labelInicio.setText(_translate("mainWindow", "Início:"))
        self.gbRelatorio.setTitle(_translate("mainWindow", "Relatório:"))
        self.bt_GerarRelatorio.setText(_translate("mainWindow", "Gerar"))
        self.bt_Sair.setText(_translate("mainWindow", "Sair"))
        self.label.setText(_translate("mainWindow", "Leitura do arquivo:"))
        self.label_2.setText(_translate("mainWindow", "Processamento:"))
        self.menuSobre.setTitle(_translate("mainWindow", "Ajuda"))
        self.actionSobre.setText(_translate("mainWindow", "Sobre"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
