import requests

print("#############################################")
print("Simple File Uploader -- Written by Nightmare")
print("#############################################\n\n")

file = raw_input("Path to file: ")
url = raw_input("Url to upload to: ")

try:
	with open(str(file), 'rb') as f:
	    r = requests.post(str(url), files={str(file): f})
	print("File has been uploaded successfully")

except:
	print("An error has occurred with the upload")
