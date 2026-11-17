---
titolo: IPhone 15 Pro Stuck at 1 Percent Charging and No Battery Data 0xa1 Panic Log
  Code
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_15_Pro_Stuck_at_1_Percent_Charging_and_No_Battery_Data_0xa1_Panic_Log_Code
cronologia: https://repair.wiki/w/IPhone_15_Pro_Stuck_at_1_Percent_Charging_and_No_Battery_Data_0xa1_Panic_Log_Code?action=history
revisione: '2025-06-04T21:18:23Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPhone 15 Pro Stuck at 1 Percent Charging and No Battery Data 0xa1 Panic Log Code

> Fonte: [IPhone 15 Pro Stuck at 1 Percent Charging and No Battery Data 0xa1 Panic Log Code — repair.wiki](https://repair.wiki/w/IPhone_15_Pro_Stuck_at_1_Percent_Charging_and_No_Battery_Data_0xa1_Panic_Log_Code), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
iPhone 15 Pro that is not charging. It says it is at 1% battery level & doesn't go up. The USB meter is constantly fluctuating. When you plug in the charging cable, it pops up as 0% remaining. 

It also restarts every 3 minutes due to lack of battery data. The panic log error will be 0xa1.

Even with a new battery and charging port installed, the symptoms will remain the same.

This tends to happen when the phone gets water damaged & fries the PMIC.

## Symptoms
- Not Charging at 9V
- USB Meter is fluctuating 
- Always reads battery at 1%
- When plugging in the charger, it says 0% remaining
- Restarts every 3 minutes
- Panic Log Error code is 0xa1 (Figure 1)

## Solution
### Diagnostic Steps
1. Test with known good parts. Specifically battery & charging port
1. Check the battery connector for damage. The pins should all be straight & not bent, warped or missing
1. Check the connector **Diode Mode Values**: 
  1. ZXW Pin 1: 0.439V  
    1. I2C2_SMC_CHARGER_BI_GG_SDA_1V8  
  1. ZXW Pin 2: 0.548  
    1. I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN  
  1. ZXW Pin 5: OL  
    1. ANALOG_BATT_VCELL_NEG_CONN  
  1. ZXW Pin 6: 0.505V  
    1. ANALOG_BATT_VCELL_POS_CONN 
1. Check the **voltage** of the battery connector pins, by connecting the board only, with charging port flex. Then plug in the charger to it & measure each pin:  
  1. ZXW Pin 1: 1.5V  
    1. I2C2_SMC_CHARGER_BI_GG_SDA_1V8  
  1. ZXW Pin 2: 1.8V  
    1. I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN  
  1. ZXW Pin 5: 0.6V  
    1. ANALOG_BATT_VCELL_NEG_CONN  
  1. ZXW Pin 6: 0.6V  
    1. eANALOG_BATT_VCELL_POS_CONN

### Repair Steps
If you have a bad diode mode reading or low voltage on the battery connector, it's likely PMIC that has failed.
