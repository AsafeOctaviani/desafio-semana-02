from os import write
from menu_functions import menu,line



def file_exists(file_name):
    #print(f"Checking if the file {file_name} exists")
    try:
         file=open(file_name,"rt", encoding="utf-8")
         file.close()

    except FileNotFoundError as fnf_error:
        #print(f"The file \033[34m{file_name}\033[0m does not exist.")
        return False
    
    else:
        #print(f"The file \033[34m{file_name}\033[0m exists.")
        return True
    
    

def file_exists_print(file_name):
    print(f"Checking if the file {file_name} exists")
    try:
         file=open(file_name,"rt", encoding="utf-8")
         file.close()

    except FileNotFoundError as fnf_error:
        print(f"The file \033[34m{file_name}\033[0m does not exist.")
        return False
    
    else:
        print(f"The file \033[34m{file_name}\033[0m exists.")
        return True

    


def create_a_file(file_name):
    try:
        file=open(file_name,"wt+",encoding="utf-8")
        file.close()
        print(f"Creating a file named \033[34m{file_name}\033[0m")
    except Exception as error:
        print(f"An error occurred while creating the file: {error}")
    else:
        print(f"File \033[34m{file_name}\033[0m created successfully.")



def read_file(file_name):
    try:
        reading=open(file_name,"rt",encoding="utf-8")
    except Exception as error:
        print(f"An error occurred while trying to read the file: {error}")
    else:
        #menu(file_name.upper())
        #também pode ser usado o readlines()
        #print (reading.readlines())
        print(reading.read())
        for c in reading:
            data=c.split(";")
            data[1]=data[1].replace("\n","")
            print(f"Name: {data[0]:<30} Age: {data[1]:>3} years")



def sign_up(file_name,name="unknown",second_name="unknown",age=0,telefone=0,sex="unknown"):
    try:
        #testar o with open futuramente
        file=open(file_name,"at", encoding="utf-8")
    except:
        print(f"An error occurred while trying to write to the file:")
    else:
        list_data=[name,second_name,age,telefone,sex]
        list_str=["Name","Second Name","Age","Telefone","Sex"]

        try:
            # for c in range(len(list_data)):
            #     file.write(f"{list_str[c]:<15}: {list_data[c]}\n")
            # for c in list_data:
                
            #     file.write(f"{str(c)}\n")
            file.write(f"{name} {second_name};{age}\n")
        except:
            print("An error occurred while trying to write the data.")
        else:
            print(f"User {name} {second_name} added successfully.")
            file.close()



# with open("text1.txt","r",encoding="utf-8") as read:
#     print(read.read())
