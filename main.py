## Imports
from argparse import ArgumentParser

def pullFolder(folder):
    print("Downloading Folder:", folder)

def pushFolder(folder):
    print("Uploading Folder:", folder)

## Main thread check
if __name__ == '__main__':
    ## Setup the command-line arguments
    argParser = ArgumentParser(description='A Python app for syncing my WoW Addons and UI folder between machines')
    argParser.add_argument("-m", "--mode", dest="mode", choices=["pull", "push"], help="The sync mode, push or pull", type=str, default="pull")
    argParser.add_argument("-f", "--folder", dest="folder", choices=["UI", "Addons"], help="The folder to sync", type=str, default="ui")

    ## Parse the arguments from the command line to be usable
    args = argParser.parse_args()

    ## Entry point output, just for context in the command-line
    print("Syncing WoW Folders")

    ## Check the Sync mode - Pull/Push
    if args.mode == "pull":
        ## Check which folder we're Syncing
        if args.folder == "UI":
            ## Pull the UI Folder
            pullFolder(args.folder)

        elif args.folder == "Addons":
            ## Pull the Addons Folder
            pullFolder(args.folder)

        else:
            print("Pulling Unknown Folder")

    elif args.mode == "push":
        ## Check which folder we're Syncing
        if args.folder == "UI":
            ## Push the UI Folder
            pushFolder(args.folder)

        elif args.folder == "Addons":
            ## Push the Addons Folder
            pushFolder(args.folder)

        else:
            print("Pushing Unknown Folder")
