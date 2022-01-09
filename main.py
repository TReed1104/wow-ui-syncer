## Imports
from argparse import ArgumentParser

def pullFolder(folder):
    print("Downloading Folder:", folder)

def pushFolder(folder):
    print("Uploading Folder:", folder)

def main():
    ## Setup the command-line arguments
    argParser = ArgumentParser(description='A Python app for syncing my WoW Addons and UI folder between machines')
    argParser.add_argument("-m", "--mode", dest="mode", choices=["pull", "push"], help="The sync mode, push or pull", type=str, default="pull")
    argParser.add_argument("-f", "--target", dest="target", choices=["UI", "Addons"], help="The folder to sync", type=str, default="ui")

    ## Parse the arguments from the command line to be usable
    args = argParser.parse_args()

    ## Entry point output, just for context in the command-line
    print("Syncing WoW Folders")

    ## Check the Sync mode - Pull/Push
    if args.mode == "pull":
        ## Check which folder we're Syncing
        if args.target == "UI":
            ## Pull the UI Folder
            pullFolder(args.target)

        elif args.target == "Addons":
            ## Pull the Addons Folder
            pullFolder(args.target)

        else:
            print("Pulling Unknown Folder")

    elif args.mode == "push":
        ## Check which folder we're Syncing
        if args.target == "UI":
            ## Push the UI Folder
            pushFolder(args.target)

        elif args.target == "Addons":
            ## Push the Addons Folder
            pushFolder(args.target)

        else:
            print("Pushing Unknown Folder")

## Main thread check
if __name__ == '__main__':
    main()