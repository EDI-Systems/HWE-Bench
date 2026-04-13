# SINGLE-CHIP BROADCAST FM RADIO TUNER

# 1 General Description

The RDA5807MP series is the newest generation single-chip broadcast FM stereo radio tuner with fully integrated synthesizer, IF selectivity, RDS/RBDS and MPX decoder. The tuner uses the CMOS process, support multi-interface and require the least external component. All these make it very suitable for portable devices.

The RDA5807MP series has a powerful low-IF digital audio processor, this make it have optimum sound quality with varying reception conditions.

The RDA5807MP series support frequency range is from 50MHz to 115MHz.

![](images/aa74066d9cf7cb8fad116c769253fa9a998db3b4a2adfab31c235cea11842397.jpg)  
Figure1-1. RDA5807M Top View

# 1.1 Features

CMOS single-chip fully-integrated FM tuner Low power consumption  Total current consumption lower than 20mA at 3.0V power supply when under normal situation Support worldwide frequency band  50 -115 MHz Support flexible channel spacing mode  100KHz, 200KHz, 50KHz and 25KHz Support RDS/RBDS Digital low-IF tuner  Image-reject down-converter  High performance A/D converter  IF selectivity performed internally Fully integrated digital frequency synthesizer  Fully integrated on-chip RF and IF VCO  Fully integrated on-chip loop filter Autonomous search tuning Support 32.768KHz crystal oscillator Digital auto gain control (AGC) Digital adaptive noise cancellation  Mono/stereo switch

 Soft mute  High cut   
 Programmable de-emphasis (50/75 µs)   
 Receive signal strength indicator (RSSI) and SNR   
 Bass boost   
 Volume control and mute   
 Line-level analog output voltage   
 32.768 KHz 12M,24M,13M,26M,19.2M,38.4MHz Reference clock   
 Only support 2-wire bus interface (id:) Directly support 32Ω resistance loading Integrated LDO regulator  2.7 to 3.3 V operation voltage SOP－8pins

# 1.2 Applications

Cellular handsets

MP3, MP4 players

Portable radios

PDAs, Notebook

# Table of Contents

# 1 General Description .

1.1 Features .......... ........................................................................................................   
1.2 Applications ......

# Table of Contents....

# 2 Functional Description..

2.1 FM Receiver... .3   
2.2 Synthesizer .... .3   
2.3 Power Supply ... .3   
2.4 RESET and Control Interface select . .4   
2.5 Control Interface . 4

# 3 Electrical Characteristics ............ ....

4 Receiver Characteristics ......... ....

5 Serial Interface ..... .... ............

5.1 I 2 C Interface Timing..

6 Register Definition . .8

# 7 Pins Description......... 14

# 8 Application Diagram....... ..16

8.1 Audio Loading Resistance Larger than 32Ω & Reference Clock Application:.... .16   
8.1.1 Bill of Materials: . ... .16   
8.2 Audio Loading Resistance Larger than 32Ω & DCXO Application: ..... 17   
8.2.1 Bill of Materials: . 17

# 9 Physical Dimension ......... 18

# 10 PCB Land Pattern..... 19

# Change List... 21

# 11 Contact Information . 21

# 2 Functional Description

![](images/c7f340966dbf0d0bde49b1423b09639aec062643a0ee0afe1960fd81f26589ff.jpg)  
Figure 2-1. RDA5807MP FM Tuner Block Diagram

# 2.1 FM Receiver

The receiver uses a digital low-IF architecture that avoids the difficulties associated with direct conversion while delivering lower solution cost and reduces complexity, and integrates a low noise amplifier (LNA) supporting the FM broadcast band (50 to 115MHz), a multi-phase image-reject mixer array, a programmable gain control (PGA), a high resolution analog-to-digital converters (ADCs), an audio DSP and a highfidelity digital-to-analog converters (DACs).

The limiter prevents overloading and limits the amount of intermodulation products created by strong adjacent channels.

The multi-phase mixer array down converts the LNA output differential RF signal to low-IF, it also has image-reject function and harmonic tones rejection.

The PGA amplifies the mixer output IF signal and then digitized with ADCs.

The DSP core finishes the channel selection, FM demodulation, stereo MPX decoder and output audio signal. The MPX decoder can autonomous switch from stereo to mono to limit the output

noise.

The DACs convert digital audio signal to analog and change the volume at same time. The DACs has low-pass feature and -3dB frequency is about 30 KHz.

# 2.2 Synthesizer

The frequency synthesizer generates the local oscillator signal which divide to multi-phase, then be used to downconvert the RF input to a constant low intermediate frequency (IF). The synthesizer reference clock is 32.768 KHz.

The synthesizer frequency is defined by bits CHAN[9:0] with the range from 50MHz to 115MHz.

# 2.3 Power Supply

The RDA5807MP integrated one LDO which supplies power to the chip. The external supply voltage range is 2.7-3.3 V.

# 2.4 RESET and Control Interface select

The RDA5807MP is RESET itself When VDD is Power up. And also support soft reset by trigger 02H BIT1 from 0 to 1. The RDA5807MP only support I 2 C control interface bus mode.

# 2.5 Control Interface

The RDA5807MP only supports I 2 C control interface.

The I2 C interface is compliant to I2 C Bus Specification 2.1. It includes two pins: SCLK and SDIO. A I 2 C interface transfer begins with START condition, a command byte and data bytes, each byte has a followed ACK (or NACK) bit, and ends with STOP condition. The command byte includes a 7-bit chip address (0010000b) and a R/W bit. The ACK (or NACK) is always sent out by receiver. When in write transfer, data bytes is written out from MCU, and when in read transfer, data bytes is read out from RDA5807MP. There is no visible register address in I2 C interface transfers. The I2 C interface has a fixed start register address (0x02h for write transfer and 0x0Ah for read transfer), and an internal incremental address counter. If register address meets the end of register file, 0x3Ah, register address will wrap back to 0x00h. For write transfer, MCU programs registers from register 0x02h high byte, then register 0x02h low byte, then register 0x03h high byte, till the last register. RDA5807MP always gives out ACK after every byte, and MCU gives out STOP condition when register programming is finished. For read transfer, after command byte from MCU, RDA5807MP sends out register 0x0Ah high byte, then register 0x0Ah low byte, then register 0x0Bh high byte, till receives NACK from MCU. MCU gives out ACK for data bytes besides last data byte. MCU gives out NACK for last data byte, and then RDA5807MP will return the bus to MCU, and MCU will give out STOP condition.

