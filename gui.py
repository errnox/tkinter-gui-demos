import sys
import random

import Tkinter as tk
import tkMessageBox


class App(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.pack()
    self.createWidgets()
    self.mainloop()

  def createWidgets(self):
    tk.Label(self, text='This is a test.').pack()

    self.quit_button = tk.Button(self, text='Quit', command=self.quit)
    self.quit_button.pack()

    self.hello_button = tk.Button(
      self, text='Say hello',
      command=lambda : sys.stdout.write('Hello!\n'))
    self.hello_button.pack()

    self.separator()

    self.color = ' '
    self.color_radio_button1 = tk.Radiobutton(
      self, text='red', variable=self.color, value='#ff0000')
    self.color_radio_button1.pack()

    self.color_radio_button2 = tk.Radiobutton(
      self, text='green', variable=self.color, value='#00ff00')
    self.color_radio_button2.pack()

    self.color_radio_button3 = tk.Radiobutton(
      self, text='blue', variable=self.color, value='#0000ff')
    self.color_radio_button3.pack()

    tk.Label(self, text='Color:').pack()
    self.color_label = tk.Label(self, textvariable=self.color)
    self.color_label.pack()

    self.separator()

    self.temperature = 1
    tk.Scale(self, from_=0, to=10, variable=self.temperature,
             orient=tk.HORIZONTAL,).pack()
    tk.Label(self, textvariable=self.temperature).pack()

    tk.Spinbox(self, from_=0, to=30).pack()

    self.quit_button.bind('<Key>', self.quit_on_key_press)

    self.separator()

    self.canvas = tk.Canvas(self, width=500, height=300)
    self.canvas.pack()
    self.points = [[i * self.temperature * 10, random.randint(0, i * 10)]
                   for i in range(30)]
    self.line = self.canvas.create_line(self.points, fill='#ff0000')
    self.canvas.bind('<B1-Motion>', self.draw_line)

    self.bind('<B3-Motion>', self.print_mouse)

    self.new_window_button = tk.Button(
      self, text='New window', command=self.create_new_window)
    self.new_window_button.pack(side=tk.BOTTOM, fill=tk.X)

    self.show_warning_button = tk.Button(
      self, text='Show Warning', command=self.show_warning_dialog)
    self.show_warning_button.pack(side=tk.BOTTOM, fill=tk.X)

    self.show_custom_dialog_button = tk.Button(
      self, text='Custom Dialog', command=self.show_custom_dialog)
    self.show_custom_dialog_button.pack(side=tk.BOTTOM, fill=tk.X)

  def separator(self):
    tk.Label(self,text='_' * 75, fg='#AEAEAE').pack()

  def say_color(self):
    print("Color: %s" % self.color)

  def quit_on_key_press(self, event):
    if event.keycode == 24:  # 'q'
      self.master.destroy()
    elif event.keycode == 36:  # Return
      self.master.destroy()

  def print_mouse(self, event):
    print(event.x, event.y)

  def print_event(self, event):
    print(event)
      
  def draw_line(self, event):
    self.points.append([event.x, event.y])
    self.canvas.delete(self.line)
    self.line = self.canvas.create_line(self.points, fill='#ff0000')

  def say_hello(self):
    print('Hello')

  def quit_application(self):
    self.master.destroy()

  def create_new_window(self):
    window = tk.Toplevel()
    tk.Label(window, text='This is a new window.', width=20,
             height=10).pack()
    menu = tk.Menu(window)
    things_menu = tk.Menu(window)
    window.config(menu=menu)
    menu.add_command(label='Do something', command=self.say_hello)
    menu.add_cascade(label='Things', menu=things_menu)
    things_menu.add_command(label='Do a thing', command=self.say_hello)
    things_menu.add_command(label='Quit', command=self.quit_application)
    menu.add_separator()

  def show_warning_dialog(self):
    if tkMessageBox.askyesno('Info', 'Open warning box?',
                             default=tkMessageBox.NO):
      tkMessageBox.showwarning('Warning Box', 'This is a warning.')

  def show_custom_dialog(self):
    dialog = tk.Toplevel()
    dialog.title('Custom Dialog')
    tk.Label(dialog, text='This is a custom dialog', width=30,
             height=20).pack()
    cancel_button = tk.Button(dialog, text='Close',
              command=lambda : dialog.destroy())
    cancel_button.pack()
    dialog.bind('<Return>', lambda _: dialog.destroy())
    dialog.bind('<Escape>', lambda _: dialog.destroy())
    dialog.transient(self)
    cancel_button.focus()
    dialog.protocol('WM_DELETE_WINDOW', lambda : dialog.destroy())
    dialog.grab_set()
    self.wait_window(dialog)


if __name__ == '__main__':
  app = App()
  app.master.title('Test App')
