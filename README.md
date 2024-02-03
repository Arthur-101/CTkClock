# CTkClock
**A Library for CLock widget in Tkinter and CTkinter.**

## Installation
##### Since this Library is not yet ready, it's not published yet.
##### Download the folder and put it inside this directory to use:
`c:\users\me\appdata\local\programs\python\python38\lib\site-packages`

# AnalogCLock

## Usage

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