# 3 Electrical Characteristics

Table 3-1 DC Electrical Specification (Recommended Operation Conditions):   

<table><tr><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=1>DESCRIPTION</td><td rowspan=1 colspan=1>MIN</td><td rowspan=1 colspan=1>TYP</td><td rowspan=1 colspan=1>MAX</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>Supply Voltage</td><td rowspan=1 colspan=1>2.7</td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1>3.3</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Tamb</td><td rowspan=1 colspan=1>Ambient Temperature</td><td rowspan=1 colspan=1>-20</td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1>+75</td><td rowspan=1 colspan=1>°℃</td></tr><tr><td rowspan=1 colspan=1>$V\L</td><td rowspan=1 colspan=1>CMOS Low Level Input Voltage</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.3*VDD</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>ViH</td><td rowspan=1 colspan=1>CMOS High Level Input Voltage</td><td rowspan=1 colspan=1>0.7*VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VTH</td><td rowspan=1 colspan=1>CMOS Threshold Voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.5*VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr></table>

Table 3-2 DC Electrical Specification (Absolute Maximum Ratings):   

<table><tr><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=1>DESCRIPTION</td><td rowspan=1 colspan=1>MIN</td><td rowspan=1 colspan=1>TYP</td><td rowspan=1 colspan=1>MAX</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=1>Tamb</td><td rowspan=1 colspan=1>Ambient Temperature</td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+90</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>IiN</td><td rowspan=1 colspan=1>Input Current 1)</td><td rowspan=1 colspan=1>-10  •</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+10</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>ViN</td><td rowspan=1 colspan=1>Input Voltage(1))</td><td rowspan=1 colspan=1>-0.3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>VDD+0.3</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Vina</td><td rowspan=1 colspan=1>FM Input Level</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+10</td><td rowspan=1 colspan=1>dBm</td></tr></table>

Notes:

# Table 3-3 Power Consumption Specification

(VDD = 3 V, TA = 25℃, unless otherwise specified)

<table><tr><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=1>DESCRIPTION</td><td rowspan=1 colspan=1>CONDITION</td><td rowspan=1 colspan=1>TYP</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=1>IVDD</td><td rowspan=1 colspan=1>Supply Current(1)</td><td rowspan=1 colspan=1>ENABLE=1</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>IvDD</td><td rowspan=1 colspan=1>Supply Current(2)</td><td rowspan=1 colspan=1>ENABLE=1</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>1PD</td><td rowspan=1 colspan=1>Powerdown Current</td><td rowspan=1 colspan=1>ENABLE=0</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>μA</td></tr></table>

1. For Pin: SCLK, SDIO

# Notes:

1. For strong input signal condition   
2. For weak input signal condition

# 4 Receiver Characteristics

# Table 4-1 Receiver Characteristics

(VDD = 3 V, TA = 25 °C, unless otherwise specified)

<table><tr><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=1>PARAMETER</td><td rowspan=1 colspan=2>CONDITIONS</td><td rowspan=1 colspan=1>MIN</td><td rowspan=1 colspan=1>TYP</td><td rowspan=1 colspan=1>MAX</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=8>General specifications</td></tr><tr><td rowspan=1 colspan=1>Fin</td><td rowspan=1 colspan=1>FM Input Frequency Range</td><td rowspan=1 colspan=2>Adjust BAND Register</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>115</td><td rowspan=1 colspan=1>MHz</td></tr><tr><td rowspan=6 colspan=1>Vrf</td><td rowspan=6 colspan=1>Sensitivity1,2.33</td><td rowspan=6 colspan=1>S/N=26dB</td><td rowspan=1 colspan=1>50MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1.4</td><td rowspan=1 colspan=1>1.8</td><td rowspan=6 colspan=1>μV EMF</td></tr><tr><td rowspan=1 colspan=1>65MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>1.5</td></tr><tr><td rowspan=1 colspan=1>88MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1.2</td><td rowspan=1 colspan=1>1.5</td></tr><tr><td rowspan=1 colspan=1>98MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>1.5</td></tr><tr><td rowspan=1 colspan=1>108MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>1.5</td></tr><tr><td rowspan=1 colspan=1>115MHz</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>1.8</td></tr><tr><td rowspan=1 colspan=1>IP3in</td><td rowspan=1 colspan=1>Input IP34</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dBV</td></tr><tr><td rowspan=1 colspan=1>Oam</td><td rowspan=1 colspan=1>AM Suppression 1,2</td><td rowspan=1 colspan=2>m=0.3</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>S200</td><td rowspan=1 colspan=1>Adjacent Channel Selectivity</td><td rowspan=1 colspan=2>±200KHz</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>70</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>S400</td><td rowspan=1 colspan=1>400KHz Selectivity</td><td rowspan=1 colspan=2>±400KHz</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>VAFL; VAFR</td><td rowspan=1 colspan=1>Audio L/R Output Volage12(Pins LOUT and ROUT)</td><td rowspan=1 colspan=2>Volume [3:0] </td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>360</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>mV</td></tr><tr><td rowspan=2 colspan=1>S/N</td><td rowspan=2 colspan=1>Maximum Signal to NoiseRatio1,23.5</td><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1>Mono²</td><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>57</td><td rowspan=1 colspan=1>-</td><td rowspan=2 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>Stereo6</td><td rowspan=1 colspan=1>53</td><td rowspan=1 colspan=1>55</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>ascs</td><td rowspan=1 colspan=1>Stereo Channel Separation</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>RL</td><td rowspan=1 colspan=1>Audio Output LoadingResistance</td><td rowspan=1 colspan=2>ingle-ended</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>Ω</td></tr><tr><td rowspan=2 colspan=1>THD</td><td rowspan=2 colspan=1>Distortion11,3,6</td><td rowspan=2 colspan=1>=1111</td><td rowspan=1 colspan=1>Rload=1KΩ</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1>0.2</td><td rowspan=2 colspan=1>%</td></tr><tr><td rowspan=1 colspan=1>Rload=32Ω2</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=1>QAOI</td><td rowspan=1 colspan=1>AudioImbalance1.6</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=1 colspan=1>Rmute</td><td rowspan=1 colspan=1>Mute Attenuation Ratio1</td><td rowspan=1 colspan=2>Volume[3:0]=0000</td><td rowspan=1 colspan=1>60</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>dB</td></tr><tr><td rowspan=2 colspan=1>BWaudio</td><td rowspan=2 colspan=1>Audio Response&#x27;</td><td rowspan=2 colspan=1>1KHz=0dB±3dB point</td><td rowspan=1 colspan=1>Low Freq</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>-</td><td rowspan=2 colspan=1>Hz</td></tr><tr><td rowspan=1 colspan=1>High Freq</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>-</td></tr><tr><td rowspan=1 colspan=8>Pins FMIN, LOUT, ROUT</td></tr><tr><td rowspan=1 colspan=1>Vcom_rin</td><td rowspan=1 colspan=1>PinsFMINInputCommonMode Voltage</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Vcom</td><td rowspan=1 colspan=1>Audio Output Common ModeVoltage8</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>1.0</td><td rowspan=1 colspan=1>1.05</td><td rowspan=1 colspan=1>1.1</td><td rowspan=1 colspan=1>V</td></tr></table>

