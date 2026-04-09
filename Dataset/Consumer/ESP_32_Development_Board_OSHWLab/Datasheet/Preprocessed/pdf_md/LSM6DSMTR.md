# iNEMO inertial module: always-on 3D accelerometer and 3D gyroscope

Datasheet - production data

![](images/fd4a84a48a98fa4063033ea03f63bd05bfb8b2ec6cb3cc83db2352b1941926f3.jpg)

# Features

“Always-on” experience with low power consumption for both accelerometer and gyroscope Power consumption: 0.4 mA in combo normal mode and 0.65 mA in combo high-performance mode   
 Smart FIFO up to 4 kbyte based on features set   
 Android M compliant   
 Auxiliary SPI for OIS data output for gyroscope and accelerometer Hard, soft ironing for external magnetic sensor corrections   
 ±2/±4/±8/±16 g full scale ±125/±245/±500/±1000/±2000 dps full scale   
 Analog supply voltage: 1.71 V to 3.6 V SPI & I2C serial interface with main processor data synchronization Dedicated gyroscope low-pass filters for UI and OIS applications Smart embedded functions: pedometer, step detector and step counter, significant motion and tilt Standard interrupts: free-fall, wakeup, 6D/4D orientation, click and double-click Embedded temperature sensor ECOPACK®, RoHS and “Green” compliant

# Applications

 Motion tracking and gesture detection   
 Sensor hub   
 Indoor navigation   
 IoT and connected devices   
 Smart power saving for handheld devices   
 EIS and OIS for camera applications   
 Vibration monitoring and compensation

# Description

The LSM6DSM is a system-in-package featuring a 3D digital accelerometer and a 3D digital gyroscope performing at 0.65 mA in high-performance mode and enabling always-on low-power features for an optimal motion experience for the consumer.

The LSM6DSM supports main OS requirements, offering real, virtual and batch sensors with 4 kbyte for dynamic data batching.

ST’s family of MEMS sensor modules leverages the robust and mature manufacturing processes already used for the production of micromachined accelerometers and gyroscopes.

The various sensing elements are manufactured using specialized micromachining processes, while the IC interfaces are developed using CMOS technology that allows the design of a dedicated circuit which is trimmed to better match the characteristics of the sensing element.

The LSM6DSM has a full-scale acceleration range of ±2/±4/±8/±16 g and an angular rate range of ±125/±245/±500/±1000/±2000 dps.

The LSM6DSM fully supports EIS and OIS applications as the module includes a dedicated configurable signal processing path for OIS and auxiliary SPI configurable for both the gyroscope and accelerometer.

High robustness to mechanical shock makes the LSM6DSM the preferred choice of system designers for the creation and manufacturing of reliable products.

The LSM6DSM is available in a plastic land grid array (LGA) package.

Table 1. Device summary   

<table><tr><td rowspan=1 colspan=1>Part number</td><td rowspan=1 colspan=1>Temp.range [°c]</td><td rowspan=1 colspan=1>Package</td><td rowspan=1 colspan=1>Packing</td></tr><tr><td rowspan=1 colspan=1>LSM6DSM</td><td rowspan=1 colspan=1>-40 to +85</td><td rowspan=2 colspan=1>LGA-14L(2.5x3x0.83mm)</td><td rowspan=1 colspan=1>Tray</td></tr><tr><td rowspan=1 colspan=1>LSM6DSMTR</td><td rowspan=1 colspan=1>-40 to +85</td><td rowspan=1 colspan=1>Tape &amp;Reel</td></tr></table>

# Contents

Overview 17

# Embedded low-power features . . 18

2.1 Tilt detection 18   
2.2 Absolute wrist tilt 19

# Pin description 20

3.1 Pin connections 21

# Module specifications . . 23

4.4 Communication interface characteristics 28

4.4.1 SPI - serial peripheral interface . 28   
4.4.2 I2C - inter-IC control interface 29

4.5 Absolute maximum ratings . 31

4.6 Terminology 32

4.6.1 Sensitivity . . . . 32   
4.6.2 Zero-g and zero-rate level 32

# Functionality 33

5.4 Block diagram of filters . 34

5.4.1 Block diagrams of the gyroscope filters . . . . 34   
5.4.2 Block diagrams of the accelerometer filters . . 36

# 5.5 FIFO 38

5.5.1 Bypass mode . . 38   
5.5.2 FIFO mode . . 39   
5.5.3 Continuous mode . 39   
5.5.4 Continuous-to-FIFO mode . . 39   
5.5.5 Bypass-to-Continuous mode . 39   
5.5.6 FIFO reading procedure . 40

# Digital interfaces . . 41

6.1 I2C/SPI interface . . 41   
6.2 Master I2C 41   
6.3 Auxiliary SPI . 42   
6.4 I2C serial interface 42   
6.4.1 I2C operation . 42   
6.5 SPI bus interface . 44   
6.5.1 SPI read . . . 45   
6.5.2 SPI write . 46   
6.5.3 SPI read in 3-wire mode . 47

# Application hints . . . . 48

7.1 LSM6DSM electrical connections in Mode 1 48   
7.2 LSM6DSM electrical connections in Mode 2 49   
7.3 LSM6DSM electrical connections in Mode 3 and Mode 4 50

# Auxiliary SPI configurations . . 54

8.1 Gyroscope filtering 54   
8.2 Accelerometer filtering 55   
8.2.1 Accelerometer full scale set from primary interface . 55   
8.2.2 Accelerometer full scale set from auxiliary SPI . 55

# Register mapping . . 56

# Register description 60

10.1 FUNC_CFG_ACCESS (01h) 60   
10.2 SENSOR_SYNC_TIME_FRAME (04h) 60   
10.3 SENSOR_SYNC_RES_RATIO (05h) . 61   
10.4 FIFO_CTRL1 (06h) 61   
10.5 FIFO_CTRL2 (07h) 62   
10.6 FIFO_CTRL3 (08h) 63   
10.7 FIFO_CTRL4 (09h) 64   
10.8 FIFO_CTRL5 (0Ah) 65   
10.9 DRDY_PULSE_CFG (0Bh) 66   
10.10 INT1_CTRL (0Dh) 66   
10.11 INT2_CTRL (0Eh) 67   
10.12 WHO_AM_I (0Fh) . 67   
10.13 CTRL1_XL (10h) 68   
10.14 CTRL2_G (11h) 69   
10.15 CTRL3_C (12h) 70   
10.16 CTRL4_C (13h) 71   
10.17 CTRL5_C (14h) 71   
10.18 CTRL6_C (15h) 73   
10.19 CTRL7_G (16h) 74   
10.20 CTRL8_XL (17h) . 74   
10.21 CTRL9_XL (18h) . 75   
10.22 CTRL10_C (19h) 76   
10.23 MASTER_CONFIG (1Ah) . 76   
10.24 WAKE_UP_SRC (1Bh) . 77   
10.25 TAP_SRC (1Ch) . 78   
10.26 D6D_SRC (1Dh) . 78   
10.27 STATUS_REG/STATUS_SPIAux (1Eh) . 79   
10.28 OUT_TEMP_L (20h), OUT_TEMP_H (21h) 79   
10.29 OUTX_L_G (22h) 80   
10.30 OUTX_H_G (23h) . 80   
10.31 OUTY_L_G (24h) 80   
10.32 OUTY_H_G (25h) 81   
10.33 OUTZ_L_G (26h) 81   
10.34 OUTZ_H_G (27h) . 82   
10.35 OUTX_L_XL (28h) 82   
10.36 OUTX_H_XL (29h) 82   
10.37 OUTY_L_XL (2Ah) 83   
10.38 OUTY_H_XL (2Bh) . 83   
10.39 OUTZ_L_XL (2Ch) . 83   
10.40 OUTZ_H_XL (2Dh) . 83   
10.41 SENSORHUB1_REG (2Eh) . 84   
10.42 SENSORHUB2_REG (2Fh) 84   
10.43 SENSORHUB3_REG (30h) 84   
10.44 SENSORHUB4_REG (31h) 85   
10.45 SENSORHUB5_REG (32h) 85   
10.46 SENSORHUB6_REG (33h) 85   
10.47 SENSORHUB7_REG (34h) 85   
10.48 SENSORHUB8_REG (35h) 86   
10.49 SENSORHUB9_REG (36h) 86   
10.50 SENSORHUB10_REG (37h) 86   
10.51 SENSORHUB11_REG (38h) 86   
10.52 SENSORHUB12_REG (39h) 87   
10.53 FIFO_STATUS1 (3Ah) 87   
10.54 FIFO_STATUS2 (3Bh) 87   
10.55 FIFO_STATUS3 (3Ch) 88   
10.56 FIFO_STATUS4 (3Dh) 88   
10.57 FIFO_DATA_OUT_L (3Eh) . 88   
10.58 FIFO_DATA_OUT_H (3Fh) 89   
10.59 TIMESTAMP0_REG (40h) 89   
10.60 TIMESTAMP1_REG (41h) 89   
10.61 TIMESTAMP2_REG (42h) 89   
10.62 STEP_TIMESTAMP_L (49h) 90   
10.63 STEP_TIMESTAMP_H (4Ah) 90   
10.64 STEP_COUNTER_L (4Bh) 90   
10.65 STEP_COUNTER_H (4Ch) 91   
10.66 SENSORHUB13_REG (4Dh) . 91   
10.67 SENSORHUB14_REG (4Eh) . 91   
10.68 SENSORHUB15_REG (4Fh) 91   
10.69 SENSORHUB16_REG (50h) 92   
10.70 SENSORHUB17_REG (51h) 92   
10.71 SENSORHUB18_REG (52h) 92   
10.72 FUNC_SRC1 (53h) 93   
10.73 FUNC_SRC2 (54h) 93   
10.74 WRIST_TILT_IA (55h) 94   
10.75 TAP_CFG (58h) 95   
10.76 TAP_THS_6D (59h) 96   
10.77 INT_DUR2 (5Ah) 96   
10.78 WAKE_UP_THS (5Bh) . 97   
10.79 WAKE_UP_DUR (5Ch) 97   
10.80 FREE_FALL (5Dh) 98   
10.81 MD1_CFG (5Eh) 99   
10.82 MD2_CFG (5Fh) . 100   
10.83 MASTER_CMD_CODE (60h) 101   
10.84 SENS_SYNC_SPI_ERROR_CODE (61h) 101   
10.85 OUT_MAG_RAW_X_L (66h) 101   
10.86 OUT_MAG_RAW_X_H (67h) 101   
10.87 OUT_MAG_RAW_Y_L (68h) 102   
10.88 OUT_MAG_RAW_Y_H (69h) 102   
10.89 OUT_MAG_RAW_Z_L (6Ah) 102   
10.90 OUT_MAG_RAW_Z_H (6Bh) . 102   
10.91 INT_OIS (6Fh) 103   
10.92 CTRL1_OIS (70h) 103   
10.93 CTRL2_OIS (71h) 104   
10.94 CTRL3_OIS (72h) 105   
10.95 X_OFS_USR (73h) . 106   
10.96 Y_OFS_USR (74h) . . 106   
10.97 Z_OFS_USR (75h) . 106

# Embedded functions register mapping . . . 107

# 12 Embedded functions registers description - Bank A . . . . 109

