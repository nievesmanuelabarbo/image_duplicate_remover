# Image Deduplicator

## Description
A lightweight Python utility designed to scan a directory for duplicate image files. Instead of relying on potentially inaccurate file names or sizes, this script calculates the MD5 hash of each image—acting as a unique digital fingerprint. When exact content matches are identified, the duplicates are safely moved into a dedicated subfolder for easy review, keeping your main directory perfectly de-duplicated.

## Features
* **Precision Matching:** Uses cryptographic hashing (MD5) to ensure files are exact duplicates, regardless of their filenames.
* **Non-Destructive Sorting:** Safely isolates duplicates into a separate `duplicates` folder rather than permanently deleting them immediately.
* **Targeted Scanning:** Specifically filters for common image formats (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`).
* **Memory Efficient:** Reads files in 8192-byte chunks, allowing it to process massive batches of high-resolution images without freezing or crashing your system.

## Prerequisites
This script runs on pure, out-of-the-box Python. It relies entirely on Python's standard library (`os`, `hashlib`, `shutil`), so absolutely no external libraries or `pip install` commands are required. 

## How to Use
1. Open the Python script in your preferred editor.
2. Scroll to the very bottom of the code.
3. Update the folder path inside the `clean_duplicates()` function to point to the directory you want to clean up.
   * *Current Example:* `clean_duplicates(r"D:\Ma Yahoo Mail\Has attachments")`
4. Run the script. 
5. Review the newly created `duplicates` folder inside your target directory.

## How It Works
1. **Walk & Identify:** The script recursively walks through the target directory and identifies all files matching the targeted image extensions.
2. **Calculate:** It reads each image in chunks and generates an MD5 hash.
3. **Compare & Move:** It maintains a dictionary of seen hashes. If a newly scanned file generates a hash that already exists in the dictionary, it is flagged as an exact duplicate and immediately moved to the isolation folder.
