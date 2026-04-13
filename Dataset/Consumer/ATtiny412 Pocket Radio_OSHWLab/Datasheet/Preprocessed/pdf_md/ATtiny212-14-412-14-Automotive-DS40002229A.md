# tinyAVR® 1-series

# Introduction

The ATtiny212/214/412/414 Automotive are members of the tinyAVR® 1-series of microcontrollers, using the AVR® processor with hardware multiplier, running at up to 16 MHz, with 2/4 KB Flash, 128/256 bytes of SRAM, and 64/128 bytes of EEPROM in a 8- and 14-pin package. The tinyAVR® 1-series uses the latest technologies with a flexible, low-power architecture, including Event System, accurate analog features, and Core Independent Peripherals (CIPs).

# Features

# • CPU

AVR® CPU Running at up to 16 MHz Single-cycle I/O access Two-level interrupt controller Two-cycle hardware multiplier

• Memories

2/4 KB In-system self-programmable Flash memory   
– 64/128 bytes EEPROM 128/256 bytes SRAM Write/erase endurance: • Flash 10,000 cycles • EEPROM 100,000 cycles   
– Data retention: • 40 years at 55°C

• System

– Power-on Reset (POR)

– Brown-out Detector (BOD)

– Clock options:

16 MHz low-power internal RC oscillator 32.768 kHz Ultra Low-Power (ULP) internal RC oscillator 32.768 kHz external crystal oscillator External clock input

– Single-Pin Unified Program and Debug Interface (UPDI) – Three sleep modes:

• Idle with all peripherals running for immediate wake-up • Standby – Configurable operation of selected peripherals • Power-Down with full data retention

• Peripherals – One 16-bit Timer/Counter type A (TCA) with a dedicated period register and three compare channels – One 16-bit Timer/Counter type B (TCB) with input capture

– One 12-bit Timer/Counter type D (TCD) optimized for control applications One 16-bit Real-Time Counter (RTC) running from an external crystal, external clock, or internal RC oscillator Watchdog Timer (WDT) with Window mode, with a separate on-chip oscillator   
– One USART with fractional baud rate generator, auto-baud, and start-of-frame detection   
– One master/slave Serial Peripheral Interface (SPI)

– One Two-Wire Interface (TWI) with dual address match • Philips I2C compatible Standard mode (Sm, 100 kHz) Fast mode (Fm, 400 kHz) Fast mode plus (Fm+, 1 MHz)

One Analog Comparator (AC) with a low propagation delay – One 10-bit 115 ksps Analog-to-Digital Converter (ADC) One 8-bit Digital-to-Analog Converter (DAC) with one external channel – Multiple voltage references (VREF):

• 0.55V • 1.1V • 1.5V 2.5V 4.3V

Event System (EVSYS) for CPU independent and predictable inter-peripheral signaling   
Configurable Custom Logic (CCL) with two programmable look-up tables   
Automated CRC memory scan   
External interrupt on all general purpose pins

• I/O and Packages:

– Up to 12 programmable I/O lines   
– 8-pin SOIC150   
– 14-pin SOIC150

• Temperature Ranges: – -40°C to 105°C – -40°C to 125°C • Speed Grades: – 0-8 MHz @ 2.7V – 5.5V – 0-16 MHz @ 4.5V – 5.5V

# Table of Contents

Introduction..

Features.. 1   
1. Silicon Errata and Data Sheet Clarification Document.. ..9   
2. tinyAVR® 1-series Overview.... ....10   
2.1. Configuration Summary... ....10   
3. Block Diagram.. .. 12   
4. Pinout... .... 13   
4.1. 8-Pin SOIC... .... 13   
4.2. 14-Pin SOIC.. ..... 13   
5. I/O Multiplexing and Considerations.. ... 14   
5.1. Multiplexed Signals... .... 14   
6. Automotive Quality Grade... ..... 15   
7. Memories.. .... 16   
7.1. Overview.. .. 16   
7.2. Memory Map.. .... 17   
7.3. In-System Reprogrammable Flash Program Memory... .... 17   
7.4. SRAM Data Memory..... .... 18   
7.5. EEPROM Data Memory... .... 18   
7.6. User Row... ..18   
7.7. Signature Bytes.. .. 18   
7.8. I/O Memory.. ...19   
7.9. Memory Section Access from CPU and UPDI on Locked Device.. ..... 21   
7.10. Configuration and User Fuses (FUSE).... ..22

# 8. Peripherals and Architecture.. . 38

8.1. Peripheral Address Map... ..38   
8.2. Interrupt Vector Mapping.. .. 39   
8.3. System Configuration (SYSCFG).. ...40

# 9. AVR® CPU.. ... 43

9.1. Features... .. 43   
9.2. Overview... . 43   
9.3. Architecture.. ... 43   
9.4. Arithmetic Logic Unit (ALU).. .. 45   
9.5. Functional Description.. ...45   
9.6. Register Summary... ..50   
9.7. Register Description.. .. 50

# 10. NVMCTRL - Nonvolatile Memory Controller... .. 54

10.1. Features... .. 54   
10.2. Overview... .. 54   
10.3. Functional Description.. ..55   
10.4. Register Summary... ...60   
10.5. Register Description.. ... 60

11. CLKCTRL - Clock Controller.............. ...... 68

11.1. Features.... ... 68   
11.2. Overview... .. 68   
11.3. Functional Description.. ..70   
11.4. Register Summary.... ...74   
11.5. Register Description.. .. 74

# 12. SLPCTRL - Sleep Controller.. .. 84

12.1. Features... .... 84   
12.2. Overview... .... 84   
12.3. Functional Description.. ..84   
12.4. Register Summary... ....87   
12.5. Register Description.. .. 87

# 13. RSTCTRL - Reset Controller... 89

13.1. Features... .... 89   
13.2. Overview... .... 89   
13.3. Functional Description.. ..90   
13.4. Register Summary... ..94   
13.5. Register Description.. .. 94

# 14. CPUINT - CPU Interrupt Controller.. . 97

14.1. Features... ... 97   
14.2. Overview... . 97   
14.3. Functional Description.. ..98   
14.4. Register Summary .. ...103   
14.5. Register Description.. ... 103

# 15. EVSYS - Event System.. .. 108

15.1. Features... ... 108   
15.2. Overview... .. 108   
15.3. Functional Description.. .. 110   
15.4. Register Summary... ... 112   
15.5. Register Description.. .. 112

# 16. PORTMUX - Port Multiplexer.. . 119

16.1. Overview... ...119   
16.2. Register Summary.... ...120   
16.3. Register Description.. .... 120

17. PORT - I/O Pin Configuration.. .124

17.1. Features... . 124   
17.2. Overview... .. 124   
17.3. Functional Description.. ...126   
17.4. Register Summary - PORTx.. ....129   
17.5. Register Description - PORTx... .. 129   
17.6. Register Summary - VPORTx... ... 141   
17.7. Register Description - VPORTx.. ....141

18. BOD - Brown-out Detector............ ..... 146

18.1. Features.... ... 146   
18.2. Overview... .. 146   
18.3. Functional Description.. ...147   
18.4. Register Summary.... ...149   
18.5. Register Description.. ... 149

# 19. VREF - Voltage Reference... .. 156

19.1. Features... ... 156   
19.2. Overview... ... 156   
19.3. Functional Description.. ...156   
19.4. Register Summary .. ....157   
19.5. Register Description.. ... 157

# 20. WDT - Watchdog Timer.. ..160

20.1. Features... ... 160   
20.2. Overview... ... 160   
20.3. Functional Description... ...161   
20.4. Register Summary - WDT.. ... 164   
20.5. Register Description.. ... 164

21. TCA - 16-bit Timer/Counter Type A... .. 167

21.1. Features... . 167   
21.2. Overview... ... 167   
21.3. Functional Description.. ....169   
21.4. Register Summary - Normal Mode. ...179   
21.5. Register Description - Normal Mode.. .. 179   
21.6. Register Summary - Split Mode... ... 198   
21.7. Register Description - Split Mode.. ..198

# 22. TCB - 16-bit Timer/Counter Type B.. .214

22.1. Features... ... 214   
22.2. Overview.. .. 214   
22.3. Functional Description.. ...216   
22.4. Register Summary... ...224   
22.5. Register Description.. .. 224

23. TCD - 12-Bit Timer/Counter Type D.. .. 235

23.1. Features... .. 235   
23.2. Overview... .. 235   
23.3. Functional Description.. ...237   
23.4. Register Summary... ...260   
23.5. Register Description.. .. 260

24. RTC - Real-Time Counter............ .... 285

24.1. Features... .. 285   
24.2. Overview.. .. 285   
24.3. Clocks.... ..286   
24.4. RTC Functional Description.. ... 286   
24.5. PIT Functional Description.. .. 287   
24.6. Events... .. 288   
24.7. Interrupts... .. 289   
24.8. Sleep Mode Operation.. . 290   
24.9. Synchronization.. ..290   
24.10. Debug Operation..... ....290   
24.11. Register Summary... ...291   
24.12. Register Description.. ..291

# 25. USART - Universal Synchronous and Asynchronous Receiver and Transmitter........ .. 307

25.1. Features... ... 307   
25.2. Overview... .... 307   
25.3. Functional Description.. ...308   
25.4. Register Summary.... ....323   
25.5. Register Description.. .. 323

# 26. SPI - Serial Peripheral Interface.. ..339

26.1. Features... .. 339   
26.2. Overview... .. 339   
26.3. Functional Description.. ...340   
26.4. Register Summary... ...347   
26.5. Register Description.. .. 347

# 27. TWI - Two-Wire Interface.. .. 354

27.1. Features... ... 354   
27.2. Overview... .. 354   
27.3. Functional Description.. ...355   
27.4. Register Summary... ...366   
27.5. Register Description.. .. 366

# 28. CRCSCAN - Cyclic Redundancy Check Memory Scan............. ... 383

28.1. Features... ... 383   
28.2. Overview... ... 383   
28.3. Functional Description... ...384   
28.4. Register Summary - CRCSCAN... ...387   
28.5. Register Description.. ... 387

# 29. CCL - Configurable Custom Logic.. . 391

29.1. Features... ... 391   
29.2. Overview... ... 391   
29.3. Functional Description.. ...393   
29.4. Register Summary... ...401   
29.5. Register Description.. ... 401

30. AC - Analog Comparator.. .. 408

30.1. Features... ... 408   
30.2. Overview... ... 408   
30.3. Functional Description.. ...410   
30.4. Register Summary... ...412   
30.5. Register Description.. ... 412

31. ADC - Analog-to-Digital Converter... .. 417

31.1. Features... ... 417   
31.2. Overview.. .. 417   
31.3. Functional Description.. ...418   
31.4. Register Summary - ADCn.. ...425   
31.5. Register Description.. ... 425

