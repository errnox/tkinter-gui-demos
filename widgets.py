import Tkinter as tk
import tkFileDialog


class App(object):
  def __init__(self):
    self.master = tk.Tk()

    # self.master.wm_maxsize(width=500, height=700)
    # self.master.wm_minsize(width=200, height=300)

    width = self.master.winfo_screenwidth()
    height = self.master.winfo_screenheight()
    self.master.geometry('{}x{}'.format(width, height))

    self.message_text = tk.StringVar()
    self.message_text.set(
      'This is some sample text for the "Message" widget.')
    self.size = tk.StringVar()
    self.size.set('normal')
    self.shape = tk.StringVar()
    self.shape.set('triangle')
    self.num_items = tk.IntVar()
    self.num_items.set(5)

    self.generate_widgets()

  def generate_widgets(self):
    self.window = tk.Frame(
      self.master, padx=20, pady=20)
    self.window.pack()

    # self.window_frame = tk.Frame(
    #   self.master, padx=20, pady=20, width=500, height=700)
    # self.window_frame.pack()

    # self.window_canvas = tk.Canvas(self.window_frame)
    # self.window_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
    # self.window = tk.Frame(self.window_canvas)
    # self.window_canvas.create_window(
    #   (0, 0), window=self.window, anchor=tk.NW)

    # self.window_scrollbar = tk.Scrollbar(
    #   self.window_frame, command=self.window_canvas.yview)
    # self.window_scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.FALSE)
    # self.window_canvas.config(yscrollcommand=self.window_scrollbar.set)

    self.colors_listbox = tk.Listbox(self.window)
    self.colors_listbox.pack()
    self.colors_listbox.insert(tk.END, 'red')
    self.colors_listbox.insert(tk.END, 'green')
    self.colors_listbox.insert(tk.END, 'blue')
    self.colors_listbox.insert(tk.END, 'yellow')
    self.colors_listbox.insert(tk.END, 'white')
    self.colors_listbox.insert(tk.END, 'black')

    self.vsep()

    self.message_widget_frame = tk.LabelFrame(
      self.window, text='"Message" widget', padx=20, pady=20)
    self.message_widget_frame.pack(side=tk.LEFT)
    tk.Entry(self.message_widget_frame,
             textvariable=self.message_text).pack()
    tk.Message(
      self.message_widget_frame, textvariable=self.message_text, width=300,
      font='Monospace', justify=tk.CENTER).pack()

    self.vsep()
    self.optionmenu_frame = tk.LabelFrame(
      self.window, text='"OptionMenu" widget', padx=20, pady=20)
    self.optionmenu_frame.pack(side=tk.LEFT)
    tk.Label(self.optionmenu_frame, text='Size').pack()
    tk.Label(self.optionmenu_frame, textvariable=self.size,
             font='Monospace', foreground='#7A7A7A').pack()
    self.size_optionmenu = tk.OptionMenu(
      self.optionmenu_frame, self.size, 'small', 'normal', 'large',
      'extra large')
    self.size_optionmenu.pack()

    self.vsep()
    self.radiobutton_frame = tk.LabelFrame(
      self.window, text='"Radiobutton" widget', padx=20, pady=20)
    self.radiobutton_frame.pack(side=tk.LEFT)
    tk.Label(self.radiobutton_frame, text='Shape').pack()
    tk.Label(self.radiobutton_frame, textvariable=self.shape,
             font='Monospace', foreground='#7A7A7A').pack()
    tk.Radiobutton(
      self.radiobutton_frame, text='Square',
      variable=self.shape, value='square').pack()
    tk.Radiobutton(
      self.radiobutton_frame, text='Triangle',
      variable=self.shape, value='triangle').pack()
    tk.Radiobutton(
      self.radiobutton_frame, text='Circle',
      variable=self.shape, value='circle').pack()
    tk.Radiobutton(
      self.radiobutton_frame, text='Polygon',
      variable=self.shape, value='polygon').pack()

    self.vsep()
    tk.Label(self.window, text='# of items:').pack()
    tk.Label(self.window, textvariable=self.num_items,
             font='Monospace', foreground='#7A7A7A').pack()
    self.num_items_scale = tk.Scale(
      self.window, variable=self.num_items, from_=0, to=20,
      orient='horizontal')
    self.num_items_scale.pack()

    self.show_toplevel_button = tk.Button(
      self.window, text='Show window', command=self.show_toplevel)
    self.show_toplevel_button.pack()

    tk.Button(self.window, text='Open file', command=self.ask_file).place(
      relx=0.5, rely=0.5, relwidth=0.2, anchor=tk.NE)

    self.master.mainloop()

  def vsep(self, height=0):
    tk.Label(self.window, pady=height).pack()

  def show_toplevel(self):
    self.toplevel = tk.Toplevel(self.window, padx=20, pady=20)
    self.toplevel.transient(master=self.master)
    tk.Label(self.toplevel, text='This is a toplevel window.').pack()
    tk.Button(
      self.toplevel, text='Close', command=self.toplevel.destroy).pack()

  def ask_file(self):
    print(tkFileDialog.askopenfilename())


if __name__ == '__main__':
  app = App()
