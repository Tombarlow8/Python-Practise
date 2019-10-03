import os
from os import scandir
from pathlib import Path
  
# takes a directory and replaces a string withign the files to whateveres set
def replace_string_in_files(directory_to_amend):
    dir_entries = scandir(directory_to_amend)
    for entry in dir_entries:
        if entry.is_file():           
            file_in = Path(entry)
            fin = open(file_in, "rt")
            data = fin.read()
            data = data.replace('00.00.0000', str(entry.name[:10]))
            fin.close()

            fin = open(file_in, "wt")
            fin.write(data)
            fin.close()

in_directory = r"C:\Users\TomBa\Downloads\filesforscript"  
 
replace_string_in_files(in_directory)