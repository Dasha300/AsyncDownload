import files


def print_files():
    for i in range(3):
        list_files = files.get_list_file_names(f"./tmp/{i}")
        files.update_list_file_hashes(list_files)
        for file in list_files:
            print(f'{file.name}: {file.hash256}')
