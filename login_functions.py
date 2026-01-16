
import time
import menu_functions
#import database_functions

def login_sex():
    """
    Docstring for login
    :return: "Female" or "Male"
    This function prompts the user to choose their sex
    param sex: The sex input by the user
    param stripped: trimmed input
    param formatted_sex: formatted input to uppercase first letter
    """
    while True:
        try:
            sex = input("Sex: (F/M):")
            stripped = sex.strip()
            if not stripped:
                raise KeyboardInterrupt
            formatted_sex = stripped.upper()[0]
            if formatted_sex not in ("F", "M"):
                raise ValueError
        except ValueError:
            menu_functions.line()
            print("\033[31mInput ERROR! Please enter F or M.\033[m")
        except KeyboardInterrupt:
            menu_functions.line()
            print("\033[31mInput ERROR! Sex cannot be empty.\033[m")
        else:
            break

    if formatted_sex == 'F':
        return "Female"
    else:
        return "Male"
        
def time_sleep():
    print("Signing in.")
    time.sleep(1)
    print("Signing in..")
    time.sleep(1)
    print("Signing in...")
    time.sleep(1)
    print("Welcome!")
        



def login():
    library={}
    
    while True:
        while True:
            try:
                #Username:
                library['first name'] = str(input("First name:"))
                if not library['first name'].isalpha():
                    raise ValueError("Error! invalid name")



                #se nome não for str levanta erro
            except (ValueError,TypeError,IndexError):
                menu_functions.line()
                print("\033[31mInput ERROR! Please enter the data correctly.\033[m")
            except KeyboardInterrupt:
                menu_functions.line()
                print("\033[31mInput ERROR! First name cannot be empty.\033[m")
            else:
                if library['first name'].isalpha():
                   break
        
        while True:
            try:
                library['second name']= (input("Second name:"))
            
                if not library['second name'].isalpha():
                    raise ValueError("Error! invalid name")
            except (ValueError,TypeError,IndexError):
                menu_functions.line()
                print("\033[31mInput ERROR! Please enter the data correctly.\033[m")
            except KeyboardInterrupt:
                menu_functions.line()
                print("\033[31mInput ERROR! Second name cannot be empty.\033[m")
            else:
                break

            


        
        while True:
            try:
                library['Age']=int(input("Age:"))
                if library['Age']<0:
                    raise ValueError("error! negative age")
                if library['Age']>130:
                    raise ValueError("error! age too high")
            except (ValueError,TypeError,IndexError):
                menu_functions.line()
                print("\033[31mInput ERROR! Please enter the data correctly.\033[m")
            except KeyboardInterrupt:
                menu_functions.line()
                print("\033[31mInput ERROR! Age cannot be empty.\033[m")
            else:
                break
        while True:
        
            try:
                    
                library['telefone']=str(input("Telefone:").replace("-",""))
                library['telefone']=int(library['telefone'])
            except (ValueError,TypeError,IndexError):
                menu_functions.line()
                print("\033[31mInput ERROR! Please enter the data correctly.\033[m")
                continue
            except KeyboardInterrupt:
                menu_functions.line()
                print("\033[31mInput ERROR! telefone cannot be empty.\033[m")
            else:
                break
        while True:
            try:
                library["sex"]=login_sex()
            except (ValueError,TypeError,IndexError):
                menu_functions.line()
                print("\033[31mInput ERROR! Please enter the data correctly.\033[m")
            except KeyboardInterrupt:
                menu_functions.line()
                print("\033[31mInput ERROR! sex cannot be empty.\033[m")
            else:
                break
        while True:
            try:
                library['saldo']=float(input("Initial balance:\n(Negative value is not allowed) R$"))
                if library['saldo']<0:
                    raise ValueError("error! negative balance")
            except KeyboardInterrupt:
                menu_functions.line()
                print("\033[31mInput ERROR! balance cannot be empty.\033[m")
            except (ValueError,TypeError,IndexError):
                menu_functions.line()
                print("\033[31mInput ERROR! Please enter the data correctly.\033[m")
            else:
                time_sleep()
                break
        #else:

        return library
        #return database


















#option01=option()
#print(f"Option chosen: {option01}")
#if option01==False:
#    break