import os
import download_handler
import scryfall_handler
import db_handler

def error_handling(input):
        print("Something went wrong")

def help_menu():
    print("This is the help menu")

def eval_input(num_input):
    if (num_input == "0"):
        print("Default? y/n")
        input_default = input()
        if(input_default == "y" or input_default == "Y"):
            download_handler.default_bulk_dl()
            db_handler.dbAdd_bulkDef
        elif(input_default == "n" or input_default == "N"):
            download_handler.all_bulk_dl()
            db_handler.dbAdd_bulkAll()
        else:
            error_handling(input_default)
        return
    elif (num_input == "1"):
        scryfall_handler.get_bulk_json()
        scryfall_handler.get_type_jsons()
    elif (num_input == "h"):
        help_menu()
        return
    else:
        error_handling(num_input)
    return

def main():
    # if os.path.exists('.env'):
    #     pass

    print ("0: Download Bulks\n1: Get data jsons\nh: Help Menu")
    choice_input = input()

    eval_input(choice_input)

if __name__ == "__main__":
    main()