import os
import hashlib


class File:

    def __init__(self, name=None, hash256=None):
        self.name = name
        self.hash256 = hash256

    def set_name(self, name):
        self.name = name

    def set_hash256(self, hash256):
        self.hash256 = hash256


def get_list_file_names(folder_name):
    list_files = []
    for dirs, folders, files in os.walk(folder_name):
        if files:
            for file in files:
                new_file = File()
                new_file.set_name(os.path.join(dirs, file))
                list_files.append(new_file)
    return list_files


def update_list_file_hashes(list_files):
    for file in list_files:
        sha256_hash = hashlib.new('sha256')
        if file.name:
            with open(file.name, 'rb') as f:
                while True:
                    data = f.read()
                    if not data:
                        break
                    sha256_hash.update(data)
                    file.set_hash256(sha256_hash.hexdigest())
        list_files = [file if not file.hash256 else file for file in list_files]
