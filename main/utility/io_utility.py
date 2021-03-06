import json
import os
import csv
from os import path
from main import MAIN_ROOT_DIR, DEMO_ROOT_DIR, TEST_ROOT_DIR, ROOT_DIR


def read_dictionary_from_file(filepath):
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()
        return json.loads("".join(lines))


def write_dictionary_to_file(dictionary, filepath):
    with open(filepath, "w") as f:
        f.write(json.dumps(dictionary, indent=4))


def read_csv_to_list(path_string):
    with open(path_string, 'r') as f:
        reader = csv.reader(f)
        return list(reader)


def write_list_to_csv(lines, file_name):
    with open(file_name, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)


def standardize_path(path_string):
    path_string = path_string.strip()
    path_string = path_string.replace("\\", "/")
    return path_string


def __get_relative_path(relative_to, relative_path):
    relative_path = standardize_path(relative_path)
    return standardize_path(os.path.join(relative_to, relative_path))


def get_project_path(relative_path):
    return __get_relative_path(ROOT_DIR, relative_path)

def get_main_path(relative_path):
    return __get_relative_path(MAIN_ROOT_DIR, relative_path)

