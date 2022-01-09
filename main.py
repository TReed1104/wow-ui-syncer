## Imports
from argparse import ArgumentParser
import shutil

## Path Variables
installPathBase = ":\\Program Files (x86)\\World of Warcraft\\_classic_\\"
addonsDirectory = installPathBase + "Interface\\"
uiDirectory = installPathBase + "WTF\\Account\\"
googleDrivePath = "C:\\Users\\treed\\Google Drive\\Games\\Wow\\"

## Account Varialbes
accountName = "FALCO985"


## Pull the target folder
def pullFolder(args):
    ## User selected the UI to sync
    if args.target == "UI":
        sourcePath = f"{googleDrivePath}{accountName}.zip"
        targetPath = f"{args.drive}{uiDirectory}{accountName}"
    ## User selected the Addons folder to sync
    elif args.target == "Addons":
        sourcePath = f"{googleDrivePath}Addons.zip"
        targetPath = f"{args.drive}{addonsDirectory}Addons"
    else:
        ## Target is unrecognised
        return

    ## Console output
    print(">> Pull:", sourcePath, "-->", targetPath)

    ## Unzip the folder from Google drive to the target destination
    shutil.unpack_archive(sourcePath, extract_dir=targetPath)


## Push the target folder
def pushFolder(args):
    ## User selected the UI to sync
    if args.target == "UI":
        sourcePath = f"{args.drive}{uiDirectory}{accountName}"
        targetPath = f"{googleDrivePath}"
        zipOutputName = f"{accountName}.zip"
    ## User selected the Addons folder to sync
    elif args.target == "Addons":
        sourcePath = f"{args.drive}{addonsDirectory}Addons"
        targetPath = f"{googleDrivePath}"
        zipOutputName = f"Addons.zip"
    else:
        ## Target is unrecognised
        return

    ## Console output
    print(">> Push:", sourcePath, "-->", targetPath)

    ## Zip the local folder and push it to Google drive
    createdZip = shutil.make_archive(sourcePath, "zip", sourcePath)
    ## make_archive creates the zip in the same directory, so copy the output zip to the target location
    shutil.move(createdZip, targetPath + zipOutputName)


## App Main
def main():
    ## Setup the command-line arguments
    argParser = ArgumentParser(
        description=
        'A Python app for syncing my WoW Addons and UI folder between machines'
    )
    argParser.add_argument("-d",
                           "--drive",
                           dest="drive",
                           choices=["C", "D"],
                           help="The drive WoW i",
                           type=str,
                           default="C")
    argParser.add_argument("-m",
                           "--mode",
                           dest="mode",
                           choices=["pull", "push"],
                           help="The sync mode, push or pull",
                           type=str,
                           default="pull")
    argParser.add_argument("-f",
                           "--target",
                           dest="target",
                           choices=["UI", "Addons"],
                           help="The folder to sync",
                           type=str,
                           default="ui")

    ## Parse the arguments from the command line to be usable
    args = argParser.parse_args()

    ## Entry point output, just for context in the command-lines installed on
    print("> Syncing WoW Folders")

    ## Check the Sync mode - Pull/Push
    if args.mode == "pull":
        ## Update the local files
        pullFolder(args)

    elif args.mode == "push":
        ## Update the Google drive files
        pushFolder(args)


## Main thread check
if __name__ == '__main__':
    main()
