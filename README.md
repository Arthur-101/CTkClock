# CTkClock
**A Library for CLock widget in Tkinter and CTkinter.**

## Installation
##### Since this Library is not yet ready, it's not published yet.
##### Download the folder and put it inside this directory to use:
`c:\users\me\appdata\local\programs\python\python38\lib\site-packages`

# AnalogCLock

## Usage:

**Example 1:**
```python
from tkinter import *
from CTkClock import *

root = Tk()
root.title('Tkinter example')

clock = AnalogClock(root, radius = 150,)
clock.pack()

root.mainloop()
```
![Example 1](https://github.com/Arthur-101/CTkClock/blob/main/Images/example%20clock1.png)

**Example 2:**
```python
from customtkinter import *
from CTkClock import *

root = CTk()
root.title('Custom Tkinter Example')
set_appearance_mode("dark")

clock = AnalogClock(root, radius = 150, font_color = "white", font=("Fira Code", 15, "bold"),
                    border_width=5, second_hand_width=3, minute_hand_width=5, hour_hand_width=7, 
                    hour_color='white', minute_color='white', start_time='05:15:49')
clock.pack()

root.mainloop()
```
![Example 2](https://github.com/Arthur-101/CTkClock/blob/main/Images/example%20clock2.png)

**Example 3:**
```python
from customtkinter import *
from CTkClock import *

root = CTk()
root.geometry("800x700")
root.title('Custom Tkinter Example')

clock = AnalogClock(root, radius = 160, font_color = "black", font=("Fira Code", 15, "bold"),
                    border_width=5, second_hand_width=4, minute_hand_width=6, hour_hand_width=8, )
clock.place(relx=0.05, rely=0.05,)

clock = AnalogClock(root, radius = 150, font_color = "black", font=("Fira Code", 15, "bold"), border_color='#008000',
                    border_width=5, second_hand_width=4, minute_hand_width=6, hour_hand_width=8,
                    hour_color="red", minute_color="purple", second_color="green", 
                    start_time='03:45:55', shape='rectangle', )
clock.place(relx=0.55, rely=0.05,)

clock = AnalogClock(root, radius = 150, font_color = "black", font=("Fira Code", 15, "bold"),
                    border_width=5, fg_color='#d3d3d3', 
                    quarter_hour=True,)
clock.place(relx=0.05, rely=0.55,)

clock = AnalogClock(root, radius = 150, font_color = "black", font=("Fira Code", 15, "bold"),
                    border_width=5, fg_color='#d3d3d3', 
                    quarter_hour=True, quarter_symbol='*', )
clock.place(relx=0.55, rely=0.55,)

root.mainloop()
```
![Example 3](https://github.com/Arthur-101/CTkClock/blob/main/Images/example%20clock3.png)

## Arguments:

  | Parameters  | Description  |
  | --------  | -----------  |
  | _master_  | widget or window where the clock will be placed.  |
  | _radius_  | (int): Radius of the clock in pixels.  |
  | _shape_  | (str): The shape of the clock face, either 'circle' or 'rectangle'. Default: 'circle'  |
  | _border_width_  | (int): Width of the clock border.  |
  | _border_color_  | (str): The color of the border.  |
  | _clock_face_style_  | (str): The style of clock face. Either 'Digit' or 'Roman' or 'Tick' or 'NONE'. Default: 'digit'  |
  | _fg_color_  | (str): The foreground color of the clock face or 'transparent' to match the parent's background. Default: 'transparent'  |
  | _bg_color_  | (str): The background color of the clock face or 'transparent' to match the parent's background. Default: 'transparent'  |
  | _font_  | (Tuple[str, int, str]): Font specifications for the clock numbers.  |
  | _font_color_  | (str): The color of the clock numbers.  |
  | _hour_color_  | (str): The color of the hour hand.  |
  | _minute_color_  | (str): The color of the minute hand.  |
  | _second_color_  | (str): The color of the second hand.  |
  |  _hour_hand_width_  | (int): The width of the hour hand.  |
  | _minute_hand_width_  | (int): The width of the minute hand.  |
  | _second_hand_width_  | (int): The width of the second hand.  |
  | _start_time_  | (Optional[str]): The initial time in the format 'HH:MM:SS'.  |
  | _quarter_hour_  | (bool): If True, display only 3, 6, 9, 12 and optional quarter symbols.  |
  | _quarter_symbol_  | (Optional[str]): Symbol to be displayed instead of numbers not divisible by 3.  |
  | _quarter_symbol_color_  | (Optional[str]): Color of the quarter symbols.  |

## Methods:
  | Methods  | Description  |
  | -------  | -----------  |
  | _.get_current_time()_  |  Get the current time of the clock as a datetime object.  |
  | _.get_current_strftime(format_string="%H:%M:%S")_  | Get the current time of the clock as a formatted string.  |
  | _.configure()_  | To configure some options of the clock.  |

