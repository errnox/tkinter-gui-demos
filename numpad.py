import Tkinter as tk


class App(object):
  def __init__(self):
    self.master = tk.Tk()
    self.window = tk.Frame(self.master, padx=20, pady=30)
    self.window.pack()
    self.display_text = tk.StringVar()
    self.display_text.set('')
    self.display_numbers = []
    # Canvas bars
    self.bars = []
    self.message_text = tk.StringVar()
    self.grid_row_i = -1
    self.grid_column_i = -1
    self.create_widgets()
    width = self.master.winfo_screenwidth()
    height = self.master.winfo_height()
    w, h = 250, 500
    x = width / 2 - w / 2
    y = height / 2 + h / 4
    self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    self.window.mainloop()

  def create_widgets(self):
    self.menu = tk.Menu(self.master)
    self.menu.add_command(
      label='One', command=lambda : self.message('One'))
    self.menu.add_command(
      label='Two', command=lambda : self.message('Two'))
    self.menu.add_command(
      label='Three', command=lambda : self.message('Three'))
    self.master.config(menu=self.menu)

    self.message_label = tk.Label(
      self.window, textvariable=self.message_text, wraplength=200,
      foreground='#454545')
    self.message_label.grid(row=0, column=0, columnspan=4)
    self.message_label.bind('<Button-1>', func=lambda _: self.message(''))

    self.display = tk.Entry(
      self.window, textvariable=self.display_text, width=5, font=25,
      state=tk.DISABLED, disabledforeground='#121212')
    self.display.grid(row=1, column=0, columnspan=3, sticky=tk.W+tk.E)

    self.key_7 = tk.Button(
      self.window, text='7', command=lambda : self.type_in('7'),
      width=5, height=4)
    self.key_7.grid(row=2, column=0)
    self.key_8 = tk.Button(
      self.window, text='8', command=lambda : self.type_in('8'),
      width=5, height=4)
    self.key_8.grid(row=2, column=1)
    self.key_9 = tk.Button(
      self.window, text='9', command=lambda : self.type_in('9'),
      width=5, height=4)
    self.key_9.grid(row=2, column=2)

    self.key_4 = tk.Button(
      self.window, text='4', command=lambda : self.type_in('4'),
      width=5, height=4)
    self.key_4.grid(row=3, column=0)
    self.key_5 = tk.Button(
      self.window, text='5', command=lambda : self.type_in('5'),
      width=5, height=4)
    self.key_5.grid(row=3, column=1)
    self.key_6 = tk.Button(
      self.window, text='6', command=lambda : self.type_in('6'),
      width=5, height=4)
    self.key_6.grid(row=3, column=2)

    self.key_1 = tk.Button(
      self.window, text='1', command=lambda : self.type_in('1'),
      width=5, height=4)
    self.key_1.grid(row=4, column=0)
    self.key_2 = tk.Button(
      self.window, text='2', command=lambda : self.type_in('2'),
      width=5, height=4)
    self.key_2.grid(row=4, column=1)
    self.key_3 = tk.Button(
      self.window, text='3', command=lambda : self.type_in('3'),
      width=5, height=4)
    self.key_3.grid(row=4, column=2)

    self.key_quit = tk.Button(
      self.window, text='Quit', command=self.quit, fg='#696969',
      borderwidth=0, width=5, height=4)
    self.key_quit.grid(row=5, column=0)
    self.key_0 = tk.Button(
      self.window, text='0', command=lambda : self.type_in('0'),
      width=5, height=4)
    self.key_0.grid(row=5, column=1)
    self.key_clear = tk.Button(
      self.window, text='Clear', command=self.clear, fg='#696969',
      width=5, height=4)
    self.key_clear.grid(row=5, column=2)

    # Create the canvas
    self.canvas = tk.Canvas(self.window, width=200, height=50)
    self.canvas.grid(row=7, column=0, columnspan=4)
    self.canvas.create_rectangle(0, 0, 200, 50, fill='#FFFFFF',
                                 outline='#FFFFFF')
    self.export_postscript_button = tk.Button(
      self.window, text='Export Postscript',
      command=self.export_postscript)
    self.export_postscript_button.grid(row=8, column=0, columnspan=4)
    self.canvas.bind('<Control-Button-1>', self.draw_circle)

    # Animation
    self.player_x = 0
    self.player = self.canvas.create_rectangle(
      self.player_x, 0, 20, 20, fill='#337744', width=0, tags='player',
      activefill='#66AA77')
    self.player_animation_function = self.master.after(0, self.animate)
    self.do_animate_player = True

    self.player_animation_checkbutton = tk.Checkbutton(
      self.window, text='Animate player', variable=self.do_animate_player,
      command=self.toggle_player_animation)
    self.player_animation_checkbutton.grid(row=9, column=0, columnspan=4)

    # Button on top of canvas
    #
    # self.canvas_button = tk.Button(
    #   self.window, text='Say hello',
    #   command=lambda : self.message(random.choice(
    #       ['Hello!', 'Hey!', 'Hi!'])))
    # self.canvas_button_window = self.canvas.create_window(
    #   50, 50, window=self.canvas_button)

    self.canvas.tag_bind(
      'player', '<Button-1>',
      lambda _: self.message('The player has been clicked on.'))

    self.colors = {
      'red': '#FF0000',
      'green': '#00FF00',
      'blue': '#0000FF',
      'yellow': '#FFFF00',
      'white': '#FFFFFF',
      'black': '#000000',
      }
    self.colors_listbox = tk.Listbox(self.window, selectmode=tk.EXTENDED)
    self.colors_listbox.grid(row=10, column=0, columnspan=4)
    self.colors_idx = self.colors.keys()
    for i, color in enumerate(self.colors_idx):
      self.colors_listbox.insert(tk.END, color)
    self.delete_colors_button = tk.Button(
      self.window, text='Delete colors',
      command=lambda : self.report_selected_colors(
        self.colors_listbox.curselection()))
    self.delete_colors_button.grid(row=11, column=0, columnspan=4)

    # Popup menu
    self.popup_menu = tk.Menu(self.master)
    self.popup_menu.add_command(
      label='Help', command=lambda : self.message('Help'))
    self.popup_menu.add_command(
      label='Info', command=lambda : self.message('Info'))
    self.popup_menu.add_command(
      label='Copy', command=lambda : self.message('Copy'))
    self.popup_menu.add_command(
      label='Save', command=lambda : self.message('Save'))
    self.window.bind('<Button-3>', self.popup)

  def report_selected_colors(self, indices):
    selected = [self.colors_idx[i] for i in indices]
    s = 'Selected colors\n'
    for i in selected:
      s += i + ': ' + self.colors[i] + '\n'
    self.message(s)
    self.colors_listbox.delete(0, tk.END)
    for i, color in enumerate(self.colors_idx):
      if i not in indices:
        self.colors_listbox.insert(tk.END, color)

  def toggle_player_animation(self):
    if self.do_animate_player == True:
      self.canvas.after_cancel(self.player_animation_function)
      self.do_animate_player = False
    elif self.do_animate_player == False:
      self.player_animation_function = self.canvas.after(0, self.animate)
      self.do_animate_player = True

  def animate(self):
    if self.do_animate_player:
      if self.player_x < 10:
        self.player_x += 1
      else:
        if self.player_x >= 0 and self.player_x <= 10:
          self.player_x = 0
        self.player_x -= 10
      self.canvas.move(self.player, self.player_x, 0)
      self.master.after(100, self.animate)
  
  def draw_circle(self, event):
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    self.canvas.create_oval(
      x - 3, y - 3, x + 3, y + 3, fill='#45EF45', outline='#45EF45')

  def type_in(self, text):
    self.display_text.set('{}{}'.format(self.display_text.get(), text))
    n = int(text)
    self.display_numbers.append(n)
    length = len(self.display_numbers)
    width = 4
    rect = self.canvas.create_rectangle(
      length * width, 50,
      length * width + width, 50 - n * 4,
      fill='#FF0000', outline='#FFFFFF')
    self.bars.append(rect)

  def message(self, text):
    self.message_text.set(text)

  def clear(self):
    self.display_text.set('')
    self.display_numbers = []
    for bar in self.bars:
      self.canvas.delete(bar)
    self.message('Cleared successfully')

  def quit(self):
    self.master.destroy()

  def export_postscript(self):
    image_name = 'image.ps'
    self.canvas.postscript(file=image_name, colormode='color',
                           pageheight=400)
    self.message('Exported successfully to file "{}"'.format(image_name))

  def row(self):
    self.grid_row_i += 1
    return self.grid_row_i

  def column(self):
    self.grid_column_i += 1
    return self.grid_column_i

  def popup(self, event):
    self.popup_menu.post(event.x_root, event.y_root)


if __name__ == '__main__':
  app = App()
