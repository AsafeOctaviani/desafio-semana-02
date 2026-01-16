# import menu_functions


# list_options=["Change Password","Update Email","Delete Account","Back to Main Menu",
#               "lenguage","Notifications","Apparance"]

# def account_settings(options):
#     menu_functions.menu("Account Settings")
#     for i,v in enumerate (options):
#         print(f"{i+1} - {v}")
#         if i==len(options)-2:
#             apparance_settings()


# def apparance_settings():
#     menu_functions.menu("Apparance Settings")
#     list_options=["Light Mode","Dark Mode","System Default","Back to Account Settings"]]
#     for i,v in enumerate (list_options):
#         print(f"{i+1} - {v}")
#     choice=int(input("Select an option:"))
#     if choice==4:
#         break
#     elif choice == 3:
#         pass
#     elif choice == 2:
#         print("\033[33m")
#     elif choice ==1:
        

# account_settings(list_options)