Notes:1. Fin=65 to 115MHz; Fmod=1KHz; de-emphasis=75µs; MONO=1; L=R unless noted otherwise;

2. ∆f=22.5KHz; 3. B = 300Hz to 15KHz, RBW <=10Hz; 4. |f -f |>1MHz, f =2xf -f , AGC disable, F =76 to 108MHz;   
5. PRF=60dBUV; 6. ∆f=75KHz,fpilot=10% 7. Measured at VEMF = 1 m V, f RF = 65 to 108MHz   
8. At LOUT and ROUT pins 9. Adjustable

# 5 Serial Interface

# 5.1 I 2 C Interface Timing

# Table 5-1 I 2 C Interface Timing Characteristics

(VDD = 3 V, TA = 25 °C, unless otherwise specified)

<table><tr><td rowspan=1 colspan=1>PARAMETER</td><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=1>TEST CONDITION</td><td rowspan=1 colspan=1>MIN</td><td rowspan=1 colspan=1>TYP</td><td rowspan=1 colspan=1>MAX</td><td rowspan=1 colspan=1>UNIT</td></tr><tr><td rowspan=1 colspan=1>SCLK Frequency</td><td rowspan=1 colspan=1>fscl</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>KHz</td></tr><tr><td rowspan=1 colspan=1>SCLK High Time</td><td rowspan=1 colspan=1>thigh</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>SCLK Low Time</td><td rowspan=1 colspan=1>tlow</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>Setup Time for START Condition</td><td rowspan=1 colspan=1>tsu.sta</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>Hold Time for START Condition</td><td rowspan=1 colspan=1>tnd:sta</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>Setup Time for STOP Condition</td><td rowspan=1 colspan=1>tsu:sto</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>SDIO Input to SCLK↑ Setup</td><td rowspan=1 colspan=1>tsu:.dat</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>SDIO Input to SCLK↓ Hold</td><td rowspan=1 colspan=1>thd:dat</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>900</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>STOP to START Time</td><td rowspan=1 colspan=1>tbuf</td><td rowspan=1 colspan=1>•</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>SDIO Output Fall Time</td><td rowspan=1 colspan=1>tf:out</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20+0.1C</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>SDIO Input, SCLK Rise/Fall Time</td><td rowspan=1 colspan=1>trin tein</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>20+0.1Cb</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>300</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>Input Spike Suppression</td><td rowspan=1 colspan=1>tsp</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>SCLK, SDIO Capacitive Loading</td><td rowspan=1 colspan=1>$Cb$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>pF</td></tr><tr><td rowspan=1 colspan=1>Digital Input Pin Capacitance</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>pF</td></tr></table>

![](images/bee0056b6e0dbc177fb07da89d1f6eb9f7deed86020404775738f09c01e7ae9d.jpg)  
Figure 5-1. I 2 C Interface Write Timing Diagram

![](images/49c94e1b9f1506be736b151e890692e11db637c58b77a81c431d4f155dcbe1ac.jpg)  
Figure 5-2. I 2 C Interface Read Timing Diagram

# 6 Register Definition

