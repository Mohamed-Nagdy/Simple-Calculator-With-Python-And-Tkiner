'''

    Created by Mohamed Nagdy
    Date At 26-10-2019
    this is a small and simple calculator with tkinter and python
    it just used for learn how python work and lists and arithmetic operations in python
    it for learn and the beginners in programming and specific python programming with tkinter

'''

# importing tkinter library
from tkinter import *

# create our scene or our main window
root = Tk()

# this is the text box for enter the numbers and show all results
calculatorScreen = Entry(root, width=40)

# these lists for the enterd numbers and also for the signs entered (+, -, /, *)
numberList = []
signsList = []


# this function used for take numbers from the buttons and put it on the text box
# and this function is called from the buttons
def setNumber(number):
    # take the old number
    numberWasIn = calculatorScreen.get()
    # remove any text from the screen
    calculatorScreen.delete(0, END)
    # put the new number on the screen
    calculatorScreen.insert(0, str(numberWasIn) + str(number))


# this function for add '+' to the signs list when click add
def add():
    numberList.append(calculatorScreen.get())
    signsList.append('+')
    calculatorScreen.delete(0, END)


# this function for add '-' to the signs list when click sub button
def sub():
    numberList.append(calculatorScreen.get())
    signsList.append('-')
    calculatorScreen.delete(0, END)


# this function for add '*' to the signs list when click multiply button
def mul():
    numberList.append(calculatorScreen.get())
    signsList.append('*')
    calculatorScreen.delete(0, END)


# this function for add '/' to the signs list when click div button
def div():
    numberList.append(calculatorScreen.get())
    signsList.append('/')
    calculatorScreen.delete(0, END)


# this function to reset all the variables and clear the screen
def clear():
    global numberList
    global signsList
    numberList.clear()
    signsList.clear()
    calculatorScreen.delete(0, END)


# this for print the final result to the screen
def equal():
    # import the global variables we declared
    global numberList
    global signsList

    # get the last number we just entered before click equeal button and clear the screen
    numberList.append(calculatorScreen.get())
    calculatorScreen.delete(0, END)

    # while loop it loop on the numbers list and take all numbers untill it's length become 1
    while len(numberList) > 1:
        # pop the first number from the list
        firstNumber = int(numberList.pop(0))

        # this loop for check the sign and do it's operation between the first number and the number after it
        for i in range(len(signsList)):
            result = 0
            # the summation operation
            if signsList[i] == '+':
                result = firstNumber + int(numberList.pop(0))
                numberList.insert(0, result)

            # the subtraction operation
            if signsList[i] == '-':
                result = firstNumber - int(numberList.pop(0))
                numberList.insert(0, result)

            # the multiplication operation
            if signsList[i] == '*':
                result = firstNumber * int(numberList.pop(0))
                numberList.insert(0, result)

            # the division operation
            if signsList[i] == '/':
                if int(numberList[0]) == 0:
                    calculatorScreen.delete(0, END)
                    calculatorScreen.insert(0, "infinity")
                else:
                    result = firstNumber / int(numberList.pop(0))
                    numberList.insert(0, result)

    # after all the operations has done we show the result on the screen
    calculatorScreen.insert(0, numberList[0])


'''
    here we create the elements of our scene or our calculator every button has the following attributes
    width = 30, height= 20, background = #EEEEEE, textColor= blue , textOnIt = text, border= 2 and the command is the 
    function name and the function which need an parameter we call it using lambda
    the buttons clear and equal are different in width
'''
button1 = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text=1, bd=2, command=lambda: setNumber(1))
button2 = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text=2, bd=2, command=lambda: setNumber(2))
button3 = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text=3, bd=2, command=lambda: setNumber(3))
button4 = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text=4, bd=2, command=lambda: setNumber(4))
button5 = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text=5, bd=2, command=lambda: setNumber(5))
button6 = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text=6, bd=2, command=lambda: setNumber(6))
button7 = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text=7, bd=2, command=lambda: setNumber(7))
button8 = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text=8, bd=2, command=lambda: setNumber(8))
button9 = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text=9, bd=2, command=lambda: setNumber(9))
button0 = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text=0, bd=2, command=lambda: setNumber(0))

add = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text="+", bd=2, command=add)
sub = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text="-", bd=2, command=sub)
mul = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text="*", bd=2, command=mul)
div = Button(root, padx=30, pady=20, bg="#EEEEEE", fg="blue", text="/", bd=2, command=div)

clear = Button(root, padx=70, pady=20, bg="#EEEEEE", fg="blue", text="c", bd=2, command=clear)
equal = Button(root, padx=150, pady=20, bg="#EEEEEE", fg="blue", text="=", bd=2, command=equal)

# here we put the elements on the scene using grid method

calculatorScreen.grid(column=0, row=0, columnspan=3)
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)

button4.grid(column=0, row=2)
button5.grid(column=1, row=2)
button6.grid(column=2, row=2)

button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)


add.grid(column=3, row=1)
sub.grid(column=3, row=2)
mul.grid(column=3, row=3)
div.grid(column=3, row=4)


equal.grid(column=0, row=5, columnspan=4)
clear.grid(column=0, row=4, columnspan=2)
button0.grid(column=2, row=4)

# start the main loop of our calculator
root.mainloop()