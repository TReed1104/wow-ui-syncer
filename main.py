## Imports
from argparse import ArgumentParser

## Path Variables
installPathBase = ":\\Program Files (x86)\\World of Warcraft\\_classic_\\"
addonsDirectory = installPathBase + "Interface\\AddOns"
uiDirectory = installPathBase +  "WTF\\Account\\"
googleDrivePath = "C:\\Users\\treed\\Google Drive\\Games\\Wow"

## Folder Varialbes
accountName = "FALCO985"
syncedUIFolder = accountName + ".zip"
syncedAddonsFolder = "Addons.zip"

## Pull the target folder
def pullFolder(drive, folder):
    print("Downloading Folder:", drive, folder)

## Push the target folder
def pushFolder(drive, folder):
    print("Uploading Folder:", drive, folder)

def main():
    ## Setup the command-line arguments
    argParser = ArgumentParser(description='A Python app for syncing my WoW Addons and UI folder between machines')
    argParser.add_argument("-d", "--drive", dest="drive", choices=["C", "D"], help="The drive WoW i", type=str, default="C")
    argParser.add_argument("-m", "--mode", dest="mode", choices=["pull", "push"], help="The sync mode, push or pull", type=str, default="pull")
    argParser.add_argument("-f", "--target", dest="target", choices=["UI", "Addons"], help="The folder to sync", type=str, default="ui")

    ## Parse the arguments from the command line to be usable
    args = argParser.parse_args()

    ## Entry point output, just for context in the command-lines installed on
    print("Syncing WoW Folders")

    ## Check the Sync mode - Pull/Push
    if args.mode == "pull":
        ## Check which folder we're Syncing
        if args.target == "UI":
            ## Pull the UI Folder
            pullFolder(args.drive, args.target)

        elif args.target == "Addons":
            ## Pull the Addons Folder
            pullFolder(args.drive, args.target)

        else:
            print("Pulling Unknown Folder")

    elif args.mode == "push":
        ## Check which folder we're Syncing
        if args.target == "UI":
            ## Push the UI Folder
            pushFolder(args.drive, args.target)

        elif args.target == "Addons":
            ## Push the Addons Folder
            pushFolder(args.drive, args.target)

        else:
            print("Pushing Unknown Folder")

## Main thread check
if __name__ == '__main__':
    main()