<table><tr><td colspan="1" rowspan="1">REG</td><td colspan="1" rowspan="1">BITS</td><td colspan="1" rowspan="1">NAME</td><td colspan="1" rowspan="1">FUNCTION</td><td colspan="1" rowspan="1">DEFAULT</td></tr><tr><td colspan="1" rowspan="1">00H</td><td colspan="1" rowspan="1">15:0</td><td colspan="1" rowspan="1">CHIPID[7:0]</td><td colspan="1" rowspan="1">Chip ID.</td><td colspan="1" rowspan="1">0x5804</td></tr><tr><td colspan="1" rowspan="1">02H</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">DHIZ</td><td colspan="1" rowspan="1">Audio Output High-Z Disable.0 = High impedance; 1 = Normal operation</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">DMUTE</td><td colspan="1" rowspan="1">Mute Disable.0 = Mute; 1 = Normal operation</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">MONO</td><td colspan="1" rowspan="1">Mono Select.0 = Stereo; 1 = Force mono</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">BASS</td><td colspan="1" rowspan="1">Bass Boost.0 = Disabled; 1 = Bass boost enabled</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">RCLK    NON-CALIBRATEMODE</td><td colspan="1" rowspan="1">0=RCLK clock is always supply1=RCLK clock is not always supply when FMwork ( when 1, RDA5807MP can't directlysupport -20℃ ~70 ℃ temperature. Onlypoint)</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">RCLK DIRECT INPUT MODE</td><td colspan="1" rowspan="1">1=RCLK clock use the directly input mode</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">SEEKUP</td><td colspan="1" rowspan="1">Seek Up.0 = Seek down;</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">SEEK</td><td colspan="1" rowspan="1">Seek.1 = Enable</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">SKMODE</td><td colspan="1" rowspan="1">0 = wrap at the upper or lower band limit andcontinue seeking1 = stop seeking at the upper or lower bandlimit</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">6:4</td><td colspan="1" rowspan="1">CLK_MODE[2:0]</td><td colspan="1" rowspan="1">000=32.768kHz001=12Mhz101=24Mhz010=13Mhz110=26Mhz011=19.2Mhz111=38.4Mhz</td><td colspan="1" rowspan="1">000</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">RDS_EN</td><td colspan="1" rowspan="1">RDS/RBDS enableIf 1, rds/rbds enable</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">NEW_METHOD</td><td colspan="1" rowspan="1">New Demodulate Method Enable, can improvethe receive sensitivity about 1dB.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">SOFT_RESET</td><td colspan="1" rowspan="1">Soft reset.If 0, not reset;</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">If 1, reset.</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">ENABLE</td><td colspan="1" rowspan="1">Power Up Enable.0 = Disabled; 1 = Enabled</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1">03H</td><td colspan="1" rowspan="1">15:6</td><td colspan="1" rowspan="1">CHAN[9:0]</td><td colspan="1" rowspan="1">Channel Select.BAND = 0Frequency =Channel Spacing (kHz) x CHAN+ 87.0 MHzBAND = 1or 2Frequency =Channel Spacing (kHz) × CHAN + 76.0 MHzBAND = 3Frequency =Channel Spacing (kHz) x CHAN + 65.0 MHzCHAN is updated after a seek operation.</td><td colspan="1" rowspan="1">0x13f</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">DIRECT MODE</td><td colspan="1" rowspan="1">Directly Control Mode, Only used when test.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">TUNE</td><td colspan="1" rowspan="1">Tune0 = Disable1 = EnableThe tune operation begins when the TuNE bitis set high. The STC bit is set high when thetune operation completes.The tune bit is reset to low automatically whenthe tune operation completes..</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3:2</td><td colspan="1" rowspan="1">BAND[1:0]</td><td colspan="1" rowspan="1">Band Select.00=87-108 MHz (US/Europe)= 65 –76 MHz (East Europe) or 50-65MHz</td><td colspan="1" rowspan="1">00</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1:0</td><td colspan="1" rowspan="1">SPACE[1:0]</td><td colspan="1" rowspan="1">Channel Spacing.00= 100 kHz01 = 200 kHz10 = 50kHz11 =25KHz</td><td colspan="1" rowspan="1">00</td></tr><tr><td colspan="1" rowspan="1">04H</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">RSVD</td><td colspan="1" rowspan="1">Reserved</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">STCIEN</td><td colspan="1" rowspan="1">Seek/Tune Complete Interrupt Enable.0 = Disable Interrupt1 = Enable InterruptSetting STCIEN = 1 will generate a lowpulse on GPIO2 when the interruptoccurs.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">RBDS</td><td colspan="1" rowspan="1">1 = RBDS mode enable0 = RDS mode only</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">RDS_FIFO_EN</td><td colspan="1" rowspan="1">1 = RDS fifo mode enable.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">DE</td><td colspan="1" rowspan="1">De-emphasis.0 = 75 μs; 1 = 50 μs</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">RDS_FIFO_CLR</td><td colspan="1" rowspan="1">1 = clear RDS fifo</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">SOFTMUTE_EN</td><td colspan="1" rowspan="1">If 1, softmute enable</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">AFCD</td><td colspan="1" rowspan="1">AFC disable.If 0, afc work;If 1, afc disabled.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">rsvd</td><td colspan="1" rowspan="1">Read as 0.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">I2S_ENABLE</td><td colspan="1" rowspan="1">I2S enable.0 = disabled;1 = enabled.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">5:4</td><td colspan="1" rowspan="1">GPIO3[1:0]</td><td colspan="1" rowspan="1">General    Purpose    1O    3.whengpio_sel=00or1100 = High impedance01 = Mono/Stereo indicator (ST)10 = Low11 = High</td><td colspan="1" rowspan="1">00</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3:2</td><td colspan="1" rowspan="1">GPIO2[1:0]</td><td colspan="1" rowspan="1">00 = High impedance01 = Interrupt (IN10 = Low11= High</td><td colspan="1" rowspan="1">00</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1:0</td><td colspan="1" rowspan="1">GPIO1[1:0]</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">00</td></tr><tr><td colspan="1" rowspan="1">05H</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">INT _MODE</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">14:13</td><td colspan="1" rowspan="1">Seek_mode</td><td colspan="1" rowspan="1">Default value is 00; When = 10, will add theRSSI seek mode.</td><td colspan="1" rowspan="1">00</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">RSVD</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">11:8</td><td colspan="1" rowspan="1">SEEKTH[3:0]²}</td><td colspan="1" rowspan="1">Seek SNR threshold value</td><td colspan="1" rowspan="1">1000</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">7:6</td><td colspan="1" rowspan="1">LNA_PORT_SEL[1:0]</td><td colspan="1" rowspan="1">LNA input port selection bit:00: no input01: LNAN10: LNAP11: dual port input</td><td colspan="1" rowspan="1">10</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">5:4</td><td colspan="1" rowspan="1">LNA_ICSEL_BIT[1:0]</td><td colspan="1" rowspan="1">Lna working current bit:00=1.8mA01=2.1mA10=2.5mA11=3.0mA</td><td colspan="1" rowspan="1">00</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3:0</td><td colspan="1" rowspan="1">VOLUME[3:0]</td><td colspan="1" rowspan="1">DAC Gain Control Bits (Volume).0000=min; 1111=max</td><td colspan="1" rowspan="1">1011</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Volume scale is logarithmicWhen ooo0, output mute and outputimpedance is very large</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">06H</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">RSVD</td><td colspan="1" rowspan="1">reserved</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">14:13</td><td colspan="1" rowspan="1">OPEN_MODE[1:0]</td><td colspan="1" rowspan="1">Open reserved register mode.11=open behind registers writing functionothers: only open behind registers readingfunction</td><td colspan="1" rowspan="1">00</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">slave_master</td><td colspan="1" rowspan="1">I2S slave or master.1 = slave;0 = master.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">ws_lIr</td><td colspan="1" rowspan="1">Ws relation to l/r channel.If 0, ws=0 -&gt;r, ws=1 -&gt;1;If 1, ws=0 -&gt;1, ws=1 -&gt;r.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">sclk_i_edge</td><td colspan="1" rowspan="1">If 0, use normal sclk internallly:If 1, inverte sclk internally.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">data_signed</td><td colspan="1" rowspan="1">data.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">WS_I_EDGE</td><td colspan="1" rowspan="1">If O, use normal ws inermally; If 1, inverte ws internally.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">7:4</td><td colspan="1" rowspan="1">I2S_SW_CNT[4:0]Only validin master mode</td><td colspan="1" rowspan="1">4"b1000: WS_STEP_48;4'b0111: WS_STEP=44.1kbps;4'b0110: WS_STEP=32kbpS;4"b0101: WS_STEP=24kbpS;4b0100: WS_STEP=22.05kbps;4"b0011: WS_STEP=16kbps;</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">SW_O_EDGE</td><td colspan="1" rowspan="1">If 1, 1, invert ws output when as master.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">SClK_O_eDGe</td><td colspan="1" rowspan="1">If 1, invert sclk output when as master.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">L_DELY</td><td colspan="1" rowspan="1">If 1, L channel data delay 1T.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">R_DELY</td><td colspan="1" rowspan="1">If 1, R channel data delay 1T.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1">07H</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">RSVD</td><td colspan="1" rowspan="1">Reserved</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">14:10</td><td colspan="1" rowspan="1">TH_SOFRBLEND[5:0]</td><td colspan="1" rowspan="1">Threshold for noise soft blend setting, unit2dB</td><td colspan="1" rowspan="1">10000</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">65M_50M MODE</td><td colspan="1" rowspan="1">Valid when band[1:0] = 2'b11 (0x03H_bit&lt;3:2&gt;)1=65~76 MHz;0 = 50~76 MHz.</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">RSVD</td><td colspan="1" rowspan="1">Reserved</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">7:2</td><td colspan="1" rowspan="1">SEEK_TH_OLD</td><td colspan="1" rowspan="1">Seek threshold for old seek mode, Valid whenSeek_Mode=10</td><td colspan="1" rowspan="1">000000</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">SOFTBLEND_EN</td><td colspan="1" rowspan="1">If 1, Softblend enable</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">FREQ_MODE</td><td colspan="1" rowspan="1"> If 1, then freq setting changed.Freq = 76000(or 87000) kHz + freq_direct (08H)kHz.</td><td colspan="1" rowspan="1">0</td></tr></table>

