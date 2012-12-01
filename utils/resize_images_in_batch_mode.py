# -*- coding: utf-8 -*-
"""
    resize multiple images using the PIL image library
    the resulting files will have max(width)
    each resized picture will be saved under a unique filename (uuid)
    (c) by Mario Kaufmann
"""

import Image
import os
import uuid

image_dir = "resized"
image_ext = ".jpg"
curr_dir = os.getcwd()

max_width = 1000


if __name__ == "__main__":

    # only if we have jpegs in out folder  
    if not (image_ext in os.listdir(curr_dir)):

        # create file only if it does not exist
        if os.path.isdir(os.path.join(curr_dir, image_dir)):
            pass

        else:
            os.mkdir(image_dir)



        for file in os.listdir(curr_dir):


            if file.lower().endswith(image_ext):
                img = Image.open(file)
                width, height = img.size

                if width > max_width:

                    if width > height:

                        img.thumbnail((max_width, height * max_width / width), Image.BICUBIC)

                    else:

                        img.thumbnail((height * max_width / width, max_width), Image.BICUBIC)


                    img.save(os.path.join(curr_dir, image_dir,
                        str(uuid.uuid4()) + image_ext))

