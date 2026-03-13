import os
import shutil

from funcks import IsCorrect
import globals as glb

import extensionMenu as EXT
import cleanedFolderMenu as CLFLD
import currentFolderMenu as CURRFLD

devMode=True

#TODO funkcje na pod funkcje i zaktualizowac maina

def menu():
    option=0
    print(f"""
    ***********************\n
    \tDESKTOP CLEANER\n
    ***********************\n""")
    while option not in list(glb.options.keys()):
        print("""
        1. Extension menu\n
        2. Cleaned folder menu\n
        3. Current (the one to be cleaned) folder menu\n
        4. Clean!\n
        5. Exit\n\n""")
        option = input("Choose an option: ")
        try:
            option=int(option)
            if option not in list(glb.options.keys()):
                print("Choose existing option")
        except ValueError:
            print("Input correct value\n")

    return int(option)

def func4():
    glb.FilesToClean = []
    with os.scandir(glb.DirectoryPath) as it:
        for entry in it:
            if IsCorrect(entry):
                glb.FilesToClean.append(entry)

    pathNew = os.path.join(glb.DirectoryPath, glb.folderNewName)
    if len(glb.FilesToClean) != 0:
        print("These files were found to be cleaned:")
        if not os.path.isdir(pathNew):
            os.mkdir(pathNew)
        for file in glb.FilesToClean:
            print(" -", file.name)
            try:
                shutil.move(file.path, pathNew)
            except:
                print(f"A problem has occurred when trying to move the file: {file.name}")
    else:
        print("No files to be cleaned have been found")
    input("Press ENTER to continue...")


def func5():
    os.system(glb.ClearCommand)

#main
opt=menu()
while opt != list(glb.options.keys())[-1]:
    if opt==1:
        EXT.menuEXT()
    elif opt==2:
        CLFLD.menuCLFLD()
    elif opt==3:
        CURRFLD.menuCURRFLD()
    elif opt==4:
        func4()
    else:
        func5()
    os.system(glb.ClearCommand)
    opt=menu()

