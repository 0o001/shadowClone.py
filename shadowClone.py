import argparse
from zipfile import ZipFile
import os

__author__ = "mustafauzun0"

"""
shadowClone
"""

def main():
    parser = argparse.ArgumentParser(description="Git Project Get Only Changed Files")

    parser.add_argument("-t", "--target", dest="target", help="Target Git Project Folder", required=True)
    
    args = parser.parse_args()

    if args.target:
        os.chdir(args.target)

        gitInfo = os.popen("git show --name-only --oneline HEAD").read()
        gitInfoArray = gitInfo.split("\n")

        zipFileName = gitInfoArray[0] + ".zip"

        with ZipFile(zipFileName, "w") as zipObj:
            for item in gitInfoArray[1:-1]:
                zipObj.write("./" + item)

        print("Files were zipped successfully")
        print("Zip Path:", os.path.join(os.getcwd(), zipFileName))
    
if __name__ == "__main__":
    main()
