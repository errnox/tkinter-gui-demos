import ScrolledText
import Tkinter as tk
import tkSimpleDialog


class App(object):
  def __init__(self):
    self.master = tk.Tk()
    self.generate_widgets()
    self.master.mainloop()

  def generate_widgets(self):
    self.window = tk.Frame(self.master)
    self.window.pack()
    self.text_input = ScrolledText.ScrolledText(self.window)
    self.text_input.pack()

    self.ask_integer_button = tk.Button(
      self.window, text='Ask for integer', command=self.ask_integer)
    self.ask_integer_button.pack()

    self.ask_float_button = tk.Button(
      self.window, text='Ask for float', command=self.ask_float)
    self.ask_float_button.pack()

    self.ask_string_button = tk.Button(
      self.window, text='Ask for string', command=self.ask_string)
    self.ask_string_button.pack()

  def ask_integer(self):
    x = tkSimpleDialog.askinteger('Integer Asker', 'Give me your integer:')
    print(x)

  def ask_float(self):
    x = tkSimpleDialog.askfloat('Float Asker', 'Give me your float:')
    print(x)

  def ask_string(self):
    x = tkSimpleDialog.askstring('String Asker', 'Give me your string:')
    print(x)


if __name__ == '__main__':
  app = App()
