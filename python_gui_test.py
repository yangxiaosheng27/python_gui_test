#import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
import ttkbootstrap as tk
from tkinter import filedialog
import sys
import os

class my_gui():
    def __init__(self):
        self.createTheme()
        self.root_windows = ttk.Window(themename=self.themeName)
        self.root_windows.iconphoto(True, tk.PhotoImage(data=self.getIconData()))
        self.root_windows.title('I am yxd')

    def getIconData(self):
        return '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'



    def callback_button1(self):
        self.filenames = filedialog.askopenfilenames(title='请选择文件', filetypes=[('图像文件', ".txt .bin .zip"), ('所有文件', ' *')], initialdir=os.path.abspath(os.path.dirname(sys.argv[0])))
        self.Entry1.delete(0, tk.END)
        self.Entry1.insert('insert', str(self.filenames))

    def createTheme(self):
        from ttkbootstrap.themes import user
        import json
        self.themeName = 'yxd_theme'
        if os.path.realpath(sys.argv[0]).endswith('.py') == False:
            return None
        colors = {
            "primary": "#6e40c0",
            "secondary": "#ea38b8",
            "success": "#ff0080",
            "info": "#1da2f2",
            "warning": "#ffbd05",
            "danger": "#e34b54",
            "light": "#44d7e8",
            "dark": "#170229",
            "bg": "#190831",
            "fg": "#32fbe2",
            "selectbg": "#461a8a",
            "selectfg": "#ffffff",
            "border": "#060606",
            "inputfg": "#bfb6cd",
            "inputbg": "#30115e",
            "active": "#17082E"
        }
        theme = {self.themeName: {"type": "light", "colors": colors}}
        user.USER_THEMES.update(theme)
        # save user themes to file
        formatted = json.dumps(user.USER_THEMES, indent=4)
        out = 'USER_THEMES = ' + formatted
        filepath = user.__file__
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(out)

    def setup(self):
        self.fram1 = tk.Frame(self.root_windows)
        self.fram1.pack(side='top', fill='x')
        self.LabelFrame1 = ttk.LabelFrame(self.fram1, text='文件路径')
        self.LabelFrame1.pack(fill='x', padx=2, pady=2)
        self.Entry1 = tk.Entry(self.LabelFrame1, text='123')
        self.Entry1.pack(side='left', fill='x', expand='yes', padx=5, pady=2)
        self.Button1 = tk.Button(self.LabelFrame1, text='选择文件',command=self.callback_button1, bootstyle="light")
        self.Button1.pack(side='left', padx=5, pady=2)

        self.fram2 = tk.Frame(self.root_windows)
        self.fram2.pack(side='left', fill='both', expand='yes', padx=5)
        tk.Label(self.fram2, text='22222222222').pack(expand='yes')

        self.fram3 = tk.Frame(self.root_windows)
        self.fram3.pack(side='left', fill='both', expand='yes', padx=5)
        tk.Label(self.fram3, text='33333333333').pack(expand='yes')


    def show(self):
        self.root_windows.mainloop()

def main():
    gui = my_gui()
    gui.setup()
    gui.show()

if __name__ == "__main__":
    main()