# 32. DAC - Digital-to-Analog Converter... . 443

32.1. Features.. ... 443   
32.2. Overview... ... 443   
32.3. Functional Description.. ...444   
32.4. Register Summary... ...446   
32.5. Register Description.. ... 446

# 33. UPDI - Unified Program and Debug Interface........... ...... 449

33.1. Features... ... 449   
33.2. Overview... ... 449   
33.3. Functional Description.. ...451   
33.4. Register Summary... ....472   
33.5. Register Description.. .. 472

34. Instruction Set Summary... .. 483

# 35. Conventions... .. 484

35.1. Numerical Notation... ...484   
35.2. Memory Size and Type.. ...484   
35.3. Frequency and Time... ...484   
35.4. Registers and Bits.. ... 485   
35.5. ADC Parameter Definitions.. ... 486

# 36. Electrical Characteristics.. .. 489

36.1. Disclaimer.. ..489   
36.2. Absolute Maximum Ratings . ..489   
36.3. General Operating Ratings .. ..490   
36.4. Power Consumption.. ... 490   
36.5. Wake-Up Time.. ..491   
36.6. Peripherals Power Consumption. ...492   
36.7. BOD and POR Characteristics.. ... 493   
36.8. External Reset Characteristics.. .. 494   
36.9. Oscillators and Clocks.. ..494   
36.10. I/O Pin Characteristics. .... 495   
36.11. USART... ... 496   
36.12. SPI.. .. 497   
36.13. TWI.. ...498   
36.14. VREF.. ...501   
36.15. ADC.. ...502   
36.16. DAC.. ...504   
36.17. AC... ... 505   
36.18. UPDI Timing.. .. 506   
36.19. Programming Time.. ..507

# 37. Typical Characteristics.. . 508

37.1. Power Consumption.. . 508   
37.2. GPIO.. . 515   
37.3. VREF Characteristics.. .. 521   
37.4. BOD Characteristics.. ..523   
37.5. ADC Characteristics.. .. 526   
37.6. AC Characteristics.. ...531   
37.7. OSC20M Characteristics. ...535   
37.8. OSCULP32K Characteristics. . 537   
37.9. TWI SDA Hold Timing . . 538

# 38. Ordering Information............ . 539

38.1. Product Information......... ...... 539   
38.2. Product Identification System. ...539

# 39. Package Drawings... . 540

39.1. Online Package Drawings.. .. 540   
39.2. 8-Pin SOIC... ... 541   
39.3. 14-Pin SOIC.. .. 544   
39.4. Thermal Considerations.. ... 547

# 40. Errata... . 548

40.1. Errata - ATtiny212/214/412/414 Automotive... .. 548

41. Data Sheet Revision History............. ..... 549

41.1. Rev. A - 05/2020.. ..549

The Microchip Website.. .. 550

Product Change Notification Service.. ..550

Customer Support.. . 550

Product Identification System.. ..551

Microchip Devices Code Protection Feature.. .. 551

Legal Notice... . 551

Trademarks.. . 551

Quality Management System.. . 552

Worldwide Sales and Service.. ..553

# Silicon Errata and Data Sheet Clarification Document

Microchip aims to provide its customers with the best documentation possible to ensure a successful use of Microchip products. Between data sheet updates, a Silicon errata and data sheet clarification document will contain the most recent information for the data sheet. The ATtiny212/214/412/414 Automotive Silicon Errata and Data Sheet Clarification (www.microchip.com/DS80000893) is available at the device product page on www.microchip.com.

# 2. tinyAVR® 1-series Overview

The following figure shows the tinyAVR 1-series devices, laying out pin count variants and memory sizes:

Vertical migration upwards is possible without code modification, as these devices are pin-compatible and provide the same or more features. Downward migration may require code modification due to fewer available instances of some peripherals. Horizontal migration to the left reduces the pin count and, therefore, the available features

![](images/8c52d08af22c70ae799c15e414f3e901a71656945c9f4ed6e20717512a3a5ce6.jpg)  
Figure 2-1. tinyAVR® 1-series Overview

Devices with different Flash memory sizes typically also have different SRAM and EEPROM.

# 2.1 Configuration Summary

# 2.1.1 Peripheral Summary

Table 2-1. Peripheral Summary

<table><tr><td colspan="1" rowspan="1">Pins</td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">14</td></tr><tr><td colspan="1" rowspan="1">SRAM</td><td colspan="1" rowspan="1">128B</td><td colspan="1" rowspan="1">128B</td><td colspan="1" rowspan="1">256B</td><td colspan="1" rowspan="1">256B</td></tr><tr><td colspan="1" rowspan="1">Flash</td><td colspan="1" rowspan="1">2KB</td><td colspan="1" rowspan="1">2KB</td><td colspan="1" rowspan="1">4KB</td><td colspan="1" rowspan="1">4KB</td></tr><tr><td colspan="1" rowspan="1">EEPROM</td><td colspan="1" rowspan="1">64B</td><td colspan="1" rowspan="1">64B</td><td colspan="1" rowspan="1">128B</td><td colspan="1" rowspan="1">128B</td></tr><tr><td colspan="1" rowspan="1"> Max. frequency (MHz)</td><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">16</td></tr><tr><td colspan="1" rowspan="1">16-bit Timer/Counter type A (TCA)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">16-bit Timer/Counter type B (TCB)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">12-bit Timer/Counter type D (TCD)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="5" rowspan="1">….continued</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">A</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">Real-Time Counter (RTC)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">USART</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SPI</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">TW/I (12C)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">ADC</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">ADC channels</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">10</td></tr><tr><td colspan="1" rowspan="1">DAC</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">AC</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">AC inputs</td><td colspan="1" rowspan="1">1p/1n</td><td colspan="1" rowspan="1">1p/1n</td><td colspan="1" rowspan="1">1p/1n</td><td colspan="1" rowspan="1">1p/1n</td></tr><tr><td colspan="1" rowspan="1">Peripheral Touch Controller (PTC)</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td><td colspan="1" rowspan="1">No</td></tr><tr><td colspan="1" rowspan="1">Configurable Custom Logic</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">Window Watchdog</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">Event System channels</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">6</td></tr><tr><td colspan="1" rowspan="1">General purpose I/O</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">12</td></tr><tr><td colspan="1" rowspan="1">External interrupts</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">12</td></tr><tr><td colspan="1" rowspan="1">CRCSCAN</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr></table>

# 3. Block Diagram

![](images/f8fa335ee0e2e94bf1ebcbe560174c5f0c9193e0bdbf4098228f62df298f4c27.jpg)  
Figure 3-1. tinyAVR® 1-series Block Diagram

Note:  The block diagram represents the largest device of the tinyAVR 1-series, both in terms of pin count and Flash size. See sections 2.1 Configuration Summary and 5.1 Multiplexed Signals for an overview of the features of the specific devices in this data sheet.

# 4. Pinout

4.1 8-Pin SOIC

![](images/812c165df1a70d697289bc1055c8532ad2dc52c2af5e2f25221df94064c60862.jpg)

4.2 14-Pin SOIC

![](images/aa43e6d81db201ac9b31417bb07d4974a72a961870846e051663c865f0287307.jpg)

![](images/9f7dbd73cf8d85519b0155b143ff34e71047b8052fa28de7798a651c8aaee354.jpg)

# 5. I/O Multiplexing and Considerations

# 5.1 Multiplexed Signals

