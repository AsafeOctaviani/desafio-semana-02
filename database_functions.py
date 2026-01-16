import sqlite3
import login_functions
import menu_functions





connection = sqlite3.connect('database.db')
cursor=connection.cursor()

def login_storage():
    dictlog=login_functions.login()
    cursor.execute("""CREATE TABLE IF NOT EXISTS database_table 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL, 
                    second_name TEXT NOT NULL,
                    saldo REAL DEFAULT 0,
                    sexo TEXT,
                    telefone INTEGER,
                    score_credito REAL DEFAULT 0
                    )""")
    connection.commit()

    values= (dictlog['first name'], 
                    dictlog['second name'], 
                    dictlog['saldo'], 
                    dictlog['sex'], 
                    dictlog['telefone'], 
                    dictlog['saldo']*0.1)

    order=(f"""INSERT INTO database_table 
                   (name, second_name, saldo , sexo, telefone, score_credito)
                   VALUES (?, ?, ?, ?, ?, ?)""")
    cursor.execute(order, values)
    cursor.execute("SELECT * FROM database_table")
    contas=cursor.fetchall()

    #se eu conseguir separar uma linha pelo id eu posso criar uma variavel com aquela linha
    #e transformar em dicionario)
    # line_coose=cursor.execute("SELECT * FROM database_table WHERE id = ?", (select_lineid,))
    # line_data=line_coose.fetchone()
    # print(f"line_data: {line_data}")
    connection.commit()
    # for c in dictlog:
    #     print(f"{c:_<15}{dictlog[c]:_>15}")
    return contas



def show_row():
    '''
    Docstring for show_row

    '''
    while True:
        if cursor.lastrowid:
            try:
                id_account=int(input(f"""Enter the account ID to see the data:(limit {cursor.lastrowid})"""))
                if id_account > cursor.lastrowid:
                    raise ValueError(f"Line {id_account} does not exist")
            except (ValueError,TypeError,IndexError):
                        menu_functions.line()
                        print("\033[31mInput ERROR! Please enter the data correctly.\033[m")
            else:
                menu_functions.line()
                cursor.execute("SELECT * FROM database_table WHERE id = ?", (id_account,))
                row = cursor.fetchone()
                print(f"Data for account ID {id_account}: {row}")
                return row
        else: 
            print("\033[31mNo accounts are registered.\033[m")
            break




#x=login_storage(dictlogin)

#id01=show_row()

# for t in id01:
#      print(f"t {t}")
# id_account=int(input("Enter the account ID to see the data: "))
# cursor.execute(f"SELECT * FROM database_table WHERE id = ?", (id_account,))
# line_data=cursor.fetchone()
# print(f"line_data: {line_data}")




def edit_data():
    menu_functions.menu("EDIT DATA")

    last_id=cursor.lastrowid
    while True:
        if last_id:
            field=menu_functions.choose_option(["Name","Second name","Saldo","Sexo","Telefone","Score credito"])

            new_value=input("Enter the new value:")
            id_account=int(input(f"""Enter the account ID to edit the data:\n(Max ID:{last_id})"""))

            if  field not in range(1,last_id):
            #if field not in ['name', 'second_name', 'saldo', 'sexo', 'telefone', 'score_credito']:
                raise ValueError("Invalid field name")
            
            order = f"UPDATE database_table SET {field} = ? WHERE id = ?"
            cursor.execute(order, (new_value, id_account))

            connection.commit()
        else:
            print("\033[31mNo accounts are registered.\033[m")
            break










# def nop_storage(nps_score,):
#     order=("""INSERT INTO database_table
#                    (nps_score)
#                    VALUES (?)""")
#     value=(nps_score,)
#     cursor.execute(order, value)
#     connection.commit()
    
#