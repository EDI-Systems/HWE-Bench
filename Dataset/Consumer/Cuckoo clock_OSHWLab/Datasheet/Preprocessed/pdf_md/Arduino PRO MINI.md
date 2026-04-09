# 35040-MP

# Arduino PRO MINI 168

The Arduino Pro Mini is a microcontroller board based on the Atmega168. It has 14 digital input/output pins (of which 6 can be used as PWM outputs), 6 analog inputs, an on-board resonator, a reset button, and holes for mounting pin headers. A six pin header can be connected to an FTDI cable breakout board to provide USB power and communication to the board. The Arduino Pro Mini is intended for advanced users who require flexibility, low-cost, and small size. It comes with the minimum of components (no onboard USB or pin headers) to keep the cost down. Operates at 5V (like most Arduino boards), and is intended for semi-permanent installation in objects or exhibitions. The board comes without pre-mounted headers, allowing the use of various types of connectors or direct soldering of wires. The pin layout is compatible with the Arduino Mini.

Pro Mini. runs at 5V and 16 MHz.

The Arduino Pro Mini was designed and is manufactured by SparkFun Electronics.

You can find here your board warranty informations.

# Getting Started

You can find in the Getting Started section all the information you need to configure your board, use the Arduino Software (IDE), and start tinker with coding and electronics.

# Need Help?

 On the Software on the Arduino Forum  On Projects on the Arduino Forum

# Technical specs

<table><tr><td>Microcontroller</td><td>ATmega168PA-AU</td></tr><tr><td>Board Power Supply</td><td>5-12VDC</td></tr><tr><td>Circuit Operating Voltage</td><td>5V</td></tr><tr><td>Digital /O Pins</td><td>14</td></tr><tr><td>PWM Pins</td><td>6</td></tr><tr><td>UART</td><td>1</td></tr><tr><td>SPI</td><td>1</td></tr><tr><td>I2C</td><td>1</td></tr><tr><td>Analog Input Pins</td><td>8</td></tr><tr><td>External Interrupts</td><td>2</td></tr><tr><td>DC Current per I/O Pin</td><td>40 mA</td></tr><tr><td>Flash Memory</td><td>16KB of which 2 KB used by bootloader</td></tr><tr><td>SRAM</td><td>1 KB</td></tr><tr><td>EEPROM</td><td>512B</td></tr><tr><td>Clock Speed</td><td>16 MHz</td></tr></table>

The technical specifications of Arduino Pro Mini are listed below:

o The crystal oscillator present in Arduino Nano comes with a frequency of 16 MHz.   
o On-Board 5V Regulator. (For RAW input of 5-12VDC)   
o It comes with a built-in LED. The LED will blink only when we will run the program.   
o There are 8 analog pins. There are 14 digital I/O pins, which comprise of 6 PWM (Pulse Width Modulation) pins.

# Power

The Arduino Pro Mini can be powered with an FTDI cable or breakout board connected to its six pin header, or with a regulated 5V supply on the Vcc pin. There is a voltage regulator on board so it can accept voltage up to 12VDC.

If you're supplying unregulated power to the board, be sure to connect to the "RAW" pin on not VCC.

The power pins are as follows: RAW For supplying a raw voltage to the board. VCC The regulated 5 volt supply. GND Ground pins.

# Memory

