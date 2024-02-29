import os
import shutil
import argparse
from collections import defaultdict
from datetime import datetime

def organize_by_type(directory):
    # Organize files in the specified directory by file type.
    files_by_type = defaultdict(list)

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_type = filename.split('.')[-1]
            files_by_type[file_type].append(filename)

    for file_type, filenames in files_by_type.items():
        # Define the directory name based on file type
        dir_name = os.path.join(directory, file_type.upper())
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        # Move files to their respective directories
        for filename in filenames:
            shutil.move(os.path.join(directory, filename), os.path.join(dir_name, filename))
    print(f"Files in '{directory}' organized by file type.")

def organize_by_size(directory):
    # Organize files in the specified directory by file size.
    files_by_size = defaultdict(list)
    size_ranges = {
        '0-1MB': (0, 1*1024**2),
        '1MB-10MB': (1*1024**2, 10*1024**2),
        '10MB-100MB': (10*1024**2, 100*1024**2),
        '100MB-1GB': (100*1024**2, 1024**3),
        '1GB+': (1024**3, float('inf')),
    }

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_size = os.path.getsize(filepath)
            for size_range, (min_size, max_size) in size_ranges.items():
                if min_size <= file_size < max_size:
                    files_by_size[size_range].append(filename)
                    break

    for size_range, filenames in files_by_size.items():
        # Define the directory name based on size range
        dir_name = os.path.join(directory, size_range)
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        # Move files to their respective directories
        for filename in filenames:
            shutil.move(os.path.join(directory, filename), os.path.join(dir_name, filename))
    print(f"Files in '{directory}' organized by size.")

def organize_by_creation_date(directory):
    # Organize files in the specified directory by creation date.
    files_by_date = defaultdict(list)

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Get the creation time and convert it to a date string
            creation_time = os.path.getctime(filepath)
            date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
            files_by_date[date].append(filename)

    for date, filenames in files_by_date.items():
        # Define the directory name based on the date
        dir_name = os.path.join(directory, date)
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        # Move files to their respective directories
        for filename in filenames:
            shutil.move(os.path.join(directory, filename), os.path.join(dir_name, filename))
    print(f"Files in '{directory}' organized by creation date.")

def organize_by_date(directory):
    # Organize files in the specified directory by last modification date.
    files_by_date = defaultdict(list)

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Get the last modification time and convert it to a date string
            mod_time = os.path.getmtime(filepath)
            date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
            files_by_date[date].append(filename)

    for date, filenames in files_by_date.items():
        # Define the directory name based on the date
        dir_name = os.path.join(directory, date)
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        # Move files to their respective directories
        for filename in filenames:
            shutil.move(os.path.join(directory, filename), os.path.join(dir_name, filename))
    print(f"Files in '{directory}' organized by modification date.")

def organize_directory(directory, criteria):
        # Organize files in the specified directory based on the given criteria.
        if criteria == 'type':
            organize_by_type(directory)
        elif criteria == 'size':
            organize_by_size(directory)
        elif criteria == 'date':
            organize_by_date(directory)
        else:
         print(f"Criteria '{criteria}' is not supported yet.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a directory.")
    parser.add_argument("directory", type=str, help="The directory to organize")
    parser.add_argument("--criteria", type=str, choices=['type', 'size', 'date'], default='type', help="Criteria for organizing files")
    
    args = parser.parse_args()

    organize_directory(args.directory, args.criteria)
