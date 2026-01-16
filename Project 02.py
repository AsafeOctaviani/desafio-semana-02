import file_handling_funtions
import menu_functions
import yes_no_fuctions
import nps_functions
import login_functions
import database_functions
import time

while True:
    menu_functions.menu("MENU OPTIONS")
    option01=menu_functions.choose_option(["See acoount","Edit data","Log in","Quit"])
    if option01==4:
        yn=yes_no_fuctions.option_quit("Are you sure you want to quit? (Y/N):")
        if yn==True:
            break


    elif option01==3:
        data=database_functions.login_storage()
    
    elif option01==2:
        #menu_functions.choose_option(["Name","Second name","Saldo","Sexo","Telefone","Score credito"]).lower().replace(" ","_")
        database_functions.edit_data()



    elif option01==1:
        database_functions.show_row()

nps1=nps_functions.nps()
print(f"NPS Score recorded: {nps1}")

