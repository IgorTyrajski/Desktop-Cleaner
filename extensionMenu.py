import globals as glb
import os


def funcEXT1():
    for ext in glb.typesToRemove:
        print(f".{ext}",end=" ")
    input("Press ENTER to continue...")


def funcEXT2():
    newExt=str(input("Input a new extension to be added: "))
    if newExt[0] == '.':
        newExt=newExt[1:]
    if newExt not in glb.typesToRemove:
        glb.typesToRemove.append(newExt)
    else:
        print("Given extension is already in the list")

def funcEXT3():
    extToRem=str(input("Input an extension to be removed from the list: "))
    if extToRem[0] == '.':
        extToRem=extToRem[1:]
    if extToRem in glb.typesToRemove:
        glb.typesToRemove.remove(extToRem)
    else:
        print("Given extension is already not in the list")


def menuEXT():
    os.system(glb.ClearCommand)
    while True:
        print(f"""
            ***********************\n
            \tExtensions options\n
            ***********************\n""")
        print("""
        1. Write all file extensions that are to be cleaned\n
        2. Add a file extension to be cleaned\n
        3. Delete a file extension to be cleaned\n
        4.  Exit\n\n""")
        option = input("Choose an option: ")
        try:
            option_int = int(option)
            if option_int == 4:
                return
            elif 1 <= option_int <= 3:
                eval(f"funcEXT{option_int}()")
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