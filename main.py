## Imports
from argparse import ArgumentParser
import shutil

## Path Variables
installPathBase = ":\\Program Files (x86)\\World of Warcraft\\_classic_\\"
addonsDirectory = installPathBase + "Interface\\"
uiDirectory = installPathBase +  "WTF\\Account\\"
googleDrivePath = "C:\\Users\\treed\\Google Drive\\Games\\Wow\\"

## Account Varialbes
accountName = "FALCO985"

## Pull the target folder
def pullFolder(target, drive):
    ## User selected the UI to sync
    if target == "UI":
        sourcePath = f"{googleDrivePath}{accountName}.zip"
        targetPath = f"{drive}{uiDirectory}{accountName}"

    ## User selected the Addons folder to sync
    elif target == "Addons":
        sourcePath = f"{googleDrivePath}Addons.zip"
        targetPath = f"{drive}{addonsDirectory}Addons"

    ## Console output
    print(">> Pull:", sourcePath, "-->", targetPath)

    ## Unzip the folder from Google drive to the target destination
    shutil.unpack_archive(sourcePath, extract_dir=targetPath)

## Push the target folder
def pushFolder(target, drive):
    ## User selected the UI to sync
    if target == "UI":
        sourcePath = f"{drive}{uiDirectory}{accountName}"
        targetPath = f"{googleDrivePath}"
        zipOutputName = f"{accountName}.zip"

    ## User selected the Addons folder to sync
    elif target == "Addons":
        sourcePath = f"{drive}{addonsDirectory}Addons"
        targetPath = f"{googleDrivePath}"
        zipOutputName = f"Addons.zip"

    ## Console output
    print(">> Push:", sourcePath, "-->", targetPath)

    ## Zip the local folder and push it to Google drive
    createdZip = shutil.make_archive(sourcePath, "zip", sourcePath)
    ## make_archive creates the zip in the same directory, so copy the output zip to the target location
    shutil.move(createdZip, targetPath + zipOutputName)

## App Main
def main():
    ## Setup the command-line arguments
    argParser = ArgumentParser(description='A Python app for syncing my WoW Addons and UI folder between machines')
    argParser.add_argument("-d", "--drive", dest="drive", choices=["C", "D"], help="The drive WoW i", type=str, default="C")
    argParser.add_argument("-m", "--mode", dest="mode", choices=["pull", "push"], help="The sync mode, push or pull", type=str, default="pull")
    argParser.add_argument("-f", "--target", dest="target", choices=["UI", "Addons"], help="The folder to sync", type=str, default="ui")

    ## Parse the arguments from the command line to be usable
    args = argParser.parse_args()

    ## Entry point output, just for context in the command-lines installed on
    print("> Syncing WoW Folders")

    ## Check the Sync mode - Pull/Push
    if args.mode == "pull":
        ## Check which folder we're Syncing
        if args.target == "UI":
            ## Pull the UI Folder
            pullFolder(args.target, args.drive)

        elif args.target == "Addons":
            ## Pull the Addons Folder
            pullFolder(args.target, args.drive)

        else:
            print("Pulling Unknown Folder")

    elif args.mode == "push":
        ## Check which folder we're Syncing
        if args.target == "UI":
            ## Push the UI Folder
            pushFolder(args.target, args.drive)

        elif args.target == "Addons":
            ## Push the Addons Folder
            pushFolder(args.target, args.drive)

        else:
            print("Pushing Unknown Folder")

## Main thread check
if __name__ == '__main__':
    main()