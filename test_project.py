from project import *


def test_Password_Validator():
    assert Password_Validator(0,0,0,0,"easypassword")==1
    assert Password_Validator(1,0,0,0,"easypassword")==0
    assert Password_Validator(0,1,0,0,"easypassword")==0
    assert Password_Validator(0,0,1,0,"easypassword")==0
    assert Password_Validator(0,0,0,1,"easypassword")==0
    assert Password_Validator(1,0,0,0,"thisIsCs50p")==0
    assert Password_Validator(1,0,0,0,"thisIsCs50p_")==1
    assert Password_Validator(0,1,1,0,"thisIsCs50p")==1
    assert Password_Validator(0,0,0,1,"thisIsCs50p")==0
    assert Password_Validator(1,1,1,1,"rndm_CS50P")==1



def test_check_in_dictionary():
    assert check_in_dictionary("bnhhcatuu",1,["q","2"],1)==0
    assert check_in_dictionary("bnhhcatuu",0,["q","2"],1)==1
    assert check_in_dictionary("qwot_pp21",1,["q","2"],1)==1
    assert check_in_dictionary("npnpnp_ALIEN_21pss",1,["q","2"],1)==0
    assert check_in_dictionary("password_containing_words",0,["q","2"],1)==1
    assert check_in_dictionary("password_containing_words",1,["q","2"],1)==0
    assert check_in_dictionary("smbols_21avg",1,["q","2"],1)==1
    assert check_in_dictionary("123456789",1,["q","2"],1)==1
    assert check_in_dictionary("I_LOVE_CS50",0,["q","2"],1)==1
    assert check_in_dictionary("I_LOVE_CS50",1,["q","2"],1)==0



def test_check_generated_password():
    assert check_generated_password("secure_password","password",["password","s","e","c","u","r","e","_"])==1
    assert check_generated_password("secure_password","password",["password","s","e","c","u","r","e"])==0
    assert check_generated_password("secure_password","password",["s","e","c","u","r","e"])==0
    assert check_generated_password("secure_password","",["password","s","e","c","u","r","e"])==0
    assert check_generated_password("oope3/cat_","cat",["cat","o","o","p","e","3","/","_"])==1
    assert check_generated_password("oope3/cat_","cat",["cat","o","o","p","e","3","/","_","i"])==0
    assert check_generated_password("oope3/cat_","cat",["cat","o","o","p","e","3","/"])==0
    assert check_generated_password("oope3/cat_","",["c","a","t","o","o","p","e","3","/","_"])==1
    assert check_generated_password("BYEBYE_CS50P","CS50P",["B","Y","E","CS50P","B","Y","E","_"])==1
    assert check_generated_password("BYEBYE_CS50P","CS50P",["b","y","e","cs50p","b","y","e","_"])==0

    

#----GUI Functions Not Tested By PyTest----



