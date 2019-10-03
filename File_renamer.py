import os
from datetime import datetime
from os import scandir
from pathlib import Path
# https://realpython.com/working-with-files-in-python/

#The st_mtime attribute returns a float value that represents seconds since the epoch in timestamp converts to  '1565369027.9890034' to '09.08.2019'
def convert_date(timestamp):
    my_date = datetime.utcfromtimestamp(timestamp)
    formated_date = str(my_date.strftime('%d %m %Y')).replace(' ','.')
    return formated_date

def rename_files(directory_Path, replace_file_string):
    dir_entries = scandir(directory_Path)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()            
            data_file = Path(entry)
            data_file.replace(str(data_file).replace(replace_file_string,str(convert_date(info.st_mtime))))
            print(info.st_mtime)

my_directory = r"C:\Users\TomBa\Downloads\filesforscript"   
replace_file_string = "00.00.0000"  
# rename files takes a directory and a string in which to rename the file replacing the string with the last modified date of that file 
rename_files(my_directory, replace_file_string)