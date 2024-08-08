
import json
import os
base_file_directory  = os.getcwd()
from file_upload_func import file_upload

def classify_file(dirpath,filename,config):
    if os.path.splitext(filename)[1] in config['file_type_for_s3']:
        print(f"The {filename} will be uploaded to S3")
        #file_upload(dirpath+"\\"+filename,config,"s3")
        return "push to s3"
    elif os.path.splitext(filename)[1] in config['file_type_for_GD']:
        print(f"The {filename} will be uploaded to google drive")
        #file_upload(dirpath+"\\"+filename,config,"google_drive")
        return "push to google drive"
    else:
        print(f"The {filename} will be not pushed to any of the cloud storage")
        return "Not categorized"
    
def read_all_files(file_dir):
    try:

        config=read_config(base_file_directory)
        if config.get('input_file_directory'):
            file_dir=config.get('input_file_directory')
        w = os.walk(file_dir)
        for (dirpath, dirnames, filenames) in w:
            for f in filenames:
                response=classify_file(dirpath,f,config)

        return response
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

def read_config(base_file_directory):
    base_file_directory  = os.getcwd()
    f= open(base_file_directory+"\\config\\config.json")
    config = json.load(f)
    return config

if __name__=="__main__":
    read_all_files(base_file_directory+"\\file_input_dir\\")
