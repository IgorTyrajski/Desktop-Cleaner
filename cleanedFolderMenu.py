import os
import globals as glb

def func1CLFLD():
    newName=str(input("Input a new name for the directory folder: "))
    if len(newName) == 0:
        print("Given name was too short")
    else:
        glb.folderNewName=newName

def func2CLFLD():
    print(f"{glb.folderNewName}")
    input("Press ENTER to continue...")

def menuCLFLD():
    os.system(glb.ClearCommand)
    while True:
        print(f"""
            ***********************\n
            \tDESKTOP CLEANER\n
            ***********************\n""")
        print("""
        1. Change cleaned folder name\n
        2. Show current cleaned folder name\n
        3. Exit\n\n""")
        option = input("Choose an option: ")
        try:
            option_int = int(option)
            if option_int == 3:
                return
            elif 1 <= option_int <= 2:
                eval(f"func{option_int}CLFLD()")
            else:
                print("Choose existing option")
                input("Press ENTER to continue...")

        except ValueError:
            print("Input correct value (number)\n")
            input("Press ENTER to continue...")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Choose existing option")
            input("Press ENTER to continue...")
        os.system(glb.ClearCommand)