The information contained herein is the exclusive property of RDA and shall not be distributed, reproduced, or disclosed in whole or in part without prior written permission of RDA. Page 11 of 21

<table><tr><td colspan="1" rowspan="1">REG</td><td colspan="1" rowspan="1">BITS</td><td colspan="1" rowspan="1">NAME</td><td colspan="1" rowspan="1">FUNCTION</td><td colspan="1" rowspan="1">DEFAULT</td></tr><tr><td colspan="1" rowspan="1">08H</td><td colspan="1" rowspan="1">15:0</td><td colspan="1" rowspan="1">freq_direct[15:0]</td><td colspan="1" rowspan="1">Valid when freq_mode = 1.</td><td colspan="1" rowspan="1">0x0</td></tr><tr><td colspan="1" rowspan="1">0AH</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">RDSR</td><td colspan="1" rowspan="1">RDS ready0 = No RDS/RBDS group ready(default)1 = New RDS/RBDS group ready</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">STC</td><td colspan="1" rowspan="1">Seek/Tune Complete.0 = Not complete1 = CompleteThe seek/tune complete flag is set when theseek or tune operation completes.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">SF</td><td colspan="1" rowspan="1">Seek Fail.0 = Seek successful; 1 = Seek failureThe seek fail flag is set when the seekoperation fails to find a channel with an RssIlevel greater than SEEKTH[3:0].</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">RDSS</td><td colspan="1" rowspan="1">RDS Synchronization0 = RDs decoder not synchronized(default)1 = RDS decoder synchronizedAvailable only in RDS Verbose mode</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">BLK_E</td><td colspan="1" rowspan="1">When RDS enable:1 = Block E has been found0 = no Block E has been found</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">ST</td><td colspan="1" rowspan="1">Stereo Indicator.0 = Mono; 1 = Stereo</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">9:0</td><td colspan="1" rowspan="1">READCHAN[9:0]</td><td colspan="1" rowspan="1">BAND = 1 or 2Frequency = Channel Spacing (kHz) xREADCHAN[9:0]+ 76.0 MHzBAND = 3Frequency = Channel Spacing (kHz) xREADCHAN[9:0]+ 65.0 MHzREADCHAN[9:0] is updated after a tune orseek operation.</td><td colspan="1" rowspan="1">8'h00</td></tr><tr><td colspan="1" rowspan="1">OBH</td><td colspan="1" rowspan="1">15:9</td><td colspan="1" rowspan="1">RSSI[6:0]</td><td colspan="1" rowspan="1">RSSI.000000 = min111111 = maxRSSI scale is logarithmic.</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">FM TRUE</td><td colspan="1" rowspan="1">1 = the current channel is a station0 = the current channel is not a station</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">FM_READY</td><td colspan="1" rowspan="1">1=ready0=not ready</td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">&lt;6:5&gt;</td><td colspan="1" rowspan="1">reserved</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">&lt;4&gt;</td><td colspan="1" rowspan="1">ABCD_E</td><td colspan="1" rowspan="1">1= the block id of register OcH,0dH,0eH,ofH is EO= the block id of register OcH, OdH, OeH,ofH isA,B, C, D</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">&lt;3:2&gt;</td><td colspan="1" rowspan="1">BLERA[1:0]</td><td colspan="1" rowspan="1">Block Errors Level of RDS_DATA_0, and isalways read as Errors Level of RDS BLOcK A(in RDS mode) or BLOCK E (in RBDS modewhen ABCD_E flag is 1)00= 0 errors requiring correction01= 1~2 errors requiring correction10= 3~5 errors requiring correction11= 6+ errors or error in checkword, correctionnot possible.Available only in RDS Verbose mode</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">&lt;1:0&gt;</td><td colspan="1" rowspan="1">BLERB[1:0]</td><td colspan="1" rowspan="1">Block Errors Level of RDS_DATA_1, and isalways read as Errors Level of RDS BLOcK B(in RDS mode ) or E (in RBDS mode whenABCD_E flag is 1).00= 0 errors requiring correction-01= 1~2 errors requiring correction10= 3~5 errors requiring correction11= 6+ errors or error in checkword, correctionnot possible.Available only in RDs Verbose mode</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">OCH</td><td colspan="1" rowspan="1">&lt;15:0&gt;</td><td colspan="1" rowspan="1">RDSA[15:0]</td><td colspan="1" rowspan="1">BLOCK A（in RDSmode) or BLOcK E (inRBDS mode when ABCD_E flag is 1)</td><td colspan="1" rowspan="1">16'h5803</td></tr><tr><td colspan="1" rowspan="1">ODH</td><td colspan="1" rowspan="1">&lt;15:0&gt;</td><td colspan="1" rowspan="1">RDSB[15:0]</td><td colspan="1" rowspan="1">BLock B ( in RDS mode) or BLOCK E (in</td><td colspan="1" rowspan="1">16'h5804</td></tr><tr><td colspan="1" rowspan="1">OEH</td><td colspan="1" rowspan="1">&lt;15:0&gt;</td><td colspan="1" rowspan="1">RDSC[15:0]</td><td colspan="1" rowspan="1">BLOCK C ( in RDS mode) or BLOCK E (inRBDS mode when ABCD_E flag is 1)</td><td colspan="1" rowspan="1">16'h5808</td></tr><tr><td colspan="1" rowspan="1">OFH</td><td colspan="1" rowspan="1">&lt;15:0&gt;</td><td colspan="1" rowspan="1">RDSD[15::0]</td><td colspan="1" rowspan="1">BLOCK D ( in RDS mode) or BLOCK E (inRBDS mode when ABCD_E flag is 1)</td><td colspan="1" rowspan="1">16'h5804</td></tr></table>

