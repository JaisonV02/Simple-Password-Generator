# Import tkinter library to create a GUI interface
from tkinter import *
from tkinter import messagebox

# Import generate() function from PasswordGenerator.py
from PasswordGenerator import generate

# Function to call the function which generates a password
def get_password():
    password = generate(range_slider.get(), uppercase.get(), numbers.get(), special.get())
    password_label.config(text=password)

# Function which allows the user to copy the password to their clipboard
def copy_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_label.cget('text'))
    messagebox.showinfo('Password copied', 'Your password was copied to the clipboard')

# Create window object using tkinter
window = Tk()
window.minsize(450, 200)

# Set the title and icon
icon = PhotoImage(file='Resources\\access-hand-key-icon.png')
window.iconphoto(True, icon)
window.title('Password Generator')

# Adding Widgets
# Adding a range slider to select the length of the password
range_slider = Scale(window, from_=4, to=60, orient=HORIZONTAL)
range_slider.set(8)
range_slider.pack()

# Adding Checkboxes for user options
# Checkbox for uppercase letters
uppercase = IntVar()
check_button1 = Checkbutton(window, text='Uppercase Letters ABC', variable=uppercase)
check_button1.pack()

# Checkbox for numbers
numbers = IntVar()
check_button2 = Checkbutton(window, text='Numbers 0-9', variable=numbers)
check_button2.pack()

# Checkbox for special characters
special = IntVar()
check_button3 = Checkbutton(window, text='Special Characters !?@#', variable=special)
check_button3.pack()

# Button to generate password
generate_button = Button(window, text='Generate Password', command=get_password)
generate_button.pack()

# Label to display password
password_label = Label(window, text='')
password_label.pack()

# Button to copy password
copy_button = Button(window, text='Copy', command=copy_clipboard)
copy_button.pack()

# Display the window to the user's screen
window.mainloop() 
