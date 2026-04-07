# 17-V H-Bridge Driver

# Features

1-A Max Output Current

Supports 2.5-V to 17-V Operating Supply Voltage

Supports 1.8-V, 3.3-V, 5-V Logic Voltage

PWM (IN1/IN2) interface

Protection

Undervoltage Lockout Protection (UVLO) Over-Current Protection (OCP) Thermal Shutdown (TSD)

Small Package Footprint DFN-8 Package

# Description

The TPM8837C is a high-voltage H-bridge driver. It is designed to control inductive loads such as DC motors, solenoids and relays. It can provide up-to 1-A drive current with maximum 17- V power supply.

The TPM8837C features a solution for motors used widely in consumer products, toys and other low-to-mid voltage or battery-powered motion control applications. The output driver is an H-bridge with VM voltage ranges from 2.5 V to 17 V. Control logic can operate on 1.8-V, 3.3-V and 5-V rails.

Internal protection features such as overcurrent protection, short circuit protection undervoltage lockout and over temperature improve reliability of the whole system.

# Applications

⚫ Surveillance Cameras ⚫ E-Lock   
⚫ Consumer devices   
⚫ Toys

![](images/eacefcb0f7698d0820406f9f79c2f7c2f4b31bd7ec653cb7168d0bd98231e2a6.jpg)  
Typical Application Diagram

# 17-V H-Bridge Driver

# Table of Contents

Features . . 1   
Applications... .. 1   
Description..... ... 1   
Table of Contents . .. 2   
Order Information.. .. 3   
Pin Configuration and Functions ..... .... 3   
Pin Functions . .... 3   
Absolute Maximum Ratings Note 1. .. 4   
ESD Rating.... ... 4   
Thermal Information ... .. 4   
Electrical Characteristics . .. 5   
Typical Performance Characteristics.. .... 6   
Detailed Description . .. 8   
Overview ..... ...... 8   
Functional Block Diagram . .... 9   
Feature Description. .... 9   
Tape and Reel Information . ... 11   
Package Outline Dimensions... ... 12   
IMPORTANT NOTICE AND DISCLAIMER . .. 14

17-V H-Bridge Driver

Revision History   

<table><tr><td rowspan=1 colspan=1>Date</td><td rowspan=1 colspan=1>Revision</td><td rowspan=1 colspan=1>Notes</td></tr><tr><td rowspan=1 colspan=1>2019/12/24</td><td rowspan=1 colspan=1>Rev1.0</td><td rowspan=1 colspan=1>Miscellaneous update</td></tr><tr><td rowspan=1 colspan=1>2020/09/10</td><td rowspan=1 colspan=1>Rev 1.1</td><td rowspan=1 colspan=1>Added SOP8 Thermal Resistance and Start up timing requirement</td></tr><tr><td rowspan=1 colspan=1>2020/05/20</td><td rowspan=1 colspan=1>Rev 1.2</td><td rowspan=1 colspan=1>Added TPM8837C-DF4R-S</td></tr></table>

# Order Information

<table><tr><td rowspan=1 colspan=1>Order Number</td><td rowspan=1 colspan=1>Operating AmbientTemperature Range</td><td rowspan=1 colspan=1>Package</td><td rowspan=1 colspan=1>Marking Information</td><td rowspan=1 colspan=1>MSL</td><td rowspan=1 colspan=1>Transport Media, Quantity</td></tr><tr><td rowspan=1 colspan=1>TPM8837C-DF4R</td><td rowspan=1 colspan=1>-40℃-125°C(1)</td><td rowspan=1 colspan=1>DFN2X2-8L</td><td rowspan=1 colspan=1>837</td><td rowspan=1 colspan=1>MSL3</td><td rowspan=1 colspan=1>3000</td></tr><tr><td rowspan=1 colspan=1>TPM8837C-DF4R-S</td><td rowspan=1 colspan=1>-40℃-125℃ (1)</td><td rowspan=1 colspan=1>DFN2X2-8L</td><td rowspan=1 colspan=1>837</td><td rowspan=1 colspan=1>MSL3</td><td rowspan=1 colspan=1>3000</td></tr><tr><td rowspan=1 colspan=1>TPM8837C-S01R</td><td rowspan=1 colspan=1>-40℃-125℃(1)</td><td rowspan=1 colspan=1>SOP8</td><td rowspan=1 colspan=1>837</td><td rowspan=1 colspan=1>MSL3</td><td rowspan=1 colspan=1>4000</td></tr></table>

