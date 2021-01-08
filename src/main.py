from PyQt5 import QtWidgets, QtGui, QtCore, sip
from PyQt5.QtWidgets import QWidget, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence, QPixmap
import sys, os

import interface.py.main_window as mw
import interface.py.sobre as sb
import values_to_grafico as vtg
import gerarRelatorio as gr

icone = "./src/img/icone.png"
fundo = "./src/img/fundo.png"
logos = "./src/img/logos.png"


class MainWindow(QtWidgets.QMainWindow, mw.Ui_mainWindow):
    global progressBar

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(icone)))
        self.setFixedSize(self.size())
        self.atalhoAbrir = QShortcut(QKeySequence("Ctrl+A"), self)
        self.atalhoAbrir.activated.connect(self.Abrir)
        self.bt_Abrir.clicked.connect(self.Abrir)
        self.bt_Sair.clicked.connect(self.sair)
        self.atalhoGrafico = QShortcut(QKeySequence("Ctrl+G"), self)
        self.atalhoGrafico.activated.connect(self.Grafico)
        self.bt_Grafico.clicked.connect(self.Grafico)
        self.gbTipo.setEnabled(True)
        self.rb_Periodo.clicked.connect(self.dt_Inicio.setEnabled)
        self.rb_Periodo.clicked.connect(self.dt_Final.setEnabled)
        self.rb_Periodo.clicked.connect(self.dt_Inicio.show)
        self.rb_Periodo.clicked.connect(self.dt_Final.show)
        self.rb_Completo.clicked.connect(self.dt_Inicio.setDisabled)
        self.rb_Completo.clicked.connect(self.dt_Final.setDisabled)
        self.dt_Inicio.hide()
        self.dt_Final.hide()
        self.rb_Completo.clicked.connect(self.dt_Inicio.hide)
        self.rb_Completo.clicked.connect(self.dt_Final.hide)
        self.atalhoRelatorio = QShortcut(QKeySequence("Ctrl+R"), self)
        self.atalhoRelatorio.activated.connect(self.Relatorio)
        self.bt_GerarRelatorio.clicked.connect(self.Relatorio)
        self.bt_Sair.setStyleSheet("background-color: red")
        self.bt_GerarRelatorio.setStyleSheet("background-color: blue")
        self.shortcut = QShortcut(QKeySequence("Esc"), self)
        self.shortcut.activated.connect(self.sair)
        self.atalhoSobre = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.atalhoSobre.activated.connect(self.showSobre)
        self.actionSobre.triggered.connect(self.showSobre)

    def showSobre(self):
        global tela
        tela = SobreWindow()
        tela.show()

    def Abrir(self):
        import easygui as eg

        try:
            global corrente_list, tensao_list, potencia_list, temperatura_list, combined_list, content
            global corrente_backup, tensao_backup, potencia_backup, temperatura_backup, combined_backup
            global primeiro, ultimo
            file = eg.fileopenbox(filetypes=["*.txt", "*.csv"])
            with open(file) as file:
                content = file.readlines()
            file.close()
            self.progressBarProcessamento.setValue(0)
            try:
                (
                    corrente_list,
                    tensao_list,
                    potencia_list,
                    temperatura_list,
                    combined_list,
                ) = self.Values_From_Txt(content, "L")
            except Exception as error:
                print(error)
            corrente_backup = corrente_list
            tensao_backup = tensao_list
            potencia_backup = potencia_list
            temperatura_backup = temperatura_list
            combined_backup = combined_list
            primeiro = combined_list[0]
            ultimo = combined_list[len(combined_list) - 1]
            self.labelInicio.setText(
                "Início: " + primeiro.strftime("%d/%m/%y - %H:%M:%S")
            )
            self.labelFinal.setText("Final:  " + ultimo.strftime("%d/%m/%y - %H:%M:%S"))
            #            self.dt_Inicio.setMinimumDateTime(primeiro)
            #            self.dt_Inicio.setMaximumDateTime(ultimo)
            #            self.dt_Final.setMinimumDateTime(primeiro)
            #            self.dt_Final.setMaximumDateTime(ultimo)
            self.dt_Inicio.setDateTime(primeiro)
            self.dt_Final.setDateTime(ultimo)
        except:
            pass

    def fazerCalculos(self):
        global corrente_list, tensao_list, potencia_list, temperatura_list, combined_list
        global plotCorrente, plotTensao, plotPotencia, plotTemperatura

        corrente_list = corrente_backup
        tensao_list = tensao_backup
        potencia_list = potencia_backup
        combined_list = combined_backup
        temperatura_list = temperatura_backup

        if self.rb_Periodo.isChecked():
            ini = self.dt_Inicio.dateTime().toPyDateTime()
            fin = self.dt_Final.dateTime().toPyDateTime()
            (
                corrente_p,
                tensao_p,
                potencia_p,
                temperatura_p,
                combined_p,
            ) = self.Values_Periodo(
                ini,
                fin,
                corrente_list,
                tensao_list,
                potencia_list,
                temperatura_list,
                combined_list,
                "P",
            )
            corrente_list = corrente_p
            tensao_list = tensao_p
            potencia_list = potencia_p
            combined_list = combined_p
            temperatura_list = temperatura_p
        else:
            (
                corrente_list,
                tensao_list,
                potencia_list,
                temperatura_list,
                combined_list,
            ) = self.Values_From_Txt(content, "P")

        plotCorrente = {
            "y": corrente_list,
            "titulo": "Corrente x Tempo",
            "xlabel": "Tempo",
            "ylabel": "Corrente [A]",
            "color": "blue",
        }
        plotTensao = {
            "y": tensao_list,
            "titulo": "Tensão x Tempo",
            "xlabel": "Tempo",
            "ylabel": "Tensão [V]",
            "color": "red",
        }
        plotPotencia = {
            "y": potencia_list,
            "titulo": "Potência x Tempo",
            "xlabel": "Tempo",
            "ylabel": "Potência [W]",
            "color": "green",
        }
        plotTemperatura = {
            "y": temperatura_list,
            "titulo": "Temperatura x Tempo",
            "xlabel": "Tempo",
            "ylabel": "Temperatura [ºC]",
            "color": "purple",
        }

    def periodoOk(self):
        import datetime as dt

        if self.rb_Periodo.isChecked():
            dados_dtInicio = self.dt_Inicio.dateTime().toPyDateTime()
            dados_dtFinal = self.dt_Final.dateTime().toPyDateTime()
            if (
                (dados_dtInicio >= dados_dtFinal)
                or ((dados_dtFinal - dados_dtInicio) < dt.timedelta(minutes=1))
                or (dados_dtInicio < primeiro)
                or (dados_dtFinal > ultimo)
            ):
                w = QWidget()
                w.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(icone)))
                QMessageBox.information(
                    w,
                    "Atenção",
                    "Verificar período especificado.\nObs: Mínimo de 1 minuto.",
                )
                return False
        return True

    def sair(self):
        sys.exit()

    def createTempDir(self):
        import os
        try:
            os.mkdir("./src/temp")
        except FileExistsError:
            pass


    def Relatorio(self):
        self.createTempDir()
        w = QWidget()
        w.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(icone)))
        try:
            if self.periodoOk():
                self.fazerCalculos()
                vtg.aux = 0
                medicoes = [plotCorrente, plotPotencia, plotTensao, plotTemperatura]
                vtg.plotSeparado(combined_list, medicoes)
                medicoes = [plotCorrente, plotTensao]
                vtg.plotJunto(combined_list, medicoes, "Corrente e Tensão x Tempo")
                medicoes = [plotCorrente, plotTemperatura]
                vtg.plotJunto(combined_list, medicoes, "Corrente e Temperatura x Tempo")
                gr.gerarRelatorio(
                    corrente_list,
                    tensao_list,
                    potencia_list,
                    temperatura_list,
                    combined_list,
                )
                vtg.aux = 1
                QMessageBox.information(w, "Aviso", "Relatório gerado com sucesso!")
        except Exception as error:
            print(error)
            QMessageBox.information(w, "Atenção", "Selecione um arquivo primeiro!")

    def Grafico(self):
        w = QWidget()
        w.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(icone)))
        if self.periodoOk():
            cbC = self.cb_Corrente.isChecked()
            cbT = self.cb_Tensao.isChecked()
            cbP = self.cb_Potencia.isChecked()
            cbTp = self.cb_Temperatura.isChecked()
            # nenhum selecionado
            if not cbC and not cbT and not cbP and not cbTp:
                QMessageBox.information(
                    w, "Atenção", "Selecione ao menos um item para visualizar!"
                )
            # 4 selecionados para o mesmo gráfico
            elif cbC and cbT and cbP and cbTp and self.rb_Juntos.isChecked():
                QMessageBox.information(
                    w, "Atenção", "Máximo de 3 variáveis no mesmo gráfico!"
                )
            else:
                try:
                    self.fazerCalculos()
                    cjC = {"cb": cbC, "valores": plotCorrente, "nome": "Corrente"}
                    cjT = {"cb": cbT, "valores": plotTensao, "nome": "Tensão"}
                    cjP = {"cb": cbP, "valores": plotPotencia, "nome": "Potência"}
                    cjTp = {
                        "cb": cbTp,
                        "valores": plotTemperatura,
                        "nome": "Temperatura",
                    }
                    conjuntoCj = [cjC, cjT, cjP, cjTp]
                    conjunto = list()
                    medicoes = list()
                    for cada in conjuntoCj:
                        if cada["cb"]:
                            conjunto.append(cada)
                            medicoes.append(cada["valores"])
                    total = len(conjunto)
                    # 1 selecionado
                    if total == 1:
                        vtg.plotSeparado(combined_list, medicoes)
                    ##2 selecionados
                    if total == 2:
                        tit = (
                            conjunto[0]["nome"]
                            + " e "
                            + conjunto[1]["nome"]
                            + " x Tempo"
                        )
                        if self.rb_Separado.isChecked():
                            vtg.plotSeparado(combined_list, medicoes)
                        if self.rb_Juntos.isChecked():
                            vtg.plotJunto(combined_list, medicoes, tit)
                    ##3 selecionados
                    if total == 3:
                        if self.rb_Separado.isChecked():
                            vtg.plotSeparado(combined_list, medicoes)
                        if self.rb_Juntos.isChecked():
                            vtg.plotJunto(combined_list, medicoes, "Medições")
                    # 4 selecionados para diferentes gráficos
                    if total == 4:
                        if self.rb_Separado.isChecked():
                            vtg.plotSeparado(combined_list, medicoes)
                except Exception as error:
                    print(error)
                    QMessageBox.information(
                        w, "Atenção", "Selecione um arquivo primeiro!"
                    )

    def Values_From_Txt(self, content, qual):
        try:
            import datetime as dt

            dia_list = []
            mes_list = []
            ano_list = []
            hora_list = []
            minuto_list = []
            segundo_list = []
            corrente_list = []
            tensao_list = []
            temperatura_list = []
            potencia_list = []
            combined_list = []

            # dados separados por virgulas
            for linha in range(len(content)):
                (
                    hora,
                    minuto,
                    segundo,
                    mes,
                    dia,
                    ano,
                    corrente,
                    tensao,
                    temperatura,
                ) = content[linha].split(",")
                dia_list.append(dia)
                mes_list.append(mes)
                ano_list.append(ano)
                hora_list.append(hora)
                minuto_list.append(minuto)
                segundo_list.append(segundo)
                corrente_list.append(float(corrente))
                tensao_list.append(float(tensao))
                potencia_list.append(float(corrente) * float(tensao))
                temperatura_list.append(float(temperatura))
                combined_list.append(
                    dt.datetime(
                        int(ano),
                        int(mes),
                        int(dia),
                        int(hora),
                        int(minuto),
                        int(segundo),
                    )
                )

                self.valorBarra(linha, content, qual)

            return (
                corrente_list,
                tensao_list,
                potencia_list,
                temperatura_list,
                combined_list,
            )
        except Exception as error:
            w = QWidget()
            w.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(icone)))
            QMessageBox.information(w, "Atenção", "Erro com a leitura do arquivo!")

    def Values_Periodo(
        self,
        inicio,
        final,
        corrente_list,
        tensao_list,
        potencia_list,
        temperatura_list,
        combined_list,
        qual,
    ):
        import matplotlib.dates as mdates

        dt_dentro = []
        c_dentro = []
        t_dentro = []
        temp_dentro = []
        p_dentro = []

        combined_num = mdates.date2num(combined_list)
        inicio_num = mdates.date2num(inicio)
        final_num = mdates.date2num(final)

        for x in range(len(combined_list)):
            if combined_num[x] >= inicio_num and combined_num[x] <= final_num:
                c_dentro.append(corrente_list[x])
                t_dentro.append(tensao_list[x])
                p_dentro.append(potencia_list[x])
                temp_dentro.append(temperatura_list[x])
                dt_dentro.append(combined_num[x])
            self.valorBarra(x, combined_list, qual)
        dentro = mdates.num2date(dt_dentro)

        return c_dentro, t_dentro, p_dentro, temp_dentro, dentro

    def valorBarra(self, x, lista, qual):
        in_min = 1
        in_max = len(lista)
        out_min = 0
        out_max = 100
        x = x + 1
        pbValor = int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
        if qual == "L":
            self.progressBarLeitura.setValue(pbValor)
        if qual == "P":
            self.progressBarProcessamento.setValue(pbValor)


class SobreWindow(QtWidgets.QMainWindow, sb.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.bt_Voltar.clicked.connect(self.hide)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(icone)))
        self.atalhoSair = QShortcut(QKeySequence("Esc"), self)
        self.atalhoSair.activated.connect(self.hide)
        pixmapFundo = QPixmap(fundo)
        self.lb_Fundo.setFixedSize(self.size())
        self.lb_Fundo.setGeometry(self.geometry())
        pixmapFundo = pixmapFundo.scaled(self.size())
        self.lb_Fundo.setPixmap(pixmapFundo)
        self.setFixedSize(self.size())
        self.bt_Voltar.setStyleSheet("background-color: red")
        self.lbEmail.setStyleSheet("color: blue")


def main():
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle("Fusion")
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15, 15, 15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    form = MainWindow()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()