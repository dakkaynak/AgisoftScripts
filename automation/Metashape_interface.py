

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Metashape_interface_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("993x800+447+101")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0,  0)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.che49 = tk.IntVar()

        self.style.map('TNotebook.Tab', background =
            [('selected', _bgcolor), ('active', _tabbg1),
            ('!active', _tabbg2)], foreground =
            [('selected', _fgcolor), ('active', _tabfg1), ('!active',  _tabfg2)])
        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(x=410, y=20, height=766, width=574)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text='''Match & Align''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text='''Filtering''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t2.configure(background="#d9d9d9")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(2, text='''Dense Cloud''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t3.configure(background="#d9d9d9")
        self.TNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3.configure(highlightcolor="black")
        self.TNotebook1_t4 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4, padding=3)
        self.TNotebook1.tab(3, text='''Model''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t4.configure(background="#d9d9d9")
        self.TNotebook1_t4.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t4.configure(highlightcolor="black")
        self.TNotebook1_t5 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t5, padding=3)
        self.TNotebook1.tab(4, text='''Normal Maps''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t5.configure(background="#d9d9d9")
        self.TNotebook1_t5.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t5.configure(highlightcolor="black")
        self.TNotebook1_t6 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t6, padding=3)
        self.TNotebook1.tab(5, text='''Depth Maps''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t6.configure(background="#d9d9d9")
        self.TNotebook1_t6.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t6.configure(highlightcolor="black")
        self.TNotebook1_t7 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t7, padding=3)
        self.TNotebook1.tab(6, text='''Report''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t7.configure(background="#d9d9d9")
        self.TNotebook1_t7.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t7.configure(highlightcolor="black")

        self.frame_match = tk.LabelFrame(self.TNotebook1_t1)
        self.frame_match.place(x=10, y=10, height=165, width=550)
        self.frame_match.configure(relief='groove')
        self.frame_match.configure(foreground="#000000")
        self.frame_match.configure(text='''Matching''')
        self.frame_match.configure(background="#d9d9d9")
        self.frame_match.configure(highlightbackground="#d9d9d9")
        self.frame_match.configure(highlightcolor="black")

        self.check_generic_preselection = tk.Checkbutton(self.frame_match)
        self.check_generic_preselection.place(x=20, y=90, height=25, width=135
                , bordermode='ignore')
        self.check_generic_preselection.configure(activebackground="beige")
        self.check_generic_preselection.configure(activeforeground="#000000")
        self.check_generic_preselection.configure(anchor='w')
        self.check_generic_preselection.configure(background="#d9d9d9")
        self.check_generic_preselection.configure(command=Metashape_interface_support.generic_preselection)
        self.check_generic_preselection.configure(compound='left')
        self.check_generic_preselection.configure(cursor="fleur")
        self.check_generic_preselection.configure(disabledforeground="#a3a3a3")
        self.check_generic_preselection.configure(foreground="#000000")
        self.check_generic_preselection.configure(highlightbackground="#d9d9d9")
        self.check_generic_preselection.configure(highlightcolor="black")
        self.check_generic_preselection.configure(justify='left')
        self.check_generic_preselection.configure(selectcolor="#d9d9d9")
        self.check_generic_preselection.configure(text='''Generic Preselection''')
        self.check_generic_preselection.configure(variable=self.che49)

        self.entry_keypoint_limit = ttk.Entry(self.frame_match)
        self.entry_keypoint_limit.place(x=20, y=30, height=21, width=126
                , bordermode='ignore')
        self.entry_keypoint_limit.configure(takefocus="")
        self.entry_keypoint_limit.configure(cursor="ibeam")

        self.entry_tiepoint_limit = ttk.Entry(self.frame_match)
        self.entry_tiepoint_limit.place(x=20, y=60, height=21, width=126
                , bordermode='ignore')
        self.entry_tiepoint_limit.configure(takefocus="")
        self.entry_tiepoint_limit.configure(cursor="ibeam")

        self.check_reference_preselection = tk.Checkbutton(self.frame_match)
        self.check_reference_preselection.place(x=20, y=120, height=25, width=151
                , bordermode='ignore')
        self.check_reference_preselection.configure(activebackground="beige")
        self.check_reference_preselection.configure(activeforeground="#000000")
        self.check_reference_preselection.configure(anchor='w')
        self.check_reference_preselection.configure(background="#d9d9d9")
        self.check_reference_preselection.configure(command=Metashape_interface_support.test)
        self.check_reference_preselection.configure(compound='left')
        self.check_reference_preselection.configure(disabledforeground="#a3a3a3")
        self.check_reference_preselection.configure(foreground="#000000")
        self.check_reference_preselection.configure(highlightbackground="#d9d9d9")
        self.check_reference_preselection.configure(highlightcolor="black")
        self.check_reference_preselection.configure(justify='left')
        self.check_reference_preselection.configure(selectcolor="#d9d9d9")
        self.check_reference_preselection.configure(text='''Reference Preselection''')
        self.check_reference_preselection.configure(variable=self.che49)

        self.label_keypoint_limit = tk.Label(self.frame_match)
        self.label_keypoint_limit.place(x=150, y=30, height=21, width=83
                , bordermode='ignore')
        self.label_keypoint_limit.configure(anchor='w')
        self.label_keypoint_limit.configure(background="#d9d9d9")
        self.label_keypoint_limit.configure(compound='left')
        self.label_keypoint_limit.configure(disabledforeground="#a3a3a3")
        self.label_keypoint_limit.configure(foreground="#000000")
        self.label_keypoint_limit.configure(text='''Keypoint Limit''')

        self.label_tiepoint_limit = tk.Label(self.frame_match)
        self.label_tiepoint_limit.place(x=150, y=60, height=21, width=83
                , bordermode='ignore')
        self.label_tiepoint_limit.configure(activebackground="#f9f9f9")
        self.label_tiepoint_limit.configure(anchor='w')
        self.label_tiepoint_limit.configure(background="#d9d9d9")
        self.label_tiepoint_limit.configure(compound='left')
        self.label_tiepoint_limit.configure(disabledforeground="#a3a3a3")
        self.label_tiepoint_limit.configure(foreground="#000000")
        self.label_tiepoint_limit.configure(highlightbackground="#d9d9d9")
        self.label_tiepoint_limit.configure(highlightcolor="black")
        self.label_tiepoint_limit.configure(text='''Tiepoint Limit''')

def start_up():
    Metashape_interface_support.main()

if __name__ == '__main__':
    Metashape_interface_support.main()




