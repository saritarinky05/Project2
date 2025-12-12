from tkinter import *						
import math
import tkinter.messagebox
import numpy as np

root = Tk()                                 # Create the main window by Tk() class of tkinter
root.title("Scientific Calculator")
root.configure(background = 'grey')  # Set background color of the calculator
root.resizable(width=False, height=False)   # Prevent resizing of the calculator window
root.geometry("450x550+0+0")             	# Set the default size of the calculator with position on the screen
calc = Frame(root)							# Create a frame inside the main window to hold calculator widgets
calc.grid()									# Use grid layout manager for placing widgets	

class Calc():                               # Create a class Calc to handle calculator operations
	def __init__(self):                     # Initialize the class with necessary variables
		self.total=0                        # To store the total value of calculations 
		self.current=''                     # To store the current input value
		self.input_value=True               # Flag to check if input is being entered
		self.check_sum=False                # Flag to check if a calculation is pending
		self.op=''                          # To store the current operation
		self.result=False                   # Flag to check if the result is displayed

	def numberEnter(self, num):             # Method to handle number entry
		self.result=False
		firstnum=txtDisplay.get()           # Get the current value from the display
		secondnum=str(num)                  # Convert the entered number to string
		if self.input_value:				
			self.current = secondnum       	
			self.input_value=False			
		else:
			if secondnum == '.':			# Handle decimal point entry
				if secondnum in firstnum:
					return
			self.current = firstnum+secondnum
		self.display(self.current)

	def sum_of_total(self):
		self.result=True
		self.current=float(self.current)
		if self.check_sum==True:
			self.valid_function()
		else:
			self.total=float(txtDisplay.get())

	def display(self, value):
		txtDisplay.delete(0, END)
		txtDisplay.insert(0, value)

	def valid_function(self):
		if self.op == "add":
			self.total += self.current
		if self.op == "sub":
			self.total -= self.current
		if self.op == "multi":
			self.total *= self.current
		if self.op == "divide":
			self.total /= self.current
		if self.op == "mod":
			self.total %= self.current
		if self.op == "pow":
			self.total = math.pow(self.total, self.current)
		self.input_value=True
		self.check_sum=False
		self.display(self.total)

	def operation(self, op):								# Method to handle operations like add, subtract, multiply, divide
		self.current = float(self.current)
		if self.check_sum:						
			self.valid_function()
		elif not self.result:
			self.total=self.current
			self.input_value=True
		self.check_sum=True
		self.op=op
		self.result=False

	def Clear_Entry(self):									# Method to clear the current entry
		self.result = False
		self.current = "0"
		self.display(0)
		self.input_value=True

#	def All_Clear_Entry(self):								# Method to clear all entries and reset the calculator	
#		self.Clear_Entry()
#		self.total=0

	def Delete(self):										# Method to delete the last character from the current entry
		self.result = False
		self.current = str(txtDisplay.get())[:-1]
		self.display(self.current)

	def pi(self):				
		self.result = False
		self.current = math.pi
		self.display(self.current)

	def dpi(self):											# Method to insert the value of tau (2*pi)
		self.result = False
		self.current = math.tau
		self.display(self.current)

	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)

	def abs(self):											# Method to calculate absolute value of the current entry
		self.result = False
		self.current = abs(float(txtDisplay.get()))
		self.display(self.current)

	def mathPM(self):													# Method to change the sign of the current entry
		self.result = False
		self.current = -(float(txtDisplay.get()))
		self.display(self.current)

	def sqroot(self):							
		self.result = False
		self.current = math.sqrt(float(txtDisplay.get()))				# calculate square root of the input value
		self.display(self.current)

	def cos(self):
		self.result = False
		self.current = math.cos(math.radians(float(txtDisplay.get())))	# calculate cosine in radians of the input value
		self.display(self.current)

	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(float(txtDisplay.get())))	# calculate hyperbolic cosine in radians of the input value
		self.display(self.current)

	def tan(self):
		self.result = False
		self.current = math.tan(math.radians(float(txtDisplay.get())))	# calculate tangent in radians of the input value
		self.display(self.current)

	def tanh(self):
		self.result = False
		self.current = math.tanh(math.radians(float(txtDisplay.get())))	# calculate hyperbolic tangent in radians of the input value
		self.display(self.current)

	def sin(self):
		self.result = False
		self.current = math.sin(math.radians(float(txtDisplay.get())))	# calculate sine in radians of the input value
		self.display(self.current)

	def sinh(self):
		self.result = False
		self.current = math.sinh(math.radians(float(txtDisplay.get())))	# calculate hyperbolic sine in radians of the input value
		self.display(self.current)

	def log(self):
		self.result = False
		self.current = math.log(float(txtDisplay.get()))				# calculate natural logarithm of the input value
		self.display(self.current)

	def exp(self):														
		self.result = False
		self.current = math.exp(float(txtDisplay.get()))				# calculate exponential (e^x) of the input value
		self.display(self.current)

	def acosh(self):
		self.result = False
		self.current = math.acosh(float(txtDisplay.get()))				# calculate inverse hyperbolic cosine of the input value
		self.display(self.current)

	def asinh(self):
		self.result = False
		self.current = math.asinh(float(txtDisplay.get()))				# calculate inverse hyperbolic sine of the input value
		self.display(self.current)

	def inverse(self):
		self.result = False
		self.current = np.reciprocal(float(txtDisplay.get()))				# calculate reciprocal (1/x) for the input value
		self.display(self.current)

	def factorial(self):
		self.result = False
		self.current = math.factorial(int(txtDisplay.get()))			# calculate factorial of the input value
		self.display(self.current)

	def degrees(self):
		self.result = False
		self.current = math.degrees(float(txtDisplay.get()))			# convert radians to degrees for the input value
		self.display(self.current)

	def log2(self):
		self.result = False
		self.current = math.log2(float(txtDisplay.get()))				# calculate base-2 logarithm of the input value
		self.display(self.current)

	def log10(self):
		self.result = False
		self.current = math.log10(float(txtDisplay.get()))				# calculate base-10 logarithm of the input value
		self.display(self.current)
		