12.1 SLV0_ADD (02h) 109   
12.2 SLV0_SUBADD (03h) 109   
12.3 SLAVE0_CONFIG (04h) . 109   
12.4 SLV1_ADD (05h) 110   
12.5 SLV1_SUBADD (06h) 110   
12.6 SLAVE1_CONFIG (07h) . .111   
12.7 SLV2_ADD (08h) .111   
12.8 SLV2_SUBADD (09h) .111   
12.9 SLAVE2_CONFIG (0Ah) 112   
12.10 SLV3_ADD (0Bh) 112   
12.11 SLV3_SUBADD (0Ch) 112   
12.12 SLAVE3_CONFIG (0Dh) 113   
12.13 DATAWRITE_SRC_MODE_SUB_SLV0 (0Eh) . 113   
12.14 CONFIG_PEDO_THS_MIN (0Fh) 113   
12.15 SM_THS (13h) . . 114   
12.16 PEDO_DEB_REG (14h) . 114   
12.17 STEP_COUNT_DELTA (15h) . 114   
12.18 MAG_SI_XX (24h) 115   
12.19 MAG_SI_XY (25h) 115   
12.20 MAG_SI_XZ (26h) 115   
12.21 MAG_SI_YX (27h) 115   
12.22 MAG_SI_YY (28h) 116   
12.23 MAG_SI_YZ (29h) 116   
12.24 MAG_SI_ZX (2Ah) 116   
12.25 MAG_SI_ZY (2Bh) 116   
12.26 MAG_SI_ZZ (2Ch) 117   
12.27 MAG_OFFX_L (2Dh) 117   
12.28 MAG_OFFX_H (2Eh) 117   
12.29 MAG_OFFY_L (2Fh) 117   
12.30 MAG_OFFY_H (30h) 118   
12.31 MAG_OFFZ_L (31h) 118   
12.32 MAG_OFFZ_H (32h) 118

# Embedded functions registers description - Bank B . . . 119

13.1 A_WRIST_TILT_LAT (50h) . 119   
13.2 A_WRIST_TILT_THS (54h) 119   
13.3 A_WRIST_TILT_Mask (59h) 119

# Soldering information . 120

15

Package information . . . 121

15.1 LGA-14L package information 121   
15.2 LGA-14 packing information . 122

16 Revision history 124

# List of tables

Table 1. Device summary . . 1   
Table 2. Pin description 22   
Table 3. Mechanical characteristics . 2 3   
Table 4. Electrical characteristics . 2 6   
Table 5. Temperature sensor characteristics 27   
Table 6. SPI slave timing values. 28   
Table 7. I2C slave timing values . 2 9   
Table 8. I2C master timing values. . 3 0   
Table 9. Absolute maximum ratings . 31   
Table 10. Serial interface pin description . 41   
Table 11. Master I2C pin details . 41   
Table 12. Auxiliary SPI pin details 42   
Table 13. I2C terminology . 42   
Table 14. SAD+Read/Write patterns 43   
Table 15. Transfer when master is writing one byte to slave . 43   
Table 16. Transfer when master is writing multiple bytes to slave . 43   
Table 17. Transfer when master is receiving (reading) one byte of data from slave 43   
Table 18. Transfer when master is receiving (reading) multiple bytes of data from slave 43   
Table 19. Internal pin status . . . 52   
Table 20. Registers address map. 56   
Table 21. FUNC_CFG_ACCESS register. . 60   
Table 22. FUNC_CFG_ACCESS register description 60   
Table 23. Configuration of embedded functions register banks . 60   
Table 24. SENSOR_SYNC_TIME_FRAME register. . 60   
Table 25. SENSOR_SYNC_TIME_FRAME register description 60   
Table 26. SENSOR_SYNC_RES_RATIO register . . 61   
Table 27. SENSOR_SYNC_RES_RATIO register description. 61   
Table 28. FIFO_CTRL1 register . . 61   
Table 29. FIFO_CTRL1 register description. 61   
Table 30. FIFO_CTRL2 register . 62   
Table 31. FIFO_CTRL2 register description. 62   
Table 32. FIFO_CTRL3 register . 63   
Table 33. FIFO_CTRL3 register description. 63   
Table 34. Gyro FIFO decimation setting. . 63   
Table 35. Accelerometer FIFO decimation setting 63   
Table 36. FIFO_CTRL4 register . . . . 64   
Table 37. FIFO_CTRL4 register description. 64   
Table 38. Fourth FIFO data set decimation setting. 64   
Table 39. Third FIFO data set decimation setting. 64   
Table 40. FIFO_CTRL5 register . 65   
Table 41. FIFO_CTRL5 register description. 65   
Table 42. FIFO ODR selection . 65   
Table 43. FIFO mode selection. 65   
Table 44. DRDY_PULSE_CFG register . . 66   
Table 45. DRDY_PULSE_CFG register description. 66   
Table 46. INT1_CTRL register . 66   
Table 47. INT1_CTRL register description . 66   
Table 48. INT2_CTRL register . 67   
Table 49. INT2_CTRL register description . 67   
Table 50. WHO_AM_I register . 67   
Table 51. CTRL1_XL register . 68   
Table 52. CTRL1_XL register description. 68   
Table 53. Accelerometer ODR register setting . 68   
Table 54. CTRL2_G register. . 69   
Table 55. CTRL2_G register description 69   
Table 56. Gyroscope ODR configuration setting 69   
Table 57. CTRL3_C register . . . 70   
Table 58. CTRL3_C register description. 70   
Table 59. CTRL4_C register . . . 71   
Table 60. CTRL4_C register description. . 71   
Table 61. CTRL5_C register 71   
Table 62. CTRL5_C register description. 71   
Table 63. Output registers rounding pattern . 72   
Table 64. Angular rate sensor self-test mode selection 72   
Table 65. Linear acceleration sensor self-test mode selection. 72   
Table 66. CTRL6_C register. . . 73. 73   
Table 67. CTRL6_C register description.   
Table 68. Trigger mode selection . 73   
Table 69. Gyroscope LPF1 bandwidth selection 73   
Table 70. CTRL7_G register. . . 74   
Table 71. CTRL7_G register description 74   
Table 72. CTRL8_XL register . . . 74   
Table 73. CTRL8_XL register description. . 74   
Table 74. Accelerometer bandwidth selection 75   
Table 75. CTRL9_XL register . . 75   
Table 76. CTRL9_XL register description. 75   
Table 77. CTRL10_C register. 76   
Table 78. CTRL10_C register description. 76   
Table 79. MASTER_CONFIG register 76   
Table 80. MASTER_CONFIG register description 77   
Table 81. WAKE_UP_SRC register . 77   
Table 82. WAKE_UP_SRC register description . 77   
Table 83. TAP_SRC register 78   
Table 84. TAP_SRC register description 78   
Table 85. D6D_SRC register . . . 78   
Table 86. D6D_SRC register description . 78   
Table 87. STATUS_REG register. . 79   
Table 88. STATUS_REG register description. 79   
Table 89. STATUS_SPIAux register. . 79   
Table 90. STATUS_SPIAux description . 79   
Table 91. OUT_TEMP_L register . 79   
Table 92. OUT_TEMP_H register. . 79   
Table 93. OUT_TEMP register description. 79   
Table 94. OUTX_L_G register 80   
Table 95. OUTX_L_G register description . 80   
Table 96. OUTX_H_G register . 80   
Table 97. OUTX_H_G register description . 80   
Table 98. OUTY_L_G register . . . . 81   
Table 99. OUTY_L_G register description . 81   
Table 100. OUTY_H_G register . 81   
Table 101. OUTY_H_G register description . . 81   
Table 102. OUTZ_L_G register . . 81   
Table 103. OUTZ_L_G register description 81   
Table 104. OUTZ_H_G register . 82   
Table 105. OUTZ_H_G register description . 82   
Table 106. OUTX_L_XL register. . 82   
Table 107. OUTX_L_XL register description 82   
Table 108. OUTX_H_XL register 82   
Table 109. OUTX_H_XL register description . 82   
Table 110. OUTY_L_XL register. . 83   
Table 111. OUTY_L_XL register description 83   
Table 112. OUTY_H_XL register . . 83   
Table 113. OUTY_H_XL register description . 83   
Table 114. OUTZ_L_XL register. . . . 83   
Table 115. OUTZ_L_XL register description 83   
Table 116. OUTZ_H_XL register . . 83   
Table 117. OUTZ_H_XL register description . 83   
Table 118. SENSORHUB1_REG register 84   
Table 119. SENSORHUB1_REG register description 84   
Table 120. SENSORHUB2_REG register 84   
Table 121. SENSORHUB2_REG register description 84   
Table 122. SENSORHUB3_REG register 84   
Table 123. SENSORHUB3_REG register description 84   
Table 124. SENSORHUB4_REG register 85   
Table 125. SENSORHUB4_REG register description 85   
Table 126. SENSORHUB5_REG register . . . 85   
Table 127. SENSORHUB5_REG register description . 85   
Table 128. SENSORHUB6_REG register 85   
Table 129. SENSORHUB6_REG register description . 85   
Table 130. SENSORHUB7_REG register 85   
Table 131. SENSORHUB7_REG register description . 85   
Table 132. SENSORHUB8_REG register 86   
Table 133. SENSORHUB8_REG register description . 86   
Table 134. SENSORHUB9_REG register 86   
Table 135. SENSORHUB9_REG register description . 86   
Table 136. SENSORHUB10_REG register 86   
Table 137. SENSORHUB10_REG register description 86   
Table 138. SENSORHUB11_REG register . 86   
Table 139. SENSORHUB11_REG register description . 86   
Table 140. SENSORHUB12_REG register . . . . 87   
Table 141. SENSORHUB12_REG register description 87   
Table 142. FIFO_STATUS1 register 87   
Table 143. FIFO_STATUS1 register description 87   
Table 144. FIFO_STATUS2 register 87   
Table 145. FIFO_STATUS2 register description 87   
Table 146. FIFO_STATUS3 register 88   
Table 147. FIFO_STATUS3 register description 88   
Table 148. FIFO_STATUS4 register 88   
Table 149. FIFO_STATUS4 register description 88   
Table 150. FIFO_DATA_OUT_L register . . 88   
Table 151. FIFO_DATA_OUT_L register description . 88   
Table 152. FIFO_DATA_OUT_H register. . . 89   
Table 153. FIFO_DATA_OUT_H register description. . 89   
Table 154. TIMESTAMP0_REG register 89   
Table 155. TIMESTAMP0_REG register description 89   
Table 156. TIMESTAMP1_REG register . 89   
Table 157. TIMESTAMP1_REG register description 89   
Table 158. TIMESTAMP2_REG register 89   
Table 159. TIMESTAMP2_REG register description 89   
Table 160. STEP_TIMESTAMP_L register. . . 90   
Table 161. STEP_TIMESTAMP_L register description 90   
Table 162. STEP_TIMESTAMP_H register . . . 90   
Table 163. STEP_TIMESTAMP_H register description . 90   
Table 164. STEP_COUNTER_L register . . 90   
Table 165. STEP_COUNTER_L register description . . 90   
Table 166. STEP_COUNTER_H register . . . 91   
Table 167. STEP_COUNTER_H register description. . 91   
Table 168. SENSORHUB13_REG register 91   
Table 169. SENSORHUB13_REG register description . 91   
Table 170. SENSORHUB14_REG register . 91   
Table 171. SENSORHUB14_REG register description 91   
Table 172. SENSORHUB15_REG register 91   
Table 173. SENSORHUB15_REG register description 91   
Table 174. SENSORHUB16_REG register . 92   
Table 175. SENSORHUB16_REG register description 92   
Table 176. SENSORHUB17_REG register . 92   
Table 177. SENSORHUB17_REG register description 92   
Table 178. SENSORHUB18_REG register . . . 92   
Table 179. SENSORHUB18_REG register description 92   
Table 180. FUNC_SRC1 register . . 93   
Table 181. FUNC_SRC1 register description. 93   
Table 182. FUNC_SRC2 register . 93   
Table 183. FUNC_SRC2 register description. 93   
Table 184. WRIST_TILT_IA register . 94   
Table 185. WRIST_TILT_IA register description 94   
Table 186. TAP_CFG register . . 95   
Table 187. TAP_CFG register description 95   
Table 188. TAP_THS_6D register 96   
Table 189. TAP_THS_6D register description 96   
Table 190. Threshold for D4D/D6D function. 96   
Table 191. INT_DUR2 register . . . . 96   
Table 192. INT_DUR2 register description. . 96   
Table 193. WAKE_UP_THS register 97   
Table 194. WAKE_UP_THS register description 97   
Table 195. WAKE_UP_DUR register . . 97   
Table 196. WAKE_UP_DUR register description . 97   
Table 197. FREE_FALL register. 98   
Table 198. FREE_FALL register description 98   
Table 199. Threshold for free-fall function 98   
Table 200. MD1_CFG register . 99   
Table 201. MD1_CFG register description . 99   
Table 202. MD2_CFG register . . 100   
Table 203. MD2_CFG register description . 100   
Table 204. MASTER_CMD_CODE register . 101   
Table 205. MASTER_CMD_CODE register description. 101   
Table 206. SENS_SYNC_SPI_ERROR_CODE register 101   
Table 207. SENS_SYNC_SPI_ERROR_CODE register description . 101   
Table 208. OUT_MAG_RAW_X_L register 101   
Table 209. OUT_MAG_RAW_X_L register description 101   
Table 210. OUT_MAG_RAW_X_H register . 101   
Table 211. OUT_MAG_RAW_X_H register description . 101   
Table 212. OUT_MAG_RAW_Y_L register 102   
Table 213. OUT_MAG_RAW_Y_L register description 102   
Table 214. OUT_MAG_RAW_Y_H register . . 102   
Table 215. OUT_MAG_RAW_Y_H register description . 102   
Table 216. OUT_MAG_RAW_Z_L register. . . 102   
Table 217. OUT_MAG_RAW_Z_L register description 102   
Table 218. OUT_MAG_RAW_Z_H register . . 102   
Table 219. OUT_MAG_RAW_Z_H register description . 102   
Table 220. INT_OIS register . . 103   
Table 221. INT_OIS register description. 103   
Table 222. CTRL1_OIS register . 103   
Table 223. CTRL1_OIS register description. 103   
Table 224. DEN mode selection . 104   
Table 225. CTRL2_OIS register . 104   
Table 226. CTRL2_OIS register description. 104   
Table 227. Gyroscope OIS chain LPF1 bandwidth selection 104   
Table 228. CTRL3_OIS register . . 105   
Table 229. CTRL3_OIS register description. . 105   
Table 230. Accelerometer OIS channel bandwidth selection . 105   
Table 231. Self-test nominal output variation . . 106   
Table 232. X_OFS_USR register . 106   
Table 233. X_OFS_USR register description . 106   
Table 234. Y_OFS_USR register . 106   
Table 235. Y_OFS_USR register description . 106   
Table 236. Z_OFS_USR register 106   
Table 237. Z_OFS_USR register description . 106   
Table 238. Register address map - Bank A - embedded functions . 107   
Table 239. Register address map - Bank B - embedded functions . 108   
Table 240. SLV0_ADD register. . . 109   
Table 241. SLV0_ADD register description 109   
Table 242. SLV0_SUBADD register . . . 109   
Table 243. SLV0_SUBADD register description. . 109   
Table 244. SLAVE0_CONFIG register . . 109   
Table 245. SLAVE0_CONFIG register description. 110   
Table 246. SLV1_ADD register. . 110   
Table 247. SLV1_ADD register description 110   
Table 248. SLV1_SUBADD register . 110   
Table 249. SLV1_SUBADD register description. 110   
Table 250. SLAVE1_CONFIG register . . 111   
Table 251. SLAVE1_CONFIG register description. 111   
Table 252. SLV2_ADD register. . . . 111   
Table 253. SLV2_ADD register description 111   
Table 254. SLV2_SUBADD register . . 111   
Table 255. SLV2_SUBADD register description. 111   
Table 256. SLAVE2_CONFIG register . . 112   
Table 257. SLAVE2_CONFIG register description. 112   
Table 258. SLV3_ADD register. . 112   
Table 259. SLV3_ADD register description 112   
Table 260. SLV3_SUBADD register . 112   
Table 261. SLV3_SUBADD register description. 112   
Table 262. SLAVE3_CONFIG register . . 113   
Table 263. SLAVE3_CONFIG register description. 113   
Table 264. DATAWRITE_SRC_MODE_SUB_SLV0 register . 113   
Table 265. DATAWRITE_SRC_MODE_SUB_SLV0 register description. 113   
Table 266. CONFIG_PEDO_THS_MIN register. . . 113   
Table 267. CONFIG_PEDO_THS_MIN register description. 113   
Table 268. SM_THS register . . . 114   
Table 269. SM_THS register description 114   
Table 270. PEDO_DEB_REG register . 114   
Table 271. PEDO_DEB_REG register description . 114   
Table 272. STEP_COUNT_DELTA register . 114   
Table 273. STEP_COUNT_DELTA register description. 114   
Table 274. MAG_SI_XX register. . 115   
Table 275. MAG_SI_XX register description 115   
Table 276. MAG_SI_XY register. . 115   
Table 277. MAG_SI_XY register description 115   
Table 278. MAG_SI_XZ register. . . 115   
Table 279. MAG_SI_XZ register description 115   
Table 280. MAG_SI_YX register. . . 115   
Table 281. MAG_SI_YX register description 115   
Table 282. MAG_SI_YY register. . 116   
Table 283. MAG_SI_YY register description 116   
Table 284. MAG_SI_YZ register. . 116   
Table 285. MAG_SI_YZ register description 116   
Table 286. MAG_SI_ZX register. 116   
Table 287. MAG_SI_ZX register description 116   
Table 288. MAG_SI_ZY register. . 116   
Table 289. MAG_SI_ZY register description 116   
Table 290. MAG_SI_ZZ register . . . 117   
Table 291. MAG_SI_ZZ register description. 117   
Table 292. MAG_OFFX_L register . . 117   
Table 293. MAG_OFFX_L register description. . 117   
Table 294. MAG_OFFX_H register. . . 117   
Table 295. MAG_OFFX_H register description 117   
Table 296. MAG_OFFY_L register . . 117   
Table 297. MAG_OFFY_L register description. . 117   
Table 298. MAG_OFFY_H register. . 118   
Table 299. MAG_OFFY_H register description 118   
Table 300. MAG_OFFZ_L register . 118   
Table 301. MAG_OFFZ_L register description. 118   
Table 302. MAG_OFFZ_H register. . 118   
Table 303. MAG_OFFZ_H register description 118   
Table 304. A_WRIST_TILT_LAT register. . 119   
Table 305. A_WRIST_TILT_LAT register description. 119   
Table 306. A_WRIST_TILT_THS register . . . . . 119   
Table 307. A_WRIST_TILT_THS register description . 119   
Table 308. A_WRIST_TILT_Mask register. . 119   
Table 309. A_WRIST_TILT_Mask register description. . . 119   
Table 310. Reel dimensions for carrier tape of LGA-14 package. 123   
Table 311. Document revision history. . . 124

