import tkinter as tk
from typing_extensions import IntVar
import string
import random as rand


def main():
    #----Calling The First GUI To Take User Input----
    special_char,uppercase_char,number_char,dict_char,keyword_str,validate_str=GUI_display()
    #    print(special_char)
    #    print(uppercase_char)
    #    print(number_char)
    #    print(dict_char)
    #    print(keyword_str)
    #    print(validate_str)

    Password_Generator(special_char,uppercase_char,number_char,dict_char,keyword_str)





def GUI_display():

    #----Some Functions That Help In Catching Dynamic Variables----
    def save_keyword():
        keyword_generate.set(Entry1.get())
        # password_validate.set("empty")
        main_window.destroy()
    def save_password():
        password_validate.set(Entry2.get())
        # keyword_generate.set("empty")
        main_window.destroy()


    #----Creating A Window With Suitable Title And Size----
    main_window=tk.Tk()
    main_window.title("Password Generator And Validator Application")
    main_window.geometry("850x550")
    main_window.configure(bg="grey")

    #----Defining Some Varibales----
    special_char=tk.IntVar()
    uppercase_char=tk.IntVar()
    number_char=tk.IntVar()
    dict_char=tk.IntVar()
    keyword_generate=tk.StringVar()
    password_validate=tk.StringVar()

    #----Creating A Main Label----
    Label1=tk.Label(text="Password Generator And Validator",font=("Times New Roman",20),bg="grey")
    Label1.place(x=425,y=30,anchor="center")

    #----Creating Another Label----
    Label2=tk.Label(text="How secure do you want this password to be ? ",font=("Times New Roman",15),bg="grey")
    Label2.place(x=10,y=75)

    #----Creating CheckButtons To Identify Level Of Security----
    box1=tk.Checkbutton(text="Must include a special character",font=("Times New Roman",13),variable=special_char,bg="grey")
    box1.place(x=25,y=170)

    box2=tk.Checkbutton(text="Must include an upper case letter",font=("Times New Roman",13),variable=uppercase_char,bg="grey")
    box2.place(x=25,y=140)
    
    box3=tk.Checkbutton(text="Must include a number",font=("Times New Roman",13),variable=number_char,bg="grey")
    box3.place(x=25,y=110)

    box4=tk.Checkbutton(text="Must not include a word from the English dictionary",font=("Times New Roman",13),variable=dict_char,bg="grey")
    box4.place(x=25,y=200)

    #----Creating A Label For Generating----
    Label3=tk.Label(text="Generate Password",font=("Times New Roman",15),bg="grey")
    Label3.place(x=212,y=300,anchor="center")

    #----Creating A Label For Validating----
    Label3=tk.Label(text="Validate Password",font=("Times New Roman",15),bg="grey")
    Label3.place(x=613,y=300,anchor="center")

    #----Creating An Entry Field For A Keyword----
    Label4=tk.Label(text="Keyword you want to be included in your password \n(optional)",font=("Times New Roman",13),bg="grey")
    Label4.place(x=212,y=360,anchor="center")
    Entry1=tk.Entry(width="30")
    Entry1.place(x=217,y=400,anchor="center")
    Button1=tk.Button(text="Generate",font=("Times New Roman",13),command=save_keyword)
    Button1.place(x=217,y=430,anchor="center")


    #----Creating An Entry Field For A Password----
    Label5=tk.Label(text="Password you want to Validate",font=("Times New Roman",13),bg="grey")
    Label5.place(x=612,y=350,anchor="center")
    Entry2=tk.Entry(width="30")
    Entry2.place(x=617,y=397,anchor="center")
    Button2=tk.Button(text="Validate",font=("Times New Roman",13),command=save_password)
    Button2.place(x=617,y=430,anchor="center")


    main_window.mainloop()


    return special_char.get() , uppercase_char.get() , number_char.get() , dict_char.get() , keyword_generate.get(), password_validate.get()



def Password_Generator(specialChar,uppercaseChar,numberChar,dictChar,keyword):
    
    #----Making A List Of All Lowercase Letters----
    lower_case_letters=list(string.ascii_lowercase)
    
    #----Making A List For Each Of The User Specified Requirements----
    special_letters=list(string.punctuation)
    uppercase_letters=list(string.ascii_uppercase)
    numbers=list(string.digits)

    #----Making A Random List Of The Charachters----
    final_list=[]

    if specialChar==1:
        final_list.append(rand.choice(special_letters))
    if uppercaseChar==1:
        final_list.append(rand.choice(uppercase_letters))
    if numberChar==1:
        final_list.append(rand.choice(numbers))
    if keyword:
        final_list.append(keyword)

    print(final_list)
        


def function_n():
    ...


if __name__ == "__main__":
    main()