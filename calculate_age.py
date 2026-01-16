import datetime


def calculate_age():

    while True:
        try:
            born=(input("Born:(MM/DD/YYYY)")).split("/")
            if "/" not in born:
                raise ValueError("Invalid date format/////")
            # if len(born)!=3:
            #     raise ValueError("Invalid date format333333")
            
        except (ValueError,TypeError,KeyboardInterrupt,IndexError) as error:
            print("Invalid date! Please try again")
            print(f"class error:{error.__class__}")
        
        

        else:
            print(born)
            # month=born[0]
            # #print(month)
            # day=born[1]
            # #print(day)
            # year=born[2]
            # #print(year)
            break
        # login_born=datetime.date(int(year),int(month),int(day))
        # today=datetime.date.today()
        # strtoday=today.strftime("%d/%m/%y") #Transforma uma variavel em uma variavel de data quando você escolhe d/m/y ou d/m/Y para 4 digios de ano
        # print(strtoday)
        # #age=(today.year - login_born.year - ((today.month,today.day) <  (login_born.month,logn_born.day)))
        # print(f"Today is {today}")
        # print(f"You have {age} years old")

born01=calculate_age()