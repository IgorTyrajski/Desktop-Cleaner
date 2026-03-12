import os

numberOfOpt=int(5) #number of menus
options = {i: f"func{4}()" for i in range(1, numberOfOpt+1)}

numberOfEXTOpt=int(4) #number of options in ExtensionMenu
extOptions = {i: f"func{4}()" for i in range(1, numberOfEXTOpt+1)}

numberOfCLFLDOpt=int(3) #number of options in cleanedFolderMenu
CLFLDOptions = {i: f"func{4}()" for i in range(1, numberOfCLFLDOpt+1)}

numberOfCURRFLDOpt=int(5) #number of options in cleanedFolderMenu
CURRFLDOptions = {i: f"func{4}()" for i in range(1, numberOfCURRFLDOpt+1)}



typesToRemove=["jpg", "jpeg", "png", "pdf", "doc", "docx", "mp3", "mp4", "wav", "bmp", "cpp", "py", "txt"]
SourcePath = os.path.join(os.path.expanduser("~"), "Desktop") #default - path of Desktop
DirectoryPath=SourcePath #default - folder with cleaned files will be on Desktop
folderNewName="CleanedFiles"
ClearCommand = "cls" if os.name == "nt" else "clear"

FilesToClean=[]
