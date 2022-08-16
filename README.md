# Password Generator And Validator With GUI

### Video demo: [click to visit](https://youtu.be/cnbeK9R2sDk)
    
## Description:
    
    User friendly password generator and validator.

    Through an interactive GUI, the user chooses what level of security they want their password to be, then 
    they can choose to either:

    1- Generate a password meeting those requirements

    2- Validate if a certain password is meeting those requirements or not


    A strong security level can be achieved by making sure the password does not contain any actual words 
    from the English dictionary, but instead the password is a random sequence of letters,number and special 
    characters.
    
# Project files
    
## project.py

The main file

It is responsible for creating the GUI window and displaying it to the user, Then it waits for user's
interactive input, and depending on that it calls the appropriate function

It contains the password_generator function that is responsible for creating a random list of 
characters that are then put together into a string and returned as password

It contains the password_validator function that checks if the passed password is meeting all the requirements
passed in by the user and returns True if so

It is responsible for creating another window and displaying either the generated/validated outcome

It contains other small functions that are used multiple times to avoid code duplication. They are pytested
in the test_project.py file

## test_project.py

The testing file (pytest)

It contains 3 function that assert some corner cases that may  be taken during input

It tests the password_validator function by taking the password and the requirements that should be met

It tests the check_in_dictionary function by taking a string and checking if it contains a word that is in 
the English dictionary by searching through the "words.txt" file

It tests the generated password by making sure that it actually meets all the requirements before actually
it is displayed to the user

## words.txt

A text file consisting of about 6,000 lines containing all the words in the English dictionary

This file is opened and read in the project.py file whenever we check for words in a password

## requirements.txt

A text file containing the pip installable libraries that are needed to run this program



