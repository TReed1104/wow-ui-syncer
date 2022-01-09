## Imports
from argparse import ArgumentParser
from InterfaceSync import InterfaceSync

## App Main
def main():
    ## Setup the command-line arguments
    argParser = ArgumentParser(description="A Python app for syncing my WoW Addons and UI folder between machines")
    argParser.add_argument("-i", "--input", dest="config", help="The config file to use", type=str, default="configs/config.json")
    argParser.add_argument("-m", "--mode", dest="mode", choices=["pull", "push"], help="The sync mode, push or pull", type=str, default="pull")
    argParser.add_argument("-t", "--target", dest="target", choices=["UI", "Addons"], help="The folder to sync", type=str, default="UI")

    ## Parse the arguments from the command line to be usable
    args = argParser.parse_args()

    ## Entry point output, just for context in the command-lines installed on
    print("> Syncing WoW Folders")

    ## Create the app and run
    app = InterfaceSync(args.config, args.mode, args.target)
    app.Run()

## Main thread check
if __name__ == '__main__':
    main()
