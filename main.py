import os
import cloudinary
import cloudinary.uploader
from decouple import config


cloudinary.config(
    cloud_name=config("CLOUDINARY_CLOUD_NAME"),
    api_key=config("CLOUDINARY_API_KEY"),
    api_secret=config("CLOUDINARY_API_SECRET"),
)

ignored_files = []


def upload_mp3_files(folder_path):
    cloud_folder = "cloudinary_name_folder"

    for filename in os.listdir(folder_path):
        try:
            file_path = os.path.join(folder_path, filename)
            public_id = f"{cloud_folder}/{filename[:-4]}"
            response = cloudinary.uploader.upload(
                file_path, resource_type="video", public_id=public_id
            )
            print(f"File uploaded: {response['secure_url']}")
        except Exception as e:
            print(f"Error uploading {filename}: {str(e)}")
            ignored_files.append(filename)
            continue


folder_path = "local_folder_path"
upload_mp3_files(folder_path)
print(ignored_files)
