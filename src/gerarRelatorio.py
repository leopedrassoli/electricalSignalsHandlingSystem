import os

temp_path = "./src/temp/"
titulos = [
    "Corrente [A]",
    "Tensão [V]",
    "Potência [W]",
    "Temperatura [ºC]",
    "Corrente e Tensão x Tempo",
    "Corrente e Temperatura x Tempo",
]


def gerarRelatorio(
    corrente_list, tensao_list, potencia_list, temperatura_list, combined_list
):
    import datetime as dt
    import numpy as np

    primeiro = combined_list[0]
    ultimo = combined_list[len(combined_list) - 1]
    corrente_np = np.asarray(corrente_list)
    tensao_np = np.asarray(tensao_list)
    temperatura_np = np.asarray(temperatura_list)
    potencia_np = np.asarray(potencia_list)
    potencia_kw = potencia_np / 1000

    kwh = 0
    for x in range(len(combined_list) - 1):
        atual = x
        proximo = x + 1
        tempo = (combined_list[proximo] - combined_list[atual]).seconds / 3600
        kwh += ((potencia_kw[atual] + potencia_kw[proximo]) * tempo) / 2

    filename = "Relatorio.html"

    formato = ".png"
    date_fmt = "%d/%m/%y - %H:%M:%S"
    width = "450"
    height = "337"

    file = open(temp_path + filename, "w")
    message = (
        """<html><head><title>Relatório Elétrico</title></head><body>
    <p style="text-align: center;"><span style="font-size: 15pt;"><strong>RELATÓRIO</strong></span></p><ul>
    <li style="text-align: left;"><span style="font-size: 13pt;"><span style="font-size: 13pt;">
    <strong>Período analisado: """
        + primeiro.strftime(date_fmt)
        + """ até """
        + ultimo.strftime(date_fmt)
        + """</strong></span></span></li></ul>
    
    <p><span style="font-size: 13pt;"><strong>Corrente:</strong></span></p><ul>
    <li><span style="font-size: 10pt;"><strong>Máxima: """
        + str(corrente_np.max())
        + """A -> """
        + str(combined_list[corrente_np.argmax()].strftime(date_fmt))
        + """
    </strong></span></li><li style="text-align: left;"><span style="font-size: 10pt;"><strong>Mínima: """
        + str(corrente_np.min())
        + """A -> """
        + str(combined_list[corrente_np.argmin()].strftime(date_fmt))
        + """</strong></span></li>
    <li style="text-align: left;"><span style="font-size: 10pt;"><strong>Média: """
        + "%.4f" % (corrente_np.mean())
        + """A</strong></span></li></ul>
    
    
    <p style="text-align:center;"><img src='"""
        + temp_path
        + titulos[0]
        + formato
        + """' width="""
        + width
        + """ height="""
        + height
        + """ ></p>
    
    <p><span style="font-size: 13pt;"><strong>Tensão:</strong></span></p><ul>
    <li><span style="font-size: 10pt;"><strong>Máxima: """
        + str(tensao_np.max())
        + """V -> """
        + str(combined_list[tensao_np.argmax()].strftime(date_fmt))
        + """
    </strong></span></li><li style="text-align: left;"><span style="font-size: 10pt;"><strong>Mínima: """
        + str(tensao_np.min())
        + """V -> """
        + str(combined_list[tensao_np.argmin()].strftime(date_fmt))
        + """</strong></span></li>
    <li style="text-align: left;"><span style="font-size: 10pt;"><strong>Média: """
        + "%.4f" % (tensao_np.mean())
        + """V</strong></span></li></ul>
    
    
    <p style="text-align:center;"><img src='"""
        + temp_path
        + titulos[1]
        + formato
        + """' width="""
        + width
        + """ height="""
        + height
        + """ ></p>
    
    
    <p><span style="font-size: 13pt;"><strong>Potência:</strong></span></p><ul>
    <li><span style="font-size: 10pt;"><strong>Máxima: """
        + str(potencia_np.max())
        + """W -> """
        + str(combined_list[potencia_np.argmax()].strftime(date_fmt))
        + """
    </strong></span></li><li style="text-align: left;"><span style="font-size: 10pt;"><strong>Mínima: """
        + str(potencia_np.min())
        + """W -> """
        + str(combined_list[potencia_np.argmin()].strftime(date_fmt))
        + """</strong></span></li>
    <li style="text-align: left;"><span style="font-size: 10pt;"><strong>Média: """
        + "%.4f" % (potencia_np.mean())
        + """W</strong></span></li></ul>
    
    <br><br>
    <p style="text-align:center;"><img src='"""
        + temp_path
        + titulos[2]
        + formato
        + """' width="""
        + width
        + """ height="""
        + height
        + """ ></p>
    
    <br>
     <p><span style="font-size: 13pt;"><strong>Temperatura:</strong></span></p><ul>
    <li><span style="font-size: 10pt;"><strong>Máxima: """
        + str(temperatura_np.max())
        + """ºC -> """
        + str(combined_list[temperatura_np.argmax()].strftime(date_fmt))
        + """
    </strong></span></li><li style="text-align: left;"><span style="font-size: 10pt;"><strong>Mínima: """
        + str(temperatura_np.min())
        + """ºC -> """
        + str(combined_list[temperatura_np.argmin()].strftime(date_fmt))
        + """</strong></span></li>
    <li style="text-align: left;"><span style="font-size: 10pt;"><strong>Média: """
        + "%.4f" % (temperatura_np.mean())
        + """ºC</strong></span></li></ul>
    
    <br>
    <p style="text-align:center;"><img src='"""
        + temp_path
        + titulos[3]
        + formato
        + """' width="""
        + width
        + """ height="""
        + height
        + """ ></p>
    
    <br><br>
    <p><span style="font-size: 13pt;"><strong>Gráficos junção: </strong></span></p>
    <br><br>
    <p style="text-align:center;"><img src='"""
        + temp_path
        + titulos[4]
        + formato
        + """' width="""
        + width
        + """ height="""
        + height
        + """ ></p>
    <br>
    <p style="text-align:center;"><img src='"""
        + temp_path
        + titulos[5]
        + formato
        + """' width="""
        + width
        + """ height="""
        + height
        + """ ></p>
    <br><br><br><br>
    <p><span style="font-size: 13pt;"><strong>Energia consumida no período: """
        + str(kwh)
        + """ kWh</strong></span></p>
    <p><span style="font-size: 13pt;"><strong>Data de geração do relatório: """
        + dt.datetime.now().strftime(date_fmt)
        + """</strong></span></p>
    
    </body></html>
    """
    )
    file.write(message)
    file.close()

    salvarComo()
    deleteTempFiles()


def salvarComo():
    import easygui as eg

    arquivo_html = temp_path + "Relatorio.html"

    try:
        caminho = eg.filesavebox(filetypes=["*.pdf"])
        try:
            nome, formato = caminho.split(".")
        except:
            caminho = caminho + ".pdf"
        gerarPDF(arquivo_html, caminho)
    except:
        pass


def gerarPDF(arquivo_html, caminho):
    from PyQt5.QtGui import QTextDocument
    from PyQt5.QtPrintSupport import QPrinter

    doc = QTextDocument()
    html = open(arquivo_html).read()
    doc.setHtml(html)

    printer = QPrinter()
    printer.setOutputFileName(caminho)
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setPageSize(QPrinter.A4)
    doc.print_(printer)
    os.startfile(caminho)


def deleteTempFiles():
    import os, glob

    files = glob.glob("./src/temp/*")
    for f in files:
        os.remove(f)
    os.rmdir(temp_path)