import os
import shutil

def organize_files(directory):
    file_types = {
        'Documents': ['.pdf', '.docx', '.txt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Audio': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mov'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv'],
        'Archives': ['.zip', '.tar', '.gz'],
    }
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            for folder, extensions in file_types.items():
                if os.path.splitext(filename)[1].lower() in extensions:
                    target_folder = os.path.join(directory, folder)
                    try:
                        if not os.path.exists(target_folder):
                            os.makedirs(target_folder)
                        shutil.move(file_path, target_folder)
                        print(f'Moved {filename} to {folder}')
                        break
                    except Exception as e:
                        print(f'Error moving {filename}: {e}')
                        break

if __name__ == '__main__':
    directory = input("Enter the directory to organize: ")  # Get directory from user
    if os.path.exists(directory):
        organize_files(directory)
        print('File organization complete.')
    else:
        print(f'Error: Directory "{directory}" does not exist.')