import os
import zipfile
from io import BytesIO
from typing import List
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

def save_images_to_dir(images: List[FileStorage], dir_path: str) -> List[str]:
    """
    Saves images in the given directory and returns their saved paths.

    Args:
        images (List[FileStorage]): Images to be saved.
        dir_path (str): Path of the directory where the images will be saved.

    Returns:
        List[str]: List of paths to the saved images.

    Raises: 
        ValueError: If no images are provided or an image is invalid.
    """
    if not images:
        raise ValueError('No images provided.')

    saved_paths = []
    os.makedirs(dir_path, exist_ok=True)

    for img in images:
        if not img or img.filename == '':
            raise ValueError('One or more images are invalid or missing filenames.')
        
        filename = secure_filename(img.filename)
        img_path = os.path.join(dir_path, filename)
        img.save(img_path)
        saved_paths.append(img_path)

    return saved_paths


def send_image_bytes(img_path: str) -> BytesIO:
    """
    Reads an image file from disk and returns it as a BytesIO stream.

    Args:
        img_path (str): Path of the image to be read.

    Returns:
        BytesIO: The image content in memory.

    Raises:
        ValueError: If the provided path is empty or the file does not exist.
    """
    if not img_path or not os.path.isfile(img_path):
        raise ValueError(f'Invalid image path: {img_path}')

    with open(img_path, 'rb') as img:
        return BytesIO(img.read())
    
def zip_images(image_paths: List[str]) -> BytesIO:
    """
    Zips all the images.

    Args:
        image_paths: list of paths of images.

    Returns:
        BytesIO: zip file stream.

    Raises:
        ValueError: when no images are provided.
    """
    if not image_paths or len(image_paths) == 0:
        raise ValueError('No image path provided.')
    
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zf:
        for pth in image_paths:
            if os.path.exists(pth):
                with open(pth, 'rb') as f:
                    zf.writestr(os.path.basename(pth), f.read())
    zip_buffer.seek(0)
    return zip_buffer