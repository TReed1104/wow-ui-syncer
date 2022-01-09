## Imports
import shutil
import json

## Interface Sync Class
class InterfaceSync:
    def __init__(self, config, mode, target):
        ## Load the config json
        configFile = open(config)
        configData = json.load(configFile)
        configFile.close()

        ## Set the class variables
        self.target = target
        self.mode = mode

        ## Copy the config data to the object
        self.accountName = configData["account_name"]
        self.installPathWarcraft = configData["wow_install_path"]
        self.installPathGoogleDrive = configData["google_drive_path"]
        self.directoryUI = configData["ui_directory"]
        self.directoryAddons = configData["addons_directory"]
        

    ## Pull the target folder
    def __pullFolder(self):
        ## User selected the UI to sync
        if self.target == "UI":
            sourcePath = f"{self.installPathGoogleDrive}{self.accountName}.zip"
            targetPath = f"{self.installPathWarcraft}{self.directoryUI}{self.accountName}"
        ## User selected the Addons folder to sync
        elif self.target == "Addons":
            sourcePath = f"{self.installPathGoogleDrive}Addons.zip"
            targetPath = f"{self.installPathWarcraft}{self.directoryAddons}Addons"
        else:
            ## Target is unrecognised
            print(">>> ERROR: Unknown Target type")
            return

        ## Console output
        print(">> Pull:", sourcePath, "-->", targetPath)

        ## Unzip the folder from Google drive to the target destination
        shutil.unpack_archive(sourcePath, extract_dir=targetPath)

    ## Push the target folder
    def __pushFolder(self):
        ## User selected the UI to sync
        if self.target == "UI":
            sourcePath = f"{self.installPathWarcraft}{self.directoryUI}{self.accountName}"
            targetPath = f"{self.installPathGoogleDrive}"
            zipOutputName = f"{self.accountName}.zip"
        ## User selected the Addons folder to sync
        elif self.target == "Addons":
            sourcePath = f"{self.installPathWarcraft}{self.directoryAddons}Addons"
            targetPath = f"{self.installPathGoogleDrive}"
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

    ## Execution of the App
    def Run(self):
        ## Check the Sync mode - Pull/Push
        if self.mode == "pull":
            ## Update the local files
            self.__pullFolder()
        elif self.mode == "push":
            ## Update the Google drive files
            self.__pushFolder()
