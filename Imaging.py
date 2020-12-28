#Imports
import os
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import winreg


#Main Setup Class
class Setup:
    def corplaptop_setup():

        #Variables
        name = os.environ['COMPUTERNAME']
        agentInstall = Path("C:/Program Files (x86)/LANDesk/LDClient/2020.1 Corporate Agent.msi")
        inventoryScan = Path(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Inv.txt")
        patches = Path(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Patch.txt")
        pcName = Path(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}")
        bitlocker = Path(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Bitlocker.txt")
        systemUpdate = Path(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Update.txt")

        #Make Directory for Text files
        if pcName.is_dir():
            pass
        else:
            os.mkdir(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}")

        # Capture Serial
        serial = os.popen("wmic bios get serialnumber").read()
        f= open(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Serial.txt","w+")
        f.write(serial)
        f.close()

        #Bitlocker Start
        if bitlocker.is_file():
            pass
        else:
            os.system(r"%windir%\sysnative\manage-bde -on -RecoveryPassword C:")
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\RunOnce',0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(reg_key, 'Bitlocker', 0, winreg.REG_SZ, "\"\\\\nismith\\share\\Lenovo Setup\\Setup Files\\Bitlocker.exe\"")

        #Setup
        if agentInstall.is_file():
            pass
        else:
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/2020.1 Corporate Agent_with_status.exe"')

        if inventoryScan.is_file():
            inv = tk.messagebox.askyesno("Inventory Scan", "Inventory Scan already completed. Would you like to run again?")
            if inv == True:
                subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/LDISCN32.EXE" /V')               
        else:
            subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/LDISCN32.EXE" /V')

        open(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Inv.txt","w+")

        os.system("taskkill /im vulscan.exe /F")

        if patches.is_file():
            patch = tk.messagebox.askyesno("Patching", "Patching already completed. Would you like to run again?")
            if patch == True:
                subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/vulscan.exe" /showui=true /0 /taskid=%taskid% /maintEnable=False /IgnoreSubsequentAttempts=False /AgentBehavior=TIVMS01_v3997')   
        else:
            subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/vulscan.exe" /showui=true /0 /taskid=%taskid% /maintEnable=False /IgnoreSubsequentAttempts=False /AgentBehavior=TIVMS01_v3997')

        open(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Patch.txt","w+")

        driver = tk.messagebox.askyesno("Gen 2 Dock Driver", "Would you like to install Gen 2 Dock Drivers?")
        if driver == True:
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/Gen2_dock_driver.exe"')
        else:
            pass

        if systemUpdate.is_file():
            inv = tk.messagebox.askyesno("System Update", "System Update already completed. Would you like to run again?")
            if inv == True:
                subprocess.call('"C:/Program Files (x86)/Lenovo/System Update/tvsu.exe"')
        else:  
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/system_update_5.07.0110.exe"')
            subprocess.call('"C:/Program Files (x86)/Lenovo/System Update/tvsu.exe"')
        
        open(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Update.txt","w+")
        
        tk.messagebox.askokcancel("Complete","Laptop is ready!")
    
    def corpdesktop_setup():

        #Variables
        name = os.environ['COMPUTERNAME']
        agentInstall = Path("C:/Program Files (x86)/LANDesk/LDClient/2020.1 Corporate Agent.msi")
        inventoryScan = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Inv.txt")
        patches = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Patch.txt")
        pcName = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}")
        systemUpdate = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Update.txt")

        #Make Directory for Text files
        if pcName.is_dir():
            pass
        else:
            os.mkdir(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}")

        # Capture Serial
        serial = os.popen("wmic bios get serialnumber").read()
        f= open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Serial.txt","w+")
        f.write(serial)
        f.close()

        #Setup
        if agentInstall.is_file():
            pass
        else:
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/2020.1 Corporate Agent_with_status.exe"')
        if inventoryScan.is_file():
            inv = tk.messagebox.askyesno("Inventory Scan", "Inventory Scan already completed. Would you like to run again?")
            if inv == True:
                subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/LDISCN32.EXE" /V')
        else:
            subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/LDISCN32.EXE" /V')

        open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Inv.txt","w+")

        if patches.is_file():
            patch = tk.messagebox.askyesno("Patching", "Patching already completed. Would you like to run again?")
            if patch == True:
                subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/vulscan.exe" /showui=true /0 /taskid=%taskid% /maintEnable=False /IgnoreSubsequentAttempts=False /AgentBehavior=TIVMS01_v3997') 
        else:
            subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/vulscan.exe" /showui=true /0 /taskid=%taskid% /maintEnable=False /IgnoreSubsequentAttempts=False /AgentBehavior=TIVMS01_v3997')
        open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Patch.txt","w+")

        if systemUpdate.is_file():
            inv = tk.messagebox.askyesno("System Update", "System Update already completed. Would you like to run again?")
            if inv == True:
                subprocess.call('"C:/Program Files (x86)/Lenovo/System Update/tvsu.exe"')
        else:  
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/system_update_5.07.0110.exe"')
            subprocess.call('"C:/Program Files (x86)/Lenovo/System Update/tvsu.exe"')
        
        open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Update.txt","w+")

        tk.messagebox.askokcancel("Complete","Desktop is ready!")
    
    def whlaptop_setup():

        #Variables
        name = os.environ['COMPUTERNAME']
        agentInstall = Path("C:/Program Files (x86)/LANDesk/LDClient/2020.1 Corporate Agent.msi")
        inventoryScan = Path(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Inv.txt")
        patches = Path(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Patch.txt")
        pcName = Path(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}")
        systemUpdate = Path(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Update.txt")

        #Make Directory for Text files
        if pcName.is_dir():
            pass
        else:
            os.mkdir(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}")

        # Capture Serial
        serial = os.popen("wmic bios get serialnumber").read()
        f= open(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Serial.txt","w+")
        f.write(serial)
        f.close()

        #Setup
        if agentInstall.is_file():
            pass
        else:
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/2020.1 Corporate Agent_with_status.exe"')
        if inventoryScan.is_file():
            inv = tk.messagebox.askyesno("Inventory Scan", "Inventory Scan already completed. Would you like to run again?")
            if inv == True:
                subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/LDISCN32.EXE" /V')
        else:
            subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/LDISCN32.EXE" /V')

        open(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Inv.txt","w+")

        if patches.is_file():
            patch = tk.messagebox.askyesno("Patching", "Patching already completed. Would you like to run again?")
            if patch == True:
                subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/vulscan.exe" /showui=true /0 /taskid=%taskid% /maintEnable=False /IgnoreSubsequentAttempts=False /AgentBehavior=TIVMS01_v3997') 
        else:
            subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/vulscan.exe" /showui=true /0 /taskid=%taskid% /maintEnable=False /IgnoreSubsequentAttempts=False /AgentBehavior=TIVMS01_v3997')

        open(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Patch.txt","w+")

        if systemUpdate.is_file():
            inv = tk.messagebox.askyesno("System Update", "System Update already completed. Would you like to run again?")
            if inv == True:
                subprocess.call('"C:/Program Files (x86)/Lenovo/System Update/tvsu.exe"')
        else:  
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/system_update_5.07.0110.exe"')
            subprocess.call('"C:/Program Files (x86)/Lenovo/System Update/tvsu.exe"')
        
        open(f"//nismith/share/Lenovo Setup/Imaged Laptops/{name}/Update.txt","w+")

        tk.messagebox.askokcancel("Complete","Laptop is ready!")
    
    def whdesktop_setup():

        #Variables
        name = os.environ['COMPUTERNAME']
        agentInstall = Path("C:/Program Files (x86)/LANDesk/LDClient/2020.1 Warehouse Agent.msi")
        inventoryScan = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Inv.txt")
        patches = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Patch.txt")
        pcName = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}")
        systemUpdate = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Update.txt")

        #Make Directory for Text files
        if pcName.is_dir():
            pass
        else:
            os.mkdir(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}")

        # Capture Serial
        serial = os.popen("wmic bios get serialnumber").read()
        f= open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Serial.txt","w+")
        f.write(serial)
        f.close()

        #Setup
        if agentInstall.is_file():
            pass
        else:
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/2020.1 Warehouse Agent_with_status.exe"')
        if inventoryScan.is_file():
            inv = tk.messagebox.askyesno("Inventory Scan", "Inventory Scan already completed. Would you like to run again?")
            if inv == True:
                subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/LDISCN32.EXE" /V')
        else:
            subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/LDISCN32.EXE" /V')

        open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Inv.txt","w+")

        if patches.is_file():
            patch = tk.messagebox.askyesno("Patching", "Patching already completed. Would you like to run again?")
            if patch == True:
                subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/vulscan.exe" /showui=true /0 /taskid=%taskid% /maintEnable=False /IgnoreSubsequentAttempts=False /AgentBehavior=TIVMS01_v3997')
        else:
            subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/vulscan.exe" /showui=true /0 /taskid=%taskid% /maintEnable=False /IgnoreSubsequentAttempts=False /AgentBehavior=TIVMS01_v3997')

        open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Patch.txt","w+")

        if systemUpdate.is_file():
            inv = tk.messagebox.askyesno("System Update", "System Update already completed. Would you like to run again?")
            if inv == True:
                subprocess.call('"C:/Program Files (x86)/Lenovo/System Update/tvsu.exe"')
        else:  
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/system_update_5.07.0110.exe"')
            subprocess.call('"C:/Program Files (x86)/Lenovo/System Update/tvsu.exe"')
        
        open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{name}/Update.txt","w+")

        tk.messagebox.askokcancel("Complete","Desktop is ready!")

    
    def storefolder(store):
        storeNo = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}")
        if storeNo.is_dir():
            pass
        else:
            os.mkdir(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}")
    


    def retaildesktop_setup(store):
        #Variables
        name = os.environ['COMPUTERNAME']
        agentInstall = Path("C:/Program Files (x86)/LANDesk/LDClient/2020.1 Store Agent.msi")
        inventoryScan = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}/Inv.txt")
        patches = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}/Patch.txt")
        pcName = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}")
        systemUpdate = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}/Update.txt")
        RPOS = Path(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}/RPOS.txt"

        #Make Directory for Text files
        if pcName.is_dir():
            pass
        else:
            os.mkdir(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}")

        # Capture Serial
        serial = os.popen("wmic bios get serialnumber").read()
        f= open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}/Serial.txt","w+")
        f.write(serial)
        f.close()

        #Setup
        if agentInstall.is_file():
            pass
        else:
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/2020.1 Store Agent_with_status.exe"')
        if inventoryScan.is_file():
            inv = tk.messagebox.askyesno("Inventory Scan", "Inventory Scan already completed. Would you like to run again?")
            if inv == True:
                subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/LDISCN32.EXE" /V')
        else:
            subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/LDISCN32.EXE" /V')

        open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}/Inv.txt","w+")

        if patches.is_file():
            patch = tk.messagebox.askyesno("Patching", "Patching already completed. Would you like to run again?")
            if patch == True:
                subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/vulscan.exe" /showui=true /0 /taskid=%taskid% /maintEnable=False /IgnoreSubsequentAttempts=False /AgentBehavior=TIVMS01_v3997')   
        else:
            subprocess.call('"C:/Program Files (x86)/LANDesk/LDClient/vulscan.exe" /showui=true /0 /taskid=%taskid% /maintEnable=False /IgnoreSubsequentAttempts=False /AgentBehavior=TIVMS01_v3997')

        open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}/Patch.txt","w+")

        #RPOS Install
        if RPOS.is_file():
            pass
        else:
            os.system(r"%windir%\sysnative\manage-bde -on -RecoveryPassword C:")
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\RunOnce',0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(reg_key, 'RPOS', 0, winreg.REG_SZ, "\"\\\\nismith\\share\\Lenovo Setup\\Setup Files\\RPOSUpdaterInstaller.exe\"")
            open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}/RPOS.txt","w+")


        if systemUpdate.is_file():
            inv = tk.messagebox.askyesno("System Update", "System Update already completed. Would you like to run again?")
            if inv == True:
                subprocess.call('"C:/Program Files (x86)/Lenovo/System Update/tvsu.exe"')
        else:  
            subprocess.call('"//nismith/share/Lenovo Setup/Setup Files/system_update_5.07.0110.exe"')
            subprocess.call('"C:/Program Files (x86)/Lenovo/System Update/tvsu.exe"')
        
        open(f"//nismith/share/Lenovo Setup/Imaged Desktops/{store}/{name}/Update.txt","w+")

        tk.messagebox.askokcancel("Complete","Desktop is ready!")