import os
import subprocess
import argparse

# [ ] backup
# [ ] export
# [ ] support folders

def send_to_remarkable(filename, destination):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"{filename} does not exist!")
    
    try:
        command = ["rmapi", "put", filename, destination]
        subprocess.run(command, check=True)
        print(f"Sent {filename} to reMarkable at {destination}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to send {filename} to {destination}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a file to a reMarkable tablet using rmapi.")
    parser.add_argument("filename", help="The file to send to the reMarkable tablet.")
    parser.add_argument("destination", nargs="?", default="/", help="The optional destination folder on the reMarkable tablet. Defaults to root ('/').")

    args = parser.parse_args()

    send_to_remarkable(args.filename, args.destination)