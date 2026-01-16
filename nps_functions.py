import yes_no_fuctions as yes_no
import menu_functions

def nps():
    """
    Docstring for nps
    :return: NPS score between 0 and 10
    This function prompts the user to input an NPS score and categorizes it.
    param nps: Net Promoter Score
    param nps_score: The score input by the user
    """
    menu_functions.line()
    print("\033[33mNPS executed.\033[m")

    while True:
        try:
        
            nps_score =  int(input("On a scale from 0 to 10, how likely are you to "
             "recommend us to a friend or colleague?").strip())
            # int(input("On a scale from 0 to 10, how likely are you to recommend" \
            # " our company (or product/service) to a friend or colleague? ").strip())
        

            if nps_score not in range(0, 11):
                raise ValueError("error! out of range")
                
        except (ValueError,TypeError,KeyboardInterrupt):
                menu_functions.line()
                print("\033[31mInvalid input. Please enter a number between 0 and 10.\033[m")
                

        #Mostrar par ao usuário a classificação normalmente não é 
        # mostrada, essa parte pode ser removida se necessário
        else:
            menu_functions.line()
            if nps_score in range(0, 7):
                print("You are a \033[31mDetractor\033[m.")
            elif nps_score in range(7, 9):
                print("You are a \033[33mPassive\033[m.")
            else:
                print("You are a \033[32mPromoter\033[m.")

            print(f"Your NPS score is: {nps_score}")
            print("We appreciate your feedback!")
            #print("Thank you for participating in our NPS survey.")


            #Se remover esse line e adicionar um line no finally, as linhas serão divididas
            #uma por vez em vez de duas por vez
            menu_functions.line()
            return nps_score
        # finally:
        #     line()
       
    

# nps_score=nps()
# print(f"NPS Score recorded: {nps_score}")

