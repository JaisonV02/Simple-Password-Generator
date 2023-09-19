# Simple-Password-Generator

A program which generates a password for the user.
This password generator was created using Python.

## Features
This program has a GUI which was built using the tkinter library.
The user is able to select what the password contains by using the slider and selecting the checkbox.
The user is able to select:
- Password length
- Uppercase letters (ABC)
- Numbers (0-9)
- Special characters (@!~? etc.)

The user can generate a password using the generate button.
The password can be copied to the clipboard by pressing the copy button.

## How to run the program
To run the program, run the Main.pyw file.
Make sure that python is installed on your system.

## Contents
This program contains two python files:
- Main.pyw
- PasswordGenerator.py

The Main.pyw file contains all the tkinter configurations and calls the function inside PasswordGenerator.py.
The PasswordGenerator.py contains the function which generates the password

There is an image inside the Resources folder which is used as an icon for the tkinter window

## Limitations
The password generator only generates a password with the max size of 60 because there is usually no need for passwords as big as this

If you've selected extra requirements such as uppercase, numbers and special characters, make sure that you select an appropriate length for the password.
This is because there is a chance that some of these requirements which were selected is not shown in the password because of its short length, so the random genereator never generated a character for that requirement.
