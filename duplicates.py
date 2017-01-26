import os
import filecmp

def are_files_duplicates(file_path1, file_path_2):
    pass


def make_dict_filepath_size(folder):
    dict_path_size = {}
    for path, dirs, files in folder:
        for file in files:
            dict_path_size[os.path.join(path, file)] = os.stat(file).st_size
    return dict_path_size

if __name__ == '__main__':
    path = os.walk('D:\Test')
    dict_path_size = make_dict_filepath_size(path)
    # for pair in dict_path_size.keys():
    path_list = list(dict_path_size.keys())
    print(filecmp.cmp('D:\\Test\\1.py', 'D:\\Test\\Folder\\1.py'))





    # for i in path_list:
        # print(i)