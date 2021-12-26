from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def create_and_upload_file(file_name='test.txt', file_content='Hey Dude!'):
    
    try:
        drive = GoogleDrive(gauth)
        
        my_file = drive.CreateFile({'title': f'{file_name}'})
        my_file.SetContentString(file_content)
        my_file.Upload()
        
        return f'File {file_name} was uploaded!Have a good day!'
    except Exception as _ex:
        return 'Got some trouble, check your code please!'
    
    
def upload_dir(dir_path=''):
    
    try:
        drive = GoogleDrive(gauth)
        
        for file_name in os.listdir(dir_path):
        
            my_file = drive.CreateFile({'title': f'{file_name}'})
            my_file.SetContentFile(os.path.join(dir_path, file_name))
            my_file.Upload()
            
            print(f'File {file_name} was uploaded!')
            
        return 'Success!Have a good day!'
    except Exception as _ex:
        return 'Got some trouble, check your code please!'
    
    
def main():
    # print(create_and_upload_file(file_name='hello.txt', file_content='Hello Friend'))
    print(upload_dir(dir_path='path_to_dir'))
    
    
if __name__ =='__main__':
    main()
