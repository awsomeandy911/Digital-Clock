import tkinter as ui
import time
# Window variable to call tkinter module
window = ui.Tk()

# Updates clock to current time
def updateClock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    AM_PM = time.strftime("%p")
    clockText = hours + ":" + minutes + ":" + seconds + " " + AM_PM
    digitalclockLabel.config(text = clockText)
    # after label allows to keep updating clock by the second (1000 miliseconds)
    digitalclockLabel.after(1000, updateClock)

# Label to hold the current time for clock
digitalclockLabel = ui.Label(window, text = "00:00:00", font = "Helvetica 100 bold")
digitalclockLabel.pack()

# use updateClock function
updateClock()

# Use main loop function on window for module to show
window.mainloop()



