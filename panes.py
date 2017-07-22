import Tkinter as tk


class App(object):
  def __init__(self):
    self.master = tk.Tk()
    self.generate_widgets()
    self.master.mainloop()

  def generate_widgets(self):
    self.window = tk.PanedWindow(
      orient=tk.HORIZONTAL, sashrelief=tk.SUNKEN)
    self.window.pack()
    self.window.add(tk.Label(text='One', padx=50, pady=50))
    self.window.add(tk.Label(text='Two', padx=50, pady=50))
    self.window.add(tk.Label(text='Three', padx=50, pady=50))


if __name__ == '__main__':
  app = App()
