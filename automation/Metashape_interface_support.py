

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Metashape_interface

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = Metashape_interface.Toplevel1(_top1)
    root.mainloop()

def generic_preselection(*args):
    print('Metashape_interface_support.Generic Preselection')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()

def test(*args):
    print('Metashape_interface_support.Test')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()

if __name__ == '__main__':
    Metashape_interface.start_up()




