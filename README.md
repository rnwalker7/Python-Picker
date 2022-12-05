# Python-Picker

Created in response to 81 TRG requirement to restart NCOD; I created this simple Python script to randomly pick two names to cover shifts for NCOD. For now, the only functionality is to run the picker, and is being converted to PowerShell.

## Usage

1.  Get current recall rosters
2.  Change extension of rosters to .ZIP
3.  Unzip the rosters (this gives you access to the underlying XML files
4.  For ease of use, rename the unzipped folders UUA, UUB, UUC
5.  Run "pick-names.py"
6.  Run "set-rotation.py"
7.  Profit! (hopefully)