(1) Ambient temperature indicates device operation condition range. Application thermal behavior needs to be taken care of when operating in high temperature scenarios.

# Pin Configuration and Functions

![](images/f119792f62fa5d88d94e6780e38cd31a8ee93a853be50c822fb7ee0a05bab77c.jpg)

# Pin Functions

<table><tr><td rowspan=1 colspan=2>Pin</td><td rowspan=1 colspan=1>1/0</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>Ground</td><td rowspan=1 colspan=1>Device ground</td></tr><tr><td rowspan=1 colspan=1>IN1</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>Input</td><td rowspan=1 colspan=1>Bridge input 1</td></tr><tr><td rowspan=1 colspan=1>IN2</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>Input</td><td rowspan=1 colspan=1>Bridge input 2</td></tr><tr><td rowspan=1 colspan=1>nSLEEP</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Input</td><td rowspan=1 colspan=1>Device enable, active high</td></tr><tr><td rowspan=1 colspan=1>OUT1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>Output</td><td rowspan=1 colspan=1>H-Bridge output 1</td></tr><tr><td rowspan=1 colspan=1>OUT2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>Output</td><td rowspan=1 colspan=1>H-Bridge output 2</td></tr></table>

# 17-V H-Bridge Driver

<table><tr><td rowspan=1 colspan=1>VCC</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>IO Power</td><td rowspan=1 colspan=1>Device power supply</td></tr><tr><td rowspan=1 colspan=1>VM</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>Motor Power</td><td rowspan=1 colspan=1>Motor power supply</td></tr></table>

# Absolute Maximum Ratings Note 1

<table><tr><td rowspan=1 colspan=1>Parameters</td><td rowspan=1 colspan=1>Rating</td></tr><tr><td rowspan=1 colspan=1>Motor Power Supply voltage, VM</td><td rowspan=1 colspan=1>-0.3 Vto 18V</td></tr><tr><td rowspan=1 colspan=1>Device Power Supply voltage, VCC</td><td rowspan=1 colspan=1>-0.3Vto6V</td></tr><tr><td rowspan=1 colspan=1>Outputs, OUT1, OUT2</td><td rowspan=1 colspan=1>-0.3V to 18V</td></tr><tr><td rowspan=1 colspan=1>Digital Input Voltage, IN1, IN2</td><td rowspan=1 colspan=1>-0.3Vto 6V</td></tr><tr><td rowspan=1 colspan=1>Peak output current</td><td rowspan=1 colspan=1>Internally limited</td></tr><tr><td rowspan=1 colspan=1>Continuous motor drive output current</td><td rowspan=1 colspan=1>1A</td></tr><tr><td rowspan=1 colspan=1>Output Short-Circuit Duration Note 3</td><td rowspan=1 colspan=1>Infinite</td></tr><tr><td rowspan=1 colspan=1>Maximum Junction Temperature</td><td rowspan=1 colspan=1>150℃</td></tr><tr><td rowspan=1 colspan=1>Operating Junction Temperature Range</td><td rowspan=1 colspan=1>−40 to 150℃</td></tr><tr><td rowspan=1 colspan=1>Storage Temperature Range</td><td rowspan=1 colspan=1>-65 to 150℃</td></tr><tr><td rowspan=1 colspan=1>Lead Temperature (Soldering, 10 sec)</td><td rowspan=1 colspan=1>260°℃</td></tr></table>

Note 1: Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. Exposure to any Absolute Maximum Rating condition for extended periods may affect device reliability and lifetime.

