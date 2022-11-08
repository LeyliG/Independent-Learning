Practice solutions following the LPHW book by Zed A. Shaw



# PowerShell Terminal

Learn how to make a directory/folder in the PowerShell (Terminal) :
  New-Item "C:\Users\lga\Python_learning" -Type Directory
  *mkdir* Python_learning

Learn how to change into a directory in the PowerShell (Terminal) :
  Set-Location -Path "C:\Users\lga\Python_learning"
  *cd* Python_learning

List the directory to see your files :
  Inside the directory: 
  - Get-ChildItem 
  - *dir*

  Outside the directory: Get-ChildItem D:\Temp\
