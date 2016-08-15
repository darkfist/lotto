# widgets
from tkinter import *

window = Tk()
img = PhotoImage(file = "logo.gif")

imgLabel = Label(window, image = img)
label1 = Label(window, relief = "groove", width = 2)
label2 = Label(window, relief = "groove", width = 2)
label3 = Label(window, relief = "groove", width = 2)
label4 = Label(window, relief = "groove", width = 2)
label5 = Label(window, relief = "groove", width = 2)
label6 = Label(window, relief = "groove", width = 2)
getButton = Button(window)
resetButton = Button(window)

# layout
imgLabel.grid(row = 1, column = 1, rowspan = 2)
label1.grid(row = 1, column = 2, padx = 10)
label2.grid(row = 1, column = 3, padx = 10)
label3.grid(row = 1, column = 4, padx = 10)
label4.grid(row = 1, column = 5, padx = 10)
label5.grid(row = 1, column = 6, padx = 10)
label6.grid(row = 1, column = 7, padx = 10)
getButton.grid(row = 2, column = 2, columnspan = 4)
resetButton.grid(row = 2, column = 6, columnspan = 2)

# windows properties
window.title("Lotto - Random Number Generator")
window.resizable(0,0)
getButton.configure(text = "Generate Random Numbers")
resetButton.configure(text = "Reset")

# initial properties
label1.configure(text = "...")
label2.configure(text = "...")
label3.configure(text = "...")
label4.configure(text = "...")
label5.configure(text = "...")
label6.configure(text = "...")
resetButton.configure(state = DISABLED)

# generate random numbers
from random import sample

def generateRandomNumbers():
	nums = sample(range(1, 99), 6)
	label1.configure(text = nums[0])
	label2.configure(text = nums[1])
	label3.configure(text = nums[2])
	label4.configure(text = nums[3])
	label5.configure(text = nums[4])
	label6.configure(text = nums[5])
	getButton.configure(state = DISABLED)
	resetButton.configure(state = NORMAL)
	
def reset():
	label1.configure(text = "...")
	label2.configure(text = "...")
	label3.configure(text = "...")
	label4.configure(text = "...")
	label5.configure(text = "...")
	label6.configure(text = "...")
	getButton.configure(state = NORMAL)
	resetButton.configure(state = DISABLED)
	
getButton.configure(command = generateRandomNumbers)
resetButton.configure(command = reset)

# infite loop to sustain window
window.mainloop()