import tkinter as tk
import string
import random as rand


def main():
    #----Calling The First GUI To Take User Input----
    special_char,uppercase_char,number_char,dict_char,keyword_str,validate_str,mode_of_display=GUI_display()

    #----Deciding Which Window To Display To User----
    if mode_of_display==0:
        generated_password=Password_Generator(special_char,uppercase_char,number_char,dict_char,keyword_str)
        GUI_display_password(generated_password)
    elif mode_of_display==1:
        Is_Valid=Password_Validator(special_char,uppercase_char,number_char,dict_char,validate_str)
        GUI_display_validation(Is_Valid)
    


def GUI_display():

    #----Some Functions That Help In Catching Dynamic Variables----
    def save_keyword():
        keyword_generate.set(Entry1.get())
        mode.set(0)
        # password_validate.set("empty")
        main_window.destroy()
    def save_password():
        password_validate.set(Entry2.get())
        mode.set(1)
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
    mode=tk.IntVar()
    mode.set(-1)

    #----Creating A Main Label----
    Label1=tk.Label(text="Password Generator And Validator",font=("Times New Roman",20),bg="grey")
    Label1.place(x=425,y=30,anchor="center")

    #----Creating Another Label----
    Label2=tk.Label(text="How secure do you want this password to be ? ",font=("Times New Roman",15),bg="grey")
    Label2.place(x=10,y=75)

    #----Creating CheckButtons To Identify Level Of Security----
    box1=tk.Checkbutton(text="Must include special characters",font=("Times New Roman",13),variable=special_char,bg="grey")
    box1.place(x=25,y=170)

    box2=tk.Checkbutton(text="Must include upper case letters",font=("Times New Roman",13),variable=uppercase_char,bg="grey")
    box2.place(x=25,y=140)
    
    box3=tk.Checkbutton(text="Must include numbers",font=("Times New Roman",13),variable=number_char,bg="grey")
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


    return special_char.get() , uppercase_char.get() , number_char.get() , dict_char.get() , keyword_generate.get(), password_validate.get(),mode.get()



def Password_Generator(specialChar,uppercaseChar,numberChar,dictChar,keyword):
    
    #----Making A List Of All Lowercase Letters----
    lower_case_letters=list(string.ascii_lowercase)
    
    #----Making A List For Each Of The User Specified Requirements----
    special_letters=list(string.punctuation)
    uppercase_letters=list(string.ascii_uppercase)
    numbers=list(string.digits)

    #----Making A Random List Of The Characters----
    final_list=[]

    number_of_specials_letters=0
    number_of_uppercase_letters=0
    number_of_numbers=0

    if specialChar==1:
        number_of_specials_letters=rand.choice([1,2,3])
        for _ in range(number_of_specials_letters):
            final_list.append(rand.choice(special_letters))
    if uppercaseChar==1:
        number_of_uppercase_letters=rand.choice([1,2,3])
        for _ in range(number_of_uppercase_letters):
            final_list.append(rand.choice(uppercase_letters))
    if numberChar==1:
        number_of_numbers=rand.choice([1,2,3])
        for _ in range(number_of_numbers):
            final_list.append(rand.choice(numbers))


    #----checking If User Entered Keyword Is In English Dictionary When Needed To----
    add_keyword=1
    add_keyword=check_in_dictionary(keyword,dictChar,final_list,add_keyword)

    #----Finalizing The List Of Characters----
    for i in range(10-number_of_numbers-number_of_uppercase_letters-number_of_specials_letters-add_keyword):
        final_list.append(rand.choice(lower_case_letters))

    #----Cloning The final_list For Later Test----
    test_list=[]
    for letter in final_list:
        test_list.append(letter)

    #----Creating A Password From Final_List----
    password=""      
    for _ in range(len(final_list)):
        random_letter=rand.choice(final_list)
        password+=random_letter
        final_list.remove(random_letter)

    #----Checking That Password Is From Formed Random List Before Returning Password----
    Is_Valid_Password=check_generated_password(password,keyword,test_list)
    if Is_Valid_Password:
        return password
    else:
        return "Password Generated Is Invalid"

