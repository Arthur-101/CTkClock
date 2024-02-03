# CTkClock
**A Library for CLock widget in Tkinter and CTkinter.**

## Installation
Download the folder and put it inside:
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
