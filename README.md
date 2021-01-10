# System for Handling Electrical Signals

## What is this?

It's a system of measurement of attributes related to electrical engineering that together with a developed computer system, provides aid  for  the  accomplishment  of  measures  that  may  be related to the control of electric energy or maintenance expenses machinery and apparatus.

This system was developed with professor *Igor Santos Peretta* in a scientific research project and was presented at CEEL 2018 - Conferência de Estudos em Engenharia Elétrica (Electrical Engineering Studies Conference).

## Full project

* Assemble the wiring diagram as in the image *support/esquematico.png* using Arduino
* Load *support/SetTime/SetTime.ino* to synchronize the Arduino RTC module date and time
* Load *support/ArduinoFinal/ArduinoFinal.ino* to generate the datalog (*.txt* file) with the possibles electric measurements (voltage, current and temperature)
* Upload the file generated on the SD card module to the developed application

## Dependencies

Requirements:

* Python 3.7.4
* support/requirements.txt

## Quick Use

* Run *main.py* file
* Click "Abrir" button and select *test/LEITURAS.txt*
* Select attributes (current, voltage, power, temperature)
* Generate graphs:
  * "Separado": one window for each attribute
  * "Único": same window for all attributes (max of 4)
  * Click "Visualizar" button
* Generate report:
  * full period: "Completo"
  * specific period: "Período"
  * Click "Gerar" button
  * Save the result file in *result/relatorio.pdf*
* Exit application
  * Click "Sair" button

## Layout

![final_layout](src\img\layout_final.png)

## Contact

* Leonardo Pedrassoli Silva
  * Computer engineering
  * leopedrassoli@ufu.br (UFU - Federal University of Uberlândia, Brazil)
