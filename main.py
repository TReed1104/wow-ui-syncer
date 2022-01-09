## Imports
from argparse import ArgumentParser
import shutil
import json


## Pull the target folder
def pullFolder(args, config):
    ## User selected the UI to sync
    if args.target == "UI":
        sourcePath = f"{config['google_drive_path']}{config['account_name']}.zip"
        targetPath = f"{config['wow_install_path']}{config['ui_directory']}{config['account_name']}"
    ## User selected the Addons folder to sync
    elif args.target == "Addons":
        sourcePath = f"{config['google_drive_path']}Addons.zip"
        targetPath = f"{config['wow_install_path']}{config['addons_directory']}Addons"
    else:
        ## Target is unrecognised
        print(">>> ERROR: Unknown Target type")
        return

    ## Console output
    print(">> Pull:", sourcePath, "-->", targetPath)

    ## Unzip the folder from Google drive to the target destination
    shutil.unpack_archive(sourcePath, extract_dir=targetPath)


## Push the target folder
def pushFolder(args, config):
    ## User selected the UI to sync
    if args.target == "UI":
        sourcePath = f"{config['wow_install_path']}{config['ui_directory']}{config['account_name']}"
        targetPath = f"{config['google_drive_path']}"
        zipOutputName = f"{config['account_name']}.zip"
    ## User selected the Addons folder to sync
    elif args.target == "Addons":
        sourcePath = f"{config['wow_install_path']}{config['addons_directory']}Addons"
        targetPath = f"{config['google_drive_path']}"
        zipOutputName = f"Addons.zip"
    else:
        ## Target is unrecognised
        print(">>> ERROR: Unknown Target type")
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
    argParser.add_argument("-i",
                           "--input",
                           dest="config",
                           help="The config file to use",
                           type=str,
                           default="config.json")
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
                           default="UI")

    ## Parse the arguments from the command line to be usable
    args = argParser.parse_args()

    ## Load the config json
    configFile = open(args.config)
    configData = json.load(configFile)
    configFile.close()

    ## Entry point output, just for context in the command-lines installed on
    print("> Syncing WoW Folders")

    ## Check the Sync mode - Pull/Push
    if args.mode == "pull":
        ## Update the local files
        pullFolder(args, configData)
    elif args.mode == "push":
        ## Update the Google drive files
        pushFolder(args, configData)


## Main thread check
if __name__ == '__main__':
    main()
