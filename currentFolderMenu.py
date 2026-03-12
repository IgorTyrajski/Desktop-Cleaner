import os
import globals as glb

def func1CURRFLD():
    newDir=str(input("Input new directory for the folder with cleaned files: "))
    if len(newDir)==0:
        print("Input correct value")
        return
    if newDir[0] == '"' and newDir[-1]=='"':
        newDir=newDir[1:-1]
    if not os.path.isdir(newDir):
        print("Input correct directory")
        return
    glb.DirectoryPath=newDir


def func2CURRFLD():
    print(f'"{glb.DirectoryPath}"')
    input("Press ENTER to continue...")

def func3CURRFLD():
    contents = os.listdir(glb.DirectoryPath)
    extToShow=[]
    for content in contents:
        part=content.split(".")
        if len(part)>1:
            extToAdd="." +".".join(part[1:])
            if extToAdd not in extToShow:
                extToShow.append(extToAdd)
    for ext in extToShow:
        print(ext,end=" ")
    print("\n")
    input("Press ENTER to continue...")


def func4CURRFLD():
    contents=os.listdir(glb.DirectoryPath)
    i=0
    for content in contents:
        print(content, end="\t")
        if i==4:
            print("\n")
            i=1
        else:
            i+=1
    input("Press ENTER to continue...")

def menuCURRFLD():
    os.system(glb.ClearCommand)
    while True:
        print(f"""
            ***********************\n
            \tDESKTOP CLEANER\n
            ***********************\n""")
        print("""
        1. Change folder (the one to be cleaned) directory \n
        2. Show current folder (the one to be cleaned) directory \n
        3. Show current folder contents extensions\n
        4. Show current folder contents\n
        5. Exit\n\n""")
        option = input("Choose an option: ")
        try:
            option_int = int(option)
            if option_int == 5:
                return
            elif 1 <= option_int <= 4:
                eval(f"func{option_int}CURRFLD()")
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