def check_generated_password(password,keyword,test_list):

    #----Making A String From The words_list----
    temp_password=""
    for word in test_list:
        temp_password+=word


    #-----Checking They Have Same Length----
    if not len(password)==len(temp_password):
        return False

    #----Making A List Of All Letters In temp_password----
    letters_list=[]
    for letter in temp_password:
        letters_list.append(letter)
    
    #----Checking If Password And temp_password Have Same Characters----
    for letter in password:
        if letter in letters_list:
            letters_list.remove(letter)
        else:
            return False

    #----If Passed All Checks----
    return True



        

def check_in_dictionary(keyword,dictChar,final_list,add_keyword):

    words_file=open("words.txt","r")
    if keyword and dictChar:
        keyword=keyword.lower()
        for line in words_file:
            if line.rstrip("\n") in keyword:
                add_keyword=0
                break
        if add_keyword==1:
            final_list.append(keyword)
    elif keyword:
        final_list.append(keyword)
    else:
        add_keyword=0

    words_file.close()
    return int(add_keyword)


def GUI_display_password(password):
    
    #----Creating A window----
    window=tk.Tk()
    window.title("Password Generator And Validator Application")
    window.geometry("650x250")
    window.configure(bg="light blue")

    #----Creating A Label----
    Label1=tk.Label(text="The Generated Password",bg="light blue",font=("Times New Roman",20))
    Label1.place(x=325,y=90,anchor="center")

    #----Creating A Label For The Password----
    Label2=tk.Label(text=password,bg="light blue",font=("Times New Roman",18))
    Label2.place(x=325,y=125,anchor="center")

    #----Display The Window----
    window.mainloop()


def Password_Validator(special_char,uppercase_char,number_char,dict_char,password):
    
    #----Defining Character Sets----
    lower_case_letters=list(string.ascii_lowercase)
    special_letters=list(string.punctuation)
    uppercase_letters=list(string.ascii_uppercase)
    numbers=list(string.digits)

    #----Check For Special Characters----
    if special_char==1:
        counter=0
        for letter in password:
            if letter in special_letters:
                break
            else:
                counter+=1
        
        if counter==len(password):
            return False

    #----Check For Uppercase Letters----
    if uppercase_char==1:
        counter=0
        for letter in password:
            if letter in uppercase_letters:
                break
            else:
                counter+=1
        
        if counter==len(password):
            return False

    #----Check For Numbers----
    if number_char==1:
        counter=0
        for letter in password:
            if letter in numbers:
                break
            else:
                counter+=1
        
        if counter==len(password):
            return False

    #----Check If Contains A Word From Dicionary----
    words_file=open("words.txt","r")
    if dict_char==1:
        for word in words_file:
            if word.rstrip("\n") in password:
                return False
        
    words_file.close()

    #----If Passed All Tests And Is Not An Empty String Return True----
    if password:
        return True
    else:
        return False
    

def GUI_display_validation(Is_Valid):

    #----Create A New Display Window----
    window=tk.Tk()
    window.title("Password Generator And Validator Application")
    window.geometry("650x250")
    window.configure(bg="light blue")

    #----Create A Label----
    Label1=tk.Label(text="Your Password Is",font=("Times New Roman",20),bg="light blue")
    Label1.place(x=325,y=50,anchor="center")

    #----Create Another Label----
    valid_text=""
    if Is_Valid:
        valid_text="Strong Enough"
    else:
        valid_text="Not Strong Enough"
    Label2=tk.Label(text=valid_text,font=("Times New Roman",20),bg="light blue")
    Label2.place(x=325,y=100,anchor="center")

    #----Display Window----
    window.mainloop()

if __name__ == "__main__":
    main()