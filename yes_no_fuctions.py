import time
import menu_functions


def option_contine(message="Do you want to continue? (Y/N): "):
    """"
    Docstring for option
    :return: True for Yes and False for No
    This function prompts the user to choose Yes or No.
    param yn: yes or no input from user
    param stripped: trimmed input
    param formatted_yn: formatted input to uppercase first letter
    """
    while True:
        try:
            yn = input("Do you want to continue? (Y/N): ")
            stripped = yn.strip()
            if not stripped:
                raise ValueError
            formatted_yn = stripped.upper()[0]
            if formatted_yn not in ("Y", "N"):
                raise ValueError
        except ValueError:
            print("\033[31mInput ERROR! Please enter Y or N.\033[m")
            continue

        if formatted_yn == 'Y':
            print("Continuing.")
            time.sleep(1)
            print("Continuing..")
            time.sleep(1)
            print("Continuing...")
            time.sleep(1)
            return True
        else:
            menu_functions.line()
            print("Exiting the program.")
            time.sleep(1)
            print("Exiting the program..")
            time.sleep(1)
            print("Exiting the program...")
            time.sleep(1)
            return False



# if option_continue==False:
#    break

def option_quit(message="Do you want to quit? (Y/N): "):
    """
    Docstring for option_quit
    
    :param message: Description
    :return: True for Yes and False for No
    This function prompts the user to choose Yes or No.
    param yn: yes or no input from user
    param stripped: trimmed input
    param formatted_yn: formatted input to uppercase first letter
    """
    
    while True:
        try:
            yn = input(message)
            stripped = yn.strip()
            if not stripped:
                raise ValueError
            formatted_yn = stripped.upper()[0]
            if formatted_yn not in ("Y", "N"):
                raise ValueError
        except ValueError:
            print("\033[31mInput ERROR! Please enter Y or N.\033[m")
            continue

        if formatted_yn == 'N':
            print("Continuing.")
            time.sleep(1)
            print("Continuing..")
            time.sleep(1)
            print("Continuing...")
            time.sleep(1)
            return False
        else:
            menu_functions.line()
            print("Exiting the program.")
            time.sleep(1)
            print("Exiting the program..")
            time.sleep(1)
            print("Exiting the program...")
            time.sleep(1)
            return True



# if option_quit==True:
#    break
