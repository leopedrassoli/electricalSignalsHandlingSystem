int modulo_sd = 53;
int sensorcorrente = A0;
int sensortensao = A1;
int potenciometro = A2;
int sensorTemperatura = 41;
int testetensao;
int cont = 0;

//Módulo RTC
#include <Wire.h>
#include <TimeLib.h>
#include <DS1307RTC.h>
tmElements_t tm;

//Módulo SD
#include <SPI.h>
#include <SD.h>
Sd2Card card;
int aux = 0;

//Sensor Corrente
#include "EmonLib.h"
EnergyMonitor scorrente;

//Sensor Temperatura
#include <OneWire.h>
#include <DallasTemperature.h>
OneWire oneWire(sensorTemperatura);
DallasTemperature sensors(&oneWire);
DeviceAddress sensor1;

//Display
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>
Adafruit_PCD8544 display = Adafruit_PCD8544(8, 9, 10, 11, 12);

void setup() {
  Serial.begin(9600);

  //pinMode(modulo_sd, OUTPUT);
  pinMode(sensorcorrente, INPUT);
  pinMode(sensortensao, INPUT);
  pinMode(potenciometro, INPUT);

  sensors.begin(); //Inicia sensor de temperatura
  if (!sensors.getAddress(sensor1, 0))
    Serial.println("Sensores nao encontrados !");

  scorrente.current(sensorcorrente, 58); //pino do sensor de corrente, constante

  display.begin();
  display.setContrast(50); //Ajusta o contraste do display
  display.clearDisplay();   //Apaga o buffer e o display
  display.setTextSize(1);  //Seta o tamanho do texto
  display.setTextColor(BLACK, WHITE);

  if (!card.init(SPI_HALF_SPEED, modulo_sd)) aux = 1;
  SD.begin(modulo_sd);
  RTC.chipPresent();
  verifica();

}

void loop() {

  limpaRuido();
  while (1) {

    if (cont == 30) {
      verifica();
      cont = 0;
    }
    File arquivo = SD.open("leituras.txt", FILE_WRITE);
    double corrente = calcCorrente();
    double potenciometro = calcPotenciometro();
    double tensao = calcTensao() * potenciometro;
    double temperatura = calcTemperatura();

    if ((analogRead(sensortensao) < 483)) testetensao = 127; //TENSÃO DE 127V
    else testetensao = 220; //TENSÃO DE 220V

    //Log no Cartão SD - 10,51,17,1,14,2017,14.130000,178.730000,14.130000
    if (RTC.read(tm)) {
      arquivo.print(tm.Hour);
      arquivo.print(',');
      arquivo.print(tm.Minute);
      arquivo.print(',');
      arquivo.print(tm.Second);
      arquivo.print(",");
      arquivo.print(tm.Month);
      arquivo.print(",");
      arquivo.print(tm.Day);
      arquivo.print(',');
      arquivo.print(tmYearToCalendar(tm.Year));
      arquivo.print(',');
      arquivo.print(corrente);
      arquivo.print(',');
      arquivo.print(tensao);
      arquivo.print(',');
      arquivo.println(temperatura);
      arquivo.close();
    }
    display.print(tm.Hour);
    display.print(':');
    display.print(tm.Minute);
    display.print("-");
    display.print(tm.Day);
    display.print('/');
    display.print(tm.Month);
    display.print("/");
    display.println(tmYearToCalendar(tm.Year) - 2000);

    //LOG NO DISPLAY
    display.print("I:");
    display.print(corrente);
    display.print("A\nV:");
    display.print(tensao);
    display.print("V");
    if (testetensao == 127) {
      if (tensao <= 109) display.print("-BAIXA");
      else if (tensao >= 135) display.print("-ALTA");
    } else {
      if (tensao <= 200) display.print("-BAIXA");
      else if (tensao >= 235) display.print("- ALTA");
    }

    display.print("\nP:");
    display.print(corrente * tensao);
    display.print("W");

    display.print("\nTemp:");
    display.print(temperatura);
    display.println("C");

    display.display();
    display.clearDisplay();

    delay(1000);
    cont++;
  }
}

void limpaRuido()
{
  for (int i = 0; i < 3; i++) {
    double corrente = calcCorrente();
    double potenciometro = calcPotenciometro();
    double tensao = calcTensao() * potenciometro;
    double temperatura = calcTemperatura();
    delay(1000);
  }
 delay(2000);
}

double calcTensao()
{
  double tensaorecebida, tensao;

  tensaorecebida = analogRead(sensortensao);
  if ((tensaorecebida > 100) & (tensaorecebida < 483)) //TENSÃO DE 127V
    tensao = ((tensaorecebida * 5) / 1023) * 74.2;
  else if ((tensaorecebida > 665) & (tensaorecebida < 1023)) //TENSÃO DE 220V
    tensao = ((tensaorecebida * 5) / 1023) * 57.0;
  else
    tensao = ((tensaorecebida * 5) / 1023) * 64.8;
  return tensao;
}

double calcCorrente()
{
  double corrente = scorrente.calcIrms(1480);
  if (corrente <= 0.1) corrente = 0;
  return corrente;
}

double calcTemperatura()
{
  sensors.requestTemperatures();
  float temperatura = sensors.getTempC(sensor1);
  return temperatura;
}

double calcPotenciometro()
{
  //int valPot = 0;
  float valPot = analogRead(potenciometro);
  valPot = map(valPot, 0, 1023, 80, 120) / 100.00;

  return valPot;
}

void verifica() {

  display.println("Status:");
  File arquivo = SD.open("leituras.txt", FILE_WRITE);
  if (aux == 0) {
    if (arquivo) {
      display.print("SD OK");
      arquivo.close();
    }
    else display.print("SD com erro no arquivo");
  }
  else display.print("SD nao encontrado");
  display.print("\n");

  if (RTC.read(tm)) {
    display.print("RTC OK");
  } else {
    if (RTC.chipPresent()) {
      display.print("RTC com hora e data desconfigurada - Carregar SetTime");
    }  else {
      display.print("RTC nao encontrado");
    }
  }
  display.display();
  delay(5000);
  display.clearDisplay();
}

