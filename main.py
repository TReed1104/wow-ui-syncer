## Imports
from argparse import ArgumentParser

## Main thread check
if __name__ == '__main__':
    ## Setup the command-line arguments
    argParser = ArgumentParser(description='A Python app for syncing my WoW Addons and UI folder between machines')
    argParser.add_argument("-m", "--mode", dest="mode", choices=["pull", "push"], help="The sync mode, push or pull", type=str, default="pull")
    argParser.add_argument("-f", "--folder", dest="folder", choices=["ui", "addons"], help="The folder to sync", type=str, default="ui")

    ## Parse the arguments from the command line to be usable
    args = argParser.parse_args()

    ## Entry point output, just for context in the command-line
    print("Syncing WoW Folders")
    