added_value = Calc()													# Create an instance of the Calc class

txtDisplay = Entry(calc, font=('Times New Roman',20,'bold'),			# Create the display entry widget
				bg='black',fg='white',
				bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)	
txtDisplay.insert(0,"0")

# Define buttons and their placements here
numberpad = "789456123"
i=0
btn = []
for j in range(2,5):
	for k in range(3):
		btn.append(Button(calc, width=6, height=2, bg='white',fg='black', font=('Times New Roman',20,'bold'),
		bd=4, text=numberpad[i]))
		btn[i].grid(row=j, column=k, pady=1)
		btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
		i+=1


btnClear = Button(calc, text=chr(67),
					width=6, height=2, bg='powder blue',
					font=('Times New Roman',20,'bold'), bd=4,
					command=added_value.Clear_Entry).grid(row=1, column= 0, pady = 1)

btnDel = Button(calc, text="⌫",
					width=6, height=2, bg='powder blue',
					font=('Times New Roman',20,'bold'), bd=4,
					command=added_value.Delete).grid(row=1, column= 1, pady = 1)

btnMod = Button(calc, text="%",width=6,
				height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
				bd=4,command=lambda:added_value.operation("mod")
				).grid(row=1, column= 2, pady = 1)

btnAdd = Button(calc, text="+",width=6, height=2,
				bg='powder blue', font=('Times New Roman',20,'bold'),
				bd=4,command=lambda:added_value.operation("add")
				).grid(row=1, column= 3, pady = 1)

btnSub = Button(calc, text="-",width=6,
				height=2,bg='powder blue', font=('Times New Roman',20,'bold'),
				bd=4,command=lambda:added_value.operation("sub")
				).grid(row=2, column= 3, pady = 1)

btnMul = Button(calc, text="x",width=6,
				height=2,bg='powder blue', font=('Times New Roman',20,'bold'),
				bd=4,command=lambda:added_value.operation("multi")
				).grid(row=3, column= 3, pady = 1)

btnDiv = Button(calc, text="/",width=6,
				height=2,bg='powder blue', font=('Times New Roman',20,'bold'),
				bd=4,command=lambda:added_value.operation("divide")
				).grid(row=4, column= 3, pady = 1)

btnPM = Button(calc, text=chr(177),width=6,
			height=2,bg='powder blue', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.mathPM
			).grid(row=5, column= 0, pady = 1)

btnZero = Button(calc, text="0",width=6,
				height=2,bg='white',fg='black', font=('Times New Roman',20,'bold'),
				bd=4,command=lambda:added_value.numberEnter(0)
				).grid(row=5, column= 1, pady = 1)

btnDot = Button(calc, text=".",width=6,
				height=2,bg='powder blue', font=('Times New Roman',20,'bold'),
				bd=4,command=lambda:added_value.numberEnter(".")
				).grid(row=5, column= 2, pady = 1)

