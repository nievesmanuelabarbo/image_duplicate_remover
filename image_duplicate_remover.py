import os
import hashlib
import shutil

def file_hash(path, algo="md5", chunk_size=8192):
    """Generate a hash for a file."""
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

def clean_duplicates(folder, move_to="duplicates"):
    """Find and move duplicate images to a separate folder."""
    seen = {}
    dup_folder = os.path.join(folder, move_to)
    os.makedirs(dup_folder, exist_ok=True)

    for root, _, files in os.walk(folder):
        for name in files:
            if name.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")):
                path = os.path.join(root, name)
                h = file_hash(path)
                if h in seen:
                    print(f"Duplicate found: {path}")
                    shutil.move(path, os.path.join(dup_folder, name))
                else:
                    seen[h] = path

# Use your folder path
clean_duplicates(r"D:\Ma Yahoo Mail\Has attachments")
