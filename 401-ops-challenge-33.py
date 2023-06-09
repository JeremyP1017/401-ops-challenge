import os
import hashlib
import requests
from datetime import datetime

# Prompt the user to enter a directory to search in
directory = input("Enter the directory to search in: ")

# Initialize counters
files_searched = 0
hits_found = 0

# Define your VirusTotal API key
api_key = "***********"

# Connect to the VirusTotal API
def connect_to_virustotal(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {
        "x-apikey": api_key,
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Search for files in the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        files_searched += 1

        try:
            # Generate MD5 hash for the file
            with open(file_path, 'rb') as f:
                md5_hash = hashlib.md5()
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    md5_hash.update(data)

            # Get file information
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Print file information
            print(f"Timestamp: {timestamp}")
            print(f"File Name: {file_name}")
            print(f"File Size: {file_size} bytes")
            print(f"File Path: {file_path}")
            print(f"MD5 Hash: {md5_hash.hexdigest()}")

            # Connect to VirusTotal API and compare hashes
            vt_response = connect_to_virustotal(md5_hash.hexdigest())
            positives = vt_response["data"]["attributes"]["last_analysis_stats"]["malicious"]
            total_files = vt_response["data"]["attributes"]["last_analysis_stats"]["total"]

            print(f"Positives: {positives}")
            print(f"Total Files Scanned: {total_files}")
            print("---------------------------------------")

            hits_found += 1

        except IOError:
            print(f"Error accessing file: {file_path}")

# Print the search summary
print("\nSearch Summary:")
print("Files searched:", files_searched)
print("Hits found:", hits_found)



#this script was written with the help of chat gpt
