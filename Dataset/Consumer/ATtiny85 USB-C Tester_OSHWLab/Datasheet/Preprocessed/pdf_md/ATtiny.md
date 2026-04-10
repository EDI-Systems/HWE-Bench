# Atmel 8-bit AVR Microcontroller with 2/4/8K Bytes In-System Programmable Flash

# ATtiny25/V / ATtiny45/V / ATtiny85/V Summary

# Features

• High Performance, Low Power AVR® 8-Bit Microcontroller

dvanced RISC Architecture   
– 120 Powerful Instructions – Most Single Clock Cycle Execution   
– 32 x 8 General Purpose Working Registers   
– Fully Static Operation

• Non-volatile Program and Data Memories – 2/4/8K Bytes of In-System Programmable Program Memory Flash • Endurance: 10,000 Write/Erase Cycles – 128/256/512 Bytes In-System Programmable EEPROM • Endurance: 100,000 Write/Erase Cycles – 128/256/512 Bytes Internal SRAM – Programming Lock for Self-Programming Flash Program and EEPROM Data Security

• Peripheral Features

– 8-bit Timer/Counter with Prescaler and Two PWM Channels   
– 8-bit High Speed Timer/Counter with Separate Prescaler • 2 High Frequency PWM Outputs with Separate Output Compare Registers • Programmable Dead Time Generator   
– USI – Universal Serial Interface with Start Condition Detector   
– 10-bit ADC • 4 Single Ended Channels • 2 Differential ADC Channel Pairs with Programmable Gain (1x, 20x) • Temperature Measurement

– Programmable Watchdog Timer with Separate On-chip Oscillator – On-chip Analog Comparator

• Special Microcontroller Features

– debugWIRE On-chip Debug System   
– In-System Programmable via SPI Port External and Internal Interrupt Sources Low Power Idle, ADC Noise Reduction, and Power-down Modes Enhanced Power-on Reset Circuit   
– Programmable Brown-out Detection Circuit   
– Internal Calibrated Oscillator

• I/O and Packages – Six Programmable I/O Lines – 8-pin PDIP, 8-pin SOIC, 20-pad QFN/MLF, and 8-pin TSSOP (only ATtiny45/V)

• Operating Voltage – 1.8 - 5.5V for ATtiny25V/45V/85V – 2.7 - 5.5V for ATtiny25/45/85

• Speed Grade – ATtiny25V/45V/85V: 0 – 4 MHz @ 1.8 - 5.5V, 0 - 10 MHz @ 2.7 - 5.5V – ATtiny25/45/85: 0 – 10 MHz @ 2.7 - 5.5V, 0 - 20 MHz @ 4.5 - 5.5V

• Industrial Temperature Range • Low Power Consumption – Active Mode: • 1 MHz, 1.8V: 300 µA – Power-down Mode: • 0.1 µA at 1.8V

![](images/33e83501e1b0a5df1ac4427c9f2d4aea07c905b5f608d7af8a68aaa82560205e.jpg)  
Figure 1-1. Pinout ATtiny25/45/85   
NOTE: Bottom pad should be soldered to ground. DNC: Do Not Connect

# 1.1 Pin Descriptions

1.1.1 VCC Supply voltage.

1.1.2 GND Ground.

# 1.1.3 Port B (PB5:PB0)

Port B is a 6-bit bi-directional I/O port with internal pull-up resistors (selected for each bit). The Port B output buffers have symmetrical drive characteristics with both high sink and source capability. As inputs, Port B pins that are externally pulled low will source current if the pull-up resistors are activated. The Port B pins are tri-stated when a reset condition becomes active, even if the clock is not running.

# Atmel

Port B also serves the functions of various special features of the ATtiny25/45/85 as listed in “Alternate Functions of Port B” on page 60.

On ATtiny25, the programmable I/O ports PB3 and PB4 (pins 2 and 3) are exchanged in ATtiny15 Compatibilit Mode for supporting the backward compatibility with ATtiny15.

# 1.1.4 RESET

Reset input. A low level on this pin for longer than the minimum pulse length will generate a reset, even if the clock is not running and provided the reset pin has not been disabled. The minimum pulse length is given in Table 21-4 on page 165. Shorter pulses are not guaranteed to generate a reset.

The reset pin can also be used as a (weak) I/O pin.

# 2. Overview

The ATtiny25/45/85 is a low-power CMOS 8-bit microcontroller based on the AVR enhanced RISC architecture. By executing powerful instructions in a single clock cycle, the ATtiny25/45/85 achieves throughputs approaching 1 MIPS per MHz allowing the system designer to optimize power consumption versus processing speed.

# 2.1 Block Diagram

![](images/10fea05c98072613787e81e646095a0109622eb41be7385c81c993f3a7ebb4f4.jpg)  
Figure 2-1. Block Diagram

The AVR core combines a rich instruction set with 32 general purpose working registers. All 32 registers are directly connected to the Arithmetic Logic Unit (ALU), allowing two independent registers to be accessed in one single instruction executed in one clock cycle. The resulting architecture is more code efficient while achieving throughputs up to ten times faster than conventional CISC microcontrollers.

The ATtiny25/45/85 provides the following features: 2/4/8K bytes of In-System Programmable Flash, 128/256/512 bytes EEPROM, 128/256/256 bytes SRAM, 6 general purpose I/O lines, 32 general purpose working registers, one 8-bit Timer/Counter with compare modes, one 8-bit high speed Timer/Counter, Universal Serial Interface, Internal and External Interrupts, a 4-channel, 10-bit ADC, a programmable Watchdog Timer with internal Oscillator, and three software selectable power saving modes. Idle mode stops the CPU while allowing the SRAM, Timer/Counter, ADC, Analog Comparator, and Interrupt system to continue functioning. Power-down mode saves the register contents, disabling all chip functions until the next Interrupt or Hardware Reset. ADC Noise Reduction mode stops the CPU and all I/O modules except ADC, to minimize switching noise during ADC conversions.

The device is manufactured using Atmel’s high density non-volatile memory technology. The On-chip ISP Flash allows the Program memory to be re-programmed In-System through an SPI serial interface, by a conventional non-volatile memory programmer or by an On-chip boot code running on the AVR core.

The ATtiny25/45/85 AVR is supported with a full suite of program and system development tools including: C Compilers, Macro Assemblers, Program Debugger/Simulators and Evaluation kits.

# 3. About

# 3.1 Resources

A comprehensive set of development tools, application notes and datasheets are available for download on http://www.atmel.com/avr.

# 3.2 Code Examples

This documentation contains simple code examples that briefly show how to use various parts of the device. These code examples assume that the part specific header file is included before compilation. Be aware that not all C compiler vendors include bit definitions in the header files and interrupt handling in C is compiler dependent. Please confirm with the C compiler documentation for more details.

For I/O Registers located in the extended I/O map, “IN”, “OUT”, “SBIS”, “SBIC”, “CBI”, and “SBI” instructions must be replaced with instructions that allow access to extended I/O. Typically, this means “LDS” and “STS” combined with “SBRS”, “SBRC”, “SBR”, and “CBR”. Note that not all AVR devices include an extended I/O map.

# 3.3 Capacitive Touch Sensing

Atmel QTouch Library provides a simple to use solution for touch sensitive interfaces on Atmel AVR microcon trollers. The QTouch Library includes support for QTouch® and QMatrix® acquisition methods.

Touch sensing is easily added to any application by linking the QTouch Library and using the Application Programming Interface (API) of the library to define the touch channels and sensors. The application then calls the API to retrieve channel information and determine the state of the touch sensor.

The QTouch Library is free and can be downloaded from the Atmel website. For more information and details o implementation, refer to the QTouch Library User Guide – also available from the Atmel website.

# 3.4 Data Retention

Reliability Qualification results show that the projected data retention failure rate is much less than 1 PPM over 20 years at 85°C or 100 years at 25°C.

# 4. Register Summary

Note: 1. For compatibility with future devices, reserved bits should be written to zero if accessed. Reserved I/O memory addresses   

