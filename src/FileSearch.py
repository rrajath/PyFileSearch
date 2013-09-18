'''
Created on Sep 16, 2013

@author: rajath
'''
import os, fnmatch

# This function takes rootpath and pattern as argument and returns a 'list' of filenames that match the pattern
# For example, if you search for all the *.py files in your workspace, then it returns a list of strings which
# are full paths to these files
def rec_dir_list(rootpath, pattern):
    files = []
    for root, dirs, files in os.walk(rootpath):
        print type(dirs)
        for filename in fnmatch.filter(files, pattern):
            files.append(os.path.join(root, filename))
    return files
#end

# This function takes rootpath as the argument and returns a 'list' of all files along with their full paths.
def list_all_files(rootpath):
    all_files = []
    for root, dirs, files in os.walk(rootpath):
        for filename in files:
            all_files.append(os.path.join(root, filename))
    return all_files
#end

# This function takes rootpath as the parameter and creates a dictionary of filenames categorizing them by filetypes
def all_files_dict(rootpath):
    dict_files = {}
    for root, dirs, files in os.walk(rootpath):
        for filename in files:
            filetype = filename[filename.rfind('.'):]
            file_path = os.path.join(root, filename)
            try:
                tmp = dict_files[filetype]
                dict_files[filetype] = tmp.append(file_path)
            except:
                tmp = []
                tmp.append(file_path)
                dict_files[filetype] = tmp
    return dict_files
#end

# This function takes rootpath as argument and returns a dictionary with directories as keys and its files as values.
def dirs_dict(rootpath):
    dict_dirs = {}
    for root, dirs, files in os.walk(rootpath):
        for filename in files:
            file_path = os.path.join(root, filename)
            os.chdir(os.path.join(root, file_path[:file_path.rfind('/')]))
            dir_path = os.getcwd()
            try:
                dict_dirs[dir_path].append(file_path)
            except:
                tmp = []
                tmp.append(file_path)
                dict_dirs[dir_path] = tmp
    return dict_dirs
#end

# This function takes rootpath as the argument and returns a 'list' of all the directories with their full paths.
def list_all_dirs(rootpath):
    all_dirs = []
    for root, dirs, files in os.walk(rootpath):
        for dirname in dirs:
            all_dirs.append(os.path.join(root, dirname))
    return all_dirs
#end

# This function takes rootpath and filename as arguments and returns the filepath of the filename specified in the argument
def search_file(rootpath, file):
    for root, dirs, files in os.walk(rootpath):
        for filename in files:
            if file == filename:
                return os.path.join(root, filename)
    return None
#end

# This function takes rootpath and dirname as arguments and returns the dirpath of the dirname specified in the argument
def search_dir(rootpath, dir):
    for root, dirs, files in os.walk(rootpath):
        for dirname in dirs:
            if dir == dirname:
                return os.path.join(root, dirname)
    return None
#end