# List of figures

Figure 1. Pin connections 20   
Figure 2. LSM6DSM connection modes . 21   
Figure 3. SPI slave timing diagram 28   
Figure 4. I2C timing diagram 29   
Figure 5. Block diagram of filters . . 34   
Figure 6. Gyroscope digital chain - Mode 1 (UI/EIS) and Mode 2 . 34   
Figure 7. Gyroscope digital chain - Mode 3 / Mode 4 (OIS/EIS) 35   
Figure 8. Accelerometer chain . 36   
Figure 9. Accelerometer composite filter (for Modes 1/2 and Mode 3\*). . . 36   
Figure 10. Accelerometer composite filter (Mode 4 only\*) . 37   
Figure 11. Read and write protocol . . 44   
Figure 12. SPI read protocol . 45   
Figure 13. Multiple byte SPI read protocol (2-byte example). . 45   
Figure 14. SPI write protocol . . . 46   
Figure 15. Multiple byte SPI write protocol (2-byte example). . . 46   
Figure 16. SPI read protocol in 3-wire mode . . 47   
Figure 17. LSM6DSM electrical connections in Mode 1 . 48   
Figure 18. LSM6DSM electrical connections in Mode 2 . 49   
Figure 19. LSM6DSM electrical connections in Mode 3 and Mode 4 (auxiliary 3-wire SPI) 50   
Figure 20. LSM6DSM electrical connections in Mode 3 and Mode 4 (auxiliary 4-wire SPI) . 51   
Figure 21. Gyroscope chain. . . 54   
Figure 22. Accelerometer chain (available only in Mode 4) . 55   
Figure 23. LGA-14L 2.5x3x0.86 mm package outline and mechanical data . 121   
Figure 24. Carrier tape information for LGA-14 package. . . 122   
Figure 25. LGA-14 package orientation in carrier tape . 122   
Figure 26. Reel information for carrier tape of LGA-14 package . . 123

# Overview

The LSM6DSM is a system-in-package featuring a high-performance 3-axis digital accelerometer and 3-axis digital gyroscope.

The integrated power-efficient modes are able to reduce the power consumption down to 0.65 mA in high-performance mode, combining always-on low-power features with superior sensing precision for an optimal motion experience for the consumer thanks to ultra-low noise performance for both the gyroscope and accelerometer.

The LSM6DSM delivers best-in-class motion sensing that can detect orientation and gestures in order to empower application developers and consumers with features and capabilities that are more sophisticated than simply orienting their devices to portrait and landscape mode.

The event-detection interrupts enable efficient and reliable motion tracking and contextual awareness, implementing hardware recognition of free-fall events, 6D orientation, click and double-click sensing, activity or inactivity, and wakeup events.

The LSM6DSM supports main OS requirements, offering real, virtual and batch mode sensors. In addition, the LSM6DSM can efficiently run the sensor-related features specified in Android, saving power and enabling faster reaction time. In particular, the LSM6DSM has been designed to implement hardware features such as significant motion, tilt, pedometer functions, timestamping and to support the data acquisition of an external magnetometer with ironing correction (hard, soft).

The LSM6DSM offers hardware flexibility to connect the pins with different mode connections to external sensors to expand functionalities such as adding a sensor hub, auxiliary SPI, etc.

Up to 4 kbyte of FIFO with dynamic allocation of significant data (i.e. external sensors, timestamp, etc.) allows overall power saving of the system.

The LSM6DSM fully supports OIS/EIS applications using both the gyroscope and accelerometer sensor. The device can output OIS data through a dedicated auxiliary SPI and includes a dedicated configurable signal processing path for OIS. OIS data can be sent directly to the application processor for data processing. The gyroscope UI signal processing path is completely independent from that of the OIS and is readable through FIFO.

Like the entire portfolio of MEMS sensor modules, the LSM6DSM leverages the robust and mature in-house manufacturing processes already used for the production of micromachined accelerometers and gyroscopes. The various sensing elements are manufactured using specialized micromachining processes, while the IC interfaces are developed using CMOS technology that allows the design of a dedicated circuit which is trimmed to better match the characteristics of the sensing element.