The Atmega168 has 16 kB of flash memory for storing code (of which 0.5kB is used for the bootloader). It has 1 kB of SRAM and 512Bs of EEPROM (which can be read and written with the EEPROM library.

# Input and Output

Each of the 14 digital pins on the Pro Mini can be used as an input or output, using pinMode, digitalWrite, and digitalRead functions. They operate at 5 volts. Each pin can provide or receive a maximum of 40 mA and has an internal pull-up resistor (disconnected by default) of 20-50 kOhms. In addition, some pins have specialized functions:

 Serial: 0 (RX) and 1 (TX). Used to receive (RX) and transmit (TX) TTL serial data. These pins are connected to the TX-0 and RX-1 pins of the six pin header.

 External Interrupts: 2 and 3. These pins can be configured to trigger an interrupt on a low value, a rising or falling edge, or a change in value. See the attachInterrupt function for details.

 PWM: 3, 5, 6, 9, 10, and 11. Provide 8-bit PWM output with the analogWrite function.

 SPI: 10 (SS), 11 (MOSI), 12 (MISO), 13 (SCK). These pins support SPI communication, which, although provided by the underlying hardware, is not currently included in the Arduino language.

 LED: 13. There is a built-in LED connected to digital pin 13. When the pin is HIGH value, the LED is on, when the pin is LOW, it's off.

The Pro Mini has 8 analog inputs, each of which provide 10 bits of resolution (i.e. 1024 different values). Four of them are on the headers on the edge of the board; two (inputs 4 and 5) on holes in the interior of the board. The analog inputs measure from ground to VCC. Additionally, some pins have specialized functionality:

 I 2 C: A4 (SDA) and A5 (SCL). Support I2 C (TWI) communication using the Wire library.

There is another pin on the board:

 Reset. Bring this line LOW to reset the microcontroller. Typically used to add a reset button to shields which block the one on the board.

# Communication

The Arduino Pro Mini has a number of facilities for communicating with a computer, another Arduino, or other microcontrollers. The Atmega168PA-AU provides UART TTL serial communication, which is available on digital pins 0 (RX) and 1 (TX). The Arduino software includes a serial monitor which allows simple textual data to be sent to and from the Arduino board via a USB connection.

A SoftwareSerial library allows for serial communication on any of the Pro Mini's digital pins.

The Atmega168P also supports I2C (TWI) and SPI communication. The Arduino software includes a Wire library to simplify use of the I2C bus; see the reference for details. To use the SPI communication, please see the Atmega168P datasheet.

# Programming

The Arduino Pro Mini can be programmed with the Arduino software download. For details, see the reference and tutorials.

The ATmega328 on the Arduino Pro Mini comes preburned with a bootloader that allows you to upload new code to it without the use of an external hardware programmer. It communicates using the original STK500 protocol reference , C header files.

You can also bypass the bootloader and program the ATmega328 with an external programmer; see these instructions for details.

# Automatic (Software) Reset

Rather then requiring a physical press of the reset button before an upload, the Arduino Pro Mini is designed in a way that allows it to be reset by software running on a connected computer. One of the pins on the six-pin header is connected to the reset line of the Atmega1688 via a capacitor. This pin connects to one of the hardware flow control lines of the USB-to-serial convertor connected to the header: RTS when using an FTDI cable, DTR when using the breakout board. When this line is asserted (taken low), the reset line drops long enough to reset the chip. The Arduino software uses this capability to allow you to upload code by simply pressing the upload button in the Arduino environment. This means that the bootloader can have a shorter timeout, as the lowering of the reset line can be well-coordinated with

the start of the upload.

This setup has other implications. When the Pro Mini is connected to either a computer running Mac OS X or Linux, it resets each time a connection is made to it from software (via USB). For the following half-second or so, the bootloader is running on the Pro. While it is programmed to ignore malformed data (i.e. anything besides an upload of new code), it will intercept the first few bytes of data sent to the board after a connection is opened. If a sketch running on the board receives one-time configuration or other data when it first starts, make sure that the software with which it communicates waits a second after opening the connection and before sending this data.

![](images/f7fd7de5dd0d357bf2e294dd328b48e7efb7d5c85590b2352d3dfb8fc3518131.jpg)  
PRO Mini with ATmega 168PA-AU

# Pin Descriptions

GND: There are three GND (Ground) pins present on the Pro Mini board.

Tx0: Tx0 and RX1 pins are used for serial communication. These two pins can also be used as the digital I/O pins. The Tx0 pin is used for transmission of the data.

RX1: RX1 is the communication pin, which is used for receiving the data.

RST: It is used to add a Reset button to the connection.

Vcc: It is the regulated voltage of 5VDC.

Vin: (RAW) The Vin is the input voltage pin, which is applied while using the external power source (5-12VDC)

A0 - A7: A0, A1, A2, A3, A4, A5, A6, and A7 are the analog pins. The resolution of the analog pins is 10 bits. The 8 analog pins are used as the analog inputs in the Arduino Pro Mini board.

2 – 13: The Pins 2 to 13 are the digital I/O pins.

# How to get started with Arduino Pro Mini?

We can program the Arduino Pro Mini using the Arduino IDE.

We can also use Arduino Web Editor, which allows us to upload sketches and write the code from our web browser (Google Chrome recommended) to any Arduino Board. It is an online platform.

The steps to get started with Arduino Pro Mini are listed below:

1. Open the code or sketch written in the Arduino software.

Select the port and the type of board.   
The ATmega168P microcontroller is used in the Arduino Pro Mini. So, we will select the Processor as ATmega168P.

# Click on 'Tools' and select Processor, as shown below:

![](images/667934b587cc42d79206e66f21e412270b3f89271315a23d09e7ac331fd577db.jpg)

2. We can select the 3.3V or 5V versions of the Arduino board. We can also choose the board type Nano w/ ATmega328P or Nano w/ ATmega168. The Arduino Pro Mini board is powered and connected to the USB called FTDI TTL-232R-3V3. It is the TTL serial level converter cable.

3. Now, upload and run the written code or sketch.

To upload and run, click on the button present on the top panel of the Arduino display, as shown below:

Within the few seconds after the compilation and run of code or sketch, the RX and TX light present on the Arduino board will flash.

The 'Done Uploading' message will appear after the code is successfully uploaded. The message will be visible in the status bar.