from zipfile import ZipFile
from datetime import datetime, timedelta


# def yesterday(frmt='%b-%d-%Y', string=True):
#     yesterday = datetime.now() - timedelta(1)
#     if string:
#         return yesterday.strftime(frmt)
#     return yesterday
# print(yesterday())  
# specifying the zip file name

def unzip():
    file_name = "Emred.zip"
    with ZipFile(file_name, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')