Table 5-1. PORT Function Multiplexing, 14 Pins   

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Pin Name (1,2)</td><td rowspan=1 colspan=1>Other/Special</td><td rowspan=1 colspan=1>ADCO</td><td rowspan=1 colspan=1>ACO</td><td rowspan=1 colspan=1>DACO</td><td rowspan=1 colspan=1>USARTO</td><td rowspan=1 colspan=1>SPI0</td><td rowspan=1 colspan=1>TWI0</td><td rowspan=1 colspan=1>TCAO</td><td rowspan=1 colspan=1>TCBO</td><td rowspan=1 colspan=1>TCDO</td><td rowspan=1 colspan=1>CCL</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>PAO</td><td rowspan=1 colspan=1>RESET/UPDI</td><td rowspan=1 colspan=1>AINO</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LUTO-INO</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>PA1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AIN1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>TxD(3)</td><td rowspan=1 colspan=1>MOSI</td><td rowspan=1 colspan=1>SDA(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LUTO-IN1</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>PA2</td><td rowspan=1 colspan=1>EVOUTO</td><td rowspan=1 colspan=1>AIN2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>RxD(3)</td><td rowspan=1 colspan=1>MISO</td><td rowspan=1 colspan=1>SCL(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LUTO-IN2</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>PA3</td><td rowspan=1 colspan=1>EXTCLK</td><td rowspan=1 colspan=1>AIN3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>xCK(3)</td><td rowspan=1 colspan=1>SCK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WO3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>PA4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AIN4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>XDIR(3)</td><td rowspan=1 colspan=1>SS</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WO4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WOA</td><td rowspan=1 colspan=1>LUTO-OUT</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>PA5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AIN5</td><td rowspan=1 colspan=1>OUT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WO5</td><td rowspan=1 colspan=1>wo</td><td rowspan=1 colspan=1>WOB</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>PA6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AIN6</td><td rowspan=1 colspan=1>AINNO</td><td rowspan=1 colspan=1>OUT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MOS1(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>PA7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AIN7</td><td rowspan=1 colspan=1>AINPO</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MISO(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LUT1-OUT</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>PB3</td><td rowspan=1 colspan=1>TOSC1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>RxD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>wO0(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>$PB2</td><td rowspan=1 colspan=1>TOSC2, EVOUT1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>TxD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WO2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>PB1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AIN10</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>XCK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=1>W01</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>PBO</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AIN11</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>XDIR</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=1>WO0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

# Notes:

1. Pin names are of type Pxn, with x being the PORT instance (A, B) and n the pin number. The notation for signals is PORTx_PINn. All pins can be used as event input.

2. All pins can be used for external interrupt, where pins Px2 and Px6 of each port have full asynchronous detection.

3. Alternate pin positions. For selecting the alternate positions, refer to section 16. PORTMUX - Port Multiplexer.

Table 5-2. PORT Function Multiplexing, Eight Pins   

<table><tr><td rowspan=2 colspan=1>SOIC 8-Pin</td><td rowspan=1 colspan=1>Pin Name</td><td rowspan=1 colspan=1>Other/</td><td rowspan=1 colspan=1>ADCO</td><td rowspan=1 colspan=1>ACO</td><td rowspan=2 colspan=1>DACO</td><td rowspan=2 colspan=1>USARTO</td><td rowspan=2 colspan=1>SPI0</td><td rowspan=2 colspan=1>TWI0</td><td rowspan=2 colspan=1>TCAO</td><td rowspan=2 colspan=1>TCBO</td><td rowspan=2 colspan=1>TCDO</td><td rowspan=2 colspan=1>CCL</td></tr><tr><td rowspan=1 colspan=1>(1,2)</td><td rowspan=1 colspan=1>Special</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>PAO</td><td rowspan=1 colspan=1>RESETUPDI AINO</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>XDIR</td><td rowspan=1 colspan=1>Ss</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LUTO-INO</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>PA1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AIN1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>TxD(3)</td><td rowspan=1 colspan=1>MOSI</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=1>W01</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LUTO-IN1</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>PA2</td><td rowspan=1 colspan=1>EVOUTO</td><td rowspan=1 colspan=1>AIN2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>RxD(3)</td><td rowspan=1 colspan=1>MISO</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=1>WO2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LUTO-IN2</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>PA3</td><td rowspan=1 colspan=1>EXTCLK</td><td rowspan=1 colspan=1>AIN3</td><td rowspan=1 colspan=1>OUT</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>xCK</td><td rowspan=1 colspan=1>SCK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WO0/W03</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>VDD</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>PA6</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AIN6</td><td rowspan=1 colspan=1>AINNO</td><td rowspan=1 colspan=1>OUT</td><td rowspan=1 colspan=1>TxD</td><td rowspan=1 colspan=1>MOS1(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WOo</td><td rowspan=1 colspan=1>WOA</td><td rowspan=1 colspan=1>LUTO-OUT</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>PA7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>AIN7</td><td rowspan=1 colspan=1>AINPO</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>RxD</td><td rowspan=1 colspan=1>MISO(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>woo(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WOB</td><td rowspan=1 colspan=1>LUT1-OUT</td></tr></table>

# Notes:

1. Pin names are of type Pxn, with x being the PORT instance (A, B) and n the pin number. Notation for signals is PORTx_PINn. All pins can be used as event inputs.   
2. All pins can be used for external interrupts, where pins Px2 and Px6 of each port have full asynchronous detection.   
3. Alternate pin positions. For selecting the alternate positions, refer to section 16. PORTMUX - Port Multiplexer.

# 6. Automotive Quality Grade

The devices have been manufactured according to the most stringent requirements of the international standard ISO/TS 16949. This data sheet contains limit values extracted from the results of extensive characterization (temperature and voltage).

The quality and reliability have been verified during regular product qualification as per AEC-Q100 grade 1 (–40°C to +125°C) and grade 2 (–40°C to +105°C).

Table 6-1. Temperature Grade Identification for Automotive Products   

<table><tr><td rowspan=1 colspan=1>Temperature (°C)</td><td rowspan=1 colspan=1>Temperature Identifier</td><td rowspan=1 colspan=1>Comments</td></tr><tr><td rowspan=1 colspan=1>−40 to +125</td><td rowspan=1 colspan=1>Z</td><td rowspan=1 colspan=1>Automotive temperature grade 1</td></tr><tr><td rowspan=1 colspan=1>−40 to +105</td><td rowspan=1 colspan=1>B</td><td rowspan=1 colspan=1>Automotive temperature grade 2</td></tr></table>

# 7. Memories

# 7.1 Overview

The main memories are SRAM data memory, EEPROM data memory, and Flash program memory. Also, the peripheral registers are located in the I/O memory space.

Table 7-1. Physical Properties of Flash Memory   

<table><tr><td rowspan=1 colspan=1>Property</td><td rowspan=1 colspan=1>ATtiny212</td><td rowspan=1 colspan=1>ATtiny214</td><td rowspan=1 colspan=1>ATtiny412</td><td rowspan=1 colspan=1>ATtiny414</td></tr><tr><td rowspan=1 colspan=1>Size</td><td rowspan=1 colspan=1>2KB</td><td rowspan=1 colspan=1>2KB</td><td rowspan=1 colspan=1>4KB</td><td rowspan=1 colspan=1>4KB</td></tr><tr><td rowspan=1 colspan=1>Page size</td><td rowspan=1 colspan=1>64B</td><td rowspan=1 colspan=1>64B</td><td rowspan=1 colspan=1>64B</td><td rowspan=1 colspan=1>64B</td></tr><tr><td rowspan=1 colspan=1>Number of pages</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>64</td></tr><tr><td rowspan=1 colspan=1>Start adress</td><td rowspan=1 colspan=1>0x8000</td><td rowspan=1 colspan=1>0x8000</td><td rowspan=1 colspan=1>0x8000</td><td rowspan=1 colspan=1>0×8000</td></tr></table>

Table 7-2. Physical Properties of SRAM   

<table><tr><td rowspan=1 colspan=1>Property</td><td rowspan=1 colspan=1>ATtiny212</td><td rowspan=1 colspan=1>ATtiny214</td><td rowspan=1 colspan=1>ATtiny412</td><td rowspan=1 colspan=1>ATtiny414</td></tr><tr><td rowspan=1 colspan=1>Size</td><td rowspan=1 colspan=1>128B</td><td rowspan=1 colspan=1>128B</td><td rowspan=1 colspan=1>256B</td><td rowspan=1 colspan=1>256B</td></tr><tr><td rowspan=1 colspan=1>Start address</td><td rowspan=1 colspan=1>0x3F80</td><td rowspan=1 colspan=1>0x3F80</td><td rowspan=1 colspan=1>0x3F00</td><td rowspan=1 colspan=1>0x3F00</td></tr></table>

Table 7-3. Physical Properties of EEPROM   

<table><tr><td rowspan=1 colspan=1>Property</td><td rowspan=1 colspan=1>ATtiny212</td><td rowspan=1 colspan=1>ATtiny214</td><td rowspan=1 colspan=1>ATtiny412</td><td rowspan=1 colspan=1>ATtiny414</td></tr><tr><td rowspan=1 colspan=1>Size</td><td rowspan=1 colspan=1>64B</td><td rowspan=1 colspan=1>64B</td><td rowspan=1 colspan=1>128B</td><td rowspan=1 colspan=1>128B</td></tr><tr><td rowspan=1 colspan=1>Page size</td><td rowspan=1 colspan=1>32B</td><td rowspan=1 colspan=1>32B</td><td rowspan=1 colspan=1>32B</td><td rowspan=1 colspan=1>32B</td></tr><tr><td rowspan=1 colspan=1>Number of pages</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>Start address</td><td rowspan=1 colspan=1>0x1400</td><td rowspan=1 colspan=1>0×1400</td><td rowspan=1 colspan=1>0x1400</td><td rowspan=1 colspan=1>0x1400</td></tr></table>

# 7.2 Memory Map

![](images/34ea5e209c5e9d5ee418ae5e21027c8002c4a63240942e2095df776f924e851d.jpg)  
Figure 7-1. Memory Map

# 7.3 In-System Reprogrammable Flash Program Memory

The ATtiny212/214/412/414 Automotive contains 2/4 KB on-chip in-system reprogrammable Flash memory for program storage. Since all AVR instructions are 16 or 32-bit wide, the Flash is organized as 4K x 16. For write protection, the Flash program memory space can be divided into three sections (see the illustration below): Bootloader section, Application code section, and Application data section, with restricted access rights among them.

The Program Counter (PC) is 11-bit wide to address the whole program memory. The procedure for writing Flash memory is described in detail in the documentation of the Nonvolatile Memory Controller (NVMCTRL) peripheral.

The entire Flash memory is mapped in the memory space and is accessible with normal LD/ST instructions as well as the LPM instruction. For LD/ST instructions, the Flash is mapped from address 0x8000. For the LPM instruction, the Flash start address is 0x0000.

The ATtiny212/214/412/414 Automotive also has a CRC peripheral that is a master on the bus.

<table><tr><td rowspan="3">FLASH</td><td>BOOT</td><td rowspan="3">FLASHSTART: 0x8000 BOOTEND&gt;0:0x8000+BOOTEND*256</td></tr><tr><td>APPLICATION CODE</td><td></td></tr><tr><td>APPLICATION DATA</td><td>APPEND&gt;0: 0x8000+APPEND*256 FLASHEND</td></tr></table>

# 7.4 SRAM Data Memory

The 128/256 bytes SRAM is used for data storage and stack.

# 7.5 EEPROM Data Memory

The ATtiny212/214/412/414 Automotive has 64/128 bytes of EEPROM data memory, see section 7.2 Memory Map. The EEPROM memory supports single-byte read and write. The EEPROM is controlled by the Nonvolatile Memory Controller (NVMCTRL).

# 7.6 User Row

In addition to the EEPROM, the ATtiny212/214/412/414 Automotive has one extra page of EEPROM memory that can be used for firmware settings; the User Row (USERROW). This memory supports single-byte read and write as the normal EEPROM. The CPU can write and read this memory as normal EEPROM, and the UPDI can write and read it as a normal EEPROM memory if the part is unlocked. The User Row can be written by the UPDI when the part is locked. USERROW is not affected by a chip erase.

# 7.7 Signature Bytes

All tinyAVR® microcontrollers have a 3-byte signature code that identifies the device. The three bytes reside in a separate address space. For the device, the signature bytes are given in the following table.

Note:  When the device is locked, only the System Information Block (SIB) can be accessed.

Table 7-4. Device ID   

<table><tr><td rowspan=2 colspan=1>Device Name</td><td rowspan=1 colspan=3>Signature Bytes Address</td></tr><tr><td rowspan=1 colspan=1>0x00</td><td rowspan=1 colspan=1>0×01</td><td rowspan=1 colspan=1>0×02</td></tr><tr><td rowspan=1 colspan=1>ATtiny212</td><td rowspan=1 colspan=1>0x1E</td><td rowspan=1 colspan=1>0x91</td><td rowspan=1 colspan=1>0x21</td></tr><tr><td rowspan=1 colspan=1>ATtiny214</td><td rowspan=1 colspan=1>Ox1E</td><td rowspan=1 colspan=1>0×91</td><td rowspan=1 colspan=1>0×20</td></tr><tr><td rowspan=1 colspan=1>ATtiny412</td><td rowspan=1 colspan=1>0x1E</td><td rowspan=1 colspan=1>0×92</td><td rowspan=1 colspan=1>0x23</td></tr><tr><td rowspan=1 colspan=1>ATtiny414</td><td rowspan=1 colspan=1>Ox1E</td><td rowspan=1 colspan=1>0×92</td><td rowspan=1 colspan=1>0x22</td></tr></table>

# 7.8 I/O Memory

All ATtiny212/214/412/414 Automotive I/Os and peripherals are located in the I/O memory space. The I/O address range from 0x00 to 0x3F can be accessed in a single cycle using IN and OUT instructions. The extended I/O memory space from 0x0040 to 0x0FFF can be accessed by the LD/LDS/LDD and ST/STS/STD instructions, transferring data between the 32 general purpose working registers and the I/O memory space.

I/O registers within the address range 0x00-0x1F are directly bit-accessible using the SBI and CBI instructions. In these registers, the value of single bits can be checked by using the SBIS and SBIC instructions. Refer to the Instruction Set section for more details.

For compatibility with future devices, reserved bits must be written to ‘0’, if accessed. Reserved I/O memory addresses must never be written.

Some of the interrupt flags are cleared by writing a ‘1’ to them. On ATtiny212/214/412/414 Automotive devices, the CBI and SBI instructions will only operate on the specified bit and can be used on registers containing such interrupt flags. The CBI and SBI instructions work with registers 0x00-0x1F only.

# General Purpose I/O Registers

The ATtiny212/214/412/414 Automotive devices provide four general purpose I/O registers. These registers can be used for storing any information, and they are particularly useful for storing global variables and interrupt flags. General purpose I/O registers, which reside in the address range 0x1C-0x1F, are directly bit-accessible using the SBI, CBI, SBIS, and SBIC instructions.

# 7.8.1 Register Summary

<table><tr><td rowspan=1 colspan=1>Offset</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Bit Pos.</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=3>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>0x00</td><td rowspan=1 colspan=1>GPIORO</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=10>GPIOR[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x01</td><td rowspan=1 colspan=1>GPIOR1</td><td rowspan=1 colspan=1>7:0</td><td rowspan=2 colspan=10>GPIOR[7:0]GPIOR[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x02</td><td rowspan=1 colspan=1>GPIOR2</td><td rowspan=1 colspan=1>7:0</td><td rowspan=2 colspan=7>GPIOR[7:0]GPIOR[7:0]</td><td rowspan=2 colspan=3></td></tr><tr><td rowspan=1 colspan=1>0x03</td><td rowspan=1 colspan=1>GPIOR3</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=2></td></tr></table>

# 7.8.2 Register Description

# 7.8.2.1 General Purpose I/O Register n

Name: GPIORn   
Offset: 0x00 + n\*0x01 [n=0..3]   
Reset: 0x00   
Property:

These are general purpose registers that can be used to store data, such as global variables and flags, in the bitaccessible I/O memory space.

Bits 7:0 – GPIOR[7:0] General Purpose I/O Register Byte   

<table><tr><td rowspan="2">Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">GPIOR[7:0]</td></tr><tr><td>Access</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr><tr><td>Reset</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

# 7.9 Memory Section Access from CPU and UPDI on Locked Device

The device can be locked so that the memories cannot be read using the UPDI. The locking protects both the Flash (all Boot, Application Code, and Application Date sections), SRAM, and the EEPROM including the FUSE data. This prevents successful reading of application data or code using the debugger interface. Regular memory access from within the application is still enabled.

The device is locked by writing a non-valid key to the LOCKBIT bit field in FUSE.LOCKBIT.

Table 7-5. Memory Access Unlocked (FUSE.LOCKBIT Valid Key)(1)   

<table><tr><td rowspan=2 colspan=1>Memory Section</td><td rowspan=1 colspan=2>CPU Access</td><td rowspan=1 colspan=2>UPDI Access</td></tr><tr><td rowspan=1 colspan=1>Read</td><td rowspan=1 colspan=1>Write</td><td rowspan=1 colspan=1>Read</td><td rowspan=1 colspan=1>Write</td></tr><tr><td rowspan=1 colspan=1>SRAM</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>Registers</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>Flash</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>EEPROM</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>USERROW</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr><tr><td rowspan=1 colspan=1>SIGROW</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>Other fuses</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td></tr></table>

Table 7-6. Memory Access Locked (FUSE.LOCKBIT Invalid Key)(1)   

<table><tr><td rowspan=2 colspan=1>Memory Section</td><td rowspan=1 colspan=2>CPU Access</td><td rowspan=1 colspan=2>UPDI Access</td></tr><tr><td rowspan=1 colspan=1>Read</td><td rowspan=1 colspan=1>Write</td><td rowspan=1 colspan=1>Read</td><td rowspan=1 colspan=1>Write</td></tr><tr><td rowspan=1 colspan=1>SRAM</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>Registers</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>Flash</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>EEPROM</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>USERROW</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>Yes(2)</td></tr><tr><td rowspan=1 colspan=1>SIGROW</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td></tr><tr><td rowspan=1 colspan=1>Other fuses</td><td rowspan=1 colspan=1>Yes</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td><td rowspan=1 colspan=1>No</td></tr></table>

# Notes:

1. Read operations marked No in the tables may appear to be successful, but the data are not valid. Hence, any attempt of code validation through the UPDI will fail on these memory sections.

2. In the Locked mode, the USERROW can be written using the Fuse Write command, but the current USERROW values cannot be read out.

Important:  The only way to unlock a device is through a CHIPERASE. No application data are retained.

# 7.10 Configuration and User Fuses (FUSE)

Fuses are part of the nonvolatile memory and hold the device configuration. The fuses are available from the device power-up. The fuses can be read by the CPU or the UPDI, but can only be programmed or cleared by the UPDI. The configuration values stored in the fuses are written to their respective target registers at the end of the start-up sequence.

The fuses for peripheral configuration (FUSE) are pre-programmed but can be altered by the user. Altered values in the configuration fuse will be effective only after a Reset.

Note:  When writing the fuses, all reserved bits must be written to ‘1’.

7.10.1 Signature Row Summary   

<table><tr><td rowspan=1 colspan=1>Offset</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Bit Pos.</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>0×00</td><td rowspan=1 colspan=1>DEVICEIDO</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>DEVICEID[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x01</td><td rowspan=1 colspan=1>DEVICEID1</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>DEVICEID[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x02</td><td rowspan=1 colspan=1>DEVICEID2</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>DEVICEID[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x03</td><td rowspan=1 colspan=1>SERNUMO</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>SERNUM[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x04</td><td rowspan=1 colspan=1>SERNUM1</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>SERNUM[7:0]</td></tr><tr><td rowspan=1 colspan=1>0×05</td><td rowspan=1 colspan=1>SERNUM2</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>SERNUM[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x06</td><td rowspan=1 colspan=1>SERNUM3</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>SERNUM[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x07</td><td rowspan=1 colspan=1>SERNUM4</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>SERNUM[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x08</td><td rowspan=1 colspan=1>SERNUM5</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>SERNUM[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x09</td><td rowspan=1 colspan=1>SERNUM6</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>SERNUM[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x0A</td><td rowspan=1 colspan=1>SERNUM7</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>SERNUM[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x0B</td><td rowspan=1 colspan=1>SERNUM8</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>SERNUM[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x0C</td><td rowspan=1 colspan=1>SERNUM9</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>SERNUM[7:0]</td></tr><tr><td rowspan=1 colspan=1>0xOD0x21</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x22</td><td rowspan=1 colspan=1>OSC16ERR3V</td><td rowspan=1 colspan=1>7:0</td><td rowspan=2 colspan=8>OSC16ERR3V[7:0]OSC16ERR5V[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x23</td><td rowspan=1 colspan=1>OSC16ERR5V</td><td rowspan=1 colspan=1>7:0</td></tr></table>

# 7.10.2 Signature Row Description

# 7.10.2.1 Device ID n

Name: DEVICEIDn Offset: 0x00 + n\*0x01 [n=0..2] Default: [Device ID] Property:

Each device has a device ID identifying this device and its properties such as memory sizes, pin count, and die revision. This can be used to identify a device and hence, the available features by software. The Device ID consists of three bytes: SIGROW.DEVICEID[2:0].

<table><tr><td rowspan="2">Bit</td><td rowspan="2">7</td><td rowspan="2">6</td><td rowspan="2">5</td><td rowspan="2">4</td><td rowspan="2">3</td><td rowspan="2">2</td><td rowspan="2">1</td><td rowspan="2">0</td></tr><tr><td colspan="2">DEVICEID[7:0]</td></tr><tr><td>Access</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr><tr><td>Default</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></table>

# 7.10.2.2 Serial Number Byte n

Name: SERNUMn Offset: 0x03 + n\*0x01 [n=0..9] Default: [device serial number] Property:

Each device has an individual serial number, representing a unique ID. This can be used to identify a specific device in the field. The serial number consists of ten bytes: SIGROW.SERNUM[9:0].

Bits 7:0 – SERNUM[7:0] Serial Number Byte n   

<table><tr><td>Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td colspan="8">SERNUM[7:0]</td></tr><tr><td>Access</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr><tr><td>Default</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></table>

# 7.10.2.3 OSC16 Error at 3V

Name: OSC16ERR3V   
Offset: 0x22   
Default: [Oscillator frequency error value]   
Property: Bits 7:0 – OSC16ERR3V[7:0] OSC16 Error at 3V   
These registers contain the signed oscillator frequency error value relative to the nominal oscillator frequency when running at an internal 16 MHz at 3V, as measured during production.

<table><tr><td>Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td colspan="6">OSC16ERR3V[7:0]</td><td></td><td></td></tr><tr><td>Access</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr><tr><td>Default</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></table>

# 7.10.2.4 OSC16 Error at 5V

Name: OSC16ERR5V   
Offset: 0x23   
Default: [Oscillator frequency error value]   
Property: Bits 7:0 – OSC16ERR5V[7:0] OSC16 Error at 5V   
These registers contain the signed oscillator frequency error value relative to the nominal oscillator frequency when running at an internal 16 MHz at 5V, as measured during production.

<table><tr><td>Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td colspan="6">OSC16ERR5V[7:0]</td><td></td><td></td></tr><tr><td>Access</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr><tr><td>Default</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></table>

# 7.10.3 Fuse Summary - FUSE

<table><tr><td rowspan=1 colspan=1>Offset</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Bit Pos.</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>0x00</td><td rowspan=1 colspan=1>WDTCFG</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=4>WINDOW[3:0]</td><td rowspan=1 colspan=4>PERIOD[3:0]</td></tr><tr><td rowspan=1 colspan=1>0x01</td><td rowspan=1 colspan=1>BODCFG</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=3>LVL[2:0]</td><td rowspan=1 colspan=1>SAMPFREQ</td><td rowspan=1 colspan=2>ACTIVE[1:0]</td><td rowspan=1 colspan=2>SLEEP[1:0]</td></tr><tr><td rowspan=1 colspan=1>0x02</td><td rowspan=1 colspan=1>OSCCFG</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=1>OSCLOCK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>FREQSEL[1:0]</td></tr><tr><td rowspan=1 colspan=1>0x03</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x04</td><td rowspan=1 colspan=1>TCDOCFG</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=1>CMPDEN</td><td rowspan=1 colspan=1>CMPCEN</td><td rowspan=1 colspan=1>CMPBEN</td><td rowspan=1 colspan=1>CMPAEN</td><td rowspan=1 colspan=1>CMPD</td><td rowspan=1 colspan=1>CMPC</td><td rowspan=1 colspan=1>CMPB</td><td rowspan=1 colspan=1>CMPA</td></tr><tr><td rowspan=1 colspan=1>0x05</td><td rowspan=1 colspan=1>SYSCFGO</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>RSTPIN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>EESAVE</td></tr><tr><td rowspan=1 colspan=1>0x06</td><td rowspan=1 colspan=1>SYSCFG1</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>SUT[2:0]</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0×07</td><td rowspan=1 colspan=1>APPEND</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=5>APPEND[7:0]</td></tr><tr><td rowspan=1 colspan=1>0x08</td><td rowspan=1 colspan=1>BOOTEND</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>BOOTEND[7:0]</td><td rowspan=1 colspan=3></td></tr><tr><td rowspan=1 colspan=1>0×09</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=3></td></tr><tr><td rowspan=1 colspan=1>0x0A</td><td rowspan=1 colspan=1>LOCKBIT</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>LOCKBIT[7:0]</td></tr></table>

# 7.10.4 Fuse Description

# 7.10.4.1 Watchdog Configuration

Name: WDTCFG Offset: 0x00 Default: 0x00 Property:

The default value given in this fuse description is the factory-programmed value, and should not be mistaken for the Reset value.

<table><tr><td rowspan="2">Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="4">WINDOW[3:0]</td><td colspan="4">PERIOD[3:0]</td></tr><tr><td>Access</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr><tr><td>Default</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Bits 7:4 – WINDOW[3:0] Watchdog Window Time-Out Period This value is loaded into the WINDOW bit field of the Watchdog Control A (WDT.CTRLA) register during Reset.

Bits 3:0 – PERIOD[3:0] Watchdog Time-Out Period This value is loaded into the PERIOD bit field of the Watchdog Control A (WDT.CTRLA) register during Reset.

# 7.10.4.2 BOD Configuration

Name: BODCFG Offset: 0x01 Default: 0x00 Property:

The default value given in this fuse description is the factory-programmed value, and should not be mistaken for the Reset value.

The bit values of this fuse register are written to the corresponding BOD configuration registers at start-up.   

<table><tr><td rowspan="2">Bit</td><td rowspan="2">7</td><td rowspan="2">6</td><td rowspan="2">5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>SAMPFREQ</td><td>ACTIVE[1:0]</td><td></td><td>SLEEP[1:0]</td><td></td></tr><tr><td>Access</td><td>R</td><td>LVL[2:0] R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr><tr><td>Default</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Bits 7:5 – LVL[2:0] BOD Level This value is loaded into the LVL bit field of the BOD Control B (BOD.CTRLB) register during Reset.   

<table><tr><td>Value</td><td>Name</td><td>Description</td></tr><tr><td>0x2</td><td>BODLEVEL2</td><td>2.6V</td></tr><tr><td>0x7</td><td>BODLEVEL7</td><td>4.2V</td></tr></table>

# Notes:

• The values in the description are typical • Refer to the BOD and POR Characteristics in Electrical Characteristics for maximum and minimum values

Bit 4 – SAMPFREQ BOD Sample Frequency This value is loaded into the SAMPFREQ bit of the BOD Control A (BOD.CTRLA) register during Reset.   

<table><tr><td>Value</td><td>Description</td></tr><tr><td>0x0</td><td>Sample frequency is 1 kHz</td></tr><tr><td>0x1</td><td>Sample frequency is 125 Hz</td></tr></table>

Bits 3:2 – ACTIVE[1:0] BOD Operation Mode in Active and Idle This value is loaded into the ACTIVE bit field of the BOD Control A (BOD.CTRLA) register during Reset.   
Bits 1:0 – SLEEP[1:0] BOD Operation Mode in Sleep   

<table><tr><td>Value</td><td>Description</td></tr><tr><td>0x0</td><td>Disabled</td></tr><tr><td>0x1</td><td>Enabled</td></tr><tr><td>0x2</td><td>Sampled</td></tr><tr><td>0x3</td><td>Enabled with wake-up halted until BOD is ready</td></tr></table>

This value is loaded into the SLEEP bit field of the BOD Control A (BOD.CTRLA) register during Reset.   

<table><tr><td>Value</td><td>Description</td></tr><tr><td>0x0</td><td>Disabled</td></tr><tr><td>0x1</td><td>Enabled</td></tr><tr><td>0x2</td><td>Sampled</td></tr><tr><td>0×3</td><td>Reserved</td></tr></table>

# 7.10.4.3 Oscillator Configuration

Name: OSCCFG Offset: 0x02 Default: 0x01 Property:

The default value given in this fuse description is the factory-programmed value, and should not be mistaken for the Reset value.

<table><tr><td rowspan="2">Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>OSCLOCK</td><td></td><td></td><td></td><td></td><td></td><td>FREQSEL[1:0]</td><td></td></tr><tr><td>Access</td><td>R</td><td></td><td></td><td></td><td></td><td></td><td>R</td><td>R</td></tr><tr><td>Default</td><td>0</td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>1</td></tr></table>

Bit 7 – OSCLOCK Oscillator Lock This fuse bit is loaded to LOCK in CLKCTRL.OSC20MCALIBB during Reset.   
Bits 1:0 – FREQSEL[1:0] Frequency Select   

<table><tr><td>Value</td><td>Description</td></tr><tr><td>0</td><td>Calibration registers of the OSC20M oscillator are accessible</td></tr><tr><td>1</td><td>Calibration registers of the OSC20M oscillator are locked</td></tr></table>

This bit field selects the operation frequency of the 16 MHz internal oscillator (OSC20M) and determines the respective factory calibration values to be written to CAL20M in CLKCTRL.OSC20MCALIBA and TEMPCAL20M in CLKCTRL.OSC20MCALIBB.

<table><tr><td>Value 0x1</td><td>Description</td></tr><tr><td></td><td>Run at 16 MHz with corresponding factory calibration Reserved</td></tr><tr><td>Other</td><td></td></tr></table>

# 7.10.4.4 Timer Counter Type D Configuration

Name: TCD0CFG Offset: 0x04 Default: 0x00 Property:

The default value given in this fuse description is the factory-programmed value, and should not be mistaken for the Reset value.

The bit values of this fuse register are written to the corresponding bits in the TCD.FAULTCTRL register of TCD0 at start-up.

<table><tr><td rowspan="2">Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>CMPDEN</td><td>CMPCEN</td><td>CMPBEN</td><td>CMPAEN</td><td>CMPD</td><td>CMPC</td><td>CMPB</td><td>CMPA</td></tr><tr><td>Access</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr><tr><td>Default</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Bits 4, 5, 6, 7 – CMPEN Compare x Enable   

<table><tr><td>Value</td><td>Description</td></tr><tr><td>0</td><td>Compare x output on Pin is disabled</td></tr><tr><td>1</td><td>Compare x output on Pin is enabled</td></tr></table>

Bits 0, 1, 2, 3 – CMP Compare x This bit selects the default state of Compare x after Reset, or when entering debug if FAULTDET is '1'.   

<table><tr><td>Value</td><td>Description</td></tr><tr><td>0</td><td>Compare x default state is &#x27;0&#x27;</td></tr><tr><td>1</td><td>Compare x default state is &#x27;1&#x27;</td></tr></table>

# 7.10.4.5 System Configuration 0

Name: SYSCFG0 Offset: 0x05 Default: 0xF6 Property:

The default value given in this fuse description is the factory-programmed value, and should not be mistaken for the Reset value.   

<table><tr><td rowspan="2">Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td>CRCSRC[1:0]</td><td></td><td></td><td></td><td>RSTPINCFG[1:0]</td><td></td><td>EESAVE</td></tr><tr><td>Access</td><td>R</td><td>R</td><td></td><td></td><td>R</td><td>R</td><td></td><td>R</td></tr><tr><td>Default</td><td>1</td><td>1</td><td></td><td></td><td>0</td><td>1</td><td></td><td>0</td></tr></table>

Bits 7:6 – CRCSRC[1:0] CRC Source See the CRC description for more information about the functionality.   

<table><tr><td>Value</td><td>Name</td><td>Description</td></tr><tr><td>0x0</td><td>FLASH</td><td>CRC of full Flash (boot, application code and application data)</td></tr><tr><td>0x1</td><td>BOOT</td><td>CRC of the boot section</td></tr><tr><td>0x2</td><td>BOOTAPP</td><td>CRC of application code and boot sections</td></tr><tr><td>0x3</td><td>NOCRC</td><td>No CRC</td></tr></table>

Bits 3:2 – RSTPINCFG[1:0] Reset Pin Configuration This bit field selects the Reset/UPDI pin configuration.   

<table><tr><td>Value</td><td>Description</td></tr><tr><td>0x0</td><td>GPIO</td></tr><tr><td>0x1</td><td>UPDI</td></tr><tr><td>0x2</td><td>RESET</td></tr><tr><td>Other</td><td>Reserved</td></tr></table>

Note:  When configuring the RESET pin as GPIO, there is a potential conflict between the GPIO actively driving the output, and a high-voltage UPDI enable sequence initiation. To avoid this, the GPIO output driver is disabled for 768 OSC32K cycles after a System Reset. Enable any interrupts for this pin only after this period.

Bit 0 – EESAVE EEPROM Save During Chip Erase Note:  If the device is locked, the EEPROM is always erased by a chip erase, regardless of this bit.

<table><tr><td>Value</td><td>Description</td></tr><tr><td>0</td><td>EEPROM erased during chip erase</td></tr><tr><td>1</td><td>EEPROM not erased under chip erase</td></tr></table>

# 7.10.4.6 System Configuration 1

Name: SYSCFG1 Offset: 0x06 Default: 0x07 Property:

The default value given in this fuse description is the factory-programmed value, and should not be mistaken for the Reset value.

<table><tr><td rowspan="2">Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>SUT[2:0]</td><td></td></tr><tr><td>Access</td><td></td><td></td><td></td><td></td><td></td><td>R</td><td>R</td><td>R</td></tr><tr><td>Default</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td></tr></table>

Bits 2:0 – SUT[2:0] Start-Up Time Setting This bit field selects the start-up time between power-on and code execution.   

<table><tr><td rowspan=2 colspan=2>Value     Description0x0       0ms</td></tr><tr><td rowspan=1 colspan=1>0x0</td></tr><tr><td rowspan=1 colspan=1>0x1</td><td rowspan=1 colspan=1>1ms</td></tr><tr><td rowspan=1 colspan=1>0×2</td><td rowspan=1 colspan=1>2ms</td></tr><tr><td rowspan=1 colspan=1>0x3</td><td rowspan=1 colspan=1>4ms</td></tr><tr><td rowspan=1 colspan=1>0x4</td><td rowspan=1 colspan=1>8ms</td></tr><tr><td rowspan=1 colspan=1>0×5</td><td rowspan=1 colspan=1>16 ms</td></tr><tr><td rowspan=1 colspan=1>0×6</td><td rowspan=1 colspan=1>32ms</td></tr><tr><td rowspan=1 colspan=1>0×7</td><td rowspan=1 colspan=1>64ms</td></tr></table>

# 7.10.4.7 Application Code End

Name: APPEND Offset: 0x07 Default: 0x00 Property:

The default value given in this fuse description is the factory-programmed value, and should not be mistaken for the Reset value.   
Bits 7:0 – APPEND[7:0] Application Code Section End   

<table><tr><td>Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td colspan="8">APPEND[7:0]</td></tr><tr><td>Access</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr><tr><td>Default</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

This bit field sets the end of the application code section in blocks of 256 bytes. The end of the application code section will be set as (BOOT size) + (application code size). The remaining Flash will be application data. A value of 0x00 defines the Flash from BOOTEND\*256 to the end of Flash as the application code. When both FUSE.APPEND and FUSE.BOOTEND are 0x00, the entire Flash is the BOOT section.

# 7.10.4.8 Boot End

Name: BOOTEND Offset: 0x08 Default: 0x00 Property:

The default value given in this fuse description is the factory-programmed value, and should not be mistaken for the Reset value.   

<table><tr><td>Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td colspan="8">BOOTEND[7:0]</td></tr><tr><td>Access</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td><td>R</td></tr><tr><td>Default</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

This bit field sets the end of the boot section in blocks of 256 bytes. A value of 0x00 defines the whole Flash as the BOOT section. When both FUSE.APPEND and FUSE.BOOTEND are 0x00, the entire Flash is the BOOT section.

# 7.10.4.9 Lockbits

Name: LOCKBIT Offset: 0x0A Default: 0xC5 Property:

The default value given in this fuse description is the factory-programmed value, and should not be mistaken for the Reset value.   

<table><tr><td>Bit</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td></td><td colspan="8">LOCKBIT[7:0]</td></tr><tr><td>Access</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td><td>R/W</td></tr><tr><td>Default</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr></table>

When the part is locked, UPDI cannot access the system bus, so it cannot read out anything but the System Information Block (SIB).

Bits 7:0 – LOCKBIT[7:0] Lockbits   

<table><tr><td>Value</td><td>Description</td></tr><tr><td>0xC5</td><td>Valid key - memory access is unlocked</td></tr><tr><td>other</td><td>Invalid key - memory access is locked</td></tr></table>

# 8. Peripherals and Architecture

# 8.1 Peripheral Address Map

The address map shows the base address for each peripheral. For complete register description and summary for each peripheral, refer to the respective sections.

Table 8-1. Peripheral Address Map   

<table><tr><td colspan="1" rowspan="1">Base Address</td><td colspan="1" rowspan="1">Name</td><td colspan="3" rowspan="1">Description</td></tr><tr><td colspan="1" rowspan="1">0×0000</td><td colspan="1" rowspan="1">VPORTA</td><td colspan="3" rowspan="1">Virtual Port A</td></tr><tr><td colspan="1" rowspan="1">0×0004</td><td colspan="1" rowspan="1">VPORTB</td><td colspan="3" rowspan="1">Virtual Port B(1)</td></tr><tr><td colspan="1" rowspan="1">0×0008</td><td colspan="1" rowspan="1">VPORTC</td><td colspan="3" rowspan="1">Virtual Port C(1)</td></tr><tr><td colspan="1" rowspan="1">0x001C</td><td colspan="1" rowspan="1">GPIO</td><td colspan="3" rowspan="1">General Purpose IO registers</td></tr><tr><td colspan="1" rowspan="1">0×0030</td><td colspan="1" rowspan="1">CPU</td><td colspan="3" rowspan="1">CPU</td></tr><tr><td colspan="1" rowspan="1">0×0040</td><td colspan="1" rowspan="1">RSTCTRL</td><td colspan="3" rowspan="1">Reset Controller</td></tr><tr><td colspan="1" rowspan="1">0×0050</td><td colspan="1" rowspan="1">SLPCTRL</td><td colspan="3" rowspan="1">Sleep Controller</td></tr><tr><td colspan="1" rowspan="1">0×0060</td><td colspan="1" rowspan="1">CLKCTRL</td><td colspan="3" rowspan="1">Clock Controller</td></tr><tr><td colspan="1" rowspan="1">0×0080</td><td colspan="1" rowspan="1">BOD</td><td colspan="3" rowspan="1">Brown-out Detector</td></tr><tr><td colspan="1" rowspan="1">OX00AO</td><td colspan="1" rowspan="1">VREF</td><td colspan="3" rowspan="1">Voltage Reference</td></tr><tr><td colspan="1" rowspan="1">0x0100</td><td colspan="1" rowspan="1">WDT</td><td colspan="3" rowspan="1">Watchdog Timer</td></tr><tr><td colspan="1" rowspan="1">0x0110</td><td colspan="1" rowspan="1">CPUINT</td><td colspan="3" rowspan="1">Interrupt Controller</td></tr><tr><td colspan="1" rowspan="1">0×0120</td><td colspan="1" rowspan="1">CRCSCAN</td><td colspan="3" rowspan="1">Cyclic Redundancy Check Memory Scan</td></tr><tr><td colspan="1" rowspan="1">0×0140</td><td colspan="1" rowspan="1">RTC</td><td colspan="3" rowspan="1">Real-Time Counter</td></tr><tr><td colspan="1" rowspan="1">0x0180</td><td colspan="1" rowspan="1">EVSYS</td><td colspan="3" rowspan="1">Event System</td></tr><tr><td colspan="1" rowspan="1">0x01C0</td><td colspan="1" rowspan="1">CCL</td><td colspan="3" rowspan="1">Configurable Custom Logic</td></tr><tr><td colspan="1" rowspan="1">0x0200</td><td colspan="1" rowspan="1">PORTMUX</td><td colspan="3" rowspan="1">Port Multiplexer</td></tr><tr><td colspan="1" rowspan="1">0x0400</td><td colspan="1" rowspan="1">PORTA</td><td colspan="3" rowspan="1">Port A Configuration</td></tr><tr><td colspan="1" rowspan="1">0×0420</td><td colspan="1" rowspan="1">PORTB</td><td colspan="3" rowspan="1">Port B Configuration(1)</td></tr><tr><td colspan="1" rowspan="1">0x0440</td><td colspan="1" rowspan="1">PORTC</td><td colspan="3" rowspan="1">Port C Configuration(1)</td></tr><tr><td colspan="1" rowspan="1">0×0600</td><td colspan="1" rowspan="1">ADCO</td><td colspan="3" rowspan="1">Analog-to-Digital Converter 0</td></tr><tr><td colspan="1" rowspan="1">0×0670</td><td colspan="1" rowspan="1">ACO</td><td colspan="3" rowspan="1">Analog Comparator 0</td></tr><tr><td colspan="1" rowspan="1">0×0680</td><td colspan="1" rowspan="1">DACO</td><td colspan="3" rowspan="1">Digital-to-Analog Converter 0</td></tr><tr><td colspan="1" rowspan="1">0x0800</td><td colspan="1" rowspan="1">USARTO</td><td colspan="3" rowspan="1">Universal Synchronous Asynchronous Receiver Transmitter 0</td></tr><tr><td colspan="1" rowspan="1">0×0810</td><td colspan="1" rowspan="1">TWI0</td><td colspan="3" rowspan="1">Two-Wire Interface 0</td></tr><tr><td colspan="1" rowspan="1">0×0820</td><td colspan="1" rowspan="1">SP10</td><td colspan="3" rowspan="1">Serial Peripheral Interface 0</td></tr><tr><td colspan="1" rowspan="1">0xOA00</td><td colspan="1" rowspan="1">TCAO</td><td colspan="3" rowspan="1">Timer/Counter Type A 0</td></tr><tr><td colspan="1" rowspan="1">0x0A40</td><td colspan="1" rowspan="1">TCBO</td><td colspan="3" rowspan="1">Timer/Counter Type B 0</td></tr><tr><td colspan="1" rowspan="1">0x0A80</td><td colspan="1" rowspan="1">TCDO</td><td colspan="3" rowspan="1">Timer/Counter Type D 0</td></tr><tr><td colspan="3" rowspan="2">...ontinuedBase Address    Name          Description</td></tr><tr><td colspan="1" rowspan="1">Base Address</td><td colspan="1" rowspan="1">Name</td></tr><tr><td colspan="1" rowspan="1">0xOF00</td><td colspan="1" rowspan="1">SYSCFG</td><td colspan="1" rowspan="1">System Configuration</td></tr><tr><td colspan="1" rowspan="1">0×1000</td><td colspan="1" rowspan="1">NVMCTRL</td><td colspan="1" rowspan="1">Nonvolatile Memory Controller</td></tr><tr><td colspan="1" rowspan="1">0×1100</td><td colspan="1" rowspan="1">SIGROW</td><td colspan="1" rowspan="1">Signature Row</td></tr><tr><td colspan="1" rowspan="1">0×1280</td><td colspan="1" rowspan="1">FUSES</td><td colspan="1" rowspan="1">Device-specific fuses</td></tr><tr><td colspan="1" rowspan="1">0x1300</td><td colspan="1" rowspan="1">USERROW</td><td colspan="1" rowspan="1">User Row</td></tr></table>

# Note:

1. The availability of this register depends on the device pin count. PORTB/VPORTB is available for devices with 14 pins or more. PORTC/VPORTC is available for devices with 20 pins or more.

# 8.2 Interrupt Vector Mapping

Each of the interrupt vectors is connected to one peripheral instance, as shown in the table below. A peripheral can have one or more interrupt sources, see the Interrupt section in the Functional Description of the respective peripheral for more details on the available interrupt sources.

When the Interrupt condition occurs, an Interrupt flag (nameIF) is set in the Interrupt Flags register of the peripheral (peripheral.INTFLAGS).

An interrupt is enabled or disabled by writing to the corresponding Interrupt Enable (nameIE) bit in the peripheral's Interrupt Control (peripheral.INTCTRL) register.

The naming of the registers may vary slightly in some peripherals.

An interrupt request is generated when the corresponding interrupt is enabled, and the interrupt flag is set. The interrupt request remains Active until the Interrupt flag is cleared. See the peripheral's INTFLAGS register for details on how to clear interrupt flags.

Interrupts must be enabled globally for interrupt requests to be generated.

Table 8-2. Interrupt Vector Mapping   

<table><tr><td rowspan=1 colspan=1>Vector Number</td><td rowspan=1 colspan=1>Program Address(word)</td><td rowspan=1 colspan=1>Peripheral Source</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0×00</td><td rowspan=1 colspan=1>RESET</td><td rowspan=1 colspan=1>RESET</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0×01</td><td rowspan=1 colspan=1>CRCSCAN_NMI</td><td rowspan=1 colspan=1> NMI - Non-Maskable Interrupt from CRC</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>0x02</td><td rowspan=1 colspan=1>BOD_VLM</td><td rowspan=1 colspan=1>VLM - Voltage Level Monitor</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0x03</td><td rowspan=1 colspan=1>PORTA_PORT</td><td rowspan=1 colspan=1>PORTA - Port A</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>0x04</td><td rowspan=1 colspan=1>PORTB_PORT</td><td rowspan=1 colspan=1>PORTB - Port B(1)</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>0×05</td><td rowspan=1 colspan=1>PORTC_PORT</td><td rowspan=1 colspan=1>PORTC - Port C(1)</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0×06</td><td rowspan=1 colspan=1>RTC_CNT</td><td rowspan=1 colspan=1>RTC - Real-Time Counter</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>0×07</td><td rowspan=1 colspan=1>RTC_PIT</td><td rowspan=1 colspan=1>PIT - Periodic Interrupt Timer (in RTCperipheral)</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>0×08</td><td rowspan=1 colspan=1>TCAO_LUNF/TCAO_OVF</td><td rowspan=1 colspan=1>TCA0 - Timer Counter Type A, LUNF/OVF</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>0×09</td><td rowspan=1 colspan=1>TCAO_HUNF</td><td rowspan=1 colspan=1>TCAO, HUNF</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>OxOA</td><td rowspan=1 colspan=1>TCAO_LCMP0/TCAO_CMPO</td><td rowspan=1 colspan=1>TCAO, LCMPO/CMPO</td></tr></table>

# ATtiny212/214/412/414 Automotive Peripherals and Architecture

<table><tr><td rowspan=1 colspan=4>... ontinued</td></tr><tr><td rowspan=1 colspan=1>Vector Number</td><td rowspan=1 colspan=1>Program Address Peripheral Source(word)</td><td rowspan=1 colspan=1>Program Address Peripheral Source</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>0xOB</td><td rowspan=1 colspan=1>TCAO_LCMP1/TCAO_CMP1</td><td rowspan=1 colspan=1>TCA0, LCMP1/CMP1</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>Ox0C</td><td rowspan=1 colspan=1>TCAO_CMP2/TCAO_LCMP2</td><td rowspan=1 colspan=1>TCA0, LCMP2/CMP2</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>0xOD</td><td rowspan=1 colspan=1>TCBO_INT</td><td rowspan=1 colspan=1>TCB0 - Timer Counter Type B</td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>OxOE</td><td rowspan=1 colspan=1>TCDO_OVF</td><td rowspan=1 colspan=1>TCDo - Timer Counter Type D, OVF</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>OxOF</td><td rowspan=1 colspan=1>TCDO_TRIG</td><td rowspan=1 colspan=1>TCDO, TRIG</td></tr><tr><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>0×10</td><td rowspan=1 colspan=1>ACO_AC</td><td rowspan=1 colspan=1>AC0 -Analog Comparator</td></tr><tr><td rowspan=1 colspan=1>17</td><td rowspan=1 colspan=1>0×11</td><td rowspan=1 colspan=1>ADCO_RESRDY</td><td rowspan=1 colspan=1>ADC0 – Analog-to-Digital Converter, RESRDY</td></tr><tr><td rowspan=1 colspan=1>18</td><td rowspan=1 colspan=1>0×12</td><td rowspan=1 colspan=1>ADCO_WCOMP</td><td rowspan=1 colspan=1>ADCO, WCOMP</td></tr><tr><td rowspan=1 colspan=1>19</td><td rowspan=1 colspan=1>0×13</td><td rowspan=1 colspan=1>TWIO_TWIS</td><td rowspan=1 colspan=1>TWI0 - Two-Wire Interface/I²C, TWIS</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>0x14</td><td rowspan=1 colspan=1>TWIO_TWIM</td><td rowspan=1 colspan=1>TWIO, TWIM</td></tr><tr><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>0×15</td><td rowspan=1 colspan=1>SPIO_INT</td><td rowspan=1 colspan=1>SPI0 - Serial Peripheral Interface</td></tr><tr><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>0×16</td><td rowspan=1 colspan=1>USARTO_RXC</td><td rowspan=1 colspan=1>USART0 - Universal Asynchronous Receiver-Transmitter, RXC</td></tr><tr><td rowspan=1 colspan=1>23</td><td rowspan=1 colspan=1>0×17</td><td rowspan=1 colspan=1>USARTO_DRE</td><td rowspan=1 colspan=1>USARTO, DRE</td></tr><tr><td rowspan=1 colspan=1>24</td><td rowspan=1 colspan=1>0×18</td><td rowspan=1 colspan=1>USARTO_TXC</td><td rowspan=1 colspan=1>USARTO, TXC</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>0×19</td><td rowspan=1 colspan=1>NVMCTRL_EE</td><td rowspan=1 colspan=1> NVM - Nonvolatile Memory</td></tr></table>

# Note:

1. The availability of the port pins depends on the device pin count. PORTB is available for devices with 14 pins or more. PORTC is available for devices with 20 pins or more.

# 8.3 System Configuration (SYSCFG)

The system configuration contains the revision ID of the part. The revision ID is readable from the CPU, making it useful for implementing application changes between part revisions.

# 8.3.1 Register Summary

<table><tr><td rowspan=1 colspan=1>Offset</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Bit Pos.</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>0x00</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x01</td><td rowspan=1 colspan=1>REVID</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=8>REVID[7:0]</td></tr></table>

# 8.3.2 Register Description

# 8.3.2.1 Device Revision ID Register

Name: REVID Offset: 0x01 Reset: [revision ID] Property: -

This register is read-only and displays the device revision ID.

![](images/819b8cea74032fd8a5f7571ec3a64ac5cf2aa7846b6503657e5bf04526a31797.jpg)

# Bits 7:0 – REVID[7:0] Revision ID

This bit field contains the device revision. 0x00 = A, 0x01 = B, and so on.

# 9. AVR® CPU

# 9.1 Features

• 8-bit, High-Performance AVR RISC CPU: – 135 instructions – Hardware multiplier

• 32 8-bit Registers Directly Connected to the ALU

• Stack in RAM

• Stack Pointer Accessible in I/O Memory Space • Direct Addressing of up to 64 KB of Unified Memory • Efficient Support for 8-, 16-, and 32-bit Arithmetic • Configuration Change Protection for System-Critical Features • Native On-Chip Debugging (OCD) Support:

– Two hardware breakpoints Change of flow, interrupt, and software breakpoints   
– Run-time read-out of Stack Pointer (SP) register, Program Counter (PC), and Status Register (SREG)   
– Register file read- and writable in Stopped mode

# 9.2 Overview

All AVR devices use the AVR 8-bit CPU. The CPU is able to access memories, perform calculations, control peripherals, and execute instructions in the program memory. Interrupt handling is described in a separate section.

# 9.3 Architecture

To maximize performance and parallelism, the AVR CPU uses a Harvard architecture with separate buses for program and data. Instructions in the program memory are executed with a single-level pipeline. While one instruction is being executed, the next instruction is pre-fetched from the program memory. This enables instructions to be executed on every clock cycle.

Refer to the Instruction Set Summary section for a summary of all AVR instructions.

![](images/40295a76d3c715d0b47745dfcf0e10cb8d3ea64141a57ad346f62316f6cdf061.jpg)  
Figure 9-1. AVR® CPU Architecture

# 9.4 Arithmetic Logic Unit (ALU)

The Arithmetic Logic Unit (ALU) supports arithmetic and logic operations between working registers, or between a constant and a working register. Also, single-register operations can be executed.

The ALU operates in a direct connection with all the 32 general purpose working registers in the register file. Arithmetic operations between working registers or between a working register and an immediate operand are executed in a single clock cycle, and the result is stored in the register file. After an arithmetic or logic operation, the Status Register (CPU.SREG) is updated to reflect information about the result of the operation.

ALU operations are divided into three main categories – arithmetic, logical, and bit functions. Both 8- and 16-bit arithmetic are supported, and the instruction set allows for efficient implementation of the 32-bit arithmetic. The hardware multiplier supports signed and unsigned multiplication and fractional formats.

# 9.4.1 Hardware Multiplier

The multiplier is capable of multiplying two 8-bit numbers into a 16-bit result. The hardware multiplier supports different variations of signed and unsigned integer and fractional numbers:

Multiplication of signed/unsigned integers Multiplication of signed/unsigned fractional numbers Multiplication of a signed integer with an unsigned integer • Multiplication of a signed fractional number with an unsigned fractional number

A multiplication takes two CPU clock cycles.

# 9.5 Functional Description

# 9.5.1 Program Flow

After being reset, the CPU will execute instructions from the lowest address in the Flash program memory, 0x0000.   
The Program Counter (PC) addresses the next instruction to be fetched.

The program flow is supported by conditional and unconditional change of flow instructions, capable of addressing the whole address space directly. Most AVR instructions use a 16-bit word format, and a limited number use a 32-bit format.

During interrupts and subroutine calls, the return address PC is stored on the stack as a word pointer. The stack is allocated in the general data SRAM, and consequently, the stack size is only limited by the total SRAM size and the usage of the SRAM. After the Stack Pointer (SP) is reset, it points to the highest address in the internal SRAM. The SP is read/write accessible in the I/O memory space, enabling easy implementation of multiple stacks or stack areas. The data SRAM can easily be accessed through the five different Addressing modes supported by the AVR CPU.

# 9.5.2 Instruction Execution Timing

The AVR CPU is clocked by the CPU clock, CLK_CPU. No internal clock division is applied. The figure below shows the parallel instruction fetches and executions enabled by the Harvard architecture and the fast-access register file concept. This is the basic pipelining concept enabling up to 1 MIPS/MHz performance with high efficiency.

![](images/c1823580ac1a6ba79417802fd0747c0eddf3c0239c01f31dfdd1000ee3ab5933.jpg)  
Figure 9-2. The Parallel Instruction Fetches and Executions   
The following figure shows the internal timing concept for the register file. In a single clock cycle, an ALU operation using two register operands is executed, and the result is stored in the destination register.

![](images/8ea22a196cba460ce32254bdc286094f3fc1ceb83b59a1bcd4a1017ec4b73eaa.jpg)  
Figure 9-3. Single Cycle ALU Operation

# 9.5.3 Status Register

The Status Register (CPU.SREG) contains information about the result of the most recently executed arithmetic or logic instructions. This information can be used for altering the program flow to perform conditional operations.

CPU.SREG is updated after all ALU operations, as specified in the Instruction Set Summary section. This will, in many cases, remove the need for using the dedicated compare instructions, resulting in a faster and more compact code. CPU.SREG is not automatically stored or restored when entering or returning from an Interrupt Service Routine (ISR). Therefore, maintaining the Status Register between context switches must be handled by user-defined software. CPU.SREG is accessible in the I/O memory space.

# 9.5.4 Stack and Stack Pointer

The stack is used for storing return addresses after interrupts and subroutine calls. Also, it can be used for storing temporary data. The Stack Pointer (SP) always points to the top of the stack. The SP is defined by the Stack Pointer bits in the Stack Pointer register (CPU.SP). The CPU.SP is implemented as two 8-bit registers that are accessible in the I/O memory space.

Data are pushed and popped from the stack using the PUSH and POP instructions. The stack grows from higher to lower memory locations. This means that pushing data onto the stack decreases the SP, and popping data off the stack increases the SP. The SP is automatically set to the highest address of the internal SRAM after being reset. If the stack is changed, it must be set to point above the SRAM start address (see the SRAM Data Memory section in the Memories chapter for the SRAM start address), and it must be defined before any subroutine calls are executed and before interrupts are enabled. See the table below for SP details.

Table 9-1. Stack Pointer Instructions   

<table><tr><td rowspan=1 colspan=1>Instruction</td><td rowspan=1 colspan=1>Stack Pointer</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>PUSH</td><td rowspan=1 colspan=1>Decremented by 1</td><td rowspan=1 colspan=1>Decremented by 1 Data are pushed onto the stack</td></tr><tr><td rowspan=1 colspan=1>ICALLRCALL</td><td rowspan=1 colspan=1>Decremene 2</td><td rowspan=1 colspan=1> Decremented by 2| A return address is pushed onto the stack with a subroutine call or interrupt</td></tr><tr><td rowspan=1 colspan=1>POP</td><td rowspan=1 colspan=1>Incremented by 1</td><td rowspan=1 colspan=1>Data are popped from the stack</td></tr><tr><td rowspan=1 colspan=1>RET RETI</td><td rowspan=1 colspan=1>Incremented by 2</td><td rowspan=1 colspan=1>A return address is popped from the stack with a return from subroutine or returnfrom interrupt</td></tr></table>

During interrupts or subroutine calls, the return address is automatically pushed on the stack as a word pointer, and the SP is decremented by two. The return address consists of two bytes and the Least Significant Byte (LSB) is pushed on the stack first (at the higher address). As an example, a byte pointer return address of 0x0006 is saved on the stack as 0x0003 (shifted one bit to the right), pointing to the fourth 16-bit instruction word in the program memory. The return address is popped off the stack with RETI (when returning from interrupts) and RET (when returning from subroutine calls), and the SP is incremented by two.

The SP is decremented by ‘1’ when data are pushed on the stack with the PUSH instruction, and incremented by ‘1’ when data are popped off the stack using the POP instruction.

To prevent corruption when updating the SP from software, a write to SPL will automatically disable interrupts for up to four instructions or until the next I/O memory write, whichever comes first.

# 9.5.5 Register File

The register file consists of 32 8-bit general purpose working registers used by the CPU. The register file is located in a separate address space from the data memory.

All CPU instructions that operate on working registers have direct and single-cycle access to the register file. Some limitations apply to which working registers can be accessed by an instruction, like the constant arithmetic and logic instructions SBCI, SUBI, CPI, ANDI ORI, and LDI. These instructions apply to the second half of the working registers in the register file, R16 to R31. See the AVR Instruction Set Manual for further details.

Figure 9-4. AVR® CPU General Purpose Working Registers   

<table><tr><td colspan="2">7 0</td><td>Addr.</td></tr><tr><td>R0</td><td></td><td>0x00</td></tr><tr><td>R1</td><td></td><td>0x01</td></tr><tr><td>R2</td><td></td><td>0x02</td></tr></table>

<table><tr><td rowspan=1 colspan=1>R13</td><td rowspan=1 colspan=1>0x0D</td></tr><tr><td rowspan=1 colspan=1>R14</td><td rowspan=1 colspan=1>Ox0E</td></tr><tr><td rowspan=1 colspan=1>R15</td><td rowspan=1 colspan=1>0x0F</td></tr><tr><td rowspan=1 colspan=1>R16</td><td rowspan=1 colspan=1>0x10</td></tr><tr><td rowspan=1 colspan=1>R17</td><td rowspan=1 colspan=1>0x11</td></tr></table>

<table><tr><td>R26</td><td rowspan="5">0x1A 0x1B 0x1C 0x1D</td><td rowspan="5">X-register Low Byte X-register High Byte Y-register Low Byte Y-register High Byte Z-register Low Byte Z-register High Byte</td></tr><tr><td>R27</td></tr><tr><td>R28</td></tr><tr><td>R29 0x1E</td></tr><tr><td>R30 R31</td></tr></table>

# 9.5.5.1 The X-, Y-, and Z-Registers

Working registers R26...R31 have added functions besides their general purpose usage.

These registers can form 16-bit Address Pointers for indirect addressing of data memory. These three address registers are called the X-register, Y-register, and Z-register. The Z-register can also be used as Address Pointer for program memory.

![](images/46024ff5b609c368123186be8881a6adc0fd0a0d3880b8ef236e45b88388d4d8.jpg)  
Figure 9-5. The X-, Y-, and Z-Registers

The lowest register address holds the Least Significant Byte (LSB), and the highest register address holds the Most Significant Byte (MSB). These address registers can function as fixed displacement, automatic increment, and automatic decrement, with different LD\*/ST\* instructions. See the Instruction Set Summary section for details.

# 9.5.6 Accessing 16-bit Registers

Most of the registers for the ATtiny212/214/412/414 Automotive devices are 8-bit registers, but the devices also features a few 16-bit registers. As the AVR data bus has a width of 8 bits, accessing the 16-bit requires two read or write operations. All the 16-bit registers of the ATtiny212/214/412/414 Automotive devices are connected to the 8-bit bus through a temporary (TEMP) register.

![](images/515715b46c6a5b07dceff92c9f4da9c18b8483658a0e9fb839da623e90c0ce60.jpg)  
Figure 9-6. 16-Bit Register Write Operation

For a 16-bit write operation, the low byte register (e.g. DATAL) of the 16-bit register must be written before the high byte register (e.g. DATAH). Writing the low byte register will result in a write to the temporary (TEMP) register instead of the low byte register, as shown in the left side of Figure 9-6. When the high byte register of the 16-bit register is written, TEMP will be copied into the low byte of the 16-bit register in the same clock cycle, as shown in the right side of Figure 9-6.

![](images/7c400303ded462e9f19444c9b2eeff7d5ebfd00813a3c362ddb278ffeae9194c.jpg)  
Figure 9-7. 16-Bit Register Read Operation   
For a 16-bit read operation, the low byte register (e.g. DATAL) of the 16-bit register must be read before the high byte register (e.g. DATAH). When the low byte register is read, the high byte register of the 16-bit register is copied into

the temporary (TEMP) register in the same clock cycle, as show in the left side of Figure 9-7. Reading the high byte register will result in a read from TEMP instead of the high byte register, as shown in right side of Figure 9-7.

The described mechanism ensures that the low and high bytes of 16-bit registers are always accessed simultaneously when reading or writing the registers.

Interrupts can corrupt the timed sequence if an interrupt is triggered during a 16-bit read/write operation and a 16-bit register within the same peripheral is accessed in the interrupt service routine. To prevent this, interrupts should be disabled when writing or reading 16-bit registers. Alternatively, the temporary register can be read before and restored after the 16-bit access in the interrupt service routine.

# 9.5.7 Configuration Change Protection (CCP)

System critical I/O register settings are protected from accidental modification. Flash self-programming (via store to NVM controller) is protected from accidental execution. This is handled globally by the Configuration Change Protection (CCP) register.

Changes to the protected I/O registers or bits, or execution of protected instructions, are only possible after the CPU writes a signature to the CCP register. The different signatures are listed in the description of the CCP register (CPU.CCP).

There are two modes of operation: One for protected I/O registers, and one for protected self-programming.

# 9.5.7.1 Sequence for Write Operation to Configuration Change Protected I/O Registers

In order to write to registers protected by CCP, these steps are required:

1. The software writes the signature that enables change of protected I/O registers to the CCP bit field in the CPU.CCP register.   
2. Within four instructions, the software must write the appropriate data to the protected register. Most protected registers also contain a Write Enable/Change Enable/Lock bit. This bit must be written to ‘1’ in the same operation as the data are written.

The protected change is immediately disabled if the CPU performs write operations to the I/O register or data memory, if load or store accesses to Flash, NVMCTRL, or EEPROM are conducted, or if the SLEEP instruction is executed.

# 9.5.7.2 Sequence for Execution of Self-Programming

In order to execute self-programming (the execution of writes to the NVM controller’s command register), the following steps are required:

1. The software temporarily enables self-programming by writing the SPM signature to the CCP register (CPU.CCP).   
2. Within four instructions, the software must execute the appropriate instruction. The protected change is immediately disabled if the CPU performs accesses to the Flash, NVMCTRL, or EEPROM, or if the SLEEP instruction is executed.

Once the correct signature is written by the CPU, interrupts will be ignored for the duration of the configuration change enable period. Any interrupt request (including non-maskable interrupts) during the CCP period will set the corresponding Interrupt flag as normal, and the request is kept pending. After the CCP period is completed, any pending interrupts are executed according to their level and priority.

# 9.5.8 On-Chip Debug Capabilities

The AVR CPU includes native On-Chip Debug (OCD) support. It includes some powerful debug capabilities to enable profiling and detailed information about the CPU state. It is possible to alter the CPU state and resume code execution. Also, normal debug capabilities like hardware Program Counter breakpoints, breakpoints on change of flow instructions, breakpoints on interrupts, and software breakpoints (BREAK instruction) are present. Refer to the Unified Program and Debug Interface section for details about OCD.

# 9.6 Register Summary

<table><tr><td rowspan=1 colspan=1>Offset</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Bit Pos.</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>0x000x03</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x04</td><td rowspan=1 colspan=1>CCP</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>CCF</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x05…0xOC</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>0xOD</td><td rowspan=2 colspan=1>SP</td><td rowspan=1 colspan=1>7:0</td><td rowspan=2 colspan=8>SP[7:0]SP[15:8]</td></tr><tr><td rowspan=1 colspan=1>15:8</td></tr><tr><td rowspan=1 colspan=1>0x0F</td><td rowspan=1 colspan=1>SREG</td><td rowspan=1 colspan=1>7:0</td><td rowspan=1 colspan=1>I</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>Z</td><td rowspan=1 colspan=1>C</td></tr></table>

# 9.7 Register Description