The LSM6DSM is available in a small plastic land grid array (LGA) package of 2.5 x 3.0 x 0.83 mm to address ultra-compact solutions.

# Embedded low-power features

The LSM6DSM has been designed to be fully compliant with Android, featuring the following on-chip functions:

 4 kbyte data buffering 100% efficiency with flexible configurations and partitioning Possibility to store timestamp

 Event-detection interrupts (fully configurable):

Free-fall   
Wakeup   
6D orientation   
Click And double-click sensing   
Activity / inactivity recognition

 Specific IP blocks with negligible power consumption and high-performance:

Pedometer functions: step detector and step counters   
Tilt (refer to Section 2.1: Tilt detection for additional information   
Absolute Wrist Tilt (refer to Section 2.2: Absolute wrist tilt for additional   
information)   
Significant Motion Detection

Sensor hub Up to 6 total sensors: 2 internal (accelerometer and gyroscope) and 4 external sensors

 Data rate synchronization with external trigger for reduced sensor access and enhanced fusion

# 2.1 Tilt detection

The tilt function helps to detect activity change and has been implemented in hardware using only the accelerometer to achieve both the targets of ultra-low power consumption and robustness during the short duration of dynamic accelerations.

It is based on a trigger of an event each time the device's tilt changes. For a more customized user experience, in the LSM6DSM the tilt function is configurable through:

a programmable average window a programmable average threshold

The tilt function can be used with different scenarios, for example:

a) Triggers when phone is in a front pants pocket and the user goes from sitting to standing or standing to sitting;   
b) Doesn’t trigger when phone is in a front pants pocket and the user is walking, running or going upstairs.

# 2.2 Absolute wrist tilt

The LSM6DSM implements in hardware the Absolute Wrist Tilt (AWT) function which allows detecting when the angle between a selectable accelerometer semi-axis and the horizontal plane becomes higher than a specific user-selectable value.

Configurable threshold and latency parameters are associated with the AWT function: the threshold parameter defines the amplitude of the tilt angle; the latency parameter defines the minimum duration of the AWT event to be recognized. The AWT interrupt signal is generated if the tilt angle is higher than the threshold angle for a period of time equal to or greater than the latency period.

The AWT function is based on the accelerometer sensor only and works at 26 Hz, so the accelerometer ODR must be set at a value of 26 Hz or higher.

By default, the AWT algorithm is applied to the positive X-axis.

In order to enable the AWT function it is necessary to set to 1 both the FUNC_EN bit and the WRIST_TILT_EN bit of CTRL10_C (19h).

The AWT interrupt signal can be driven to the INT2 interrupt pin by setting to 1 the INT2_WRIST_TILT bit of the DRDY_PULSE_CFG (0Bh) register; it can also be checked by reading the WRIST_TILT_IA bit of the FUNC_SRC2 (54h) register (it will also clear the interrupt signal if latched).

WRIST_TILT_IA (55h) is the status register to be used to detect which axis has triggered the AWT event (not applicable when using one axis side only).

The full description and an example is given in the dedicated application note.

# 3 Pin description

![](images/d4aff8ce182aaae8f4df6528592d294a874bb64746935bb6598becb1129d4ac5.jpg)  
Figure 1. Pin connections

# 3.1 Pin connections

The LSM6DSM offers flexibility to connect the pins in order to have four different mode connections and functionalities. In detail:

Mode 1: I2C slave interface or SPI (3- and 4-wire) serial interface is available;   
Mode 2: I2C slave interface or SPI (3- and 4-wire) serial interface and I2C interface master for external sensor connections are available;   
Mode 3: I2C slave interface or SPI (3- and 4-wire) serial interface is available for the application processor interface while an auxiliary SPI (3- and 4-wire) serial interface for external sensor connections (i.e. camera module) is available for the gyroscope ONLY; Mode 4: I2C slave interface or SPI (3- and 4-wire) serial interface is available for the application processor interface while an auxiliary SPI (3- and 4-wire) serial interface for external sensor connections (i.e. camera module with hybrid OIS) is available for the accelerometer and gyroscope.

![](images/6544219a6b85dd4a443fa4a26993e166e4896a062087ae1bdc526e49a3d34a07.jpg)  
Figure 2. LSM6DSM connection modes   
In the following table each mode is described for the pin connections and function.

Table 2. Pin description   

<table><tr><td rowspan=1 colspan=1>Pin#</td><td rowspan=1 colspan=1>Name</td><td rowspan=1 colspan=1>Mode 1 function</td><td rowspan=1 colspan=1>Mode 2 function</td><td rowspan=1 colspan=1>Mode 3 / Mode 4 function</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>SDO/SAO</td><td rowspan=1 colspan=1>SPI 4-wire interface serialdata output (SDO)12C least significant bit of thedevice address (SA0)</td><td rowspan=1 colspan=1>SPI 4-wire interface serial dataoutput (SDO)12C least significant bit of thedevice address (SA0)</td><td rowspan=1 colspan=1>SPI 4-wire interface serialdata output (SDO)12C least significant bit of thedevice address (SA0)</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>SDx</td><td rowspan=1 colspan=1>Connect to VDDIO or GND</td><td rowspan=1 colspan=1>|2C serial data master (MSDA)</td><td rowspan=1 colspan=1>Auxiliary SPI 3/4-wireinterface serial data input(SDI)and SPI 3-wire serial dataoutput (SDO)</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>SCx</td><td rowspan=1 colspan=1>Connect to VDDIO or GND</td><td rowspan=1 colspan=1>|2C serial clock master (MSCL)</td><td rowspan=1 colspan=1>Auxiliary SPI 3-wire interfaceserial port clock (SPC_Aux)</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>INT1</td><td rowspan=1 colspan=3>Programmable interrupt 1</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>VDDIO(1)</td><td rowspan=1 colspan=3>Power supply for I/O pins</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=3>0V supply</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>GND</td><td rowspan=1 colspan=3>oV supply</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>VDD(1)</td><td rowspan=1 colspan=3>Power supply</td></tr><tr><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>INT2</td><td rowspan=1 colspan=1>Programmable interrupt 2(INT2) / Data enable (DEN)</td><td rowspan=1 colspan=1>Programmable interrupt 2(INT2)/ Data enable (DEN)/i²C master externalsynchronization signal (MDRDY)</td><td rowspan=1 colspan=1>Programmable interupt 2(INT2)/ Data enable (DEN)</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>OCS_Aux</td><td rowspan=1 colspan=1>Leave unconnected(2)</td><td rowspan=1 colspan=1>Leave unconnected(2)</td><td rowspan=1 colspan=1>Auxiliary SPI 3/4-wireinterface enable</td></tr><tr><td rowspan=1 colspan=1>11</td><td rowspan=1 colspan=1>SDO_Aux</td><td rowspan=1 colspan=1>Connect to VDD_IO or leaveunconnected(2)</td><td rowspan=1 colspan=1>Connect to VDD_IO or leaveunconnected(2)</td><td rowspan=1 colspan=1>Auxiliary SPI 3-wire interface:leave unconnected(2)Auxiiary SPI 4-wire interface:serial data output (SDO_Aux)</td></tr><tr><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>|2C/SPI mode selection(1: SPl idle mode / 12Ccommunication enabled; 0:SPI communication mode /{2C disabled)</td><td rowspan=1 colspan=1>|2C/SPl mode selection(1: SPl idle mode / 12Ccommunication enabled;0: SPI communication mode /}2Cdisabled)</td><td rowspan=1 colspan=1>|2C/SPI mode selection(1: SPl idle mode / 2Ccommunication enabled;0: SPI communication mode /{2C disabled)</td></tr><tr><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>SCL</td><td rowspan=1 colspan=1>12C serial clock (SCL)SPI serial port clock (SPC)</td><td rowspan=1 colspan=1>|2C serial clock (SCL)SPI serial port clock (SPC)</td><td rowspan=1 colspan=1>12C serial clock (SCL)SPI serial port clock (SPC)</td></tr><tr><td rowspan=1 colspan=1>14</td><td rowspan=1 colspan=1>SDA</td><td rowspan=1 colspan=1>12C serial data (SDA)SPI serial data input (SDI)3-wire interface serial dataoutput (SDO)</td><td rowspan=1 colspan=1>|2C serial data (SDA)SPI serial data input (SDI)3-wire interface serial dataoutput (SDO)</td><td rowspan=1 colspan=1>12C serial data (SDA)SPI serial data input (SDI)3-wire interface serial dataoutput (SDO)</td></tr></table>

1. Recommended 100 nF filter capacitor. 2. Leave pin electrically unconnected and soldered to PCB.

# 4 Module specifications

# 4.1 Mechanical characteristics

@ Vdd = 1.8 V, T = 25 °C unless otherwise noted.

Table 3. Mechanical characteristics   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Test conditions</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.(1)</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=4 colspan=1>LA_FS</td><td rowspan=4 colspan=1>Linear acceleration measurementrange</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±2</td><td rowspan=1 colspan=1></td><td rowspan=4 colspan=1>g</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±4</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±8</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±16</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=5 colspan=1>G_FS</td><td rowspan=5 colspan=1>Angular ratemeasurement range</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±125</td><td rowspan=1 colspan=1></td><td rowspan=5 colspan=1>dps</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±245</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±500</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±1000</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±2000</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=4 colspan=1>LA_So</td><td rowspan=4 colspan=1>Linear acceleration sensitivity(2)</td><td rowspan=1 colspan=1>FS = ±2</td><td rowspan=4 colspan=1></td><td rowspan=1 colspan=1>0.061</td><td rowspan=4 colspan=1></td><td rowspan=4 colspan=1>mg/LSB</td></tr><tr><td rowspan=1 colspan=1>FS = ±4</td><td rowspan=1 colspan=1>0.122</td></tr><tr><td rowspan=1 colspan=1>FS = ±8</td><td rowspan=1 colspan=1>0.244</td></tr><tr><td rowspan=1 colspan=1>FS = ±16</td><td rowspan=1 colspan=1>0.488</td></tr><tr><td rowspan=5 colspan=1>G_So</td><td rowspan=5 colspan=1>Angular rate sensitivity(2)</td><td rowspan=1 colspan=1>FS = ±125</td><td rowspan=5 colspan=1></td><td rowspan=1 colspan=1>4.375</td><td rowspan=5 colspan=1></td><td rowspan=5 colspan=1>mdps/LSB</td></tr><tr><td rowspan=1 colspan=1>FS = ±245</td><td rowspan=1 colspan=1>8.75</td></tr><tr><td rowspan=1 colspan=1>FS = ±500</td><td rowspan=1 colspan=1>17.50</td></tr><tr><td rowspan=1 colspan=1>FS = ±1000</td><td rowspan=1 colspan=1>35</td></tr><tr><td rowspan=1 colspan=1>FS = ±2000</td><td rowspan=1 colspan=1>70</td></tr><tr><td rowspan=1 colspan=1>G_S0%</td><td rowspan=1 colspan=1>Sensitivity tolerance(3)</td><td rowspan=1 colspan=1>at component level</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>%</td></tr><tr><td rowspan=1 colspan=1>LA_SoDr</td><td rowspan=1 colspan=1>Linear acceleration sensitivitychange vs. temperature(4)</td><td rowspan=1 colspan=1>from -40° to +85°</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±0.01</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>%1℃</td></tr><tr><td rowspan=1 colspan=1>G_SoDr</td><td rowspan=1 colspan=1>Angular rate sensitivity changevs. temperature(4)</td><td rowspan=1 colspan=1>from -40° to +85°</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±0.007</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>%1℃</td></tr><tr><td rowspan=1 colspan=1>LA_TyOff</td><td rowspan=1 colspan=1>Linear acceleration zero-g leveloffset accuracy(5)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mg</td></tr><tr><td rowspan=1 colspan=1>G_TyOff</td><td rowspan=1 colspan=1>Angular rate zero-rate leve|(5)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dps</td></tr><tr><td rowspan=1 colspan=1>LA_OffDr</td><td rowspan=1 colspan=1>Linear acceleration zero-g levelchange vs.temperature(4)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±0.1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mg/℃</td></tr><tr><td rowspan=1 colspan=1>G_OffDr</td><td rowspan=1 colspan=1>Angular rate typical zero-ratelevel change vs. temperature(4)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>±0.015</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>dps/℃</td></tr></table>

