Practice solutions following the LPHW book by Zed A. Shaw



# PowerShell Terminal

Learn how to make a directory/folder in the PowerShell (Terminal) :
  - New-Item "C:\Users\lga\Python_learning" -Type Directory
  - *mkdir* Python_learning

Learn how to change into a directory in the PowerShell (Terminal) :
  - Set-Location -Path "C:\Users\lga\Python_learning"
  - *cd* Python_learning

List the directory to see your files :
  Inside the directory: 
  - Get-ChildItem 
  - *dir*

  Outside the directory: 
    *Get-ChildItem D:\Temp\*

Run select lines from a Python file:
  - To get the first 3 lines of the code: *Get-Content ex1.py | Select -First 3*
  - To skip first 2 lines: *Get-Content ex1.py | Select -Skip 2*
  - To get only the third line: *Get-Content ex1.py | Select -First 3 | Select -Last 1*
 
 
 
 # Tips
 
 ## Debugging
  - Reading code backwards is a trick to make your brain not attach meaning to each part of the code, and doing that makes you process each piece exactly. This catches errors and is a handy error-checking technique
 
 ## Documentation
