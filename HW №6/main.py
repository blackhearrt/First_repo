import shutil
import sys
import scan
import normalize
from pathlib import Path



def handle_file(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))


def handle_archive(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)

    new_name = normalize.normalize(path.name.replace(".zip", ''))

    archive_folder = root_folder / new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(path.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        return
    path.unlink()


def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass


def get_folder_objects(root_path):
    for folder in root_path.iterdir():
        if folder.is_dir():
            remove_empty_folders(folder)
            try:
                folder.rmdir()
            except OSError:
                pass

def main(folder_path):
    scan.scan(folder_path)

    for file in scan.images:
        handle_file(file, folder_path, "IMAGES")

    for file in scan.audio:
        handle_file(file, folder_path, "AUDIO")

    for file in scan.video:
        handle_file(file, folder_path, "VIDEO")

    for file in scan.documents:
        handle_file(file, folder_path, "DOCUMENTS")

    for file in scan.others:
        handle_file(file, folder_path, "OTHERS")

    for file in scan.archives:
        handle_archive(file, folder_path, "ARCHIVE")

    get_folder_objects(folder_path)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)
    main(arg.resolve())
