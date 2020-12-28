import tkinter as tk
import os
import Imaging


#TODO
# Implement remote running of application via IP address.... but how????



class MainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        master.geometry("400x300")
        master.title("TBC Imaging")
        self.selection = tk.Label(self.frame, text="Please choose the PC type", width= 40, font=("helvetica", 12, "bold"))
        self.selection.pack(pady=15)
        self.CorpButton = tk.Button(self.frame, text = 'Corporate', bg="Steel Blue", fg="white", width = 40, command = self.newCorp, font=("helvetica", 10, "bold"))
        self.CorpButton.pack(pady=25)
        self.RetailButton = tk.Button(self.frame, text = 'Retail', bg="Steel Blue", fg="white", width = 40, command = self.newStore, font=("helvetica", 10, "bold"))
        self.RetailButton.pack(pady=25)
        self.WarehouseButton = tk.Button(self.frame, text = 'Warehouse', bg="Steel Blue", fg="white", width = 40, command = self.newWarehouse, font=("helvetica", 10, "bold"))
        self.WarehouseButton.pack(pady=25)
        self.frame.pack()
    def newCorp(self):
        self.master.destroy() # close the current window
        self.master = tk.Tk() # create another Tk instance
        self.app = Corporate(self.master) # create Demo2 window
        self.master.mainloop()
    def newStore(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Store(self.master)
        self.master.mainloop()
    def newWarehouse(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = Warehouse(self.master)
        self.master.mainloop()
    def close_windows(self):
        self.master.destroy()


class Store:
    def __init__(self, master):
        self.master = master
        master.geometry("400x200")
        master.title("Store")
        self.frame = tk.Frame(self.master)
        self.storelabel = tk.Label(self.frame, anchor="n", text = "Please enter the store #", width= 40, font=("helvetica", 10, "bold"))
        self.storelabel.pack()
        self.entry = tk.Entry(self.frame, width=34)
        self.entry.pack(pady=10)
        self.desktopButton = tk.Button(self.frame, text = 'Continue', width = 25, bg="Steel Blue", fg="White", font=("helvetica", 10, "bold"), command = lambda: [Imaging.Setup.storefolder(store = self.entry.get()), Imaging.Setup.retaildesktop_setup(store = self.entry.get()), self.master.destroy()])
        self.desktopButton.pack(pady=10)
        self.backButton = tk.Button(self.frame, text= "Back", width= 15, bg="Steel Blue", fg="White", font=("helvetica", 10, "bold"), command = lambda: [self.master.destroy(), main()])
        self.backButton.pack(anchor="s",pady=30)
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()


class Corporate:
    def __init__(self, master):
        self.master = master
        master.geometry("400x300")
        master.title("Corporate Setup")
        self.frame = tk.Frame(self.master)
        self.devicetype = tk.Label(self.frame, text= "Please choose the device type", width= 40, font=("helvetica", 10, "bold"))
        self.devicetype.pack(pady=10)
        self.laptopButton = tk.Button(self.frame, text = 'Laptop', width = 25, bg="Steel Blue", fg="White", font=("helvetica", 10, "bold"), command = Imaging.Setup.corplaptop_setup)
        self.laptopButton.pack(pady=20)
        self.desktopButton = tk.Button(self.frame, text = 'Desktop', width = 25, bg="Steel Blue", fg="White", font=("helvetica", 10, "bold"), command = Imaging.Setup.corpdesktop_setup)
        self.desktopButton.pack(pady=20)
        self.backButton = tk.Button(self.frame, text= "Back", width= 15, bg="Steel Blue", fg="White", font=("helvetica", 10, "bold"), command = lambda: [self.master.destroy(), main()])
        self.backButton.pack(anchor="s", pady=48)
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

class Warehouse:
    def __init__(self, master):
        self.master = master
        master.geometry("400x300")
        master.title("Warehouse Setup")
        self.frame = tk.Frame(self.master)
        self.devicetype = tk.Label(self.frame, text= "Please choose the device type", width= 40, font=("helvetica", 10, "bold"))
        self.devicetype.pack(pady=10)
        self.laptopButton = tk.Button(self.frame, text = 'Laptop', width = 25, bg="Steel Blue", fg="White", font=("helvetica", 10, "bold"), command = Imaging.Setup.whlaptop_setup)
        self.laptopButton.pack(pady=20)
        self.desktopButton = tk.Button(self.frame, text = 'Desktop', width = 25, bg="Steel Blue", fg="White", font=("helvetica", 10, "bold"), command = Imaging.Setup.whdesktop_setup)
        self.desktopButton.pack(pady=20)
        self.backButton = tk.Button(self.frame, text= "Back", width= 10, bg="Steel Blue", fg="White", font=("helvetica", 10, "bold"), command = lambda: [self.master.destroy(), main()])
        self.backButton.pack(anchor="s", pady=48)
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

main()