# 7 Pins Description

![](images/6d5a1172ca3e3774c287051540ef9530444d159f8a4c58a62e43de228e64aee3.jpg)  
Figure 7-1. RDA5807MP Top View

![](images/927aaac02c850b70b7abee36fe9542ce176c44151ccb80e977e17de7a6f36bd8.jpg)

Table 7-1 RDA5807MP Pins Description   

<table><tr><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=2>PIN</td><td rowspan=1 colspan=1>DESCRIPTION</td></tr><tr><td rowspan=1 colspan=1>FMIN</td><td rowspan=1 colspan=2>1</td><td rowspan=1 colspan=1>FM single input</td></tr><tr><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=1>Ground.Connect to ground planeon PCB</td></tr><tr><td rowspan=1 colspan=1>SCLK</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>Clock input for serial control bus</td></tr><tr><td rowspan=1 colspan=1>SDIO</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>Data input/output for serial controlbus</td></tr><tr><td rowspan=1 colspan=1>RCLK</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>32.768KHz crystal oscillator andreference clock input</td></tr><tr><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=2>6</td><td rowspan=1 colspan=1>Power supply</td></tr><tr><td rowspan=1 colspan=1>ROUT,LOUT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>7,8</td><td rowspan=1 colspan=1>Right/Left audio output</td></tr></table>

Table 7-2 Internal Pin Configuration   

<table><tr><td>SYMBOL</td><td>PIN</td></tr><tr><td>FMIN</td><td>FMs 2 FMIN MN1 50pF</td></tr><tr><td>RCLK</td><td>VDD 本 W5M RCLK 20pF 6 Confidentia</td></tr><tr><td>SDIO /SCLK</td><td>W47K SDIOISCLK 5/4 MN1</td></tr></table>

# 8 Application Diagram

# 8.1 Audio Loading Resistance Larger than 32Ω & Reference Clock Application:

Notes:

1. J1: Common 32Ω Resistance Headphone; 2. U1: RDA5807MP Chip; 3. V1: Power Supply (2.7\~3.3V); 4. FM Choke (L1 and C1) for Audio Common and LNA Input Common; 5. Place C2 Close to 5807MP pin1 LK6. Place C3 Close to 5807MP pin6

![](images/7c36460ce55bc200d6ffd9bf9f5f4fcf98e12b41fd3540316b30a8552660ff3d.jpg)  
Figure 8-1. RDA5807MP FM Tuner Application Diagram (Reference Clock Application)

# 8.1.1 Bill of Materials:

![](images/b8b6559edfac38f63dd116b11f7a051bee8b159e59a26bd6373d527428d20045.jpg)

<table><tr><td rowspan=1 colspan=1>COMPONENT</td><td rowspan=1 colspan=1>VALUE</td><td rowspan=1 colspan=1>DESCRIPTION</td><td rowspan=1 colspan=1>SUPPLIER</td></tr><tr><td rowspan=1 colspan=1>U1</td><td rowspan=1 colspan=1>RDA5807MP</td><td rowspan=1 colspan=1>Broadcast FM Radio Tuner</td><td rowspan=1 colspan=1>RDA</td></tr><tr><td rowspan=1 colspan=1>J1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Common 32Q Resistance Headphone</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1</td><td rowspan=1 colspan=1>100nH</td><td rowspan=1 colspan=1>LC Chock for FMIN Input</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C1</td><td rowspan=1 colspan=1>24pF</td><td rowspan=1 colspan=1>Capacitor</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C2</td><td rowspan=1 colspan=1>100pF</td><td rowspan=1 colspan=1>AC Couple Capacitors</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C3</td><td rowspan=1 colspan=1>22nF</td><td rowspan=1 colspan=1>Power Supply Bypass Capacitor</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C4,C5</td><td rowspan=1 colspan=1>4.7μF</td><td rowspan=1 colspan=1>Audio AC Couple Capacitors</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>F1/F2</td><td rowspan=1 colspan=1>1.8K@100MHz</td><td rowspan=1 colspan=1>FM Band Ferrite</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>R1,R2</td><td rowspan=1 colspan=1>10KΩ</td><td rowspan=1 colspan=1>I²C Bus Pull-up Resister</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>R3</td><td rowspan=1 colspan=1>NC/2M</td><td rowspan=1 colspan=1>Adjust clock.</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C6</td><td rowspan=1 colspan=1>0R/47pF</td><td rowspan=1 colspan=1>Adjust clock.</td><td rowspan=1 colspan=1>Murata</td></tr></table>

