import os
import sys
import glob
from tkinter import filedialog
# from PIL import Image, ImageFile
from pathlib import Path
import cv2
from joblib import Parallel, delayed

open_file = filedialog.askdirectory()

max_size = 4096


def joblib_loop(i):
    file_path = images[i]
    try:
        original_image = cv2.imread(file_path)
        original_size = round(os.stat(file_path).st_size/1024, 2)
        width, height, channels = original_image.shape
        if width > max_size:
            original_image = cv2.resize(original_image, (max_size, max_size), interpolation=cv2.INTER_AREA)
        cv2.imwrite(file_path, original_image, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
        new_size = round(os.stat(file_path).st_size/1024, 2)
        print(f"Compressed: {os.path.basename(file_path)} From {original_size} to {new_size}")
    except Exception as e:
        print(e)


images = []
for file in glob.iglob(open_file+"/**", recursive=True):
    if file.endswith(".png"):
        images.append(file)
results = Parallel(n_jobs=-2)(delayed(joblib_loop)(i) for i in range(len(images)))
