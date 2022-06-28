1  # ! /usr/bin/env python
2  # -*- coding: utf-8 -*-
3  #

import sys

9
import tkinter as tk

10
import tkinter.ttk as ttk

11
from tkinter.constants import *

12
13
import Metashape_interface_support

14
15


class Toplevel1:
    16

    def __init__(self, top=None):

        17
    '''This class configures and populates the toplevel window.
 18            top is the toplevel containing window.'''


19
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
20
_fgcolor = '#000000'  # X11 color: 'black'
21
_compcolor = 'gray40'  # X11 color: #666666
22
_ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
23
_ana2color = 'beige'  # X11 color: #f5f5dc
24
_tabfg1 = 'black'
25
_tabfg2 = 'black'
26
_tabbg1 = 'grey75'
27
_tabbg2 = 'grey89'
28
_bgmode = 'light'
29
self.style = ttk.Style()
30
if sys.platform == "win32":
    31
    self.style.theme_use('winnative')
32
self.style.configure('.', background=_bgcolor)
33
self.style.configure('.', foreground=_fgcolor)
34
self.style.configure('.', font="TkDefaultFont")
35
self.style.map('.', background=
36[('selected', _compcolor), ('active', _ana2color)])
37
38
top.geometry("993x800+447+101")
39
top.minsize(120, 1)
40
top.maxsize(1924, 1061)
41
top.resizable(0, 0)
42
top.title("Toplevel 0")
43
top.configure(background="#d9d9d9")
44
top.configure(highlightbackground="#d9d9d9")
45
top.configure(highlightcolor="black")
46
47
self.top = top
48
self.che49 = tk.IntVar()
49
50
self.style.map('TNotebook.Tab', background=
51[('selected', _bgcolor), ('active', _tabbg1),
   52('!active', _tabbg2)], foreground=
               53[('selected', _fgcolor), ('active', _tabfg1), ('!active', _tabfg2)])
