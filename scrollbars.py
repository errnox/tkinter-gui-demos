import os  # DEBUG
import Tkinter as tk


class App(object):
  def __init__(self):
    self.master = tk.Tk()
    self.generate_widgets()
    self.master.mainloop()

  def generate_widgets(self):
    self.window = tk.Frame(self.master)
    self.window.pack()

    self.text_entry = tk.Text(self.window, width=100)

    # Add a vertical scrollbar.
    self.text_entry_scrollbar_y = tk.Scrollbar(
      self.window, command=self.text_entry.yview, orient=tk.VERTICAL)
    self.text_entry_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    # Add a horizontal scrollbar.
    self.text_entry_scrollbar_x = tk.Scrollbar(
      self.window, command=self.text_entry.xview, orient=tk.HORIZONTAL)
    self.text_entry_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    self.text_entry.config(yscrollcommand=self.text_entry_scrollbar_y.set)
    self.text_entry.config(xscrollcommand=self.text_entry_scrollbar_x.set)

    # DEBUG
    s = os.popen('man -P "" man').read()
    self.text_entry.insert(tk.END, s)
    
    self.text_entry.pack(side=tk.LEFT)


if __name__ == '__main__':
  app = App()
