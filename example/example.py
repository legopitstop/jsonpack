# See '/packs/Example/scripts/main.py' for all nodes and module definitions
from customtkinter import CTk, CTkScrollableFrame, CTkButton
from tkinter import Label
import jsonpack
import os
import logging
import sys

PATH = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(format='[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s', datefmt='%I:%M:%S',handlers=[logging.FileHandler(os.path.join(PATH, 'latest.log'),mode='w'),logging.StreamHandler(sys.stdout)], level=logging.INFO)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title('Example')
        self.geometry('500x500')
        self.logger = logging.getLogger('App')

        # Widgets
        self.reg = jsonpack.App('default')
        self.reg.add_path(os.path.join(PATH, 'packs'), scripts=True) # Path to look for packs
        self.reg.bind('AfterLoad', lambda e: self.load())

        self.btn = CTkButton(self, text='Exit', command=self.destroy)
        self.btn.grid(row=0, column=0, sticky='w')

        self.lst = CTkScrollableFrame(self)
        self.lst.grid(row=1, column=0, sticky='nesw')

        self.bind('<F5>', lambda e: self.reload())

        # responsive
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)

    def load(self):
        row = 0
        column = 0
        for name, item in self.reg['data.item'].items():
            icon = item.trigger_component('default:icon')
            if icon is not None:
                lbl = Label(self.lst, image=icon, compound='left', bg=self.lst['bg'])
                item.trigger_component('default:on_click', label=lbl, item=item)
                item.trigger_component('default:on_hover', label=lbl, item=item)
                lbl.grid(row=row, column=column) 
                if column >= 6:
                    column = 0
                    row += 1
                else:
                    column += 1

    def reload(self):
        for c in self.lst.winfo_children(): c.destroy()
        self.reg.reload(threaded=True)

    def mainloop(self):
        self.reg.run()
        super().mainloop()

if __name__ == '__main__':
    app = App()
    app.mainloop()