# 8.2 Audio Loading Resistance Larger than 32Ω & DCXO Application:

Notes:

![](images/e6d65f4bbc97a77fc974ab351e8451e395c0192eac9199f2bbfb29a50ccfaf10.jpg)  
Figure 8-2. RDA5807MP FM Tuner Application Diagram (32.768K crystal)

1. J1: Common 32Ω Resistance Headphone;   
2. U1: RDA5807MP Chip;   
3. V1: Power Supply (2.7\~3.3V);   
4. FM Choke (L1 and C1) for Audio Common and LNA Input Common;   
5. Place C2 Close to 5807MP pin1   
6. Place C3 Close to 5807MP pin6

# 8.2.1 Bill of Materials:

<table><tr><td rowspan=1 colspan=1>COMPONENT</td><td rowspan=1 colspan=1>VALUE</td><td rowspan=1 colspan=1>DESCRIPTION</td><td rowspan=1 colspan=1>SUPPLIER</td></tr><tr><td rowspan=1 colspan=1>U1</td><td rowspan=1 colspan=1>RDA5807MP</td><td rowspan=1 colspan=1>Broadcast FM Radio Tuner</td><td rowspan=1 colspan=1>RDA</td></tr><tr><td rowspan=1 colspan=1>J1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Common 32Ω Resistance Headphone</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L1</td><td rowspan=1 colspan=1>100nH</td><td rowspan=1 colspan=1>LC Chock for FMIN Input</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C1</td><td rowspan=1 colspan=1>24pF</td><td rowspan=1 colspan=1>Capacitor</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C2</td><td rowspan=1 colspan=1>100pF</td><td rowspan=1 colspan=1>AC Couple Capacitors</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C3</td><td rowspan=1 colspan=1>22nF</td><td rowspan=1 colspan=1>Power Supply Bypass Capacitor</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>C4,C5</td><td rowspan=1 colspan=1>4.7μF</td><td rowspan=1 colspan=1>Audio AC Couple Capacitors</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>F1/F2</td><td rowspan=1 colspan=1>1.8K@100MHz</td><td rowspan=1 colspan=1>FM Band Ferrite</td><td rowspan=1 colspan=1>Murata</td></tr><tr><td rowspan=1 colspan=1>R1,R2</td><td rowspan=1 colspan=1>10KΩ</td><td rowspan=1 colspan=1>I2C Bus Pull-up Resister</td><td rowspan=1 colspan=1>Murata</td></tr></table>

# Physical Dimension

Figure 9-1 illustrates the package details for the RDA5807MP. The package is lead-free and RoHS-compliant.

![](images/984b158f74b1a5a5aa1d9d4a297c56072184a89fc4dffd2045a25f0a538d5a9f.jpg)  
Figure 9-1. 8-Pin SOP

DIMENsiONs (inch dimensions are derived from the original mm dimensions)   

<table><tr><td rowspan=1 colspan=1>UNIT</td><td rowspan=1 colspan=1>Amax.</td><td rowspan=1 colspan=1>A1</td><td rowspan=1 colspan=1>A2$</td><td rowspan=1 colspan=1>A3</td><td rowspan=1 colspan=1>bp</td><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>D(1)</td><td rowspan=1 colspan=1>E(2)</td><td rowspan=1 colspan=1>e</td><td rowspan=1 colspan=1>HE</td><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>Lp</td><td rowspan=1 colspan=1>Q</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>w</td><td rowspan=1 colspan=1>y</td><td rowspan=1 colspan=1>z(1)</td><td rowspan=1 colspan=1>θ</td></tr><tr><td rowspan=1 colspan=1>mm</td><td rowspan=1 colspan=1>1.75</td><td rowspan=1 colspan=1>0.250.10</td><td rowspan=1 colspan=1>1.451.25</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.490.36</td><td rowspan=1 colspan=1>0.250.19</td><td rowspan=1 colspan=1>5.04.8</td><td rowspan=1 colspan=1>4.03.8</td><td rowspan=1 colspan=1>1.27</td><td rowspan=1 colspan=1>6.25.8</td><td rowspan=1 colspan=1>1.05</td><td rowspan=1 colspan=1>1.00.4</td><td rowspan=1 colspan=1>0.70.6</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1>0.70.3</td><td rowspan=2 colspan=1>$ $</td></tr><tr><td rowspan=1 colspan=1>inches</td><td rowspan=1 colspan=1>0.069</td><td rowspan=1 colspan=1>0.0100.004</td><td rowspan=1 colspan=1>0.0570.049</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>0.0190.014</td><td rowspan=1 colspan=1>0.01000.0075</td><td rowspan=1 colspan=1>0.200.19</td><td rowspan=1 colspan=1>0.160.15</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1>0.2440.228</td><td rowspan=1 colspan=1>0.041</td><td rowspan=1 colspan=1>0.0390.016</td><td rowspan=1 colspan=1>0.0280.024</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>0.004</td><td rowspan=1 colspan=1>0.0280.012</td></tr></table>

# Notes

1. Plastic or metal protusions of 0.15 mm (0.006 inch) maximum per side are notincluded.   
2. Plastic or metal protrusions of 0.25 mm (0.01 inch) maximn um per side are not included.

<table><tr><td rowspan=2 colspan=1>OUTLINEVERSION</td><td rowspan=1 colspan=4>REFERENCES</td><td rowspan=2 colspan=1>EUROPEANPROJECTION</td><td rowspan=2 colspan=1>ISSUE DATE</td></tr><tr><td rowspan=1 colspan=1>IEC</td><td rowspan=1 colspan=1>JEDEC</td><td rowspan=1 colspan=1>JEITA</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>SOT96-1</td><td rowspan=1 colspan=1>076E03</td><td rowspan=1 colspan=1>MS-012</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>99-12-2703-02-18</td></tr></table>

# 9 PCB Land Pattern

![](images/29ca3f906709ec983ec6a2d0120e2ca6db35c9b6e1bb49e73bdb7575d70218a1.jpg)  
Figure 10-1.Classification Reflow Profile