54
self.TNotebook1 = ttk.Notebook(self.top)
55
self.TNotebook1.place(x=410, y=20, height=766, width=574)
56
self.TNotebook1.configure(takefocus="")
57
self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
58
self.TNotebook1.add(self.TNotebook1_t1, padding=3)
59
self.TNotebook1.tab(0, text='''Match & Align''', compound="left"
60, underline = '''-1''', )
61
self.TNotebook1_t1.configure(background="#d9d9d9")
62
self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
63
self.TNotebook1_t1.configure(highlightcolor="black")
64
self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
65
self.TNotebook1.add(self.TNotebook1_t2, padding=3)
66
self.TNotebook1.tab(1, text='''Filtering''', compound="left"
67, underline = '''-1''', )
68
self.TNotebook1_t2.configure(background="#d9d9d9")
69
self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
70
self.TNotebook1_t2.configure(highlightcolor="black")
71
self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
72
self.TNotebook1.add(self.TNotebook1_t3, padding=3)
73
self.TNotebook1.tab(2, text='''Dense Cloud''', compound="left"
74, underline = '''-1''', )
75
self.TNotebook1_t3.configure(background="#d9d9d9")
76
self.TNotebook1_t3.configure(highlightbackground="#d9d9d9")
77
self.TNotebook1_t3.configure(highlightcolor="black")
78
self.TNotebook1_t4 = tk.Frame(self.TNotebook1)
79
self.TNotebook1.add(self.TNotebook1_t4, padding=3)
80
self.TNotebook1.tab(3, text='''Model''', compound="left"
81, underline = '''-1''', )
82
self.TNotebook1_t4.configure(background="#d9d9d9")
83
self.TNotebook1_t4.configure(highlightbackground="#d9d9d9")
84
self.TNotebook1_t4.configure(highlightcolor="black")
85
self.TNotebook1_t5 = tk.Frame(self.TNotebook1)
86
self.TNotebook1.add(self.TNotebook1_t5, padding=3)
87
self.TNotebook1.tab(4, text='''Normal Maps''', compound="left"
88, underline = '''-1''', )
89
self.TNotebook1_t5.configure(background="#d9d9d9")
90
self.TNotebook1_t5.configure(highlightbackground="#d9d9d9")
91
self.TNotebook1_t5.configure(highlightcolor="black")
92
self.TNotebook1_t6 = tk.Frame(self.TNotebook1)
93
self.TNotebook1.add(self.TNotebook1_t6, padding=3)
94
self.TNotebook1.tab(5, text='''Depth Maps''', compound="left"
95, underline = '''-1''', )
96
self.TNotebook1_t6.configure(background="#d9d9d9")
97
self.TNotebook1_t6.configure(highlightbackground="#d9d9d9")
98
self.TNotebook1_t6.configure(highlightcolor="black")
99
self.TNotebook1_t7 = tk.Frame(self.TNotebook1)
100
self.TNotebook1.add(self.TNotebook1_t7, padding=3)
101
self.TNotebook1.tab(6, text='''Report''', compound="left"
102, underline = '''-1''', )
103
self.TNotebook1_t7.configure(background="#d9d9d9")
104
self.TNotebook1_t7.configure(highlightbackground="#d9d9d9")
105
self.TNotebook1_t7.configure(highlightcolor="black")
106
107
self.frame_match = tk.LabelFrame(self.TNotebook1_t1)
108
self.frame_match.place(x=10, y=10, height=165, width=550)
109
self.frame_match.configure(relief='groove')
110
self.frame_match.configure(foreground="#000000")
111
self.frame_match.configure(text='''Matching''')
112
self.frame_match.configure(background="#d9d9d9")
113
self.frame_match.configure(highlightbackground="#d9d9d9")
114
self.frame_match.configure(highlightcolor="black")
115
116
self.check_generic_preselection = tk.Checkbutton(self.frame_match)
117
self.check_generic_preselection.place(x=20, y=90, height=25, width=135
118, bordermode = 'ignore')
119
self.check_generic_preselection.configure(activebackground="beige")
120
self.check_generic_preselection.configure(activeforeground="#000000")
121
self.check_generic_preselection.configure(anchor='w')
122
self.check_generic_preselection.configure(background="#d9d9d9")
123
self.check_generic_preselection.configure(command=Metashape_interface_support.Generic
Preselection)
124
self.check_generic_preselection.configure(compound='left')
125
self.check_generic_preselection.configure(cursor="fleur")
126
self.check_generic_preselection.configure(disabledforeground="#a3a3a3")
127
self.check_generic_preselection.configure(foreground="#000000")
128
self.check_generic_preselection.configure(highlightbackground="#d9d9d9")
129
self.check_generic_preselection.configure(highlightcolor="black")
130
self.check_generic_preselection.configure(justify='left')
131
self.check_generic_preselection.configure(selectcolor="#d9d9d9")
132
self.check_generic_preselection.configure(text='''Generic Preselection''')
133
self.check_generic_preselection.configure(variable=self.che49)
134
135
self.entry_keypoint_limit = ttk.Entry(self.frame_match)
136
self.entry_keypoint_limit.place(x=20, y=30, height=21, width=126
137, bordermode = 'ignore')
138
self.entry_keypoint_limit.configure(takefocus="")
139
self.entry_keypoint_limit.configure(cursor="ibeam")
140
141
self.entry_ktiepoint_limit = ttk.Entry(self.frame_match)
142
self.entry_ktiepoint_limit.place(x=20, y=60, height=21, width=126
143, bordermode = 'ignore')
144
self.entry_ktiepoint_limit.configure(takefocus="")
145
self.entry_ktiepoint_limit.configure(cursor="ibeam")
146
147
self.check_reference_preselection = tk.Checkbutton(self.frame_match)
148
self.check_reference_preselection.place(x=20, y=120, height=25, width=151
149, bordermode = 'ignore')
150
self.check_reference_preselection.configure(activebackground="beige")
151
self.check_reference_preselection.configure(activeforeground="#000000")
152
self.check_reference_preselection.configure(anchor='w')
153
self.check_reference_preselection.configure(background="#d9d9d9")
154
self.check_reference_preselection.configure(command=Metashape_interface_support.Test)
155
self.check_reference_preselection.configure(compound='left')
156
self.check_reference_preselection.configure(disabledforeground="#a3a3a3")
157
self.check_reference_preselection.configure(foreground="#000000")
158
self.check_reference_preselection.configure(highlightbackground="#d9d9d9")
159
self.check_reference_preselection.configure(highlightcolor="black")
160
self.check_reference_preselection.configure(justify='left')
161
self.check_reference_preselection.configure(selectcolor="#d9d9d9")
162
self.check_reference_preselection.configure(text='''Reference Preselection''')
163
self.check_reference_preselection.configure(variable=self.che49)
164
165
self.label_keypoint_limit = tk.Label(self.frame_match)
166
self.label_keypoint_limit.place(x=150, y=30, height=21, width=83
167, bordermode = 'ignore')
168
self.label_keypoint_limit.configure(anchor='w')
169
self.label_keypoint_limit.configure(background="#d9d9d9")
170
self.label_keypoint_limit.configure(compound='left')
171
self.label_keypoint_limit.configure(disabledforeground="#a3a3a3")
172
self.label_keypoint_limit.configure(foreground="#000000")
173
self.label_keypoint_limit.configure(text='''Keypoint Limit''')
174
175
self.label_tiepoint_limit = tk.Label(self.frame_match)
176
self.label_tiepoint_limit.place(x=150, y=60, height=21, width=83
177, bordermode = 'ignore')
178
self.label_tiepoint_limit.configure(activebackground="#f9f9f9")
179
self.label_tiepoint_limit.configure(anchor='w')
180
self.label_tiepoint_limit.configure(background="#d9d9d9")
181
self.label_tiepoint_limit.configure(compound='left')
182
self.label_tiepoint_limit.configure(disabledforeground="#a3a3a3")
183
self.label_tiepoint_limit.configure(foreground="#000000")
184
self.label_tiepoint_limit.configure(highlightbackground="#d9d9d9")
185
self.label_tiepoint_limit.configure(highlightcolor="black")
186
self.label_tiepoint_limit.configure(text='''Tiepoint Limit''')
187
188


def start_up():
    189
    Metashape_interface_support.main()


190
191
if __name__ == '__main__':
    192
    Metashape_interface_support.main()
193 

