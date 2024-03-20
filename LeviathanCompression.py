import os
import sys
import glob
from tkinter import filedialog
from PIL import Image, ImageFile
from pathlib import Path
from timeit import default_timer as timer

ImageFile.LOAD_TRUNCATED_IMAGES = True
open_file = filedialog.askdirectory()

maxRes = sys.argv[1]

try:
    maxRes = int(maxRes)
except Exception:
    maxRes = 4096

for file in glob.iglob(open_file+"/**", recursive=True):
    if file.endswith(".png"):
        filesize = round(Path(file).stat().st_size / 1024)
        print("Before: " + os.path.basename(file) + " {}MB".format(round(filesize/1024, 2)))
        start = timer()
        originalImage = Image.open(file)
        width, height = originalImage.size
        if width > maxRes:
            originalImage = originalImage.resize((maxRes, maxRes))
        originalImage.save(file, "PNG", optimize=True)
        newFilesize = round(Path(file).stat().st_size) / 1024
        end = timer()
        print("After: " + os.path.basename(file) + " {}MB {}% Difference {} Seconds Taken".format(round(newFilesize/1024, 2), round(abs(((newFilesize - filesize) / filesize) * 100)), round(end-start, 2)))