<table><tr><td rowspan=1 colspan=1>Profile Feature</td><td rowspan=1 colspan=1>Sn-Pb Eutectic Assembly</td><td rowspan=1 colspan=1>Pb-Free Assembly</td></tr><tr><td rowspan=1 colspan=1>Average Ramp-Up Rate(Tsmax to Tp)</td><td rowspan=1 colspan=1>3 C/second max.</td><td rowspan=1 colspan=1>3 °C/second max.</td></tr><tr><td rowspan=1 colspan=1>Preheat-Temperature Min (Tsmin)-Temperature Max(Tsmax)-Time (tsmin to tsmax)</td><td rowspan=1 colspan=1>100℃100℃60-120 seconds</td><td rowspan=1 colspan=1>150℃200℃60-180 seconds</td></tr><tr><td rowspan=1 colspan=1>Time maintained above:-Temperature (TL)-Time (tL)</td><td rowspan=1 colspan=1>183℃60-150seconds</td><td rowspan=1 colspan=1>217℃60-150 seconds</td></tr><tr><td rowspan=1 colspan=1>Peak /ClassificationTemperature(Tp)</td><td rowspan=1 colspan=1>See Table-ll</td><td rowspan=1 colspan=1>See Table-llI</td></tr><tr><td rowspan=1 colspan=1>Time within 5 °C of actualPeak Temperature (tp)</td><td rowspan=1 colspan=1>10-30 seconds</td><td rowspan=1 colspan=1>20-40 seconds</td></tr><tr><td rowspan=1 colspan=1>Ramp-Down Rate</td><td rowspan=1 colspan=1>6 C/second max.</td><td rowspan=1 colspan=1>6 °C/seconds max.</td></tr><tr><td rowspan=1 colspan=1>Time 25 °C to PeakTemperature</td><td rowspan=1 colspan=1>6 minutes max.</td><td rowspan=1 colspan=1>8 minutes max.</td></tr></table>

# Table-I Classification Reflow Profiles

Table – II SnPb Eutectic Process – Package Peak Reflow Temperatures   

<table><tr><td rowspan=1 colspan=1>Package Thickness</td><td rowspan=1 colspan=1>Volume mm³&lt;350</td><td rowspan=1 colspan=1>Volume mm³≥350</td></tr><tr><td rowspan=1 colspan=1>&lt;2.5mm</td><td rowspan=1 colspan=1>240 + 0/-5°C</td><td rowspan=1 colspan=1>225 + 0/-5°C</td></tr><tr><td rowspan=1 colspan=1>≥2.5mm</td><td rowspan=1 colspan=1>225+ 0/-5°℃</td><td rowspan=1 colspan=1>225+ 0/-5°℃</td></tr></table>

<table><tr><td rowspan=1 colspan=1>PackageThickness</td><td rowspan=1 colspan=1>Volume mm³&lt;350</td><td rowspan=1 colspan=1>Volume mm³350-2000</td><td rowspan=1 colspan=1>Volume mm³&gt;2000</td></tr><tr><td rowspan=1 colspan=1>&lt;1.6mm</td><td rowspan=1 colspan=1>260+0°C*</td><td rowspan=1 colspan=1>260+0°℃*</td><td rowspan=1 colspan=1>260+0°C*</td></tr><tr><td rowspan=1 colspan=1>1.6mm-2.5mm</td><td rowspan=1 colspan=1>260+0°℃*</td><td rowspan=1 colspan=1>250+0°℃*</td><td rowspan=1 colspan=1>245+0°C*</td></tr><tr><td rowspan=1 colspan=1>≥2.5mm</td><td rowspan=1 colspan=1>250+0°C*</td><td rowspan=1 colspan=1>245+0°C*-</td><td rowspan=1 colspan=1>245+0°C*</td></tr><tr><td rowspan=1 colspan=4>*Tolerance : The device manufacturer/supplier shall assure process compatibility up to andincluding the stated classification temperature(this mean Peak reflow temperature + 0 °C. Forexample 260+ 0 °C ) at the rated MSL Level.</td></tr></table>

# Table – III Pb-free Process – Package Classification Reflow Temperatures

Note 1: All temperature refer topside of the package. Measured on the package body surface.

Note 2: The profiling tolerance is - X o C (based on machine variation capability)whatever is required to control the profile process but at no time will it exceed - 5 o C. The producer assures process compatibility at the peak reflow profile temperatures defined in Table –III.

Note 3: Package volume excludes external terminals(balls, bumps, lands, leads) and/or non integral heat sinks.

Note 4: The maximum component temperature reached during reflow depends on package the thickness and volume. The use of convection reflow processes reduces the thermal gradients between packages. However, thermal gradients due to differences in thermal mass of SMD package may sill exist.

Note 5: Components intended for use in a “lead-free” assembly process shall be evaluated using the “lead free” classification temperatures and profiles defined in Table-I II III whether or not lead free.

# RoHS Compliant

The product does not contain lead, mercury, cadmium, hexavalent chromium, polybrominated biphenyls (PBB) or polybrominated diphenyl ethers (PBDE), and are therefore considered RoHS compliant.

# ESD Sensitivity

Integrated circuits are ESD sensitive and can be damaged by static electricity. Proper ESD techniques should be used when handling these devices.

# Change List

<table><tr><td rowspan=1 colspan=1>REV</td><td rowspan=1 colspan=1>DATE</td><td rowspan=1 colspan=1>AUTHER</td><td rowspan=1 colspan=1>CHANGE DESCRIPTION</td></tr><tr><td rowspan=1 colspan=1>V1.0</td><td rowspan=1 colspan=1>2015-07-21</td><td rowspan=1 colspan=1>Zeng Rian</td><td rowspan=1 colspan=1>Original Draft.</td></tr></table>

# 10 Contact Information

RDA Microelectronics (Shanghai), Inc.

Suite 1108 Block A, e-Wing Center, 113 Zhichun Road Haidian District, Beijing

Tel: 86-10-62635360   
Fax: 86-10-82612663   
Postal Code: 100086

Suite 302 Building 2, 690 Bibo Road Pudong District, Shanghai Tel: 86-21-50271108 Fax: 86-21-50271099 Postal Code: 201203

# Copyright © RDA Microelectronics Inc. 2006. All rights are reserved.

Reproduction in whole or in part is prohibited without the prior written consent of the copyright owner.