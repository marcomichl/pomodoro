'''
This App implements a simple pomodoro timer.
It has fixed timings (pomodoro, short break, long break) that are defined herin.
After 3 cycles (each containing out of a pomodoro and a short break) a long break is performed.

The total concept of pomodoro is to write down the tasks that shall be performed and then the timer is started.
Within the pomodoro time, these tasks are performed. Between are short and long breaks that can be used for other activities.

'''

from tkinter import *

TIME_POMODORO = 25     # Time a pomodoro shall take
TIME_SHORT_BREAK = 5
TIME_LONG_BREAK = 15

INTERVALS = 3

currentTimer = 0
currentInterval = 0
currentState = 0    # 0 = undefined, 1 = pomodoro, 2 = short break, 3 = long break
pause = False

timer = None

timerLabel = None
intervalLabel = None
stateLabel = None

startStopButton = None
resetButton = None

def startStop():
    global pause

    if not pause:
        pause = True
        startStopButton.config(text="Start")
    else:
        pause = False
        startStopButton.config(text="Stop")

def decrease():
    global currentInterval
    global currentTimer
    global currentState

    if not pause:
        currentTimer = currentTimer - 1

    if currentTimer <= 0:
        if currentState == 1:
            if currentInterval < INTERVALS:
                currentState = 2
                currentTimer = TIME_SHORT_BREAK * 60
            if currentInterval >= INTERVALS:
                currentState = 3
                currentTimer = TIME_LONG_BREAK * 60
        elif currentState == 2:
            currentInterval = currentInterval + 1
            currentState = 1
            currentTimer = TIME_POMODORO * 60
        else :
            reset()
    
    updateGui()
    timerLabel.after(1000, decrease)

def updateIntervalLabel():
    return "Interval:   {} / {}".format(currentInterval, INTERVALS)

def updateStateLabel():
    if currentState == 1:
        return "Pomodoro"
    elif currentState == 2:
        return "Short Break"
    elif currentState == 3:
        return "Long Break"
    else:
        return "Undefined"

def updateTimerLabel():
    min = currentTimer // 60
    sec = currentTimer % 60

    return "{:02d} : {:02d}".format(min, sec)

def updateGui():
    timerLabel.config(text=updateTimerLabel())
    intervalLabel.config(text=updateIntervalLabel())
    stateLabel.config(text=updateStateLabel())

def reset():
    global currentInterval
    global currentTimer
    global currentState
    global pause

    currentTimer = TIME_POMODORO * 60
    currentState = 1
    currentInterval = 1

    pause = True
    startStopButton.config(text="Start")

root = Tk()
root.title("Pomodoro Timer")
timerLabel = Label(root, text=updateTimerLabel, font=("Courier", 30, "bold"))
timerLabel.grid(row=1, column=0, padx='5', pady='5', columnspan=2)
intervalLabel = Label(root)
intervalLabel.grid(row=0, column=0, padx='5', pady='5')
stateLabel = Label(root)
stateLabel.grid(row=0, column=1, padx='40', pady='5')

startStopButton = Button(root, text="Start", width=20, command=startStop)
startStopButton.grid(row=2, column=0, padx='5', pady='5')
resetButton = Button(root, text="Reset", width=20, command=reset)
resetButton.grid(row=2, column=1, padx='5', pady='5')

reset()
decrease()

root.mainloop()






