import requests

# Instagram API access token
APP_ACCESS_TOKEN = '1015621310.798dc31.7f24cdb0a0db4024ad0cda45d709d119'
# Base Url
BASE_URL = 'https://api.instagram.com/v1/'
def menu():
    print("******************Welcome to InstaBot*********************")
    user_input_for_main_menu = print("Please Select a option from menu Diaplayed Below: \n1.Get info About Owner\n2.Search a user")
    if len(user_input_for_main_menu) > 0:
        if user_input_for_main_menu.isnum():
            if user_input_for_main_menu == 1:
                pass
            elif user_input_for_main_menu == 2:
                pass
        else:
            print("Please enter a Numeric Value")
            menu()
    else:
        print("Input can not be empty please select a option..")
        menu()