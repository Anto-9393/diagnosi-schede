---
titolo: How To Read and Write iPhone 16 Pro SPI EEPROM using CH341A
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Read_and_Write_iPhone_16_Pro_SPI_EEPROM_using_CH341A
cronologia: https://repair.wiki/w/How_To_Read_and_Write_iPhone_16_Pro_SPI_EEPROM_using_CH341A?action=history
revisione: '2025-12-15T13:49:11Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Read and Write iPhone 16 Pro SPI EEPROM using CH341A

> Fonte: [How To Read and Write iPhone 16 Pro SPI EEPROM using CH341A — repair.wiki](https://repair.wiki/w/How_To_Read_and_Write_iPhone_16_Pro_SPI_EEPROM_using_CH341A), CC BY-SA 3.0. Autori: vedi cronologia.

## Description
Some iPhone 16 Pro and 16 Pro Max devices can develop charging-related or USB-C communication issues where the ACE charging controller is electrically functional, but its EEPROM (SPI) data becomes corrupted. This commonly occurs after the use of faulty or aftermarket chargers, power surges, or unstable power delivery.

In these cases, replacing the ACE controller alone does not resolve the issue, because the ACE EEPROM stores critical configuration data required for proper USB-C negotiation and charging behavior. When this data is damaged, it must be read, corrected, rewritten or replace the EEPROM physically.

This guide documents how to access and modify ACE EEPROM data in-circuit on iPhone 16 Pro and Pro Max, avoiding the need to split the sandwich logic board.

## Symptoms
- Device does not charge via cable, but the port is confirmed good
- Intermittent or unstable charging detection
- Charging behavior changes depending on cable or power source
- Device does not charge even after replacing the ACE charging controller  ==

## Solution
- Replace ACE Charging controller
- Program a new ROM using CH341A programmer
- Charging will be restored 

### Diagnostic Steps
1. Visual Inspection
1. * Look for signs of corrosion/Look for shorts around the ACE Charging Controller IC and ROM area
1. * Check for burnt ROM chips or ACE Charging Controller
1. Voltage Testing
1. * Use USB-C power meter
1. * Plug in USB-C and check if iPhone negotiates proper voltage  ==

### Repair Steps
1. Disconnect all power from the board
1. Solder jumpers from CH341A to ACE SPI points
1. Connect CH341A to PC
1. Open CH341A Programmer
1. Press Detect
1. Click Read
1. Click Save. (Save at least two copies of the dump)
1. Read again and compare files for consistency

## Write / Restore Procedure
1. Click Open
1. Select your file and press open 
1. Click Program
1. Confirm verification passes with no errors

## After Programming
1. Disconnect CH341A
1. Remove jumper wires
1. Inspect pads for bridges
1. Reconnect battery
1. Power on device and confirm charging works.

## Why This Method Is Used
- Preserves customer data
- Avoids sandwich board separation
- Reduces mechanical and thermal risk
- Faster and safer EEPROM access
- Uses inexpensive, widely available tools