<table><tr><td rowspan=1 colspan=1>Address</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Bit 7</td><td rowspan=1 colspan=1>Bit 6</td><td rowspan=1 colspan=1>Bit5</td><td rowspan=1 colspan=1>Bit 4</td><td rowspan=1 colspan=1>Bit 3</td><td rowspan=1 colspan=1>Bit 2</td><td rowspan=1 colspan=1>Bit 1</td><td rowspan=1 colspan=1>Bit 0</td><td rowspan=1 colspan=1>Page</td></tr><tr><td rowspan=1 colspan=1>0x3F</td><td rowspan=1 colspan=1>SREG</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>T</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>Z</td><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>page 8</td></tr><tr><td rowspan=1 colspan=1>0x3E</td><td rowspan=1 colspan=1>SPH</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>SP9</td><td rowspan=1 colspan=1>SP8</td><td rowspan=1 colspan=1>page 11</td></tr><tr><td rowspan=1 colspan=1>0x3D</td><td rowspan=1 colspan=1>SPL</td><td rowspan=1 colspan=1>SP7</td><td rowspan=1 colspan=1>SP6</td><td rowspan=1 colspan=1>SP5</td><td rowspan=1 colspan=1>SP4</td><td rowspan=1 colspan=1>SP3</td><td rowspan=1 colspan=1>SP2</td><td rowspan=1 colspan=1>SP1</td><td rowspan=1 colspan=1>SPO</td><td rowspan=1 colspan=1>page 11</td></tr><tr><td rowspan=1 colspan=1>0x3C</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x3B</td><td rowspan=1 colspan=1>GIMSK</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>INTO</td><td rowspan=1 colspan=1>PCIE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>page 51</td></tr><tr><td rowspan=1 colspan=1>0x3A</td><td rowspan=1 colspan=1>GIFR</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>INTFO</td><td rowspan=1 colspan=1>PCIF</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>page 52</td></tr><tr><td rowspan=1 colspan=1>0x39</td><td rowspan=1 colspan=1>TIMSK</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>OCIE1A</td><td rowspan=1 colspan=1>OCIE1B</td><td rowspan=1 colspan=1>OCIEOA</td><td rowspan=1 colspan=1>OCIEOB</td><td rowspan=1 colspan=1>TOIE1</td><td rowspan=1 colspan=1>TOIEO</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>pages 81, 102</td></tr><tr><td rowspan=1 colspan=1>0x38</td><td rowspan=1 colspan=1>TIFR</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>OCF1A</td><td rowspan=1 colspan=1>OCF1B</td><td rowspan=1 colspan=1>OCFOA</td><td rowspan=1 colspan=1>OCFOB</td><td rowspan=1 colspan=1>TOV1</td><td rowspan=1 colspan=1>TOVO</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>page 81</td></tr><tr><td rowspan=1 colspan=1>0x37</td><td rowspan=1 colspan=1>SPMCSR</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>RSIG</td><td rowspan=1 colspan=1>CTPB</td><td rowspan=1 colspan=1>RFLB</td><td rowspan=1 colspan=1>PGWRT</td><td rowspan=1 colspan=1>PGERS</td><td rowspan=1 colspan=1>SPMEN</td><td rowspan=1 colspan=1>page 145</td></tr><tr><td rowspan=1 colspan=1>0×36</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x35</td><td rowspan=1 colspan=1>MCUCR</td><td rowspan=1 colspan=1>BODS</td><td rowspan=1 colspan=1>PUD</td><td rowspan=1 colspan=1>SE</td><td rowspan=1 colspan=1>SM1</td><td rowspan=1 colspan=1>SMO</td><td rowspan=1 colspan=1>BODSE</td><td rowspan=1 colspan=1>ISC01</td><td rowspan=1 colspan=1>ISC0O</td><td rowspan=1 colspan=1>pages 37, 51, 64</td></tr><tr><td rowspan=1 colspan=1>0×34</td><td rowspan=1 colspan=1>MCUSR</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>WDRF</td><td rowspan=1 colspan=1>BORF</td><td rowspan=1 colspan=1>EXTRF</td><td rowspan=1 colspan=1>PORF</td><td rowspan=1 colspan=1>page 44,</td></tr><tr><td rowspan=1 colspan=1>0x33</td><td rowspan=1 colspan=1>TCCROB</td><td rowspan=1 colspan=1>FOCOA</td><td rowspan=1 colspan=1>FOCOB</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>WGM02</td><td rowspan=1 colspan=1>CS02</td><td rowspan=1 colspan=1>CS01</td><td rowspan=1 colspan=1>CS0O</td><td rowspan=1 colspan=1>page 79</td></tr><tr><td rowspan=1 colspan=1>0x32</td><td rowspan=1 colspan=1>TCNTO</td><td rowspan=1 colspan=5>Timer/Counter0</td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>page 80</td></tr><tr><td rowspan=1 colspan=1>0x31</td><td rowspan=1 colspan=1>OSCCAL</td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=2>Oscillator Calibration Register</td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>page 31</td></tr><tr><td rowspan=1 colspan=1>0x30</td><td rowspan=1 colspan=1>TCCR1</td><td rowspan=1 colspan=1>CTC1</td><td rowspan=1 colspan=1>PWM1A</td><td rowspan=1 colspan=1>COM1A1</td><td rowspan=1 colspan=1>COM1A0</td><td rowspan=1 colspan=1>CS13</td><td rowspan=1 colspan=1>CS12</td><td rowspan=1 colspan=1>CS11</td><td rowspan=1 colspan=1>CS10</td><td rowspan=1 colspan=1>pages 89, 100</td></tr><tr><td rowspan=1 colspan=1>0x2F</td><td rowspan=1 colspan=1>TCNT1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>pages 91, 102</td></tr><tr><td rowspan=1 colspan=1>0x2E</td><td rowspan=1 colspan=1>OCR1A</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>/Counter1 Outp</td><td rowspan=1 colspan=1>it Compare Reg</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>pages 91, 102</td></tr><tr><td rowspan=1 colspan=1>0x2D</td><td rowspan=1 colspan=1>OCR1C</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[Time</td><td rowspan=1 colspan=1>/Counter1 Outp</td><td rowspan=1 colspan=1>t Compare Reg</td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>pages 91, 102</td></tr><tr><td rowspan=1 colspan=1>0x2C</td><td rowspan=1 colspan=1>GTCCR</td><td rowspan=1 colspan=1>TSM</td><td rowspan=1 colspan=1>PWM1B</td><td rowspan=1 colspan=1>COM1B1</td><td rowspan=1 colspan=1>COM1B0</td><td rowspan=1 colspan=1>FOC1B</td><td rowspan=1 colspan=1>FOC1A</td><td rowspan=1 colspan=1>PSR1</td><td rowspan=1 colspan=1>PSRO</td><td rowspan=1 colspan=1>pages 77, 90, 101</td></tr><tr><td rowspan=1 colspan=1>0x2B</td><td rowspan=1 colspan=1>OCR1B</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>/Counter1 Outp</td><td rowspan=1 colspan=1>it Compare Reg</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>page 92</td></tr><tr><td rowspan=1 colspan=1>0x2A</td><td rowspan=1 colspan=1>TCCROA</td><td rowspan=1 colspan=1>COM0A1</td><td rowspan=1 colspan=1>COMOAO</td><td rowspan=1 colspan=1>COM0B1</td><td rowspan=1 colspan=1>COMOB0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>WGM01</td><td rowspan=1 colspan=1>WGM00</td><td rowspan=1 colspan=1>page 77</td></tr><tr><td rowspan=1 colspan=1>0×29</td><td rowspan=1 colspan=1>OCROA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Counter0–Outp</td><td rowspan=1 colspan=1>ut Compare Re</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>page 80</td></tr><tr><td rowspan=1 colspan=1>0x28</td><td rowspan=1 colspan=1>OCROB</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Counter0–Outp</td><td rowspan=1 colspan=1>utCompareRe</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>page 81</td></tr><tr><td rowspan=1 colspan=1>0x27</td><td rowspan=1 colspan=1>PLLCSR</td><td rowspan=1 colspan=1>LSM</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>PCKE</td><td rowspan=1 colspan=1>PLLE</td><td rowspan=1 colspan=1>PLOCK</td><td rowspan=1 colspan=1>pages 94, 103</td></tr><tr><td rowspan=1 colspan=1>0x26</td><td rowspan=1 colspan=1>CLKPR</td><td rowspan=1 colspan=1>CLKPCE</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>CLKPS3</td><td rowspan=1 colspan=1>CLKPS2</td><td rowspan=1 colspan=1>CLKPS1</td><td rowspan=1 colspan=1>CLKPSO</td><td rowspan=1 colspan=1>page 32</td></tr><tr><td rowspan=1 colspan=1>0x25</td><td rowspan=1 colspan=1>DT1A</td><td rowspan=1 colspan=1>DT1AH3</td><td rowspan=1 colspan=1>DT1AH2</td><td rowspan=1 colspan=1>DT1AH1</td><td rowspan=1 colspan=1>DT1AH0</td><td rowspan=1 colspan=1>DT1AL3</td><td rowspan=1 colspan=1>DT1AL2</td><td rowspan=1 colspan=1>DT1AL1</td><td rowspan=1 colspan=1>DT1AL0</td><td rowspan=1 colspan=1>page 107</td></tr><tr><td rowspan=1 colspan=1>0x24</td><td rowspan=1 colspan=1>DT1B</td><td rowspan=1 colspan=1>DT1BH3</td><td rowspan=1 colspan=1>DT1BH2</td><td rowspan=1 colspan=1>DT1BH1</td><td rowspan=1 colspan=1>DT1BH0</td><td rowspan=1 colspan=1>DT1BL3</td><td rowspan=1 colspan=1>DT1BL2</td><td rowspan=1 colspan=1>DT1BL1</td><td rowspan=1 colspan=1>DT1BL0</td><td rowspan=1 colspan=1>page 107</td></tr><tr><td rowspan=1 colspan=1>0x23</td><td rowspan=1 colspan=1>DTPS1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DTPS11</td><td rowspan=1 colspan=1>DTPS10</td><td rowspan=1 colspan=1>page 106</td></tr><tr><td rowspan=1 colspan=1>0x22</td><td rowspan=1 colspan=1>DWDR</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>page 140</td></tr><tr><td rowspan=1 colspan=1>0x21</td><td rowspan=1 colspan=1>WDTCR</td><td rowspan=1 colspan=1>WDIF</td><td rowspan=1 colspan=1>WDIE</td><td rowspan=1 colspan=1>WDP3</td><td rowspan=1 colspan=1>WDCE</td><td rowspan=1 colspan=1>WDE</td><td rowspan=1 colspan=1>WDP2</td><td rowspan=1 colspan=1>WDP1</td><td rowspan=1 colspan=1>WDP0</td><td rowspan=1 colspan=1>page 45</td></tr><tr><td rowspan=1 colspan=1>0x20</td><td rowspan=1 colspan=1>PRR</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>PRTIM1</td><td rowspan=1 colspan=1>PRTIMO</td><td rowspan=1 colspan=1>PRUSI</td><td rowspan=1 colspan=1>PRADC</td><td rowspan=1 colspan=1>page 36</td></tr><tr><td rowspan=1 colspan=1>0x1F</td><td rowspan=1 colspan=1>EEARH</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>EEAR8</td><td rowspan=1 colspan=1>page 20</td></tr><tr><td rowspan=1 colspan=1>0x1E</td><td rowspan=1 colspan=1>EEARL</td><td rowspan=1 colspan=1>EEAR7</td><td rowspan=1 colspan=1>EEAR6</td><td rowspan=1 colspan=1>EEAR5</td><td rowspan=1 colspan=2>EEAR4    EEAR3</td><td rowspan=1 colspan=1>EEAR2</td><td rowspan=1 colspan=2>EEAR1    EEARO</td><td rowspan=1 colspan=1>page 21</td></tr><tr><td rowspan=1 colspan=1>0x1D</td><td rowspan=1 colspan=1>EEDR</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>EEPROM Data Register</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>page 21</td></tr><tr><td rowspan=1 colspan=1>$0x1C</td><td rowspan=1 colspan=1>EECR</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>EEPM1</td><td rowspan=1 colspan=1>EEPMO</td><td rowspan=1 colspan=1>EERIE</td><td rowspan=1 colspan=1>EEMPE</td><td rowspan=1 colspan=1>EEPE</td><td rowspan=1 colspan=1>EERE</td><td rowspan=1 colspan=1>page 21</td></tr><tr><td rowspan=1 colspan=1>$0x1B</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>$0x1A</td><td rowspan=1 colspan=1>Reserved</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0×19</td><td rowspan=1 colspan=1>Reserved</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x18</td><td rowspan=1 colspan=1>PORTB</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>PORTB5</td><td rowspan=1 colspan=1>PORTB4</td><td rowspan=1 colspan=1>PORTB3</td><td rowspan=1 colspan=1>PORTB2</td><td rowspan=1 colspan=1>PORTB1</td><td rowspan=1 colspan=1>PORTB0</td><td rowspan=1 colspan=1>page 64</td></tr><tr><td rowspan=1 colspan=1>0×17</td><td rowspan=1 colspan=1>DDRB</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>DDB5</td><td rowspan=1 colspan=1>DDB4</td><td rowspan=1 colspan=1>DDB3</td><td rowspan=1 colspan=1>DDB2</td><td rowspan=1 colspan=1>DDB1</td><td rowspan=1 colspan=1>DDBO</td><td rowspan=1 colspan=1>page 64</td></tr><tr><td rowspan=1 colspan=1>0x16</td><td rowspan=1 colspan=1>PINB</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>PINB5</td><td rowspan=1 colspan=1>PINB4</td><td rowspan=1 colspan=1>PINB3</td><td rowspan=1 colspan=1>PINB2</td><td rowspan=1 colspan=1>PINB1</td><td rowspan=1 colspan=1>PINB0</td><td rowspan=1 colspan=1>page 64</td></tr><tr><td rowspan=1 colspan=1>$0x15</td><td rowspan=1 colspan=1>PCMSK</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>PCINT5</td><td rowspan=1 colspan=1>PCINT4</td><td rowspan=1 colspan=1>PCINT3</td><td rowspan=1 colspan=1>PCINT2</td><td rowspan=1 colspan=1>PCINT1</td><td rowspan=1 colspan=1>PCINTO</td><td rowspan=1 colspan=1>page 52</td></tr><tr><td rowspan=1 colspan=1>0x14</td><td rowspan=1 colspan=1>DIDR0</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>ADCOD</td><td rowspan=1 colspan=1>ADC2D</td><td rowspan=1 colspan=1>ADC3D</td><td rowspan=1 colspan=1>ADC1D</td><td rowspan=1 colspan=1>AIN1D</td><td rowspan=1 colspan=1>AINOD</td><td rowspan=1 colspan=1>pages 121, 138</td></tr><tr><td rowspan=1 colspan=1>0x13</td><td rowspan=1 colspan=1>GPIOR2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>General Purpos</td><td rowspan=1 colspan=1>e I/O Register 2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>page 10</td></tr><tr><td rowspan=1 colspan=1>0x12</td><td rowspan=1 colspan=1>GPIOR1</td><td rowspan=1 colspan=8>General Purpose IO Register 1</td><td rowspan=1 colspan=1>page 10</td></tr><tr><td rowspan=1 colspan=1>0x11</td><td rowspan=1 colspan=1>GPIOR0</td><td rowspan=1 colspan=8>General Purpose I/O Register 0</td><td rowspan=1 colspan=1>page 10</td></tr><tr><td rowspan=1 colspan=1>$0x10</td><td rowspan=1 colspan=1>USIBR</td><td rowspan=1 colspan=8>USI Buffer Register</td><td rowspan=1 colspan=1>page 115</td></tr><tr><td rowspan=1 colspan=1>0x0F</td><td rowspan=1 colspan=1>USIDR</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=6>USI Data Register</td><td rowspan=1 colspan=1>page 115</td></tr><tr><td rowspan=1 colspan=1>0xOE</td><td rowspan=1 colspan=1>USISR</td><td rowspan=1 colspan=1>USISIF</td><td rowspan=1 colspan=1>USIOIF</td><td rowspan=1 colspan=1>USIPF</td><td rowspan=1 colspan=1>USIDC</td><td rowspan=1 colspan=1>USICNT3</td><td rowspan=1 colspan=1>USICNT2</td><td rowspan=1 colspan=1>USICNT1</td><td rowspan=1 colspan=1>USICNTO</td><td rowspan=1 colspan=1>page 115</td></tr><tr><td rowspan=1 colspan=1>0xOD</td><td rowspan=1 colspan=1>USICR</td><td rowspan=1 colspan=1>USISIE</td><td rowspan=1 colspan=1>USIOIE</td><td rowspan=1 colspan=1>USIWM1</td><td rowspan=1 colspan=1>USIWMO</td><td rowspan=1 colspan=1>USICS1</td><td rowspan=1 colspan=1>USICSO</td><td rowspan=1 colspan=1>USICLK</td><td rowspan=1 colspan=1>USITC</td><td rowspan=1 colspan=1>page 116</td></tr><tr><td rowspan=1 colspan=1>0x0C</td><td rowspan=1 colspan=1>Reserved</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x0B</td><td rowspan=1 colspan=1>Reserved</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0×0A</td><td rowspan=1 colspan=1>Reserved</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x09</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=8>-</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x08</td><td rowspan=1 colspan=1>ACSR</td><td rowspan=1 colspan=1>ACD</td><td rowspan=1 colspan=1>ACBG</td><td rowspan=1 colspan=1>ACO</td><td rowspan=1 colspan=1>ACI</td><td rowspan=1 colspan=1>ACIE</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>ACIS1</td><td rowspan=1 colspan=1>ACISO</td><td rowspan=1 colspan=1>page 120</td></tr><tr><td rowspan=1 colspan=1>0x07</td><td rowspan=1 colspan=1>ADMUX</td><td rowspan=1 colspan=1>REFS1</td><td rowspan=1 colspan=1>REFSO</td><td rowspan=1 colspan=1>ADLAR</td><td rowspan=1 colspan=1>REFS2</td><td rowspan=1 colspan=1>MUX3</td><td rowspan=1 colspan=1>MUX2</td><td rowspan=1 colspan=1>MUX1</td><td rowspan=1 colspan=1>MUXO</td><td rowspan=1 colspan=1>page 134</td></tr><tr><td rowspan=1 colspan=1>0x06</td><td rowspan=1 colspan=1>ADCSRA</td><td rowspan=1 colspan=1>ADEN</td><td rowspan=1 colspan=1>ADSC</td><td rowspan=1 colspan=1>ADATE</td><td rowspan=1 colspan=1>ADIF</td><td rowspan=1 colspan=1>ADIE</td><td rowspan=1 colspan=1>ADPS2</td><td rowspan=1 colspan=1>ADPS1</td><td rowspan=1 colspan=1>ADPSO</td><td rowspan=1 colspan=1>page 136</td></tr><tr><td rowspan=1 colspan=1>0x05</td><td rowspan=1 colspan=1>ADCH</td><td rowspan=1 colspan=5>ADC Data Register High Byte</td><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>page 137</td></tr><tr><td rowspan=1 colspan=1>0x04</td><td rowspan=1 colspan=1>ADCL</td><td rowspan=1 colspan=8>ADC Data Register Low Byte</td><td rowspan=1 colspan=1>page 137</td></tr><tr><td rowspan=1 colspan=1>0x03</td><td rowspan=1 colspan=1>ADCSRB</td><td rowspan=1 colspan=8>BIN      ACME      IPR                             ADTS2    ADTS1    ADTSO</td><td rowspan=1 colspan=1>pages 120, 137</td></tr><tr><td rowspan=1 colspan=1>0x02</td><td rowspan=1 colspan=1>Reserved</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x01</td><td rowspan=1 colspan=1>Reserved</td><td rowspan=1 colspan=8>-</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0x00</td><td rowspan=1 colspan=1>Reserved</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=1></td></tr></table>

should never be written.

2. I/O Registers within the address range 0x00 - 0x1F are directly bit-accessible using the SBI and CBI instructions. In these registers, the value of single bits can be checked by using the SBIS and SBIC instructions.

3. Some of the Status Flags are cleared by writing a logical one to them. Note that, unlike most other AVRs, the CBI and SBI instructions will only operation the specified bit, and can therefore be used on registers containing such Status Flags. The CBI and SBI instructions work with registers 0x00 to 0x1F only.

<table><tr><td colspan="6" rowspan="1"> Instruction Set Summary</td></tr><tr><td colspan="1" rowspan="1">Mnemonics</td><td colspan="1" rowspan="1">Operands</td><td colspan="1" rowspan="1">Description</td><td colspan="1" rowspan="1">Operation</td><td colspan="1" rowspan="1">Flags</td><td colspan="1" rowspan="1">#Clocks</td></tr><tr><td colspan="1" rowspan="1">ARITHMETIC AND I</td><td colspan="1" rowspan="1">OGIC INSTRUCTION</td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">[</td><td colspan="1" rowspan="1">[</td></tr><tr><td colspan="1" rowspan="1">ADD</td><td colspan="1" rowspan="1">Rd, Rr</td><td colspan="1" rowspan="1">Add two Registers</td><td colspan="1" rowspan="1">Rd ←Rd + Rr</td><td colspan="1" rowspan="1">Z,C,N,V,H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">ADC</td><td colspan="1" rowspan="1">Rd, Rr</td><td colspan="1" rowspan="1">Add with Carry two Registers</td><td colspan="1" rowspan="1">Rd←Rd + Rr + C</td><td colspan="1" rowspan="1">Z,C,N,V,H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">ADIW</td><td colspan="1" rowspan="1">Rdl,K</td><td colspan="1" rowspan="1">Add Immediate to Word</td><td colspan="1" rowspan="1">Rdh:RdI &lt; Rdh:RdI + K</td><td colspan="1" rowspan="1">Z.C,N,V,S</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">SUB</td><td colspan="1" rowspan="1">Rd, Rr</td><td colspan="1" rowspan="1">Subtract two Registers</td><td colspan="1" rowspan="1">Rd ← Rd - Rr</td><td colspan="1" rowspan="1">Z,C,N,V,H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SUBI</td><td colspan="1" rowspan="1">Rd,K</td><td colspan="1" rowspan="1">Subtract Constant from Register</td><td colspan="1" rowspan="1">Rd←Rd - K</td><td colspan="1" rowspan="1">Z,C,N,V,H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SBC</td><td colspan="1" rowspan="1">Rd, Rr</td><td colspan="1" rowspan="1">Subtract with Carr two Registers</td><td colspan="1" rowspan="1">Rd &lt;Rd - Rr - C</td><td colspan="1" rowspan="1">Z,C,N,V,H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SBCI</td><td colspan="1" rowspan="1">Rd,K</td><td colspan="1" rowspan="1">Subtract with Carry Constant from Reg.</td><td colspan="1" rowspan="1">Rd←Rd-K-C</td><td colspan="1" rowspan="1">Z,C,N,V,H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SBIW</td><td colspan="1" rowspan="1">Rdl,K</td><td colspan="1" rowspan="1">Subtract Immediate from Word</td><td colspan="1" rowspan="1">Rdh:RdI ←— Rdh:Rdl - K</td><td colspan="1" rowspan="1">Z.C,N,V,S</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">AND</td><td colspan="1" rowspan="1">Rd, Rr</td><td colspan="1" rowspan="1">Logical AND Registers</td><td colspan="1" rowspan="1">Rd ←Rd·Rr</td><td colspan="1" rowspan="1">Z,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">ANDI</td><td colspan="1" rowspan="1">Rd,K</td><td colspan="1" rowspan="1">Logical AND Register and Constant</td><td colspan="1" rowspan="1">Rd ←Rd•K</td><td colspan="1" rowspan="1">Z,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">OR</td><td colspan="1" rowspan="1">Rd,Rr</td><td colspan="1" rowspan="1">Logical OR Registers</td><td colspan="1" rowspan="1">Rd &lt;− Rd v Rr</td><td colspan="1" rowspan="1">Z,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">ORI</td><td colspan="1" rowspan="1">Rd,K</td><td colspan="1" rowspan="1">Logical OR Register and Constant</td><td colspan="1" rowspan="1">Rd ←Rd v K</td><td colspan="1" rowspan="1">Z,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">EOR</td><td colspan="1" rowspan="1">Rd, Rr</td><td colspan="1" rowspan="1">Exclusive OR Registers</td><td colspan="1" rowspan="1">Rd &lt; Rd⊕Rr</td><td colspan="1" rowspan="1">Z,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">COM</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">One's Complement</td><td colspan="1" rowspan="1">Rd ← OxFF−Rd</td><td colspan="1" rowspan="1">Z,C,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">NEG</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Two's Complement</td><td colspan="1" rowspan="1">Rd ←0x00-Rd</td><td colspan="1" rowspan="1">Z,C,N,V,H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SBR</td><td colspan="1" rowspan="1">Rd,K</td><td colspan="1" rowspan="1">Set Bit(s) in Register</td><td colspan="1" rowspan="1">Rd &lt;RdvK</td><td colspan="1" rowspan="1">Z,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CBR</td><td colspan="1" rowspan="1">Rd,K</td><td colspan="1" rowspan="1">Clear Bit(s) in Register</td><td colspan="1" rowspan="1">Rd ←Rd·(OxFF - K)</td><td colspan="1" rowspan="1">Z,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">INC</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Increment</td><td colspan="1" rowspan="1">Rd ←Rd + 1</td><td colspan="1" rowspan="1">Z.,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">DEC</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Decrement</td><td colspan="1" rowspan="1">Rd←Rd-1</td><td colspan="1" rowspan="1">Z,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">TST</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Test for Zero or Minus</td><td colspan="1" rowspan="1">Rd ← Rd•Rd</td><td colspan="1" rowspan="1">Z,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CLR</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Clear Register</td><td colspan="1" rowspan="1">Rd ←Rd⊕Rd</td><td colspan="1" rowspan="1">Z,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SER</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Set Register</td><td colspan="1" rowspan="1">Rd←0xFF</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">BRANCH INSTRUCTIONS</td><td colspan="1" rowspan="1"></td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">RJMP</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Relative Jump</td><td colspan="1" rowspan="1">PC←PC+k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">JMP</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Indirect Jump to (Z)</td><td colspan="1" rowspan="1">$PC←Z$</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">RCALL</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Relative Subroutine Call</td><td colspan="1" rowspan="1">PC←PC+k+1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">3</td></tr><tr><td colspan="1" rowspan="1">ICALL</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Indirect Call to (Z)</td><td colspan="1" rowspan="1">$PC←Z$</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">3</td></tr><tr><td colspan="1" rowspan="1">RET</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Subroutine Retum</td><td colspan="1" rowspan="1">PC←STACK</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">4</td></tr><tr><td colspan="1" rowspan="1">RETI</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Interrupt Return</td><td colspan="1" rowspan="1">PC←STACK</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">4</td></tr><tr><td colspan="1" rowspan="1">CPSE</td><td colspan="1" rowspan="1">Rd,Rr</td><td colspan="1" rowspan="1">Compare, Skip if Equal</td><td colspan="1" rowspan="1">if(Rd = Rr) PC ← PC + 2 or 3</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2/13</td></tr><tr><td colspan="1" rowspan="1">CP</td><td colspan="1" rowspan="1">Rd,Rr</td><td colspan="1" rowspan="1">Compare</td><td colspan="1" rowspan="1">Rd -Rr</td><td colspan="1" rowspan="1">Z, N,V,C.H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CPC</td><td colspan="1" rowspan="1">Rd,Rr</td><td colspan="1" rowspan="1">Compare with Carry</td><td colspan="1" rowspan="1">Rd -Rr-C$</td><td colspan="1" rowspan="1">Z, N,V,C,H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CPI</td><td colspan="1" rowspan="1">Rd,K</td><td colspan="1" rowspan="1">Compare Register with Immediate</td><td colspan="1" rowspan="1">Rd -K</td><td colspan="1" rowspan="1">Z, N,V,C,H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SBRC</td><td colspan="1" rowspan="1">Rr,b</td><td colspan="1" rowspan="1">Sip if Bit inRegister Cleared</td><td colspan="1" rowspan="1">if (Rr(b)=0) PC ← PC + 2 or 3</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2/3</td></tr><tr><td colspan="1" rowspan="1">SBRS</td><td colspan="1" rowspan="1">Rr, b</td><td colspan="1" rowspan="1">Skip if Bit in Register is Set</td><td colspan="1" rowspan="1">if (Rr(b)=1) PC ← PC + 2 or 3</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2/3</td></tr><tr><td colspan="1" rowspan="1">SBIC</td><td colspan="1" rowspan="1">P.b</td><td colspan="1" rowspan="1">Skip if Bit in I/O Register Cleared</td><td colspan="1" rowspan="1">if (P(b)=0) PC ← PC + 2 or 3</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2/3</td></tr><tr><td colspan="1" rowspan="1">SBIS</td><td colspan="1" rowspan="1">P,b</td><td colspan="1" rowspan="1">Skip if Bit in O Register is Set</td><td colspan="1" rowspan="1">if (P(b)=1) PC ← PC + 2 or 3</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2/3</td></tr><tr><td colspan="1" rowspan="1">BRBS</td><td colspan="1" rowspan="1">S,k</td><td colspan="1" rowspan="1">Branch if Status Flag Set</td><td colspan="1" rowspan="1">if (SREG(s) = 1) then PC←PC+k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/12</td></tr><tr><td colspan="1" rowspan="1">BRBC</td><td colspan="1" rowspan="1">s, k</td><td colspan="1" rowspan="1">Branch if Status Flag Cleared</td><td colspan="1" rowspan="1">if (SREG(s) = 0) then PC&lt;PC+k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BREQ</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Equal</td><td colspan="1" rowspan="1">if (Z = 1) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRNE</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Not Equal</td><td colspan="1" rowspan="1">if (Z = 0) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRCS</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Carry Set</td><td colspan="1" rowspan="1">if (C = 1) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRCC</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Carry Cleared</td><td colspan="1" rowspan="1">if (C = 0) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRSH</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Same or Higher</td><td colspan="1" rowspan="1">if (C = 0) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRLO</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Lower</td><td colspan="1" rowspan="1">if (C = 1) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRMI</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Minus</td><td colspan="1" rowspan="1">if (N = 1) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRPL</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Plus</td><td colspan="1" rowspan="1">if (N = O) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRGE</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Greater or Equal, Signed</td><td colspan="1" rowspan="1">if (N ⊕ V= 0) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRLT</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Less Than Zero, Signed</td><td colspan="1" rowspan="1">if (N ⊕ V= 1) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRHS</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Hlf Carry Flag Set</td><td colspan="1" rowspan="1">if (H = 1) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRHC</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Half Carry Flag Cleared</td><td colspan="1" rowspan="1">if (H = 0) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRTS</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if T Flag Set</td><td colspan="1" rowspan="1">if (T = 1) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/12</td></tr><tr><td colspan="1" rowspan="1">BRTC</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if T Flag Cleared</td><td colspan="1" rowspan="1">if (T = 0) then PC &lt;← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRVS</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Overfl ow Flag is Set</td><td colspan="1" rowspan="1">if(V = 1) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/12</td></tr><tr><td colspan="1" rowspan="1">BRVC</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Overflow Flag is Cleared</td><td colspan="1" rowspan="1">if (V = 0) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRIE</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Interrupt Enabled</td><td colspan="1" rowspan="1">if (I= 1) then PC ← PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/2</td></tr><tr><td colspan="1" rowspan="1">BRID</td><td colspan="1" rowspan="1">k</td><td colspan="1" rowspan="1">Branch if Interrupt Disabled</td><td colspan="1" rowspan="1">if (I= 0) then PC ←− PC + k + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1/12</td></tr><tr><td colspan="1" rowspan="1">BIT AND BIT-TESTI</td><td colspan="1" rowspan="1"></td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">SB1</td><td colspan="1" rowspan="1">P.b</td><td colspan="1" rowspan="1">Set Bit in IO Register</td><td colspan="1" rowspan="1">V/O(P,b)←1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">CBI</td><td colspan="1" rowspan="1">P.b</td><td colspan="1" rowspan="1">Clear Bit in IO Register</td><td colspan="1" rowspan="1">V/O(P,b)←0</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LSL</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Logical Shift Left</td><td colspan="1" rowspan="1">Rd(n+1) ← Rd(n), Rd(0) ← 0</td><td colspan="1" rowspan="1">Z,C,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">LSR</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Logical Shift Right</td><td colspan="1" rowspan="1">Rd(n) ← Rd(n+1), Rd(7) ← 0</td><td colspan="1" rowspan="1">Z,C,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">ROL</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Rotate Left Through Carry</td><td colspan="1" rowspan="1">Rd(0)&lt;C,Rd(n+1)Rd(n),C&lt;Rd(7)</td><td colspan="1" rowspan="1">Z.C.N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">ROR</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Rotate Right Through Carry</td><td colspan="1" rowspan="1">Rd(7)←C,Rd(n)← Rd(n+1),C←Rd(O)</td><td colspan="1" rowspan="1">Z,C,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">ASR</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Arithmetic Shift Right</td><td colspan="1" rowspan="1">Rd(n) ← Rd(n+1), n=0..6</td><td colspan="1" rowspan="1">Z.C,N,V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">Mnemonics</td><td colspan="1" rowspan="1">Operands</td><td colspan="1" rowspan="1">Description</td><td colspan="1" rowspan="1">Operation</td><td colspan="1" rowspan="1">Flags</td><td colspan="1" rowspan="1">#Clocks</td></tr><tr><td colspan="1" rowspan="1">SWAP</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Swap Nibbles</td><td colspan="1" rowspan="1">Rd(3..0)−Rd(7..4),Rd(7..4)−Rd(..0)</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">BSET</td><td colspan="1" rowspan="1">S</td><td colspan="1" rowspan="1">Flag Set</td><td colspan="1" rowspan="1">SREG(s) ←1</td><td colspan="1" rowspan="1">SREG(s)</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">BCLR</td><td colspan="1" rowspan="1">S</td><td colspan="1" rowspan="1">Flag Clear</td><td colspan="1" rowspan="1">SREG(s)←0</td><td colspan="1" rowspan="1">SREG(s)</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">BST</td><td colspan="1" rowspan="1">Rr, b</td><td colspan="1" rowspan="1">Bit Store from Register to T</td><td colspan="1" rowspan="1">T←Rr(b)</td><td colspan="1" rowspan="1">T</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">BLD</td><td colspan="1" rowspan="1">Rd, b</td><td colspan="1" rowspan="1">Bit load from T to Register</td><td colspan="1" rowspan="1">Rd(b) ←−T</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SEC</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Set Carry</td><td colspan="1" rowspan="1">$C←1$</td><td colspan="1" rowspan="1">C</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CLC</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Clear Carry</td><td colspan="1" rowspan="1">$C0</td><td colspan="1" rowspan="1">C</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SEN</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Set Negative Flag</td><td colspan="1" rowspan="1">N←1</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CLN</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Clear Negative Flag</td><td colspan="1" rowspan="1">N←0</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SEZ</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Set Zero Flag</td><td colspan="1" rowspan="1">Z←1</td><td colspan="1" rowspan="1">Z</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CLZ</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Clear Zero Flag</td><td colspan="1" rowspan="1">Z←0</td><td colspan="1" rowspan="1">Z</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SEI</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Global Interrupt Enable</td><td colspan="1" rowspan="1">1←1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CLI</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Global Interrupt Disable</td><td colspan="1" rowspan="1">1←0</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SES</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Set Signed Test Flag</td><td colspan="1" rowspan="1">S←1$</td><td colspan="1" rowspan="1">S</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CLS</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Clear Signed Test Flag</td><td colspan="1" rowspan="1">S←0</td><td colspan="1" rowspan="1">S</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SEV</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Set Twos Complement Overflow.</td><td colspan="1" rowspan="1">$V←1</td><td colspan="1" rowspan="1">V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CLV</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Clear Twos Complement Overflow</td><td colspan="1" rowspan="1">$V←0</td><td colspan="1" rowspan="1">V</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SET</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Set T in SREG</td><td colspan="1" rowspan="1">T←1</td><td colspan="1" rowspan="1">T</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CLT</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Clear T in SREG</td><td colspan="1" rowspan="1">T←O</td><td colspan="1" rowspan="1">T</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">SEH</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Set Half Carry Flag in SREG</td><td colspan="1" rowspan="1">H←1</td><td colspan="1" rowspan="1">H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">CLH</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Clear Half Carry Flag in SREG</td><td colspan="1" rowspan="1">H←O</td><td colspan="1" rowspan="1">H</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">DATA TRANSFER INSTRUCTIONS</td><td colspan="1" rowspan="1"></td><td></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">MOV</td><td colspan="1" rowspan="1">Rd, Rr</td><td colspan="1" rowspan="1">Move Between Registers</td><td colspan="1" rowspan="1">Rd←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">MOVW</td><td colspan="1" rowspan="1">Rd, Rr</td><td colspan="1" rowspan="1">Copy Register Word</td><td colspan="1" rowspan="1">Rd+1:Rd ← Rr+1:Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">LDI</td><td colspan="1" rowspan="1">Rd,K</td><td colspan="1" rowspan="1">Load Immediate</td><td colspan="1" rowspan="1">Rd←K</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">LD</td><td colspan="1" rowspan="1">Rd, X</td><td colspan="1" rowspan="1">Load Indirect</td><td colspan="1" rowspan="1">Rd←()</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LD</td><td colspan="1" rowspan="1">Rd,X+$</td><td colspan="1" rowspan="1">Load Indirect and Post-Inc.</td><td colspan="1" rowspan="1">Rd←(), X←X+1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LD</td><td colspan="1" rowspan="1">Rd, - X</td><td colspan="1" rowspan="1">Load Indirect and Pre-Dec.</td><td colspan="1" rowspan="1">X←X- 1, Rd←()</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LD</td><td colspan="1" rowspan="1">Rd, Y</td><td colspan="1" rowspan="1">Load Indirect</td><td colspan="1" rowspan="1">Rd←(Y)</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LD</td><td colspan="1" rowspan="1">Rd, Y +</td><td colspan="1" rowspan="1">Load Indirect and Post-lnc.</td><td colspan="1" rowspan="1">Rd←(M), Y←Y + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LD</td><td colspan="1" rowspan="1">Rd, - Y</td><td colspan="1" rowspan="1">Load Indirect and Pre-Dec.</td><td colspan="1" rowspan="1">Y←Y-1, Rd←(Y)</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LDD</td><td colspan="1" rowspan="1">Rd,Y+q$</td><td colspan="1" rowspan="1">Load Indirect with Displacement</td><td colspan="1" rowspan="1">Rd←(Y + q)</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LD</td><td colspan="1" rowspan="1">Rd, Z</td><td colspan="1" rowspan="1">Load Indirect</td><td colspan="1" rowspan="1">Rd←(Z)</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LD</td><td colspan="1" rowspan="1">Rd, Z+</td><td colspan="1" rowspan="1">Load Indirect and Post-Inc.</td><td colspan="1" rowspan="1">Rd ←(Z), Z ← Z+1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LD</td><td colspan="1" rowspan="1">Rd, -Z</td><td colspan="1" rowspan="1">Load Indirect and Pre-Dec.</td><td colspan="1" rowspan="1">Z←Z-1,Rd←(Z)</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LDD</td><td colspan="1" rowspan="1">Rd,Z+q$</td><td colspan="1" rowspan="1">Load Indirect with Displacement</td><td colspan="1" rowspan="1">Rd←(Z + q)</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LDS</td><td colspan="1" rowspan="1">Rd, k</td><td colspan="1" rowspan="1">Load Direct from SRAM</td><td colspan="1" rowspan="1">Rd←(k)</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">ST</td><td colspan="1" rowspan="1">X, Rr</td><td colspan="1" rowspan="1">Store Indirect</td><td colspan="1" rowspan="1">(X)←Rr$</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">ST</td><td colspan="1" rowspan="1">X+, Rr</td><td colspan="1" rowspan="1">Store Indirect and Post-Inc.</td><td colspan="1" rowspan="1">() ←Rr, X←X + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">ST</td><td colspan="1" rowspan="1">-X, Rr</td><td colspan="1" rowspan="1">Store Indirect and Pre-Dec.</td><td colspan="1" rowspan="1">X←X- 1,()←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">ST</td><td colspan="1" rowspan="1">Y,Rr</td><td colspan="1" rowspan="1">Store Indirect</td><td colspan="1" rowspan="1">(Y )←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">ST</td><td colspan="1" rowspan="1">Y+, Rr</td><td colspan="1" rowspan="1">Store Indirect and Post-Inc.</td><td colspan="1" rowspan="1">(Y) ←Rr, Y ←Y + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">ST</td><td colspan="1" rowspan="1">-Y, Rr</td><td colspan="1" rowspan="1">Store Indirect and Pre-Dec.</td><td colspan="1" rowspan="1">Y←Y- 1,(Y)←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">STD</td><td colspan="1" rowspan="1">Y+q,Rr</td><td colspan="1" rowspan="1">Store Indirect with Displacement</td><td colspan="1" rowspan="1">(Y + q) ←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">ST</td><td colspan="1" rowspan="1">Z, Rr</td><td colspan="1" rowspan="1">Store Indirect</td><td colspan="1" rowspan="1">(Z)←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">ST</td><td colspan="1" rowspan="1">Z+, Rr</td><td colspan="1" rowspan="1">Store Indirect and Post-Inc.</td><td colspan="1" rowspan="1">(Z) ← Rr, Z ← Z + 1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">ST</td><td colspan="1" rowspan="1">-Z, Rr</td><td colspan="1" rowspan="1">Store Indirect and Pre-Dec.</td><td colspan="1" rowspan="1">Z←Z- 1,(Z)←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">STD</td><td colspan="1" rowspan="1">Z+q,Rr</td><td colspan="1" rowspan="1">Store Indirect with Displacement</td><td colspan="1" rowspan="1">(Z + q) ←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">STS</td><td colspan="1" rowspan="1">k, Rr</td><td colspan="1" rowspan="1">Store Direct to SRAM</td><td colspan="1" rowspan="1">(k)←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">LPM</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Load Program Memory</td><td colspan="1" rowspan="1">R0←(Z)</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">3</td></tr><tr><td colspan="1" rowspan="1">LPM</td><td colspan="1" rowspan="1">Rd, Z</td><td colspan="1" rowspan="1">Load Program Memory</td><td colspan="1" rowspan="1">Rd←(Z)</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">3</td></tr><tr><td colspan="1" rowspan="1">LPM</td><td colspan="1" rowspan="1">Rd, Z+$</td><td colspan="1" rowspan="1">Load Program Memory and Post-Inc</td><td colspan="1" rowspan="1">Rd ← (Z), Z ← Z+1</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">3</td></tr><tr><td colspan="1" rowspan="1">SPM</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Store Program Memory</td><td colspan="1" rowspan="1">(z)←R1:R0</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">IN</td><td colspan="1" rowspan="1">Rd, P</td><td colspan="1" rowspan="1">In Port</td><td colspan="1" rowspan="1">Rd←P$</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">OUT</td><td colspan="1" rowspan="1">P,Rr</td><td colspan="1" rowspan="1">Out Port</td><td colspan="1" rowspan="1">P←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">1</td></tr><tr><td colspan="1" rowspan="1">PUSH</td><td colspan="1" rowspan="1">Rr</td><td colspan="1" rowspan="1">Push Register on Stack</td><td colspan="1" rowspan="1">STACK←Rr</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="1" rowspan="1">POP</td><td colspan="1" rowspan="1">Rd</td><td colspan="1" rowspan="1">Pop Reqister from Stack</td><td colspan="1" rowspan="1">Rd&lt;STACK</td><td colspan="1" rowspan="1">None</td><td colspan="1" rowspan="1">2</td></tr><tr><td colspan="6" rowspan="1">MCU CONTROL INSTRUCTIONS</td></tr></table>

<table><tr><td rowspan=1 colspan=1>NOP</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>No Operation</td><td></td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>SLEEP</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Sleep</td><td rowspan=1 colspan=1>(see specific descr. for Sleep function)</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>WDR</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Watchdog Reset</td><td rowspan=1 colspan=1>(see specific descr. for WDR/Timer)</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>BREAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Break</td><td rowspan=1 colspan=1>For On-chip Debug Only</td><td rowspan=1 colspan=1>None</td><td rowspan=1 colspan=1>N/A</td></tr></table>

# 6. Ordering Information

# 6.1 ATtiny25

<table><tr><td rowspan=1 colspan=1>Speed (MHz) 1)</td><td rowspan=1 colspan=1>Supply Voltage (V)</td><td rowspan=1 colspan=1>Temperature Range</td><td rowspan=1 colspan=1>Package((2)</td><td rowspan=1 colspan=1>Ordering Code (3)</td></tr><tr><td rowspan=7 colspan=1>10</td><td rowspan=7 colspan=1>1.8-5.5</td><td rowspan=4 colspan=1>Industrial(-40°℃ to +85°℃)(4)</td><td rowspan=1 colspan=1>8P3</td><td rowspan=1 colspan=1>ATtiny25V-10PU</td></tr><tr><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>ATtiny25V-10SUATtiny25V-10SURATtiny25V-10SHATtiny25V-10SHR</td></tr><tr><td rowspan=1 colspan=1>S8S1</td><td rowspan=1 colspan=1>ATtiny25V-10SSUATtiny25V-10SSURATtiny25V-10SSHATtiny25V-10SSHR</td></tr><tr><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>ATtiny25V-10MUATtiny25V-10MUR</td></tr><tr><td rowspan=2 colspan=1>Industrial(-40°C to +105°℃)(5)</td><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>ATtiny25V-10SNATtiny25V-10SNR</td></tr><tr><td rowspan=1 colspan=1>S8S1</td><td rowspan=1 colspan=1>ATtiny25V-10SSNATtiny25V-10SSNR</td></tr><tr><td rowspan=1 colspan=1>Industrial (-40°C to +125°C) (6)</td><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>ATtiny25V-10MFATtiny25V-10MFR</td></tr><tr><td rowspan=7 colspan=1>20</td><td rowspan=7 colspan=1>2.7-5.5</td><td rowspan=4 colspan=1>Industrial(-40°C to +85°℃)(4)</td><td rowspan=1 colspan=1>8P3</td><td rowspan=1 colspan=1>ATtiny25-20PU</td></tr><tr><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>ATtiny25-20SUATtiny25-20SURATtiny25-20SHATtiny25-20SHR</td></tr><tr><td rowspan=1 colspan=1>S8S1</td><td rowspan=1 colspan=1>ATtiny25-20SSUATtiny25-20SSURATtiny25-20SSHATtiny25-20SSHR</td></tr><tr><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>ATtiny25-20MUATtiny25-20MUR</td></tr><tr><td rowspan=2 colspan=1>Industrial(-40°℃ to +105°C) (5)</td><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>ATtiny25-20SNATtiny25-20SNR</td></tr><tr><td rowspan=1 colspan=1>S8S1</td><td rowspan=1 colspan=1>ATtiny25-20SSNATtiny25-20SSNR</td></tr><tr><td rowspan=1 colspan=1>Industrial (-40°C to +125°C) (6)</td><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>ATtiny25-20MFATtiny25-20MFR</td></tr></table>

Notes: 1. For speed vs. supply voltage, see section 21.3 “Speed” on page 163. 2. All Pb-free, halide-free, fully green, and comply with European directive for Restriction of Hazardous Substances (RoHS). 3. Code indicators: H = NiPdAu lead finish, U/N = matte tin, R = tape & reel. 4. Can also be supplied in wafer form. Contact your local Atmel sales office for ordering information and minimum quantities. 5. For characteristics, see “Appendix A – Specification at 105C”. 6. For characteristics, see “Appendix B – Specification at 125C”.

<table><tr><td rowspan=1 colspan=2>Package Types</td></tr><tr><td rowspan=1 colspan=1>8P3</td><td rowspan=1 colspan=1>8-lead, 0.300&quot; Wide, Plastic Dual Inline Package (PDIP)</td></tr><tr><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>8-lead, 0.208&quot; Wide, Plastic Gull-Wing Small Outline (EIAJ SOIC)</td></tr><tr><td rowspan=1 colspan=1>S8S1</td><td rowspan=1 colspan=1>8-lead, 0.150&quot; Wide, Plastic Gull-Wing Small Outline (JEDEC SOIC)</td></tr><tr><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>20-pad, 4 × 4 × 0.8 mm Body, Quad Flat No-Lead/Micro Lead Frame Package (QFN/MLF)</td></tr></table>

<table><tr><td rowspan=1 colspan=1>Speed (MHz) (1)</td><td rowspan=1 colspan=1>Supply Voltage (V)</td><td rowspan=1 colspan=1>Temperature Range</td><td rowspan=1 colspan=1>Package((2)</td><td rowspan=1 colspan=1>Ordering Code (3)</td></tr><tr><td rowspan=4 colspan=1>10</td><td rowspan=4 colspan=1>1.8-5.5</td><td rowspan=4 colspan=1>Industrial(-40°℃ to +85°℃) (4)</td><td rowspan=1 colspan=1>8P3</td><td rowspan=1 colspan=1>ATtiny45V-10PU</td></tr><tr><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>ATtiny45V-10SUATtiny45V-10SURATtiny45V-10SHATtiny45V-10SHR</td></tr><tr><td rowspan=1 colspan=1>8X</td><td rowspan=1 colspan=1>ATtiny45V-10XUATtiny45V-10XUR</td></tr><tr><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>ATtiny45V-10MUATtiny45V-10MUR</td></tr><tr><td rowspan=4 colspan=1>20</td><td rowspan=4 colspan=1>2.7-5.5</td><td rowspan=4 colspan=1>Industrial(-40°C to +85°℃)(4)</td><td rowspan=1 colspan=1>8P3</td><td rowspan=1 colspan=1>ATtiny45-20PU</td></tr><tr><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>ATtiny45-20SUATtiny45-20SURATtiny45-20SHATtiny45-20SHR</td></tr><tr><td rowspan=1 colspan=1>8X</td><td rowspan=1 colspan=1>ATtiny45-20XUATtiny45-20XUR</td></tr><tr><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>ATtiny45-20MUATtiny45-20MUR</td></tr></table>

Notes: 1. For speed vs. supply voltage, see section 21.3 “Speed” on page 163.

2. All packages are Pb-free, halide-free and fully green and they comply with the European directive for Restriction of Hazardous Substances (RoHS).

3. Code indicators:

– H: NiPdAu lead finish – U: matte tin – R: tape & reel

4. These devices can also be supplied in wafer form. Please contact your local Atmel sales office for detailed ordering information and minimum quantities.

<table><tr><td rowspan=1 colspan=2>Package Types</td></tr><tr><td rowspan=1 colspan=1>8P3</td><td rowspan=1 colspan=1>8-lead, 0.300&quot; Wide, Plastic Dual Inline Package (PDIP)</td></tr><tr><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>8-lead, 0.208&quot; Wide, Plastic Gull-Wing Small Outline (EIAJ SOIC)</td></tr><tr><td rowspan=1 colspan=1>8X</td><td rowspan=1 colspan=1>8-lead, 4.4 mm Wide, Plastic Thin Shrink Small Outine Package (TSSOP)</td></tr><tr><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>20-pad, 4 × 4 × 0.8 mm Body, Quad Flat No-Lead/Micro Lead Frame Package (QFN/MLF)</td></tr></table>

# Atmel

# 6.3 ATtiny85

<table><tr><td rowspan=1 colspan=1>Speed (MHz) (1)</td><td rowspan=1 colspan=1>Supply Voltage (V)</td><td rowspan=1 colspan=1>Temperature Range</td><td rowspan=1 colspan=1>Package(2)</td><td rowspan=1 colspan=1>Ordering Code (3)</td></tr><tr><td rowspan=3 colspan=1>10</td><td rowspan=3 colspan=1>1.8-5.5</td><td rowspan=3 colspan=1>Industrial(-40°℃ to +85°℃)(4)</td><td rowspan=1 colspan=1>8P3</td><td rowspan=1 colspan=1>ATtiny85V-10PU</td></tr><tr><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>ATtiny85V-10SUATtiny85V-10SURATtiny85V-10SHATtiny85V-10SHR</td></tr><tr><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>ATtiny85V-10MUATtiny85V-10MUR</td></tr><tr><td rowspan=3 colspan=1>20</td><td rowspan=3 colspan=1>2.7-5.5</td><td rowspan=3 colspan=1>Industrial(-40°℃ to +85°℃) (4)</td><td rowspan=1 colspan=1>8P3</td><td rowspan=1 colspan=1>ATtiny85-20PU</td></tr><tr><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>ATtiny85-20SUATtiny85-20SURATtiny85-20SHATtiny85-20SHR</td></tr><tr><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>ATtiny85-20MUATtiny85-20MUR</td></tr></table>

Notes: 1. For speed vs. supply voltage, see section 21.3 “Speed” on page 163.

2. All packages are Pb-free, halide-free and fully green and they comply with the European directive for Restriction of Hazardous Substances (RoHS).

3. Code indicators:

– H: NiPdAu lead finish – U: matte tin – R: tape & reel

4. These devices can also be supplied in wafer form. Please contact your local Atmel sales office for detailed ordering information and minimum quantities.

<table><tr><td rowspan=1 colspan=2>Package Types</td></tr><tr><td rowspan=1 colspan=1>8P3</td><td rowspan=1 colspan=1>8-lead, 0.300&quot; Wide, Plastic Dual Inline Package (PDIP)</td></tr><tr><td rowspan=1 colspan=1>8S2</td><td rowspan=1 colspan=1>8-lead, 0.208&quot; Wide, Plastic Gull-Wing Small Outline (EIAJ SOIC)</td></tr><tr><td rowspan=1 colspan=1>20M1</td><td rowspan=1 colspan=1>20-pad, 4 × 4 × 0.8 mm Body, Quad Flat No-Lead/Micro Lead Frame Package (QFN/MLF)</td></tr></table>

# Atmel

# 7. Packaging Information

7.1 8P3

![](images/8119595d4d8aa640c400a97b9c6d57dc9d13205a61eaff5f875daeff09af0a62.jpg)  
Top View

![](images/b9d176d41b46e2fe3a23aa5e1aabd3cd6acdd7bde51e26439c57d88ea898383d.jpg)

![](images/18a297d76bd7b1ab8cdc3d09da6721b0b65d5fde1b3868d6a8f0e8b9a838c05d.jpg)

COMMON DIMENSIONS (Unit of Measure = inches)   

<table><tr><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=1>MIN</td><td rowspan=1 colspan=1>NOM</td><td rowspan=1 colspan=1>MAX</td><td rowspan=1 colspan=1>NOTE</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.210</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>A2</td><td rowspan=1 colspan=1>0.115</td><td rowspan=1 colspan=1>0.130</td><td rowspan=1 colspan=1>0.195</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>b</td><td rowspan=1 colspan=1>0.014</td><td rowspan=1 colspan=1>0.018</td><td rowspan=1 colspan=1>0.022</td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1>b2</td><td rowspan=1 colspan=1>0.045</td><td rowspan=1 colspan=1>0.060</td><td rowspan=1 colspan=1>0.070</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>b3</td><td rowspan=1 colspan=1>0.030</td><td rowspan=1 colspan=1>0.039</td><td rowspan=1 colspan=1>0.045</td><td rowspan=1 colspan=1>6</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>0.008</td><td rowspan=1 colspan=1>0.010</td><td rowspan=1 colspan=1>0.014</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>0.355</td><td rowspan=1 colspan=1>0.365</td><td rowspan=1 colspan=1>0.400</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>D1</td><td rowspan=1 colspan=1>0.005</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>0.300</td><td rowspan=1 colspan=1>0.310</td><td rowspan=1 colspan=1>0.325</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>E1</td><td rowspan=1 colspan=1>0.240</td><td rowspan=1 colspan=1>0.250</td><td rowspan=1 colspan=1>0.280</td><td rowspan=1 colspan=1>3</td></tr><tr><td rowspan=1 colspan=1>e</td><td rowspan=1 colspan=3>0.100 BSC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>eA</td><td rowspan=1 colspan=3>0.300 BSC</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>0.115</td><td rowspan=1 colspan=1>0.130</td><td rowspan=1 colspan=1>0.150</td><td rowspan=1 colspan=1>2</td></tr></table>

Notes: 1. This drawing is for general information only; refer to JEDEC Drawing MS-001, Variation BA for additional information. 2. Dimensions A and L are measured with the package seated in JEDEC seating plane Gauge GS-3. 3. D, D1 and E1 dimensions do not include mold Flash or protrusions. Mold Flash or protrusions shall not exceed 0.010 inch. 4. E and eA measured with the leads constrained to be perpendicular to datum. 5. Pointed or rounded lead tips are preferred to ease insertion. 6. b2 and b3 maximum dimensions do not include Dambar protrusions. Dambar protrusions shall not exceed 0.010 (0.25 mm).

01/09/02   

<table><tr><td></td><td>TITLE</td><td>DRAWING NO.</td><td>REV.</td></tr><tr><td>AMEL 2325 Orchard Parkway San Jose, CA 95131</td><td>8P3, 8-lead, 0.300&quot; Wide Body, Plastic Dual In-line Package (PDIP)</td><td>8P3</td><td>B</td></tr></table>

![](images/d15537961d873ea44e8ab0731c0481d333e474b3e551665e21a33ea2524a6739.jpg)

![](images/3a32858c0fe91e7218d758e8ea90a846679802479b70ab69431f7f0027becdf5.jpg)

COMMON DIMENSIONS (Unit of Measure = mm)   

<table><tr><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=1>MIN</td><td rowspan=1 colspan=1>NOM</td><td rowspan=1 colspan=1>MAX</td><td rowspan=1 colspan=1>NOTE</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>1.70</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.16</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>A1</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>b</td><td rowspan=1 colspan=1>0.35</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.48</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.35</td><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>5.13</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5.35</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>E1</td><td rowspan=1 colspan=1>5.18</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>5.40</td><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>7.70</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>8.26</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>0.51</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.85</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>θ</td><td rowspan=1 colspan=1>$0°$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>8^$</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>e</td><td rowspan=1 colspan=3>1.27 BSC</td><td rowspan=1 colspan=1>3</td></tr></table>

# SIDE VIEW

Notes: 1. This drawing is for general information only; refer to EIAJ Drawing EDR-7320 for additional information. 2. Mismatch of the upper and lower dies and resin burrs aren't included. 3. Determines the true geometric position. 4. Values b,C apply to plated terminal. The standard thickness of the plating layer shall measure between 0.007 to .021 mm.

4/15/08

![](images/ac8a1da02e0aedd1b1e6232a7e91024df52b75f8dda474231803e9337aced60f.jpg)

COMMON DIMENSIONS (Unit of Measure = mm)   

<table><tr><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=1>MIN</td><td rowspan=1 colspan=1>NOM</td><td rowspan=1 colspan=1>MAX</td><td rowspan=1 colspan=1>NOTE</td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>5.79</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>6.20</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>E1</td><td rowspan=1 colspan=1>3.81</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.99</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>1.35</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.75</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>A1</td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>4.80</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>4.98</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>0.17</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>b</td><td rowspan=1 colspan=1>0.31</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.51</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>0.4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.27</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>e</td><td rowspan=1 colspan=3>1.27 BSC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>$0°$</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>80$</td><td rowspan=1 colspan=1></td></tr></table>

7/28/03

![](images/6629b3a92990316884ad938570b1ae983cc50e2a5b47dfb0501701f75613c6c4.jpg)

![](images/85e2d8e6d09ca021bcc41f117a06f25cb0df9eb91ebac2bd0be7a08392c1f9a1.jpg)

![](images/0641ea05822e37cb78bead20a64c5854c7a81e8dd1bb6070a6ad0392743349df.jpg)

COMMON DIMENSIONS (Unit of Measure = mm)   

<table><tr><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=1>MIN</td><td rowspan=1 colspan=1>NOM</td><td rowspan=1 colspan=1>MAX</td><td rowspan=1 colspan=1>NOTE</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>1.05</td><td rowspan=1 colspan=1>1.10</td><td rowspan=1 colspan=1>1.20</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>A1</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1>0.10</td><td rowspan=1 colspan=1>0.15</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>b</td><td rowspan=1 colspan=1>0.25</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.30</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>C</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.127</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>2.90</td><td rowspan=1 colspan=1>3.05</td><td rowspan=1 colspan=1>3.10</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>E1</td><td rowspan=1 colspan=1>4.30</td><td rowspan=1 colspan=1>4.40</td><td rowspan=1 colspan=1>4.50</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>6.20</td><td rowspan=1 colspan=1>6.40</td><td rowspan=1 colspan=1>6.60</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>e</td><td rowspan=1 colspan=3>0.65 TYP</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>0.50</td><td rowspan=1 colspan=1>0.60</td><td rowspan=1 colspan=1>0.70</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0°</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1></td></tr></table>

4/14/05

![](images/05823f72768d3acc94d2449cd4b79960c2b139faf48facd4dcec152ce675e7dd.jpg)

![](images/864aab15f270727dd9937b6758920965da670a1bd0e723ff0ab157cb94be6a4e.jpg)

COMMON DIMENSIONS (Unit of Measure = mm)   

<table><tr><td rowspan=1 colspan=1>SYMBOL</td><td rowspan=1 colspan=1>MIN</td><td rowspan=1 colspan=1>NOM</td><td rowspan=1 colspan=1>MAX</td><td rowspan=1 colspan=1>NOTE</td></tr><tr><td rowspan=1 colspan=1>A</td><td rowspan=1 colspan=1>0.70</td><td rowspan=1 colspan=1>0.75</td><td rowspan=1 colspan=1>0.80</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>A1</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>0.01</td><td rowspan=1 colspan=1>0.05</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>A2</td><td rowspan=1 colspan=3>0.20 REF</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>b</td><td rowspan=1 colspan=1>0.18</td><td rowspan=1 colspan=1>0.23</td><td rowspan=1 colspan=1>0.30</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=3>4.00 BSC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>D2</td><td rowspan=1 colspan=1>2.45</td><td rowspan=1 colspan=1>2.60</td><td rowspan=1 colspan=1>2.75</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=3>4.00 BSC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>E2</td><td rowspan=1 colspan=1>2.45</td><td rowspan=1 colspan=1>2.60</td><td rowspan=1 colspan=1>2.75</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>e</td><td rowspan=1 colspan=3>0.50 BSC</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>L</td><td rowspan=1 colspan=1>0.35</td><td rowspan=1 colspan=1>0.40</td><td rowspan=1 colspan=1>0.55</td><td rowspan=1 colspan=1></td></tr></table>

10/27/04   

<table><tr><td>2325 Orchard Parkway</td><td>TITLE</td><td>DRAWING NO.</td><td>REV.</td></tr><tr><td>AME San Jose, CA 95131</td><td>20M1, 20-pad, 4 × 4 × 0.8 mm Body, Lead Pitch 0.50 mm, 2.6 mm Exposed Pad, Micro Lead Frame Package (MLF)</td><td>20M1</td><td>B</td></tr></table>

# 8. Errata

# 8.1 Errata ATtiny25

The revision letter in this section refers to the revision of the ATtiny25 device.

# 8.1.1 Rev D – F

No known errata.

# 8.1.2 Rev B – C

• EEPROM read may fail at low supply voltage / low clock frequency

1. EEPROM read may fail at low supply voltage / low clock frequency

Trying to read EEPROM at low clock frequencies and/or low supply voltage may result in invalid data.

# Problem Fix/Workaround

Do not use the EEPROM when clock frequency is below 1MHz and supply voltage is below 2V. If operating frequency can not be raised above 1MHz then supply voltage should be more than 2V. Similarly, if supply voltage can not be raised above 2V then operating frequency should be more than 1MHz.

This feature is known to be temperature dependent but it has not been characterised. Guidelines are given for room temperature, only.

# 8.1.3 Rev A

Not sampled.

# 8.2 Errata ATtiny45

The revision letter in this section refers to the revision of the ATtiny45 device.

# 8.2.1 Rev F – G

No known errata

# 8.2.2 Rev D – E

• EEPROM read may fail at low supply voltage / low clock frequency

1. EEPROM read may fail at low supply voltage / low clock frequency

Trying to read EEPROM at low clock frequencies and/or low supply voltage may result in invalid data.

# Problem Fix/Workaround

Do not use the EEPROM when clock frequency is below 1MHz and supply voltage is below 2V. If operating frequency can not be raised above 1MHz then supply voltage should be more than 2V. Similarly, if supply voltage can not be raised above 2V then operating frequency should be more than 1MHz.

This feature is known to be temperature dependent but it has not been characterised. Guidelines are given for room temperature, only.

8.2.3 Rev B – C

• PLL not locking • EEPROM read from application code does not work in Lock Bit Mode 3 • EEPROM read may fail at low supply voltage / low clock frequency • Timer Counter 1 PWM output generation on OC1B- XOC1B does not work correctly

1. PLL not locking

When at frequencies below 6.0 MHz, the PLL will not lock

# Problem fix / Workaround

When using the PLL, run at 6.0 MHz or higher.

2. EEPROM read from application code does not work in Lock Bit Mode 3

When the Memory Lock Bits LB2 and LB1 are programmed to mode 3, EEPROM read does not work from the application code.

# Problem Fix/Work around

Do not set Lock Bit Protection Mode 3 when the application code needs to read from EEPROM.

3. EEPROM read may fail at low supply voltage / low clock frequency

Trying to read EEPROM at low clock frequencies and/or low supply voltage may result in invalid data.

# Problem Fix/Workaround

Do not use the EEPROM when clock frequency is below 1MHz and supply voltage is below 2V. If operating frequency can not be raised above 1MHz then supply voltage should be more than 2V. Similarly, if supply voltage can not be raised above 2V then operating frequency should be more than 1MHz.

This feature is known to be temperature dependent but it has not been characterised. Guidelines are given for room temperature, only.

4. Timer Counter 1 PWM output generation on OC1B – XOC1B does not work correctly

Timer Counter1 PWM output OC1B-XOC1B does not work correctly. Only in the case when the control bits, COM1B1 and COM1B0 are in the same mode as COM1A1 and COM1A0, respectively, the OC1B-XOC1B output works correctly.

# Problem Fix/Work around

The only workaround is to use same control setting on COM1A[1:0] and COM1B[1:0] control bits, see table 14- 4 in the data sheet. The problem has been fixed for Tiny45 rev D.

8.2.4 Rev A

• Too high power down power consumption   
• DebugWIRE looses communication when single stepping into interrupts   
PLL not locking EEPROM read from application code does not work in Lock Bit Mode 3   
• EEPROM read may fail at low supply voltage / low clock frequency

# 1. Too high power down power consumption

Three situations will lead to a too high power down power consumption. These are:

– An external clock is selected by fuses, but the I/O PORT is still enabled as an output.   
– The EEPROM is read before entering power down.   
– VCC is 4.5 volts or higher.

# Problem fix / Workaround

– When using external clock, avoid setting the clock pin as Output.   
– Do not read the EEPROM if power down power consumption is important.   
– Use VCC lower than 4.5 Volts.

2. DebugWIRE looses communication when single stepping into interrupts When receiving an interrupt during single stepping, debugwire will loose communication.

# Problem fix / Workaround

– When singlestepping, disable interrupts.   
– When debugging interrupts, use breakpoints within the interrupt routine, and run into the interrupt.

# 3. PLL not locking

When at frequencies below 6.0 MHz, the PLL will not lock

# Problem fix / Workaround

When using the PLL, run at 6.0 MHz or higher.

4. EEPROM read from application code does not work in Lock Bit Mode 3

When the Memory Lock Bits LB2 and LB1 are programmed to mode 3, EEPROM read does not work from the application code.

# Problem Fix/Work around

Do not set Lock Bit Protection Mode 3 when the application code needs to read from EEPROM.

5. EEPROM read may fail at low supply voltage / low clock frequency

Trying to read EEPROM at low clock frequencies and/or low supply voltage may result in invalid data.

# Problem Fix/Workaround

Do not use the EEPROM when clock frequency is below 1MHz and supply voltage is below 2V. If operating frequency can not be raised above 1MHz then supply voltage should be more than 2V. Similarly, if supply voltage can not be raised above 2V then operating frequency should be more than 1MHz.

This feature is known to be temperature dependent but it has not been characterized. Guidelines are given for room temperature, only.

# 8.3 Errata ATtiny85

The revision letter in this section refers to the revision of the ATtiny85 device.

# 8.3.1 Rev B – C

No known errata.

# 8.3.2 Rev A

• EEPROM read may fail at low supply voltage / low clock frequency

1. EEPROM read may fail at low supply voltage / low clock frequency

Trying to read EEPROM at low clock frequencies and/or low supply voltage may result in invalid data.

# Problem Fix/Workaround

Do not use the EEPROM when clock frequency is below 1MHz and supply voltage is below 2V. If operating frequency can not be raised above 1MHz then supply voltage should be more than 2V. Similarly, if supply voltage can not be raised above 2V then operating frequency should be more than 1MHz.

This feature is known to be temperature dependent but it has not been characterised. Guidelines are given for room temperature, only.

# 9. Datasheet Revision History

# 9.1 Rev. 2586Q-08/13

“Bit 3 – FOC1B: Force Output Compare Match 1B” description in “GTCCR – General Timer/Counter1 Control 1. Register” on page 90 updated: PB3 in “compare match output pin PB3 (OC1B)” corrected to PB4.

# 9.2 Rev. 2586P-06/13

1. Updated description of “EEARH – EEPROM Address Register” and “EEARL – EEPROM Address Register” on page 20.

# 9.3 Rev. 2586O-02/13

Updated ordering codes on page 11, page 12, and page 13.

# 9.4 Rev. 2586N-04/11

1. Added: – Section “Capacitive Touch Sensing” on page 6.

Updated: – Document template.   
– Removed “Preliminary” on front page. All devices now final and in production.   
– Section “Limitations” on page 36.   
– Program example on page 49.   
– Section “Overview” on page 122.   
– Table 17-4 on page 135.   
– Section “Limitations of debugWIRE” on page 140.   
– Section “Serial Programming Algorithm” on page 151.   
– Table 21-7 on page 166.   
– EEPROM errata on pages 19, 19, 20, 21, and 22 – Ordering information on pages 11, 12, and 13.

# 9.5 Rev. 2586M-07/10

1. Clarified Section 6.4 “Clock Output Buffer” on page 31.   
2. Added Ordering Codes -SN and -SNR for ATtiny25 extended temperature.

# 9.6 Rev. 2586L-06/10

1. Added:

– TSSOP for ATtiny45 in “Features” on page 1, Pinout Figure 1-1 on page 2, Ordering Information in Section 6.2 “ATtiny45” on page 12, and Packaging Information in Section 7.4 “8X” on page 17 – Table 6-11, “Capacitance of Low-Frequency Crystal Oscillator,” on page 29 – Figure 22-36 on page 191 and Figure 22-37 on page 191, Typical Characteristics plots for Bandgap Voltage vs. VCC and Temperature – Extended temperature in Section 6.1 “ATtiny25” on page 11, Ordering Information

– Tape & reel part numbers in Ordering Information, in Section 6.1 “ATtiny25” on page 11 and Section 6.2 “ATtiny45” on page 12

2. Updated:

– “Features” on page 1, removed Preliminary from ATtiny25   
– Section 8.4.2 “Code Example” on page 44   
– “PCMSK – Pin Change Mask Register” on page 52, Bit Descriptions   
“TCCR1 – Timer/Counter1 Control Register” on page 89 and “GTCCR – General Timer/Counter1 Control Register” on page 90, COM bit descriptions clarified   
– Section 20.3.2 “Calibration Bytes” on page 150, frequencies (8 MHz, 6.4 MHz)   
– Table 20-11, “Minimum Wait Delay Before Writing the Next Flash or EEPROM Location,” on page 153, value for tWD_ERASE   
– Table 20-16, “High-voltage Serial Programming Instruction Set for ATtiny25/45/85,” on page 158   
– Table 21-1, “DC Characteristics. TA = -40C to +85C,” on page 161, notes adjusted   
– Table 21-11, “Serial Programming Characteristics, TA = -40C to +85C, VCC = 1.8 - 5.5V (Unless Otherwise Noted),” on page 170, added tSLIV   
– Bit syntax throughout the datasheet, e.g. from CS02:0 to CS0[2:0].

# 9.7 Rev. 2586K-01/08

1. Updated Document Template.

2. Added Sections:

– “Data Retention” on page 6   
– “Low Level Interrupt” on page 49   
– “Device Signature Imprint Table” on page 149

3. Updated Sections:

– “Internal PLL for Fast Peripheral Clock Generation - clkPCK” on page 24   
– “System Clock and Clock Options” on page 23   
– “Internal PLL in ATtiny15 Compatibility Mode” on page 24   
“Sleep Modes” on page 34   
“Software BOD Disable” on page 35   
– “External Interrupts” on page 49   
“Timer/Counter1 in PWM Mode” on page 97   
– “USI – Universal Serial Interface” on page 108   
“Temperature Measurement” on page 133   
– “Reading Lock, Fuse and Signature Data from Software” on page 143   
– “Program And Data Memory Lock Bits” on page 147   
– “Fuse Bytes” on page 148   
“Signature Bytes” on page 150   
– “Calibration Bytes” on page 150   
– “System and Reset Characteristics” on page 165

4. Added Figures:

– “Reset Pin Output Voltage vs. Sink Current (VCC = 3V)” on page 184   
– “Reset Pin Output Voltage vs. Sink Current (VCC = 5V)” on page 185   
– “Reset Pin Output Voltage vs. Source Current (VCC = 3V)” on page 185

5. Updated Figure: – “Reset Logic” on page 39

6. Updated Tables:

– “Start-up Times for Internal Calibrated RC Oscillator Clock” on page 28   
“Start-up Times for Internal Calibrated RC Oscillator Clock (in ATtiny15 Mode)” on page 28   
“Start-up Times for the 128 kHz Internal Oscillator” on page 28   
“Compare Mode Select in PWM Mode” on page 86   
“Compare Mode Select in PWM Mode” on page 98   
“DC Characteristics. TA = -40C to +85C” on page 161   
– “Calibration Accuracy of Internal RC Oscillator” on page 164   
– “ADC Characteristics” on page 167

7. Updated Code Example in Section: – “Write” on page 17

8. Updated Bit Descriptions in:

– “MCUCR – MCU Control Register” on page 37   
– “Bits 7:6 – COM0A[1:0]: Compare Match Output A Mode” on page 77   
“Bits 5:4 – COM0B[1:0]: Compare Match Output B Mode” on page 77   
“Bits 2:0 – ADTS[2:0]: ADC Auto Trigger Source” on page 138   
“SPMCSR – Store Program Memory Control and Status Register” on page 145.

9. Updated description of feature “EEPROM read may fail at low supply voltage / low clock frequency” in Sections:

– “Errata ATtiny25” on page 19   
– “Errata ATtiny45” on page 19   
– “Errata ATtiny85” on page 22

10. Updated Package Description in Sections:

– “ATtiny25” on page 11   
– “ATtiny45” on page 12   
– “ATtiny85” on page 13

11. Updated Package Drawing: – “S8S1” on page 16

12. Updated Order Codes for: – “ATtiny25” on page 11

# 9.8 Rev. 2586J-12/06

1. Updated “Low Power Consumption” on page 1.   
2. Updated description of instruction length in “Architectural Overview” .   
3. Updated Flash size in “In-System Re-programmable Flash Program Memory” on page 15.   
4. Updated cross-references in sections “Atomic Byte Programming” , “Erase” and “Write” , starting on page 17.   
5. Updated “Atomic Byte Programming” on page 17.

# Atmel

6. Updated “Internal PLL for Fast Peripheral Clock Generation - clkPCK” on page 24.   
7. Replaced single clocking system figure with two: Figure 6-2 and Figure 6-3.   
8. Updated Table 6-1 on page 25, Table 6-13 on page 30 and Table 6-6 on page 27.   
9. Updated “Calibrated Internal Oscillator” on page 27.   
10. Updated Table 6-5 on page 26.   
11. Updated “OSCCAL – Oscillator Calibration Register” on page 31.   
12. Updated “CLKPR – Clock Prescale Register” on page 32.   
13. Updated “Power-down Mode” on page 35.   
14. Updated “Bit 0” in “PRR – Power Reduction Register” on page 38.   
15. Added footnote to Table 8-3 on page 46.   
16. Updated Table 10-5 on page 63.   
17. Deleted “Bits 7, 2” in “MCUCR – MCU Control Register” on page 64.   
18. Updated and moved section “Timer/Counter0 Prescaler and Clock Sources”, now located on page 66.   
19. Updated “Timer/Counter1 Initialization for Asynchronous Mode” on page 86.   
20. Updated bit description in “PLLCSR – PLL Control and Status Register” on page 94 and “PLLCSR – PLL Control and Status Register” on page 103.   
21. Added recommended maximum frequency in“Prescaling and Conversion Timing” on page 125.   
22. Updated Figure 17-8 on page 129 .   
23. Updated “Temperature Measurement” on page 133.   
24. Updated Table 17-3 on page 134.   
25. Updated bit R/W descriptions in: “TIMSK – Timer/Counter Interrupt Mask Register” on page 81, “TIFR – Timer/Counter Interrupt Flag Register” on page 81, “TIMSK – Timer/Counter Interrupt Mask Register” on page 92, “TIFR – Timer/Counter Interrupt Flag Register” on page 93, “PLLCSR – PLL Control and Status Register” on page 94, “TIMSK – Timer/Counter Interrupt Mask Register” on page 102, “TIFR – Timer/Counter Interrupt Flag Register” on page 103, “PLLCSR – PLL Control and Status Register” on page 103 and “DIDR0 – Digital Input Disable Register 0” on page 138.   
26. Added limitation to “Limitations of debugWIRE” on page 140.   
27. Updated “DC Characteristics” on page 161.   
28. Updated Table 21-7 on page 166.   
29. Updated Figure 21-6 on page 171.   
30. Updated Table 21-12 on page 171.   
31. Updated Table 22-1 on page 177.   
32. Updated Table 22-2 on page 177.   
33. Updated Table 22-30, Table 22-31 and Table 22-32, starting on page 188.   
34. Updated Table 22-33, Table 22-34 and Table 22-35, starting on page 189.   
35. Updated Table 22-39 on page 192.   
36. Updated Table 22-46, Table 22-47, Table 22-48 and Table 22-49.

1. All Characterization data moved to “Electrical Characteristics” on page 161.   
2. All Register Descriptions are gathered up in seperate sections in the end of each   
chapter.   
3. Updated Table 11-3 on page 78, Table 11-5 on page 79, Table 11-6 on page 80 and   
Table 20-4 on page 148.   
4. Updated “Calibrated Internal Oscillator” on page 27.   
5. Updated Note in Table 7-1 on page 34.   
6. Updated “System Control and Reset” on page 39.   
7. Updated Register Description in “I/O Ports” on page 53.   
8. Updated Features in “USI – Universal Serial Interface” on page 108.   
9. Updated Code Example in “SPI Master Operation Example” on page 110 and “SPI   
Slave Operation Example” on page 111.   
10. Updated “Analog Comparator Multiplexed Input” on page 119.   
11. Updated Figure 17-1 on page 123.   
12. Updated “Signature Bytes” on page 150.   
13. Updated “Electrical Characteristics” on page 161.

# 9.10 Rev. 2586H-06/06

1. Updated “Calibrated Internal Oscillator” on page 27.   
2. Updated Table 6.5.1 on page 31.   
3. Added Table 21-2 on page 164.

# 9.11 Rev. 2586G-05/06

1. Updated “Internal PLL for Fast Peripheral Clock Generation - clkPCK” on page 24.   
2. Updated “Default Clock Source” on page 30.   
3. Updated “Low-Frequency Crystal Oscillator” on page 29.   
4. Updated “Calibrated Internal Oscillator” on page 27.   
5. Updated “Clock Output Buffer” on page 31.   
6. Updated “Power Management and Sleep Modes” on page 34.   
7. Added “Software BOD Disable” on page 35.   
8. Updated Figure 16-1 on page 119.   
9. Updated “Bit 6 – ACBG: Analog Comparator Bandgap Select” on page 120.   
10. Added note for Table 17-2 on page 125.   
11. Updated “Register Summary” on page 7.

# 9.12 Rev. 2586F-04/06

1. Updated “Digital Input Enable and Sleep Modes” on page 57.   
2. Updated Table 20-16 on page 158.   
3. Updated “Ordering Information” on page 11.

# 9.13 Rev. 2586E-03/06

1. Updated Features in “Analog to Digital Converter” on page 122.   
2. Updated Operation in “Analog to Digital Converter” on page 122.   
3. Updated Table 17-2 on page 133.   
4. Updated Table 17-3 on page 134.   
5. Updated “Errata” on page 19.

# 9.14 Rev. 2586D-02/06

1. Updated Table 6-13 on page 30, Table 6-10 on page 29, Table 6-3 on page 26,   
Table 6-9 on page 28, Table 6-5 on page 26, Table 9-1 on page 48,Table 17-4 on   
page 135, Table 20-16 on page 158, Table 21-8 on page 167.   
2. Updated “Timer/Counter1 in PWM Mode” on page 86.   
3. Updated text “Bit 2 – TOV1: Timer/Counter1 Overflow Flag” on page 93.   
4. Updated values in “DC Characteristics” on page 161.   
5. Updated “Register Summary” on page 7.   
6. Updated “Ordering Information” on page 11.   
7. Updated Rev B and C in “Errata ATtiny45” on page 19.   
8. All references to power-save mode are removed.   
9. Updated Register Adresses.

# 9.15 Rev. 2586C-06/05

1. Updated “Features” on page 1.   
2. Updated Figure 1-1 on page 2.   
3. Updated Code Examples on page 18 and page 19.   
4. Moved “Temperature Measurement” to Section 17.12 page 133.   
5. Updated “Register Summary” on page 7.   
6. Updated “Ordering Information” on page 11.

# 9.16 Rev. 2586B-05/05

1. CLKI added, instances of EEMWE/EEWE renamed EEMPE/EEPE, removed some   
TBD.   
Removed “Preliminary Description” from “Temperature Measurement” on page 133.   
2. Updated “Features” on page 1.   
3. Updated Figure 1-1 on page 2 and Figure 8-1 on page 39.   
4. Updated Table 7-2 on page 38, Table 10-4 on page 63, Table 10-5 on page 63   
5. Updated “Serial Programming Instruction set” on page 153.   
6. Updated SPH register in “Instruction Set Summary” on page 9.   
7. Updated “DC Characteristics” on page 161.   
8. Updated “Ordering Information” on page 11.   
9. Updated “Errata” on page 19.

# 9.17 Rev. 2586A-02/05

Initial revision.

# Atmel

# Atmel

# Enabling Unlimited Possibilities°

Atmel Corporation 1600 Technology Drive San Jose, CA 95110 USA Tel: (+1) (408) 441-0311 Fax: (+1) (408) 487-2600 www.atmel.com

Atmel Asia Limited Unit 01-5 & 16, 19F BEA Tower, Millennium City 5 418 Kwun Tong Roa Kwun Tong, Kowloon HONG KONG Tel: (+852) 2245-6100 Fax: (+852) 2722-1369

Atmel Munich GmbH   
Business Campus   
Parkring 4   
D-85748 Garching b. Munich   
GERMANY   
Tel: (+49) 89-31970-0   
Fax: (+49) 89-3194621 Atmel Japan G.K.   
16F Shin-Osaki Kangyo Bldg 1-6-4 Osaki, Shinagawa-ku Tokyo 141-0032   
JAPAN   
Tel: (+81) (3) 6417-0300   
Fax: (+81) (3) 6417-0370

© 2013 Atmel Corporation. All rights reserved. / Rev.: 2586QS–AVR–08/2013

Atmel®, Atmel logo and combinations thereof, Enabling Unlimited Possibilities®, AVR®, tinyAVR® and others are registered trademarks or trademarks of Atmel Corporation or its subsidiaries. Other terms and product names may be trademarks of others.