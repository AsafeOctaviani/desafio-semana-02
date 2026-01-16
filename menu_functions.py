from time import sleep
import yes_no_fuctions
# def choose_option(message):
#     print("-"*40)
#     print("MENU".center(40))
#     print("-"*40)

#     print("""1 - See Accounts
# 2 - Login
# 3 - Quit""")
#     print("="*40)
#     while True:
#         try:
#             option=int(input(message))

#             if option not in [1,2,3]:
#                 raise ValueError()
#         except ValueError or TypeError:
#             print(f"Input ERROR! is not a valid option.")
#         else:
#             if option==1:
#                 print("You chose to see accounts.")
#                 print("-"*40)
#                 print("ACCOUNTS".center(40))
#                 print("-"*40)
#             elif option==2:
#                 print("You chose to login.")
#                 print("You chose to see accounts.")
#                 print("-"*40)
#                 print("LOGIN".center(40))
#                 print("-"*40)
#             elif option==3:
#                 print("You chose to quit.")
#                 print("You chose to see accounts.")
#                 print("-"*40)
#                 print("QUIT".center(40))
#                 print("-"*40)
    
#             return option


def line():
    """"
    Docstring for line
    :return: prints a line"""
    print("-"*55)

def menu(tiltle):
    """
    Docstring for menu
    :param tiltle: Description of tiltle
    :return: prints a menu with a title
    param tiltle: The title to display in the menu.
    """
    line()
    print(f"{tiltle}".center(55))
    line()



def list(options):
    """
    Docstring for list
    :param options: Description of options
    :return: Description of return value
    param options: A list of menu options to display.
    This function prints a numbered list of the provided options.
    """     
    
    for pos,value in enumerate (options):
        print(f"{pos+1} - {options[pos]}")
        
        

def choose_option(options):

    list(options)
    line()
    while True:
        try:
            option=int(input("-Choose an option:"))
            sleep(2)
            if option not in range (1,len(options)+1):
                raise ValueError()
        except (ValueError, TypeError):
            print(f"\033[31mInput ERROR! is not a valid option.\033[m")
        except KeyboardInterrupt:
            print(f"\033[31mInput ERROR! The user did not enter any value.\033[m")
        
        else:
            for c in range (len(options)):
                if option==c+1:
                    menu(f"{options[c]}")

           

            return option



# print(choiced)