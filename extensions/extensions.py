def main():
    file_name = input("File name: ").lower().strip()
    file_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }
    for extension in file_types:
        if file_name.endswith(extension):
            print(file_types[extension])
            break
    else:
        print("application/octet-stream")
main()
