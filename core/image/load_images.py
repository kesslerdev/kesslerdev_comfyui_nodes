import os
import hashlib
from comfy.utils import ProgressBar
from PIL import Image, ImageOps
import torch
import numpy as np
from pathlib import Path
from ...utils import kd_image_category

class KD_LoadImagesFromFolder:
    # Dictionary to store folder hashes
    folder_hashes = {}

    @classmethod
    def IS_CHANGED(cls, folder, **kwargs):
        if not os.path.isdir(folder):
            return float("NaN")
        
        valid_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.tga']
        include_subfolders = kwargs.get('include_subfolders', False)
        
        file_data = []
        if include_subfolders:
            for root, _, files in os.walk(folder):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in valid_extensions):
                        path = os.path.join(root, file)
                        try:
                            mtime = os.path.getmtime(path)
                            file_data.append((path, mtime))
                        except OSError:
                            pass
        else:
            for file in os.listdir(folder):
                if any(file.lower().endswith(ext) for ext in valid_extensions):
                    path = os.path.join(folder, file)
                    try:
                        mtime = os.path.getmtime(path)
                        file_data.append((path, mtime))
                    except OSError:
                        pass
        
        file_data.sort()
        
        combined_hash = hashlib.md5()
        combined_hash.update(folder.encode('utf-8'))
        combined_hash.update(str(len(file_data)).encode('utf-8'))
        
        for path, mtime in file_data:
            combined_hash.update(f"{path}:{mtime}".encode('utf-8'))
        
        current_hash = combined_hash.hexdigest()
        
        old_hash = cls.folder_hashes.get(folder)
        cls.folder_hashes[folder] = current_hash
        
        if old_hash == current_hash:
            return old_hash
        
        return current_hash

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "folder": ("STRING", {"default": ""}),
            },
            "optional": {
                "image_load_cap": ("INT", {"default": 0, "min": 0, "step": 1}),
                "start_index": ("INT", {"default": 0, "min": 0, "step": 1}),
                "include_subfolders": ("BOOLEAN", {"default": False}),
                "strip_extension": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("IMAGE", "INT", "STRING",)
    RETURN_NAMES = ("image", "count", "image_filename",)
    OUTPUT_IS_LIST = (True, False, True)
    FUNCTION = "load_images"
    CATEGORY = kd_image_category
    DESCRIPTION = """Loads images from a folder into a batch."""

    def load_images(self, folder, image_load_cap, start_index, include_subfolders=False, strip_extension=True):
        if not os.path.isdir(folder):
            raise FileNotFoundError(f"Folder '{folder} cannot be found.'")
        
        valid_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.tga']
        image_paths = []
        if include_subfolders:
            for root, _, files in os.walk(folder):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in valid_extensions):
                        image_paths.append(os.path.join(root, file))
        else:
            for file in os.listdir(folder):
                if any(file.lower().endswith(ext) for ext in valid_extensions):
                    image_paths.append(os.path.join(folder, file))

        dir_files = sorted(image_paths)

        if len(dir_files) == 0:
            raise FileNotFoundError(f"No files in directory '{folder}'.")

        # start at start_index
        dir_files = dir_files[start_index:]

        images = []
        image_filename_list = []

        limit_images = False
        if image_load_cap > 0:
            limit_images = True
        image_count = 0

        pbar = ProgressBar(len(dir_files))

        for image_path in dir_files:
            if os.path.isdir(image_path):
                continue
            if limit_images and image_count >= image_load_cap:
                break
            i = Image.open(image_path)
            i = ImageOps.exif_transpose(i)
                        
            
            image = i.convert("RGB")
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            
            images.append(image)
            if strip_extension:
                filename = Path(image_path).stem
            else:
                filename = Path(image_path).name
            image_filename_list.append(filename)
            image_count += 1
            pbar.update(1)

        return (images, len(images), image_filename_list)