Note 2: The inputs are protected by ESD protection diodes to each power supply. If the input extends more than 300mV beyond the power supply, the input current should be limited to less than 10mA.

Note 3: A heat sink may be required to keep the junction temperature below the absolute maximum. This depends on the power supply voltage and how many amplifiers are shorted. Thermal resistance varies with the amount of PC board metal connected to the package. The specified values are for short traces connected to the leads.

Note 4: Power dissipation and thermal limits must be observed.

# ESD Rating

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Condition</td><td rowspan=1 colspan=1>Minimum Level</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>HBM</td><td rowspan=1 colspan=1>Human Body Model ESD</td><td rowspan=1 colspan=1>ANSI/ESDA/JEDEC JS-001</td><td rowspan=1 colspan=1>±2</td><td rowspan=1 colspan=1>kV</td></tr><tr><td rowspan=1 colspan=1>CDM</td><td rowspan=1 colspan=1>Charged Device Model ESD</td><td rowspan=1 colspan=1>ANSI/ESDA/JEDEC JS-002</td><td rowspan=1 colspan=1>±1</td><td rowspan=1 colspan=1>kV</td></tr></table>

# Thermal Information

<table><tr><td rowspan=1 colspan=1>Package Type</td><td rowspan=1 colspan=1>θJA</td><td rowspan=1 colspan=1>θJc</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>DFN2X2-8L</td><td rowspan=1 colspan=1>103</td><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>C/W</td></tr><tr><td rowspan=1 colspan=1>SOP8</td><td rowspan=1 colspan=1>112</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>°C/W</td></tr></table>

# Electrical Characteristics

