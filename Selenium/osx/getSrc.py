import os
from google_drive_downloader import GoogleDriveDownloader as gdd


def getOSXsrc():
    gids = {
                '1mKgmZ6cJqXFQyVyWshvVKCg4qEVQOEm-':'osx-chrome-releases',
                '108NRuz7EZ8Z2XO1bn5VCJm4rg5P-mWU9':'osx-firefox-releases'
            }
    for gid,name in gids.items():
        dwFileName = os.path.abspath(os.path.join(os.path.dirname(__file__),gid))
        fileName = os.path.abspath(os.path.join(os.path.dirname(__file__), name))
        if not os.path.exists(fileName):
            gdd.download_file_from_google_drive(
                                                file_id=gid,
                                                dest_path=dwFileName,
                                                unzip=True
                                                )
            os.remove(dwFileName)

def getSeleniumSrv():
    print("get")
    fileName = os.path.join(os.path.dirname(__file__),'selenium-java.zip')
    fileName_extracted = os.path.join(os.path.dirname(__file__), 'selenium-server-standalone-3.11.0.jar')
    if not os.path.exists(fileName_extracted):
        gdd.download_file_from_google_drive(
            file_id='1IIAWfCV-uHSW75cZRoc5VQd2ZiPDSlxN',
            dest_path=os.path.abspath(fileName),
            unzip=True
        )
        os.remove(fileName)
    return True