Table 3. Mechanical characteristics (continued)   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Test conditions</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.(1)</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Rn</td><td rowspan=1 colspan=1>Rate noise density in high-performance mode(6)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.8</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mdps/√Hz</td></tr><tr><td rowspan=1 colspan=1>RnRMS</td><td rowspan=1 colspan=1>Gyroscope RMS noise innormallow-power mode(7)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>75</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mdps</td></tr><tr><td rowspan=4 colspan=1>An</td><td rowspan=4 colspan=1>Acceleration noise densityinhigh-performance mode(8)</td><td rowspan=1 colspan=1>FS = ±2g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1></td><td rowspan=4 colspan=1>μg/√Hz</td></tr><tr><td rowspan=1 colspan=1>FS= +4g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FS =±8g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FS= ±16g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>130</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=4 colspan=1>RMS</td><td rowspan=4 colspan=1>Acceleration RMS noisein normallow-power mode(9)(10)</td><td rowspan=1 colspan=1>FS = ±2g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1></td><td rowspan=4 colspan=1>mg(RMS)</td></tr><tr><td rowspan=1 colspan=1>FS=+4g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.0</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FS= ±8g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2.4</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>FS= ±16g</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.0</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>LA_ODR</td><td rowspan=1 colspan=1>Linear acceleration output datarate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.6(11)12.52652104208416833166633326664</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>Hz</td></tr><tr><td rowspan=1 colspan=1>G_ODR</td><td rowspan=1 colspan=1>Angular rate output data rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>12.52652104208416833166633326664</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=3 colspan=1>Vst</td><td rowspan=1 colspan=1>Linear accelerationself-test output change(12(13)(14)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1700</td><td rowspan=1 colspan=1>mg</td></tr><tr><td rowspan=2 colspan=1>Angular rateself-test output change(15)(16)</td><td rowspan=1 colspan=1>FS = 245 dps</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>80</td><td rowspan=1 colspan=1>dps</td></tr><tr><td rowspan=1 colspan=1>FS = 2000 dps</td><td rowspan=1 colspan=1>150</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>700</td><td rowspan=1 colspan=1>dps</td></tr><tr><td rowspan=1 colspan=1>Top</td><td rowspan=1 colspan=1>Operating temperature range</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+85</td><td rowspan=1 colspan=1>C</td></tr></table>

1. Typical specifications are not guaranteed. 2. Sensitivity values after factory calibration test and trimming. 3. Subject to change.

4. Measurements are performed in a uniform temperature setup and they are based on characterization data in a limited number of samples. Not measured during final test for production.

5. Values after factory calibration test and trimming.

6. Gyroscope rate noise density in high-performance mode is independent of the ODR and FS setting.

7. Gyroscope RMS noise in normal/low-power mode is independent of the ODR and FS setting.

8. Accelerometer noise density in high-performance mode is independent of the ODR.

9. Accelerometer RMS noise in normal/low-power mode is independent of the ODR.

10. Noise RMS related to BW = ODR /2 (for ODR /9, typ value can be calculated by Typ \*0.6).

11. This ODR is available when accelerometer is in low-power mode.

12. The sign of the linear acceleration self-test output change is defined by the STx_XL bits in CTRL5_C (14h), Table 65 for all axes.

13. The linear acceleration self-test output change is defined with the device in stationary condition as the absolute value of: OUTPUT[LSb] (self-test enabled) - OUTPUT[LSb] (self-test disabled). 1LSb = 0.061 mg at ±2 g full scale.

14. Accelerometer self-test limits are full-scale independent.

15. The sign of the angular rate self-test output change is defined by the STx_G bits in CTRL5_C (14h), Table 64 for all axes.

16. The angular rate self-test output change is defined with the device in stationary condition as the absolute value of: OUTPUT[LSb] (self-test enabled) - OUTPUT[LSb] (self-test disabled). 1LSb = 70 mdps at ±2000 dps full scale.

# 4.2 Electrical characteristics

@ Vdd = 1.8 V, T = 25 °C unless otherwise noted.

Table 4. Electrical characteristics   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Test conditions</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.(1)</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Vdd</td><td rowspan=1 colspan=1>Supply voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.71</td><td rowspan=1 colspan=1>1.8</td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Vdd_10</td><td rowspan=1 colspan=1>Power supply for I/O</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.62</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3.6</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>IddHP</td><td rowspan=1 colspan=1>Gyroscope and accelerometercurrent consumption in high-performance mode</td><td rowspan=1 colspan=1>ODR = 1.6 kHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.65</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>IddNM</td><td rowspan=1 colspan=1>Gyroscope and accelerometercurrent consumptionin normal mode</td><td rowspan=1 colspan=1>ODR= 208 Hz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.45</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>IddLP</td><td rowspan=1 colspan=1>Gyroscope and accelerometercurrent consumptionin low-power mode</td><td rowspan=1 colspan=1>ODR = 52 Hz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.29</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>mA</td></tr><tr><td rowspan=1 colspan=1>LA_IddHP</td><td rowspan=1 colspan=1>Accelerometer currentconsumptionin high-performance mode</td><td rowspan=1 colspan=1>ODR &lt; 1.6 kHzODR≥ 1.6 kHz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>150160</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>LA_IddNM</td><td rowspan=1 colspan=1>Accelerometer currentconsumption in normal mode</td><td rowspan=1 colspan=1>ODR = 208 Hz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>LA_IddLM</td><td rowspan=1 colspan=1>Accelerometer currentconsumption in low-power mode</td><td rowspan=1 colspan=1>ODR = 52 HzODR = 12.5 HzODR = 1.6 Hz</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>2594.5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>IddPD</td><td rowspan=1 colspan=1>Gyroscope and accelerometercurrent consumption duringpower-down</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>μA</td></tr><tr><td rowspan=1 colspan=1>Ton</td><td rowspan=1 colspan=1>Turn-on time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ms</td></tr><tr><td rowspan=1 colspan=1>V\H</td><td rowspan=1 colspan=1>Digital high-level input voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.7 *VDD_IO</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VL</td><td rowspan=1 colspan=1>Digital low-level input voltage</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.3 *VDD_IO</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VOH</td><td rowspan=1 colspan=1>High-level output voltage</td><td rowspan=1 colspan=1>1OH = 4 mA (2)</td><td rowspan=1 colspan=1>VDD_O - 0.2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>VOL</td><td rowspan=1 colspan=1>Low-level output voltage</td><td rowspan=1 colspan=1>10L = 4 mA (2)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.2</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>Top</td><td rowspan=1 colspan=1>Operating temperature range</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+85</td><td rowspan=1 colspan=1>C</td></tr></table>

1. Typical specifications are not guaranteed. 2. 4 mA is the maximum driving capability, i.e. the maximum DC current that can be sourced/sunk by the digital pad in order to guarantee the correct digital output voltage levels VOH and VOL.

# 4.3 Temperature sensor characteristics

@ Vdd = 1.8 V, T = 25 °C unless otherwise noted.

Table 5. Temperature sensor characteristics   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Test condition</td><td rowspan=1 colspan=1>Min.</td><td rowspan=1 colspan=1>Typ.(1)</td><td rowspan=1 colspan=1>Max.</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>TODR(2)</td><td rowspan=1 colspan=1>Temperature refresh rate</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>52</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>$Hz$</td></tr><tr><td rowspan=1 colspan=1>Tofff</td><td rowspan=1 colspan=1>Temperatur offset(3)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-15</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+15</td><td rowspan=1 colspan=1>℃</td></tr><tr><td rowspan=1 colspan=1>TSen</td><td rowspan=1 colspan=1>Temperature sensitivity</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>256</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LSB/C</td></tr><tr><td rowspan=1 colspan=1>TST</td><td rowspan=1 colspan=1>Temperature stabilization time(4)</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>500</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>T_ADC_res</td><td rowspan=1 colspan=1>Temperature ADC resolution</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>bit</td></tr><tr><td rowspan=1 colspan=1>Top</td><td rowspan=1 colspan=1>Operating temperature range</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>-40</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>+85</td><td rowspan=1 colspan=1>C$</td></tr></table>

1. Typical specifications are not guaranteed. 2. When the accelerometer is in Low-Power mode and the gyroscope part is turned off, the TODR value is equal to the accelerometer ODR. 3. The output of the temperature sensor is 0 LSB (typ.) at 25 °C. 4. Time from power ON bit to valid data based on characterization data.

# 4.4 Communication interface characteristics

# 4.4.1 SPI - serial peripheral interface

Subject to general operating conditions for Vdd and Top.

Table 6. SPI slave timing values   

<table><tr><td rowspan=2 colspan=1>Symbol</td><td rowspan=2 colspan=1>Parameter</td><td rowspan=1 colspan=2>Value(1)</td><td rowspan=2 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>tc(SPC)</td><td rowspan=1 colspan=1>SPI clock cycle</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>fc(sPC)</td><td rowspan=1 colspan=1>SPI clock frequency</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>MHz</td></tr><tr><td rowspan=1 colspan=1>tsu(CS)</td><td rowspan=1 colspan=1>CS setup time</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=7 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>th(CS)</td><td rowspan=1 colspan=1>CS hold time</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tsu(S1)</td><td rowspan=1 colspan=1>SDI input setup time</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>th(s1)</td><td rowspan=1 colspan=1>SDIl input hold time</td><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tv(So)</td><td rowspan=1 colspan=1>SDO valid output time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>50</td></tr><tr><td rowspan=1 colspan=1>th(so)</td><td rowspan=1 colspan=1>SDO output hold time</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tdis(SO)</td><td rowspan=1 colspan=1>SDO output disable time</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>50</td></tr></table>

1. Values are guaranteed at 10 MHz clock frequency for SPI with both 4 and 3 wires, based on characterization results, not tested in production

![](images/dc18d2ff314d4a18dfe8558b1058866e63f773e88b332a3161576dcf008204c4.jpg)  
Figure 3. SPI slave timing diagram

Measurement points are done at 0.2·Vdd_IO and 0.8·Vdd_IO, for both input and output ports.

# 4.4.2 I2C - inter-IC control interface

Subject to general operating conditions for Vdd and Top.

![](images/a362a50f743de545103021c07c64b9b3a789191511557841708c205bdee8df15.jpg)  
Figure 4. I2C timing diagram

# 4.4.2.1 I2C slave

Table 7. I2C slave timing values   

<table><tr><td rowspan=2 colspan=1>Symbol</td><td rowspan=2 colspan=1>Parameter</td><td rowspan=1 colspan=2> |²C standard mode(1)</td><td rowspan=1 colspan=2>|²C fast mode(1)</td><td rowspan=2 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td><td rowspan=1 colspan=1>Min</td><td rowspan=1 colspan=1>Max</td></tr><tr><td rowspan=1 colspan=1>f(SCL)</td><td rowspan=1 colspan=1>SCL clock frequency</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>400</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>tw(SCLL)</td><td rowspan=1 colspan=1>SCL clock low time</td><td rowspan=1 colspan=1>4.7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=1>uS</td></tr><tr><td rowspan=1 colspan=1>tw(SCLH)</td><td rowspan=1 colspan=1>SCL clock high time</td><td rowspan=1 colspan=1>4.0</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tsu(SDA)</td><td rowspan=1 colspan=1>SDA setup time</td><td rowspan=1 colspan=1>250</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>tn(SDA)</td><td rowspan=1 colspan=1>SDA data hold time</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>3.45</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>th(ST)</td><td rowspan=1 colspan=1>START condition hold time</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td><td rowspan=4 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>tsu(SR)</td><td rowspan=1 colspan=1>Repeated START conditionsetup time</td><td rowspan=1 colspan=1>4.7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tsu(SP)</td><td rowspan=1 colspan=1>STOP condition setup time</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>tw(SP:SR)</td><td rowspan=1 colspan=1>Bus free time between STOPand START condition</td><td rowspan=1 colspan=1>4.7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1></td></tr></table>

1. Data based on standard I2C protocol requirement, not tested in production.

e: Measurement points are done at 0.2·Vdd_IO and 0.8·Vdd_IO, for both ports.

# 4.4.2.2 I2C master

When in I2C Master Mode, an external sensor can be connected to LSM6DSM. LSM6DSM supports I2C Master - Fast Mode only.

Table 8. I2C master timing values   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>$²2c$Master</td><td rowspan=1 colspan=1>$1{c$Fast Mode(min)</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>f(sCL)</td><td rowspan=1 colspan=1>SCL clock frequency</td><td rowspan=1 colspan=1>116.3</td><td rowspan=1 colspan=1>0(400 kHz max)</td><td rowspan=1 colspan=1>kHz</td></tr><tr><td rowspan=1 colspan=1>tw(SCLL)</td><td rowspan=1 colspan=1>SCL clock low time</td><td rowspan=1 colspan=1>5.86</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>tw(SCLH)</td><td rowspan=1 colspan=1>SCL clock high time</td><td rowspan=1 colspan=1>2.74</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Data valid time</td><td rowspan=1 colspan=1>3.9</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SDA hold time</td><td rowspan=1 colspan=1>≥0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SDA setup time</td><td rowspan=1 colspan=1>≥100</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>ns</td></tr><tr><td rowspan=1 colspan=1>tsu(SR)</td><td rowspan=1 colspan=1>Repeated START condition setup time</td><td rowspan=1 colspan=1>1.56</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>μs</td></tr><tr><td rowspan=1 colspan=1>tsu(HD)</td><td rowspan=1 colspan=1>Repeated START condition hold time</td><td rowspan=1 colspan=1>1.56</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>uS</td></tr><tr><td rowspan=1 colspan=1>tsu(SP)</td><td rowspan=1 colspan=1>STOP condition setup time</td><td rowspan=1 colspan=1>2.73</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>μS</td></tr><tr><td rowspan=1 colspan=1>tw(SP:SR)</td><td rowspan=1 colspan=1>Bus free time between STOP and START condition</td><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>1.3</td><td rowspan=1 colspan=1>μS</td></tr></table>

# 4.5 Absolute maximum ratings

Stresses above those listed as “Absolute maximum ratings” may cause permanent damage to the device. This is a stress rating only and functional operation of the device under these conditions is not implied. Exposure to maximum rating conditions for extended periods may affect device reliability.

Table 9. Absolute maximum ratings   

<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Ratings</td><td rowspan=1 colspan=1>Maximum value</td><td rowspan=1 colspan=1>Unit</td></tr><tr><td rowspan=1 colspan=1>Vdd</td><td rowspan=1 colspan=1>Supply voltage</td><td rowspan=1 colspan=1>-0.3 to 4.8</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>TSTG</td><td rowspan=1 colspan=1>Storage temperature range</td><td rowspan=1 colspan=1>-40 to +125</td><td rowspan=1 colspan=1>C$</td></tr><tr><td rowspan=1 colspan=1>Sg</td><td rowspan=1 colspan=1>Acceleration g for 0.2 ms</td><td rowspan=1 colspan=1>10,000</td><td rowspan=1 colspan=1>g</td></tr><tr><td rowspan=1 colspan=1>ESD</td><td rowspan=1 colspan=1>Electrostatic discharge protection (HBM)</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>kV</td></tr><tr><td rowspan=1 colspan=1>Vin</td><td rowspan=1 colspan=1>Input voltage on any control pin(including CS, SCL/SPC, SDA/SDI/SDO, SDO/SAO)</td><td rowspan=1 colspan=1>0.3 to Vdd_1O +0.3</td><td rowspan=1 colspan=1>V</td></tr></table>

Note:

Supply voltage on any pin should never exceed 4.8 V.

This device is sensitive to mechanical shock, improper handling can cause permanent damage to the part. This device is sensitive to electrostatic discharge (ESD), improper handling can cause permanent damage to the part.

# 4.6 Terminology

# 4.6.1 Sensitivity

Linear acceleration sensitivity can be determined, for example, by applying 1 g acceleration to the device. Because the sensor can measure DC accelerations, this can be done easily by pointing the selected axis towards the ground, noting the output value, rotating the sensor 180 degrees (pointing towards the sky) and noting the output value again. By doing so, ±1 g acceleration is applied to the sensor. Subtracting the larger output value from the smaller one, and dividing the result by 2, leads to the actual sensitivity of the sensor. This value changes very little over temperature and over time. The sensitivity tolerance describes the range of sensitivities of a large number of sensors (see Table 3).

An angular rate gyroscope is a device that produces a positive-going digital output for counterclockwise rotation around the axis considered. Sensitivity describes the gain of the sensor and can be determined by applying a defined angular velocity to it. This value changes very little over temperature and time (see Table 3).

# 4.6.2 Zero-g and zero-rate level

Linear acceleration zero-g level offset (TyOff) describes the deviation of an actual output signal from the ideal output signal if no acceleration is present. A sensor in a steady state on a horizontal surface will measure 0 g on both the X-axis and Y-axis, whereas the Z-axis will measure 1 g. Ideally, the output is in the middle of the dynamic range of the sensor (content of OUT registers 00h, data expressed as 2’s complement number). A deviation from the ideal value in this case is called zero-g offset.

Offset is to some extent a result of stress to MEMS sensor and therefore the offset can slightly change after mounting the sensor onto a printed circuit board or exposing it to extensive mechanical stress. Offset changes little over temperature, see “Linear acceleration zero-g level change vs. temperature” in Table 3. The zero-g level tolerance (TyOff) describes the standard deviation of the range of zero-g levels of a group of sensors.

Zero-rate level describes the actual output signal if there is no angular rate present. The zero-rate level of precise MEMS sensors is, to some extent, a result of stress to the sensor and therefore the zero-rate level can slightly change after mounting the sensor onto a printed circuit board or after exposing it to extensive mechanical stress. This value changes very little over temperature and time (see Table 3).

# Functionality

# 5.1 Operating modes

In the LSM6DSM, the accelerometer and the gyroscope can be turned on/off independently of each other and are allowed to have different ODRs and power modes.

The LSM6DSM has three operating modes available:

 only accelerometer active and gyroscope in power-down  only gyroscope active and accelerometer in power-down  both accelerometer and gyroscope sensors active with independent ODR

The accelerometer is activated from power-down by writing ODR_XL[3:0] in CTRL1_XL (10h) while the gyroscope is activated from power-down by writing ODR_G[3:0] in CTRL2_G (11h). For combo-mode the ODRs are totally independent.

# 5.2 Gyroscope power modes

In the LSM6DSM, the gyroscope can be configured in four different operating modes: power-down, low-power, normal mode and high-performance mode. The operating mode selected depends on the value of the G_HM_MODE bit in CTRL7_G (16h). If G_HM_MODE is set to '0', high-performance mode is valid for all ODRs (from 12.5 Hz up to 6.66 kHz).

To enable the low-power and normal mode, the G_HM_MODE bit has to be set to '1'. Lowpower mode is available for lower ODRs (12.5, 26, 52 Hz) while normal mode is available for ODRs equal to 104 and 208 Hz.

# 5.3 Accelerometer power modes

In the LSM6DSM, the accelerometer can be configured in four different operating modes: power-down, low-power, normal mode and high-performance mode. The operating mode selected depends on the value of the XL_HM_MODE bit in CTRL6_C (15h). If XL_HM_MODE is set to '0', high-performance mode is valid for all ODRs (from 12.5 Hz up to 6.66 kHz).

To enable the low-power and normal mode, the XL_HM_MODE bit has to be set to '1'. Lowpower mode is available for lower ODRs (1.6, 12.5, 26, 52 Hz) while normal mode is available for ODRs equal to 104 and 208 Hz.

# 5.4 Block diagram of filters

![](images/6fdfe0e18a0493f102803316143b9e917812b772b8fc6f1369f96bd1e5f100e7.jpg)  
Figure 5. Block diagram of filters

# 5.4.1 Block diagrams of the gyroscope filters

In the LSM6DSM, the gyroscope filtering chain depends on the mode configuration:

1. Mode 1 (for User Interface (UI) and Electronic Image Stabilization (EIS) functionality through primary interface) and Mode 2

![](images/bed61d10c7b6e54e751290cdea917a98342653caf352e7444007daea2db15826.jpg)  
Figure 6. Gyroscope digital chain - Mode 1 (UI/EIS) and Mode 2

In this configuration, the gyroscope ODR is selectable from 12.5 Hz up to 6.66 kHz. A lowpass filter (LPF1) is available if the auxiliary SPI is disabled, for more details about the filter characteristics see Table 69: Gyroscope LPF1 bandwidth selection.

Data can be acquired from the output registers and FIFO over the primary I2C/SPI interface. 2. Mode 3 / Mode 4 (for OIS and EIS functionality)

![](images/60b2ab4def5f98e81dc41ee8143fa7859fac30f8256dc0d10b3ae602ed434bfb.jpg)  
Figure 7. Gyroscope digital chain - Mode 3 / Mode 4 (OIS/EIS)

# Note:

HP_EN_OIS is active to select HPF on the auxiliary SPI chain only if HPF is not already used in the primary interface.

In this configuration, there are two paths:

- the chain for User Interface (UI) where the ODR is selectable from 12.5 Hz up to 6.66 kHz

- the chain for OIS/EIS where the ODR is at 6.66 kHz and the LPF1 is available. For more details about the filter characteristics see Table 227: Gyroscope OIS chain LPF1 bandwidth selection.

# 5.4.2 Block diagrams of the accelerometer filters

In the LSM6DSM, the filtering chain for the accelerometer part is composed of the following:

 Analog filter (anti-aliasing)  Digital filter (LPF1)  Composite filter

Details of the block diagram appear in the following figure.

![](images/571ae7f64ae810dbd69d91b56761c7600f94690c95f811870515aa5d9be394ea.jpg)  
Figure 8. Accelerometer chain

The configuration of the digital filter can be set using the LPF1_BW_SEL bit in CTRL1_XL (10h) and the INPUT_COMPOSITE bit in CTRL8_XL (17h).

![](images/2811ee0c07c945c185df6fd37df03830e5cb78f4bf4b824a47aef48a78cef734.jpg)  
Figure 9. Accelerometer composite filter (for Modes 1/2 and Mode 3\*)

1. Pedometer, step detector and step counter, significant motion and tilt functions.

Note:

\* Mode 3 is available only if Mode4_EN = 0 and OIS_EN_SPI2 = 1 in CTRL1_OIS (70h).

![](images/46708855f59dc777dce5970950a5136a0c3648e4fa359cce09cc850823a00ee6.jpg)  
Figure 10. Accelerometer composite filter (Mode 4 only\*)

1. Pedometer, step detector and step counter, significant motion and tilt functions.

Note: \*Mode 4 is enabled when Mode4_EN = 1 and OIS_EN_SPI2 = 1 in CTRL1_OIS (70h).

# 5.5 FIFO

The presence of a FIFO allows consistent power saving for the system since the host processor does not need continuously poll data from the sensor, but it can wake up only when needed and burst the significant data out from the FIFO.

The LSM6DSM embeds 4 kbytes data FIFO to store the following data:

 gyroscope   
 accelerometer   
 external sensors   
 step counter and timestamp   
 temperature

Writing data in the FIFO can be configured to be triggered by the:

accelerometer/gyroscope data-ready signal; in which case the ODR must be lower than or equal to both the accelerometer and gyroscope ODRs;   
sensor hub data-ready signal;   
step detection signal.

In addition, each data can be stored at a decimated data rate compared to FIFO ODR and it is configurable by the user, setting the FIFO_CTRL3 (08h) and FIFO_CTRL4 (09h) registers. The available decimation factors are 2, 3, 4, 8, 16, 32.

The programmable FIFO threshold can be set in FIFO_CTRL1 (06h) and FIFO_CTRL2 (07h) using the FTH [10:0] bits.

To monitor the FIFO status, dedicated registers (FIFO_STATUS1 (3Ah), FIFO_STATUS2 (3Bh), FIFO_STATUS3 (3Ch), FIFO_STATUS4 (3Dh)) can be read to detect FIFO overrun events, FIFO full status, FIFO empty status, FIFO threshold status and the number of unread samples stored in the FIFO. To generate dedicated interrupts on the INT1 and INT2 pads of these status events, the configuration can be set in INT1_CTRL (0Dh) and INT2_CTRL (0Eh).

The FIFO buffer can be configured according to five different modes:

 Bypass mode   
 FIFO mode   
 Continuous mode   
 Continuous-to-FIFO mode   
 Bypass-to-continuous mode

Each mode is selected by the FIFO_MODE_[2:0] bits in the FIFO_CTRL5 (0Ah) register. To guarantee the correct acquisition of data during the switching into and out of FIFO mode, the first sample acquired must be discarded.

# 5.5.1 Bypass mode

In Bypass mode (FIFO_CTRL5 (0Ah) (FIFO_MODE_[2:0] = 000), the FIFO is not operational and it remains empty.

Bypass mode is also used to reset the FIFO when in FIFO mode.

# 5.5.2 FIFO mode

In FIFO mode (FIFO_CTRL5 (0Ah) (FIFO_MODE_[2:0] = 001) data from the output channels are stored in the FIFO until it is full.

To reset FIFO content, Bypass mode should be selected by writing FIFO_CTRL5 (0Ah) (FIFO_MODE_[2:0]) to '000' After this reset command, it is possible to restart FIFO mode by writing FIFO_CTRL5 (0Ah) (FIFO_MODE_[2:0]) to '001'.

FIFO buffer memorizes up to 4096 samples of 16 bits each but the depth of the FIFO can be resized by setting the FTH [10:0] bits in FIFO_CTRL1 (06h) and FIFO_CTRL2 (07h). If the STOP_ON_FTH bit in FIFO_CTRL4 (09h) is set to '1', FIFO depth is limited up to FTH [10:0] bits in FIFO_CTRL1 (06h) and FIFO_CTRL2 (07h).

# 5.5.3 Continuous mode

Continuous mode (FIFO_CTRL5 (0Ah) (FIFO_MODE_[2:0] = 110) provides a continuous FIFO update: as new data arrives, the older data is discarded.

A FIFO threshold flag FIFO_STATUS2 (3Bh)(FTH) is asserted when the number of unread samples in FIFO is greater than or equal to FIFO_CTRL1 (06h) and FIFO_CTRL2 (07h)(FTH [10:0]).

It is possible to route FIFO_STATUS2 (3Bh) (FTH) to the INT1 pin by writing in register INT1_CTRL (0Dh) (INT1_FTH) = ‘1’ or to the INT2 pin by writing in register INT2_CTRL (0Eh) (INT2_FTH) = ‘1’.

A full-flag interrupt can be enabled, INT1_CTRL (0Dh) (INT_ FULL_FLAG) = '1', in order to indicate FIFO saturation and eventually read its content all at once.

If an overrun occurs, at least one of the oldest samples in FIFO has been overwritten and the OVER_RUN flag in FIFO_STATUS2 (3Bh) is asserted.

In order to empty the FIFO before it is full, it is also possible to pull from FIFO the number of unread samples available in FIFO_STATUS1 (3Ah) and FIFO_STATUS2 (3Bh) (DIFF_FIFO [10:0]).

# 5.5.4 Continuous-to-FIFO mode

In Continuous-to-FIFO mode (FIFO_CTRL5 (0Ah) (FIFO_MODE_[2:0] = 011), FIFO behavior changes according to the trigger event detected in one of the following interrupt registers FUNC_SRC1 (53h), TAP_SRC (1Ch), WAKE_UP_SRC (1Bh) and D6D_SRC (1Dh).

When the selected trigger bit is equal to '1', FIFO operates in FIFO mode.

When the selected trigger bit is equal to '0', FIFO operates in Continuous mode.

# 5.5.5 Bypass-to-Continuous mode

In Bypass-to-Continuous mode (FIFO_CTRL5 (0Ah) (FIFO_MODE_[2:0] = '100'), data measurement storage inside FIFO operates in Continuous mode when selected triggers in one of the following interrupt registers FUNC_SRC1 (53h), TAP_SRC (1Ch), WAKE_UP_SRC (1Bh) and D6D_SRC (1Dh) are equal to '1', otherwise FIFO content is reset (Bypass mode).

# 5.5.6 FIFO reading procedure

The data stored in FIFO are accessible from dedicated registers (FIFO_DATA_OUT_L (3Eh) and FIFO_DATA_OUT_H (3Fh)) and each FIFO sample is composed of 16 bits.

All FIFO status registers (FIFO_STATUS1 (3Ah), FIFO_STATUS2 (3Bh), FIFO_STATUS3 (3Ch), FIFO_STATUS4 (3Dh)) can be read at the start of a reading operation, minimizing the intervention of the application processor.

Saving data in the FIFO buffer is organized in four FIFO data sets consisting of 6 bytes each:

The 1st FIFO data set is reserved for gyroscope data;

The 2nd FIFO data set is reserved for accelerometer data;

The 3rd FIFO data set is reserved for the external sensor data stored in the registers from SENSORHUB1_REG (2Eh) to SENSORHUB6_REG (33h);

The 4th FIFO data set can be alternately associated to the external sensor data stored in the registers from SENSORHUB7_REG (34h) to SENSORHUB12_REG (39h), to the step counter and timestamp info, or to the temperature sensor data.

# 6 Digital interfaces

6.1

# I2C/SPI interface

The registers embedded inside the LSM6DSM may be accessed through both the I2C and SPI serial interfaces. The latter may be SW configured to operate either in 3-wire or 4-wire interface mode.

The serial interfaces are mapped onto the same pins. To select/exploit the I2C interface, the CS line must be tied high (i.e connected to Vdd_IO).

Table 10. Serial interface pin description   

<table><tr><td rowspan=1 colspan=1>Pin name</td><td rowspan=1 colspan=1>Pin description</td></tr><tr><td rowspan=1 colspan=1>CS</td><td rowspan=1 colspan=1>SPl enable12C/SPl mode selection (1: SPl idle mode /I²2C communication enabled;0: SPI communication mode / I2C disabled)</td></tr><tr><td rowspan=1 colspan=1>SCL/SPC</td><td rowspan=1 colspan=1>|2C Serial Clock (SCL)SPI Serial Port Clock (SPC)</td></tr><tr><td rowspan=1 colspan=1>SDA/SDI/SDO</td><td rowspan=1 colspan=1>|2C Serial Data (SDA)SPI Serial Data Input (SDI)3-wire Interface Serial Data Output (SDO)</td></tr><tr><td rowspan=1 colspan=1>SDO/SAO</td><td rowspan=1 colspan=1>SPI Serial Data Output (SDO)12C less significant bit of the device address</td></tr></table>

# 6.2 Master I2C

If the LSM6DSM is configured in Mode 2, a master I2C line is available. The master serial interface is mapped in the following dedicated pins.

Table 11. Master I2C pin details   

<table><tr><td rowspan=1 colspan=1>Pin name</td><td rowspan=1 colspan=1>Pin description</td></tr><tr><td rowspan=1 colspan=1>MSCL</td><td rowspan=1 colspan=1>|2C serial clock master</td></tr><tr><td rowspan=1 colspan=1>MSDA</td><td rowspan=1 colspan=1>12C serial data master</td></tr><tr><td rowspan=1 colspan=1>MDRDY</td><td rowspan=1 colspan=1>12C master external synchronization signal</td></tr></table>

# 6.3 Auxiliary SPI

If LSM6DSM is configured in Mode 3, the auxiliary SPI is available. The auxiliary SPI interface is mapped in the following dedicated pins.

Table 12. Auxiliary SPI pin details   

<table><tr><td rowspan=1 colspan=1>Pin name</td><td rowspan=1 colspan=1>Pin description</td></tr><tr><td rowspan=1 colspan=1>OCS_Aux</td><td rowspan=1 colspan=1>Auxiliary SPI 3/4-wire enable</td></tr><tr><td rowspan=1 colspan=1>SDx</td><td rowspan=1 colspan=1>Auxiliary SPI 3/4-wire data input (SDI_Aux) and SPI 3-wire data output (SDO_Aux)</td></tr><tr><td rowspan=1 colspan=1>SCx$</td><td rowspan=1 colspan=1>Auxiliary SPI 3/4-wire interface serial port clock</td></tr><tr><td rowspan=1 colspan=1>SDO_Aux</td><td rowspan=1 colspan=1>SPI serial data</td></tr></table>

# 6.4 I2C serial interface

The LSM6DSM I2C is a bus slave. The I2C is employed to write the data to the registers, whose content can also be read back.

The relevant I2C terminology is provided in the table below.

Table 13. I2C terminology   

<table><tr><td rowspan=1 colspan=1>Term</td><td rowspan=1 colspan=1>Description</td></tr><tr><td rowspan=1 colspan=1>Transmiter</td><td rowspan=1 colspan=1>The device which sends data to the bus</td></tr><tr><td rowspan=1 colspan=1>Receiver</td><td rowspan=1 colspan=1>The device which receives data from the bus</td></tr><tr><td rowspan=1 colspan=1>Master</td><td rowspan=1 colspan=1>The device which initiates a transfer, generates clock signals and terminates atransfer</td></tr><tr><td rowspan=1 colspan=1>Slave</td><td rowspan=1 colspan=1>The device addressed by the master</td></tr></table>

There are two signals associated with the I2C bus: the serial clock line (SCL) and the Serial DAta line (SDA). The latter is a bidirectional line used for sending and receiving the data to/from the interface. Both the lines must be connected to Vdd_IO through external pull-up resistors. When the bus is free, both the lines are high.

The I2C interface is implemeted with fast mode (400 kHz) I2C standards as well as with the standard mode.

In order to disable the I2C block, (I2C_disable) = 1 must be written in CTRL4_C (13h).

# 6.4.1 I2C operation

The transaction on the bus is started through a START (ST) signal. A START condition is defined as a HIGH to LOW transition on the data line while the SCL line is held HIGH. After this has been transmitted by the master, the bus is considered busy. The next byte of data transmitted after the start condition contains the address of the slave in the first 7 bits and the eighth bit tells whether the master is receiving data from the slave or transmitting data to the slave. When an address is sent, each device in the system compares the first seven bits after a start condition with its address. If they match, the device considers itself addressed by the master.

The Slave ADdress (SAD) associated to the LSM6DSM is 110101xb. The SDO/SA0 pin can be used to modify the less significant bit of the device address. If the SDO/SA0 pin is connected to the supply voltage, LSb is ‘1’ (address 1101011b); else if the SDO/SA0 pin is connected to ground, the LSb value is ‘0’ (address 1101010b). This solution permits to connect and address two different inertial modules to the same I2C bus.

Data transfer with acknowledge is mandatory. The transmitter must release the SDA line during the acknowledge pulse. The receiver must then pull the data line LOW so that it remains stable low during the HIGH period of the acknowledge clock pulse. A receiver which has been addressed is obliged to generate an acknowledge after each byte of data received.

The I2C embedded inside the LSM6DSM behaves like a slave device and the following protocol must be adhered to. After the start condition (ST) a slave address is sent, once a slave acknowledge (SAK) has been returned, an 8-bit sub-address (SUB) is transmitted. The increment of the address is configured by the CTRL3_C (12h) (IF_INC).

The slave address is completed with a Read/Write bit. If the bit is ‘1’ (Read), a repeated START (SR) condition must be issued after the two sub-address bytes; if the bit is ‘0’ (Write) the master will transmit to the slave with direction unchanged. Table 14 explains how the SAD+Read/Write bit pattern is composed, listing all the possible configurations.

Table 14. SAD+Read/Write patterns   

<table><tr><td rowspan=1 colspan=1>Command</td><td rowspan=1 colspan=1>SAD[6:1]</td><td rowspan=1 colspan=1>SAD[0] = SA0</td><td rowspan=1 colspan=1>R/W</td><td rowspan=1 colspan=1>SAD+R/W</td></tr><tr><td rowspan=1 colspan=1>Read</td><td rowspan=1 colspan=1>110101</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>11010101 (D5h)</td></tr><tr><td rowspan=1 colspan=1>Write</td><td rowspan=1 colspan=1>110101</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>11010100 (D4h)</td></tr><tr><td rowspan=1 colspan=1>Read</td><td rowspan=1 colspan=1>110101</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1101011 (D7h)</td></tr><tr><td rowspan=1 colspan=1>Write</td><td rowspan=1 colspan=1>110101</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>11010110 (D6h)</td></tr></table>

Table 15. Transfer when master is writing one byte to slave   

<table><tr><td rowspan=1 colspan=1>Master</td><td rowspan=1 colspan=1>ST</td><td rowspan=1 colspan=1>SAD + W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SUB</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SP</td></tr><tr><td rowspan=1 colspan=1>Slave</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td></tr></table>

# Table 16. Transfer when master is writing multiple bytes to slave

<table><tr><td rowspan=1 colspan=1>Master</td><td rowspan=1 colspan=1>ST</td><td rowspan=1 colspan=1>SAD + W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SUB</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SP</td></tr><tr><td rowspan=1 colspan=1>Slave</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td></tr></table>

# Table 17. Transfer when master is receiving (reading) one byte of data from slave

<table><tr><td rowspan=1 colspan=1>Master</td><td rowspan=1 colspan=1>ST</td><td rowspan=1 colspan=1>SAD + W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SUB</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SR</td><td rowspan=1 colspan=1>SAD + R</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>NMAK</td><td rowspan=1 colspan=1>SP</td></tr><tr><td rowspan=1 colspan=1>Slave</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

Table 18. Transfer when master is receiving (reading) multiple bytes of data from slave   

<table><tr><td rowspan=1 colspan=1>Master</td><td rowspan=1 colspan=1>ST</td><td rowspan=1 colspan=1>SAD+W</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SUB</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SR</td><td rowspan=1 colspan=1>SAD+R</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>MAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>NMAK</td><td rowspan=1 colspan=1>SP</td></tr><tr><td rowspan=1 colspan=1>Slave</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>SAK</td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DATA</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

Data are transmitted in byte format (DATA). Each data transfer contains 8 bits. The number of bytes transferred per transfer is unlimited. Data is transferred with the Most Significant bit (MSb) first. If a receiver can’t receive another complete byte of data until it has performed some other function, it can hold the clock line, SCL LOW to force the transmitter into a wait state. Data transfer only continues when the receiver is ready for another byte and releases the data line. If a slave receiver doesn’t acknowledge the slave address (i.e. it is not able to receive because it is performing some real-time function) the data line must be left HIGH by the slave. The master can then abort the transfer. A LOW to HIGH transition on the SDA line while the SCL line is HIGH is defined as a STOP condition. Each data transfer must be terminated by the generation of a STOP (SP) condition.

In the presented communication format MAK is Master acknowledge and NMAK is No Master Acknowledge.

# 6.5 SPI bus interface

The LSM6DSM SPI is a bus slave. The SPI allows writing and reading the registers of the device.

The serial interface communicates to the application using 4 wires: CS, SPC, SDI and SDO.

![](images/0e4db60da5993ff51c24eccbdcb2610c2e8f10392e2315642706b35fe7e029a2.jpg)  
Figure 11. Read and write protocol

CS is the serial port enable and it is controlled by the SPI master. It goes low at the start of the transmission and goes back high at the end. SPC is the serial port clock and it is controlled by the SPI master. It is stopped high when CS is high (no transmission). SDI and SDO are, respectively, the serial port data input and output. Those lines are driven at the falling edge of SPC and should be captured at the rising edge of SPC.

Both the read register and write register commands are completed in 16 clock pulses or in multiples of 8 in case of multiple read/write bytes. Bit duration is the time between two falling edges of SPC. The first bit (bit 0) starts at the first falling edge of SPC after the falling edge of CS while the last bit (bit 15, bit 23, ...) starts at the last falling edge of SPC just before the rising edge of CS.

bit 0: RW bit. When 0, the data DI(7:0) is written into the device. When 1, the data DO(7:0) from the device is read. In latter case, the chip will drive SDO at the start of bit 8.

bit 1-7: address AD(6:0). This is the address field of the indexed register.

bit 8-15: data DI(7:0) (write mode). This is the data that is written into the device (MSb first).

bit 8-15: data DO(7:0) (read mode). This is the data that is read from the device (MSb first).

In multiple read/write commands further blocks of 8 clock periods will be added. When the CTRL3_C (12h) (IF_INC) bit is ‘0’, the address used to read/write data remains the same for every block. When the CTRL3_C (12h) (IF_INC) bit is ‘1’, the address used to read/write data is increased at every block.

The function and the behavior of SDI and SDO remain unchanged.

# 6.5.1 SPI read

![](images/42f8c463c07d6cb04bb57b33c8981345abc94dbb5fba02ec262f0aff6fbfc8b6.jpg)  
Figure 12. SPI read protocol

The SPI Read command is performed with 16 clock pulses. A multiple byte read command is performed by adding blocks of 8 clock pulses to the previous one.

bit 0: READ bit. The value is 1.

bit 1-7: address AD(6:0). This is the address field of the indexed register.

bit 8-15: data DO(7:0) (read mode). This is the data that will be read from the device (MSb first).

bit 16-...: data DO(...-8). Further data in multiple byte reads.

![](images/6999a4547ba6c2377717b852faa1ef320cf77e19fa479eaa836561291984c4dc.jpg)  
Figure 13. Multiple byte SPI read protocol (2-byte example)

# 6.5.2 SPI write

![](images/86bab915a748e1c440d9df0b6219e70838df0d1ef1659e30bcea86e29fde4b43.jpg)  
Figure 14. SPI write protocol

The SPI Write command is performed with 16 clock pulses. A multiple byte write command is performed by adding blocks of 8 clock pulses to the previous one.

bit 0: WRITE bit. The value is 0.

bit 1 -7: address AD(6:0). This is the address field of the indexed register.

bit 8-15: data DI(7:0) (write mode). This is the data that is written inside the device (MSb first).

bit 16-... : data DI(...-8). Further data in multiple byte writes.

![](images/b939e4ac889453474e511911d5d21aa8d72925c3c17e848a0e5d7db71f10bfbf.jpg)  
Figure 15. Multiple byte SPI write protocol (2-byte example)

# 6.5.3 SPI read in 3-wire mode

A 3-wire mode is entered by setting the CTRL3_C (12h) (SIM) bit equal to ‘1’ (SPI serial interface mode selection).

![](images/800b27c78d9932bfbc2683c442e22f475939c27d93b0f98836e4d2d399a3c4db.jpg)  
Figure 16. SPI read protocol in 3-wire mode

The SPI read command is performed with 16 clock pulses:

bit 0: READ bit. The value is 1.

bit 1-7: address AD(6:0). This is the address field of the indexed register.

bit 8-15: data DO(7:0) (read mode). This is the data that is read from the device (MSb first).   
A multiple read command is also available in 3-wire mode.

# 7 Application hints

# 7.1 LSM6DSM electrical connections in Mode 1

![](images/f1532b85969ec61f9674d0dd40b9511d7534570a8b1f27e18f58ff49ced84e2f.jpg)  
Figure 17. LSM6DSM electrical connections in Mode 1

1. Leave pin electrically unconnected and soldered to PCB.

The device core is supplied through the Vdd line. Power supply decoupling capacitors (C1, C2 = 100 nF ceramic) should be placed as near as possible to the supply pin of the device (common design practice).

The functionality of the device and the measured acceleration/angular rate data is selectable and accessible through the SPI/I2C interface.

The functions, the threshold and the timing of the two interrupt pins for each sensor can be completely programmed by the user through the SPI/I2C interface.

# 7.2 LSM6DSM electrical connections in Mode 2

![](images/cf1fa1cdef03ebe3d3fb91a146af9b28cddd63fada41328d31b74d6603fb9692.jpg)  
Figure 18. LSM6DSM electrical connections in Mode 2

1. Leave pin electrically unconnected and soldered to PCB.

The device core is supplied through the Vdd line. Power supply decoupling capacitors (C1, C2 = 100 nF ceramic) should be placed as near as possible to the supply pin of the device (common design practice).

The functionality of the device and the measured acceleration/angular rate data is selectable and accessible through the SPI/I2C interface.

The functions, the threshold and the timing of the two interrupt pins for each sensor can be completely programmed by the user through the SPI/I2C interface.

# 7.3 LSM6DSM electrical connections in Mode 3 and Mode 4

Figure 19. LSM6DSM electrical connections in Mode 3 and Mode 4 (auxiliary 3-wire SPI)

![](images/89845538b3e7e689ff5144eeae8e876d1c74111cb61442ee50e1e905cb5bae80.jpg)

RQDOVRZKLOHWKH2,6V\VWHPLVRII