import matplotlib.pyplot as plt
import matplotlib.dates as mdates

path = "./temp/"
titulos = ["Corrente [A]", "Tensão [V]", "Potência [W]", "Temperatura [ºC]"]
formato = ".png"
date_fmt = "%d/%b, %H:%M"
date_formatter = mdates.DateFormatter(date_fmt)

aux = 1


def Layout(f1, tipo, x):

    #    days1 = mdates.HourLocator(interval = 12)
    #    dayss = mdates.HourLocator()
    #    f1.set_ylim(ymin=min(tipo['y']),ymax=max(tipo['y']))
    #    f1.set_xlim(x[0],x[len(x)-1])
    #    f1.xaxis.set_major_locator(days1)
    #    f1.xaxis.set_minor_locator(dayss)
    plt.tight_layout()
    f1.grid(True)


def plotSeparado(x, medicoes):
    plt.close("all")
    n = 0
    for tipo in medicoes:
        fig, f1 = plt.subplots(1, 1)
        f1.plot(x, tipo["y"], tipo["color"], picker=True)
        f1.xaxis.set_major_formatter(date_formatter)
        plt.gcf().autofmt_xdate()
        f1.set_xlabel(tipo["xlabel"])
        f1.set_ylabel(tipo["ylabel"])
        f1.set_title(tipo["titulo"])
        Layout(f1, tipo, x)
        if aux == 0:
            plt.savefig(path + tipo["ylabel"] + formato)
        if aux == 1:
            plt.draw()
            if n == (len(medicoes) - 1):
                plt.show()
        n += 1


def plotJunto(x, medicoes, titulo):
    plt.close("all")
    grid_linestyle = "--"

    fig, f1 = plt.subplots()
    (plot1,) = f1.plot(
        x, medicoes[0]["y"], medicoes[0]["color"], label=medicoes[0]["ylabel"]
    )
    f1.grid(color=medicoes[0]["color"], axis="y", linestyle=grid_linestyle)
    f1.tick_params("y", colors=medicoes[0]["color"])

    f2 = f1.twinx()
    (plot2,) = f2.plot(
        x, medicoes[1]["y"], medicoes[1]["color"], label=medicoes[1]["ylabel"]
    )
    f2.yaxis.grid(color=medicoes[1]["color"], linestyle=grid_linestyle)
    f2.tick_params("y", colors=medicoes[1]["color"])

    if len(medicoes) == 3:
        f3 = f1.twinx()
        (plot3,) = f3.plot(
            x, medicoes[2]["y"], medicoes[2]["color"], label=medicoes[2]["ylabel"]
        )
        f3.yaxis.grid(color=medicoes[2]["color"], linestyle=grid_linestyle)
        f3.tick_params("y", colors=medicoes[2]["color"], pad=25)
        plt.legend(
            [plot1, plot2, plot3],
            [medicoes[0]["ylabel"], medicoes[1]["ylabel"], medicoes[2]["ylabel"]],
        )
    else:
        plt.legend([plot1, plot2], [medicoes[0]["ylabel"], medicoes[1]["ylabel"]])

    f1.set_title(titulo)
    f1.set_xlabel(medicoes[0]["xlabel"])
    f1.xaxis.grid(linestyle=grid_linestyle)
    f1.xaxis.set_major_formatter(date_formatter)
    plt.gcf().autofmt_xdate()

    if aux == 0:
        plt.savefig(path + titulo + formato)
    if aux == 1:
        plt.show()