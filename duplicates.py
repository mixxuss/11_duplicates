from os import listdir, stat

def are_files_duplicates(file_path1, file_path_2):
    pass


if __name__ == '__main__':
    path = '/Users'
    filesize = stat('/Users/admin/Desktop/DBR.1.7.50.162.exe')
    print(filesize.st_size)
    print(listdir(path))
