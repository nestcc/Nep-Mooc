import os

def handle_upload_videos(file, filename, path):
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path + filename, 'wb+') as file_handler:
        for chunk in file.chunks():
            file_handler.write(chunk)

    return "SUCCESS"