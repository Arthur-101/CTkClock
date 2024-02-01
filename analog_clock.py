import tkinter as tk
from customtkinter import *
import time
import math
from datetime import datetime, timedelta

class AnalogClock(tk.Canvas):
    def __init__(
        self,
        master,
        radius: int = 150,
        border_width: int = 3,
        border_color: str = '#b5b5b5',
        fg_color: str = "transparent",
        time_to_show: str = None,
        font: tuple = ('Calibri', 12, 'regular'),
        font_color: str = 'black',
        hour_color: str = '#383838',
        minute_color: str = '#454545',
        second_color: str = '#ff3e3e',
        hour_hand_width: int = 4,
        minute_hand_width: int = 3,
        second_hand_width: int = 1,
        bg_color: str = None,
        # **kwargs
        ):

        self.master = master
        self.radius = radius
        self.border_width = border_width
        self.border_color = border_color            
        self.time_to_show = time_to_show
        self.font = font
        self.font_color = font_color
        self.hour_color = hour_color
        self.minute_color = minute_color
        self.second_color = second_color
        self.hour_hand_width = hour_hand_width
        self.minute_hand_width = minute_hand_width
        self.second_hand_width = second_hand_width
        self.fg_color = fg_color
        self.bg_color = bg_color
        
        self.initial_time_set = False
        self.base_time = datetime.now() if not time_to_show else datetime.strptime(time_to_show, "%H:%M:%S")
        self.last_update_time = datetime.now()

        # Handling the `fg_color = "transparent"` argument
        if fg_color.lower() == 'transparent':
            try:
                if master.winfo_name().startswith("!ctkframe"):
                    # getting bg_color of customtkinter frames
                    self.fg_color = master._apply_appearance_mode(master.cget("fg_color"))
                else:
                    self.fg_color = master.cget("bg")
            except:  
                self.fg_color = "white"
        else:
            self.fg_color = fg_color

        # Setting the canvas background color to match the parent's background color
        if not self.bg_color:
            try:
                if master.winfo_name().startswith("!ctkframe"):
                    # getting bg_color of customtkinter frames
                    self.bg_color = master._apply_appearance_mode(master.cget("fg_color"))
                else:
                    self.bg_color = master.cget("bg")
            except:  
                self.bg_color = "white"
        
        super().__init__(self.master, bg=self.bg_color, width=2 * radius, height=2 * radius, bd=0, highlightthickness=0)


        # Start the clock update loop
        self.update_clock()

    def update_clock(self):
        """
        Update the clock display with the current time, and schedule the next update.
        """
        now = datetime.now()
        if not self.initial_time_set:
            # Set the initial time based on time_to_show or the current time
            self.initial_time_set = True
            self.last_update_time = now

        # Calculate the time difference since the last update
        time_difference = now - self.last_update_time
        # Increment the base time by this difference
        self.base_time += time_difference
        # Update the last update time for the next cycle
        self.last_update_time = now

        seconds = self.base_time.second
        minutes = self.base_time.minute
        hours = self.base_time.hour % 12
        
        self.draw_clock(seconds, minutes, hours)
        self.after(1000, self.update_clock)

    def draw_clock(self, seconds, minutes, hours):
        """
        Draw a clock on the canvas based on the given seconds, minutes, and hours.
        Parameters:
            hours (int): The hours component of the time.
            minutes (int): The minutes component of the time.
            seconds (int): The seconds component of the time.
        """
        self.delete("all")

        # Draw clock face with a slight padding
        padding = 5
        self.create_oval(padding, padding, 2 * (self.radius - padding), 2 * (self.radius - padding),
                        width=self.border_width, fill=self.fg_color, outline=self.border_color)

        # Draw clock numbers
        for i in range(1, 13):
            angle = math.radians(i * 30)
            x = self.radius + self.radius * 0.8 * math.sin(angle)
            y = self.radius - self.radius * 0.8 * math.cos(angle)
            self.create_text(x, y, text=str(i), font=self.font, fill=self.font_color)

        # Draw hour hand
        hour_angle = math.radians((hours % 12) * 30 + (minutes / 60) * 30)
        hour_x = self.radius + self.radius * 0.4 * math.sin(hour_angle)
        hour_y = self.radius - self.radius * 0.4 * math.cos(hour_angle)
        self.create_line(self.radius, self.radius, hour_x, hour_y, width=self.hour_hand_width, fill=self.hour_color)

        # Draw minute hand
        minute_angle = math.radians(minutes * 6 + (seconds / 60) * 6)
        minute_x = self.radius + self.radius * 0.6 * math.sin(minute_angle)
        minute_y = self.radius - self.radius * 0.6 * math.cos(minute_angle)
        self.create_line(self.radius, self.radius, minute_x, minute_y,
                                width=self.minute_hand_width, fill=self.minute_color)

        # Draw second hand
        second_angle = math.radians(seconds * 6)
        second_x = self.radius + self.radius * 0.7 * math.sin(second_angle)
        second_y = self.radius - self.radius * 0.7 * math.cos(second_angle)
        self.create_line(self.radius, self.radius, second_x, second_y,
                                width=self.second_hand_width, fill=self.second_color)
    

