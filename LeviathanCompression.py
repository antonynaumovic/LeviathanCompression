import os
import sys
import glob
from tkinter import filedialog
# from PIL import Image, ImageFile
from pathlib import Path
import cv2
from joblib import Parallel, delayed

open_file = filedialog.askdirectory()


def joblib_loop(i):
    file_path = images[i]
    try:
        original_image = cv2.imread(file_path)
        cv2.imwrite(file_path, original_image, [cv2.IMWRITE_PNG_COMPRESSION, 9])
        print("Compressed: " + os.path.basename(file_path))
    except Exception as e:
        print(e)


images = []
for file in glob.iglob(open_file+"/**", recursive=True):
    if file.endswith(".png"):
        images.append(file)
results = Parallel(n_jobs=-2)(delayed(joblib_loop)(i) for i in range(len(images)))