<table><tr><td rowspan=1 colspan=7>Electrical CharacteristicsAll test condition is Vm = 5 V, TA = -40 ºC – 125 ºC, unless otherwise noted.</td></tr><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Conditions</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=7>Power Supply</td></tr><tr><td rowspan=1 colspan=1>Vn</td><td rowspan=1 colspan=1>Vm operating voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>lm</td><td rowspan=1 colspan=1>Vu operating supply current</td><td rowspan=1 colspan=1>Vm = 5 V; VCC = 3 V; IN1/N2 loW;nSLEEP=5V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>340</td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>lma</td><td rowspan=1 colspan=1>Vm quiescent supply current</td><td rowspan=1 colspan=1>Vm= 5 V; VCC = 3V; IN1/IN2 low;nSLEEP= 0V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=2 colspan=1>VuwLO</td><td rowspan=2 colspan=1>Vc under voltage lockout</td><td rowspan=1 colspan=1>Vcc risingg</td><td rowspan=1 colspan=1>1.5</td><td rowspan=1 colspan=1>1.62</td><td rowspan=1 colspan=1>1.71</td><td rowspan=2 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Vcc faliing</td><td rowspan=1 colspan=1>1.45</td><td rowspan=1 colspan=1>1.55</td><td rowspan=1 colspan=1>1.65</td></tr><tr><td rowspan=1 colspan=1>Vcc</td><td rowspan=1 colspan=1>Vecoperating voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5.5</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>lvcc</td><td rowspan=1 colspan=1>Vcc operating supply current</td><td rowspan=1 colspan=1>Vm= 5V; VCC = 3V; IN1/N2 loW;nSLEEP=5V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>135</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>lvcc</td><td rowspan=1 colspan=1>Vcc quiescent supply current</td><td rowspan=1 colspan=1>VM= 5V; VCC = 3V; IN1/IN2 loW;nSLEEP=0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>0.5</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=7> Input Characteristics</td></tr><tr><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>Input low voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.25×Vcc</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>ViH</td><td rowspan=1 colspan=1>Input high voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.5×Vcc</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Input low current</td><td rowspan=1 colspan=1>$V\N = V$</td><td rowspan=1 colspan=1>-5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>lH</td><td rowspan=1 colspan=1>Input high current</td><td rowspan=1 colspan=1>$V\N =3.3V$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>RpD</td><td rowspan=1 colspan=1>Pull-down resistance</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>k$</td></tr><tr><td rowspan=1 colspan=7>H-Bridge FETs</td></tr><tr><td rowspan=2 colspan=1>RDS(ON)</td><td rowspan=2 colspan=1>HS+LS FET ON resistance</td><td rowspan=1 colspan=1>VM= 12V, 1o= 250mA,TJ=25°C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.85</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>Ω</td></tr><tr><td rowspan=1 colspan=1>Vm=5V, lo= 250 mA, TJ= 25°℃</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.85</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>lOFF</td><td rowspan=1 colspan=1>OFF-state leakage current</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=7>Protection Circuits</td></tr><tr><td rowspan=1 colspan=1>locp</td><td rowspan=1 colspan=1>Overcurrent protection trip level</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>1.6</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>A</td></tr><tr><td rowspan=1 colspan=1>tDEG</td><td rowspan=1 colspan=1>Overcurrent deglitch time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>tocR</td><td rowspan=1 colspan=1>Overcurrent protection retry time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>DEAD</td><td rowspan=1 colspan=1>Output dead time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>TSD</td><td rowspan=1 colspan=1>Thermal shutdown temperature</td><td rowspan=1 colspan=1>Junction temperature</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1>160</td><td rowspan=1 colspan=1>180</td><td rowspan=1 colspan=1>C</td></tr><tr><td rowspan=1 colspan=1>Timing</td><td></td><td></td><td rowspan=1 colspan=4></td></tr><tr><td rowspan=1 colspan=1>t7</td><td rowspan=1 colspan=1>Output enable time</td><td rowspan=1 colspan=1>$R{=20_$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>300</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>t8</td><td rowspan=1 colspan=1>Output disable time</td><td rowspan=1 colspan=1> = 20$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>300</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>t</td><td rowspan=1 colspan=1>Delay time, INx high to OUTx high</td><td rowspan=1 colspan=1>$R L= 20_$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>160</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>t10</td><td rowspan=1 colspan=1>Delay time, INx low to OUTx low</td><td rowspan=1 colspan=1> L= 20$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>160</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>tR</td><td rowspan=1 colspan=1>Output rise time</td><td rowspan=1 colspan=1>$R L= 20_$</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>188</td><td rowspan=1 colspan=1>ns</td></tr></table>

# 17-V H-Bridge Driver

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Conditions</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Typ</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>tF</td><td rowspan=1 colspan=1>Output fall time</td><td rowspan=1 colspan=1>R L = 20Ω</td><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>188</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>tstartup</td><td rowspan=1 colspan=1>Start up time needed to keep IN1/IN2low</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>μs</td></tr></table>

# Typical Performance Characteristics

![](images/6aab70684f8a0121af257ea2682b9466bc8b9a57f08846cbd008d47234a30b11.jpg)  
Figure 1. VM Quiescent Current vs Ambient Temperature

![](images/8d7d827edbb452a53305ef97f7dec2cfd81bcbf4a96e244905a288542ae513b1.jpg)  
Figure 2. VCC Quiescent Current vs Ambient Temperature

![](images/cbbae35e96be6e99773a04a3750c1b661ac94f026e5b6f0cbd04d3265660c619.jpg)  
Figure 3. VM Operating Current vs Ambient Temperature

![](images/434552864777715cb40da489b901a3ab88a7b76d50bdc6f1e30eee56b61d49dd.jpg)  
Figure 4. VCC Operating Current vs Ambient Temperature

17-V H-Bridge Driver

![](images/04766005c4b072b8aca7105452cfe15204a53509f817f9312869a521cb36b2df.jpg)  
Figure 5. HS + LS RDS(ON) vs Ambient Temperature

![](images/2cc5086fa23ef086c4b6d75b5c350ee1f5b3cad08455118e4bb56f51a8b08fcf.jpg)  
Figure 6. HS + LS RDS(ON) vs VM

# Detailed Description

# Overview

The TPM8837C is a high-voltage H-bridge driver. It is designed to control inductive loads such as DC motors, solenoids and relays.   
It can provide up-to 1-A drive current with maximum 17-V power supply.

The TPM8837C features a solution for motors used widely in consumer products, toys and other low-to-mid voltage or batterypowered motion control applications. The output driver is an H-bridge with VM voltage ranges from 2.5V to 17V. Control logic can operate on 1.8-V, 3.3-V and 5-V rails.

Internal protection features such as overcurrent protection, short circuit protection, undervoltage lockout and overtemperature improve reliability of the whole system. It is recommended that the device keeps IN1/IN2 low after nSLEEP rising edge for 100 μs to ensure clean start up.

Protection features include ⚫ Overcurrent protection ⚫ Short circuit protection ⚫ Over-temperature protection. ⚫ Under-voltage lockout

# 17-V H-Bridge Driver

# Functional Block Diagram

![](images/7567bee9cb8d797ffef167150312ebd60e4da365a6ada93dd41e745349a41265.jpg)  
Figure 7 Functional Block Diagram

# Feature Description

# Timing

All logic inputs have a deglitch circuitry to prevent noise from affecting the output state. The input deglitch time is around 100ns. The output slew delay time is the delay contributed by gate drivers. In order to control the output rise/fall time, the gate drive limits the slew rate of gate voltage of output FETs. Typical slew delay time is around 50ns. The rise and fall time of the outputs depend on VM voltage and load conditions, and are controlled slowly to reduce EMI. Typical rise and fall time are 100ns. The dead time is measured as the time when OUTx is Hi-Z between turning off one of the H-bridge FETs and turning on the other. When sourcing current out of the pin, the output falls to one diode drop below ground during dead time. When sinking current into the pin, the output rises to one diode drop above VM. The typical dead time is 100ns. • The propagation time is measured as the between an input edge to an output change. This time is the sum of the input deglitch time, output slew delay, and output rise/fall time. The propagation time is around 350ns.

# Bridge Control

The TPM8837C uses IN/IN mode to control H-bridge:

<table><tr><td rowspan=1 colspan=1>IN1</td><td rowspan=1 colspan=1>IN2</td><td rowspan=1 colspan=1>OUT1</td><td rowspan=1 colspan=1>OUT2</td><td rowspan=1 colspan=1>Function</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>Z</td><td rowspan=1 colspan=1>Z</td><td rowspan=1 colspan=1>Coast</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>Reverse</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>Forward</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>Brake</td></tr></table>

The highside driver has a weak internal pull-up to VM during Hi-Z state.

# Protections

Over-current protection (OCP): All FETs are protected by current limit circuitry. Whenever the channel current of anyone of FETs exceeds overcurrent protection trip level, IOCP, and persists for longer than the overcurrent deglitch time, tDEG, the H

# 17-V H-Bridge Driver

bridge is disabled. After about 1ms, tOCR, all bridges are re-enabled automatically.

Short-circuit protection: thanks to the OCP function, the device is protected from OUT1 to OUT2 short-circuit, OUT1/OUT2 to ground short-circuit, and OUT1/OUT2 to VM short-circuit. When short-circuit occurs, no damage on IC and IR-CUT, Thermal shutdown (TSD): If the die temperature exceeds safe limits, all FETs in the H-bridge disable. Operation automatically resumes once the die temperature falls to a safe level. Under-voltage lockout (UVLO): If at any time the voltage on the VCC pins falls below the under-voltage lockout threshold voltage, all circuitry in the device disable, and internal logic resets. Operation resumes when VCC rises above the UVLO threshold. • During power-up, it is recommended to keep IN1/IN2 to GND to ensure clean start up.

<table><tr><td rowspan=1 colspan=1>Fault</td><td rowspan=1 colspan=1>Condition</td><td rowspan=1 colspan=1>Error Report</td><td rowspan=1 colspan=1>H-bridge</td><td rowspan=1 colspan=1>Internal circuits</td><td rowspan=1 colspan=1>Recovery</td></tr><tr><td rowspan=1 colspan=1>VM UVLO</td><td rowspan=1 colspan=1>VM&lt;UVLO</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1>Disabled</td><td rowspan=1 colspan=1>Disabled</td><td rowspan=1 colspan=1>VM&gt;UVLO</td></tr><tr><td rowspan=1 colspan=1>Overcurrent (OCP)</td><td rowspan=1 colspan=1>louT &gt; loCcP</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1>Disabled</td><td rowspan=1 colspan=1>Operating</td><td rowspan=1 colspan=1>tocR</td></tr><tr><td rowspan=1 colspan=1>Thermal shutdown (TSD)</td><td rowspan=1 colspan=1>$TJ TSD$</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1>Disabled</td><td rowspan=1 colspan=1>Operating</td><td rowspan=1 colspan=1>TJ&lt;TSD - THYS</td></tr></table>

Device Functional Modes   

<table><tr><td rowspan=1 colspan=1>Operating Mode</td><td rowspan=1 colspan=1>Condition</td><td rowspan=1 colspan=1>H-Bridge</td><td rowspan=1 colspan=1>Internal Circuits</td></tr><tr><td rowspan=1 colspan=1>Operating</td><td rowspan=1 colspan=1>VM&gt;UVLO</td><td rowspan=1 colspan=1>Operating</td><td rowspan=1 colspan=1>Operating</td></tr><tr><td rowspan=1 colspan=1>Sleep Mode</td><td rowspan=1 colspan=1>VM = 0V</td><td rowspan=1 colspan=1>Disabled</td><td rowspan=1 colspan=1>Disabled</td></tr><tr><td rowspan=1 colspan=1>Fault encountered</td><td rowspan=1 colspan=1>Any fault conditions met</td><td rowspan=1 colspan=1>Disabled</td><td rowspan=1 colspan=1>See previous table</td></tr></table>

# 17-V H-Bridge Driver

# Tape and Reel Information

![](images/b8d0c533c1cae8c270ba36d8b7301512846d3a1d780c6345fdeee6aac0bae034.jpg)  
D1: Reel Diameter

![](images/75b72b4a3148f674acf22029ed43374a260051b1d2b20e4d4dbe81c8c99d65e3.jpg)

![](images/d501291770f3abcff2640a94940bec00c4e316e070ede1d0411a98db8cfcbafe.jpg)

<table><tr><td rowspan=1 colspan=1>OrderNumber</td><td rowspan=1 colspan=1>Package</td><td rowspan=1 colspan=1>D1</td><td rowspan=1 colspan=1>W1</td><td rowspan=1 colspan=1>A0</td><td rowspan=1 colspan=1>B0</td><td rowspan=1 colspan=1>K0</td><td rowspan=1 colspan=1>PO</td><td rowspan=1 colspan=1>W0</td><td rowspan=1 colspan=1>Pin1Quadrant</td></tr><tr><td rowspan=1 colspan=1>TPM8837C-DF4R</td><td rowspan=1 colspan=1>DFN2X2-8L</td><td rowspan=1 colspan=1>180.0</td><td rowspan=1 colspan=1>13.1</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>1.1</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>Q1</td></tr><tr><td rowspan=1 colspan=1>TPM8837C-DF4R-S</td><td rowspan=1 colspan=1>DFN2X2-8L</td><td rowspan=1 colspan=1>180.0</td><td rowspan=1 colspan=1>13.1</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>2.3</td><td rowspan=1 colspan=1>1.1</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>Q1</td></tr><tr><td rowspan=1 colspan=1>TPM8837C-SO1R</td><td rowspan=1 colspan=1>SOP8</td><td rowspan=1 colspan=1>330.0</td><td rowspan=1 colspan=1>17.6</td><td rowspan=1 colspan=1>6.4</td><td rowspan=1 colspan=1>5.4</td><td rowspan=1 colspan=1>2.1</td><td rowspan=1 colspan=1>8.0</td><td rowspan=1 colspan=1>12.0</td><td rowspan=1 colspan=1>Q1</td></tr></table>

# 17-V H-Bridge Driver

# Package Outline Dimensions

![](images/346aa314c8e6e51a8283e04d28c8415c19058dd3d660597e857860810007274a.jpg)  
Aug. 2013, REV. A02

# 17-V H-Bridge Driver

![](images/92c89be1f2da34151826e8a03187724dfce917b56e2842c900f02d7779db920b.jpg)

<table><tr><td rowspan=2 colspan=1>Symbol</td><td rowspan=1 colspan=2>Dimensions In Millimeters</td><td rowspan=1 colspan=2>Dimensions In Inches</td></tr><tr><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Max.</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>1.350</td><td rowspan=1 colspan=1>1.750</td><td rowspan=1 colspan=1>0.053</td><td rowspan=1 colspan=1>0.069</td></tr><tr><td rowspan=1 colspan=1>A1</td><td rowspan=1 colspan=1>0.100</td><td rowspan=1 colspan=1>0.250</td><td rowspan=1 colspan=1>0.004</td><td rowspan=1 colspan=1>0.010</td></tr><tr><td rowspan=1 colspan=1>A2</td><td rowspan=1 colspan=1>1.350</td><td rowspan=1 colspan=1>1.550</td><td rowspan=1 colspan=1>0.053</td><td rowspan=1 colspan=1>0.061</td></tr><tr><td rowspan=1 colspan=1>b</td><td rowspan=1 colspan=1>0.330</td><td rowspan=1 colspan=1>0.510</td><td rowspan=1 colspan=1>0.013</td><td rowspan=1 colspan=1>0.020</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>0.170</td><td rowspan=1 colspan=1>0.250</td><td rowspan=1 colspan=1>0.007</td><td rowspan=1 colspan=1>0.010</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>4.700</td><td rowspan=1 colspan=1>5.100</td><td rowspan=1 colspan=1>0.185</td><td rowspan=1 colspan=1>0.201</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>5.800</td><td rowspan=1 colspan=1>6.200</td><td rowspan=1 colspan=1>0.228</td><td rowspan=1 colspan=1>0.244</td></tr><tr><td rowspan=1 colspan=1>E1</td><td rowspan=1 colspan=1>3.800</td><td rowspan=1 colspan=1>4.000</td><td rowspan=1 colspan=1>0.150</td><td rowspan=1 colspan=1>0.157</td></tr><tr><td rowspan=1 colspan=1>e</td><td rowspan=1 colspan=2>1.270(BSC)</td><td rowspan=1 colspan=2>0.050(BSC)</td></tr><tr><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>0.400</td><td rowspan=1 colspan=1>0.800</td><td rowspan=1 colspan=1>0.016</td><td rowspan=1 colspan=1>0.031</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0°</td><td rowspan=1 colspan=1>8°</td><td rowspan=1 colspan=1>0°</td><td rowspan=1 colspan=1>8°</td></tr></table>

# IMPORTANT NOTICE AND DISCLAIMER

Copyright© 3PEAK 2012-2023. All rights reserved.

Trademarks. Any of the 思瑞浦 or 3PEAK trade names, trademarks, graphic marks, and domain names contained in this document /material are the property of 3PEAK. You may NOT reproduce, modify, publish, transmit or distribute any Trademark without the prior written consent of 3PEAK.

Performance Information. Performance tests or performance range contained in this document/material are either results of design simulation or actual tests conducted under designated testing environment. Any variation in testing environment or simulation environment, including but not limited to testing method, testing process or testing temperature, may affect actual performance of the product.

Disclaimer. 3PEAK provides technical and reliability data (including data sheets), design resources (including reference designs), application or other design recommendations, networking tools, security information and other resources "As Is". 3PEAK makes no warranty as to the absence of defects, and makes no warranties of any kind, express or implied, including without limitation, implied warranties as to merchantability, fitness for a particular purpose or non-infringement of any third-party’s intellectual property rights. Unless otherwise specified in writing, products supplied by 3PEAK are not designed to be used in any life-threatening scenarios, including critical medical applications, automotive safety-critical systems, aviation, aerospace, or any situations where failure could result in bodily harm, loss of life, or significant property damage. 3PEAK disclaims all liability for any such unauthorized use.