import os

name = os.environ['COMPUTERNAME']

bitlocker = os.popen("%windir%\sysnative\manage-bde -protectors -get C: -type recoverypassword").read()
f= open(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Bitlocker.txt","w+")
f.write(bitlocker)
numpass = bitlocker[220:258]
os.system(f"%windir%\sysnative\manage-bde -protectors -adbackup C: -id {numpass}")