btnEquals = Button(calc, text="=",width=6,
				height=2,bg='powder blue',
				font=('Times New Roman',20,'bold'),
				bd=4,command=added_value.sum_of_total
				).grid(row=5, column= 3, pady = 1)

#*****************************************SCIENTIFIC BUTTONS: 1st Row***********************************************

btnAbs = Button(calc, text="|x|",width=6,
				height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
				bd=4,command=added_value.abs
				).grid(row=1, column= 4, pady = 1)

btninverse = Button(calc, text="1/x",width=6,
				height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
				bd = 4,command=added_value.inverse
				).grid(row=1, column= 5, pady = 1)

btnpower = Button(calc, text="x^y",width=6,
				height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
				bd=4,command=lambda:added_value.operation("pow")
				).grid(row=1, column= 6, pady = 1)

btnSqrt = Button(calc, text="√",width=6,
				height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
				bd=4,command=added_value.sqroot
				).grid(row=1, column= 7, pady = 1)

#*****************************************SCIENTIFIC BUTTONS: 2nd Row***********************************************

btnPi = Button(calc, text="π",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.pi
			).grid(row=2, column= 4, pady = 1)

btnsin = Button(calc, text="sin",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.sin
			).grid(row=2, column= 5, pady = 1)

btncos = Button(calc, text="cos",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.cos
			).grid(row=2, column= 6, pady = 1)

btntan = Button(calc, text="tan",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.tan
			).grid(row=2, column= 7, pady = 1)

#*****************************************SCIENTIFIC BUTTONS: 3rd Row***********************************************

btnDpi = Button(calc, text="2π",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.dpi
			).grid(row=3, column= 4, pady = 1)

btnsinh = Button(calc, text="sinh",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.sinh
			).grid(row=3, column= 5, pady = 1)

btncosh = Button(calc, text="cosh",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.cosh
			).grid(row=3, column= 6, pady = 1)

btntanh = Button(calc, text="tanh",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.tanh
			).grid(row=3, column= 7, pady = 1)

#*****************************************SCIENTIFIC BUTTONS: 4th Row***********************************************

btne = Button(calc, text="e",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.e
			).grid(row=4, column= 4, pady = 1)

btnasinh = Button(calc, text="asinh",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.asinh
			).grid(row=4, column= 5, pady = 1)

btnacosh = Button(calc, text="acosh",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.acosh
			).grid(row=4, column= 6, pady = 1)

btnfact = Button(calc, text="x!",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.factorial
			).grid(row=4, column= 7, pady = 1)

#*****************************************SCIENTIFIC BUTTONS: 5th Row***********************************************

btnexp = Button(calc, text="e^x",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.exp
			).grid(row=5, column= 4, pady = 1)

btnlog = Button(calc, text="log",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.log
			).grid(row=5, column= 5, pady = 1)

btnlog2 = Button(calc, text="log2",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.log2
			).grid(row=5, column= 6, pady = 1)

btndegrees = Button(calc, text="deg",width=6,
			height=2,bg='powder blue',fg='black', font=('Times New Roman',20,'bold'),
			bd=4,command=added_value.degrees
			).grid(row=5, column= 7, pady = 1)

#*****************************************Scintific Calculator LABEL DISPLAY*******************************************************

lblDisplay = Label(calc, text = "Scientific Calculator",
				font=('Times New Roman',30,'bold'),
				bg='powder blue',fg='black',justify=LEFT)

lblDisplay.grid(row=0, column= 4,columnspan=4)

#*************************************************MENUBAR*************************************************

def iExit():
	iExit = tkinter.messagebox.askyesno("Scientific Calculator","Do you want to exit ?")
	if iExit>0:
		root.destroy()
		return

def Scientific():
	root.resizable(width=False, height=False)
	root.geometry("894x550+0+0")

def Standard():
	root.resizable(width=False, height=False)
	root.geometry("450x550+0+0")

menubar = Menu(calc)

#*******************************************FILE MENU*************************************************

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

#*******************************************EDIT MENU*************************************************

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut", command=lambda: txtDisplay.event_generate("<<Cut>>"))
editmenu.add_command(label = "Copy", command=lambda: txtDisplay.event_generate("<<Copy>>"))
filemenu.add_separator()
editmenu.add_command(label = "Paste", command=lambda: txtDisplay.event_generate("<<Paste>>"))

root.config(menu=menubar)

root.mainloop()
