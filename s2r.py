import os
import subprocess
import argparse
import datetime

# [ ] export

def backup_remarkable(local_dest):
    current_time = datetime.datetime.now()
    backup_filename = current_time.strftime("remarkable_backup_%Y-%m-%d_%H-%M-%S")
    backup_dir = os.path.join(local_dest, backup_filename)
    os.makedirs(backup_dir, exist_ok=True)

    try:
        command = ["rmapi", "mget", "-o", backup_dir, "/"]
        subprocess.run(command, check=True)
        print(f"Backup of reMarkable created at {backup_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create backup of reMarkable: {e}")

def send_to_remarkable(filename, destination):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"{filename} does not exist!")
    
    try:
        command = ["rmapi", "put", filename, destination]
        subprocess.run(command, check=True)
        print(f"Sent {filename} to reMarkable at {destination}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to send {filename} to {destination}: {e}")

def send_folder_to_remarkable(folder, destination):
    raise Exception("Does not work!")
    """if not os.path.isdir(folder):
        raise NotADirectoryError(f"{folder} is not a valid directory!")

    try:
        command = ["rmapi", "mput", destination, folder]
        subprocess.run(command, check=True)
        print(f"Recursively uploaded {folder} to reMarkable at {destination}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to recursively upload {folder} to {destination}: {e}")"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a file to a reMarkable using rmapi.")
    parser.add_argument("filename", help="The file/folder to send to the reMarkable or if you want to back up the reMarkable, 'backup'.")
    parser.add_argument("destination", nargs="?", default="/", help="The optional destination folder on the reMarkable. Defaults to root ('/'). Also the location of the back up of the reMarkable.")

    args = parser.parse_args()

    if(args.filename == "backup"):
        backup_remarkable(args.destination)
    elif(os.path.isfile(args.filename)):
        send_to_remarkable(args.filename, args.destination)
    elif(os.path.isdir(args.filename)):
        send_folder_to_remarkable(args.filename, args.destination)
    else:
        raise Exception("Invalid Arguments!")