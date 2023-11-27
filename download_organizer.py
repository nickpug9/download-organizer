import os
import glob

#move test jpg from download to pictures folder
file_name = "wood.jpg"
source = "/users/nickp/downloads/"
destination = "/users/nickp/downloads/pictures/test/"
img_dest = "/users/nickp/downloads/images/"
pdf_dest = "/users/nickp/downloads/pdfs/"

#move all .jpgs and .pngs to /download/images

# Get all jpg files in downloads
all_jpgs = glob.glob(source  +"*.jpg")

# Check if destination exist, if not, create it
if os.path.exists(img_dest) == False:
    os.mkdir(img_dest)

# Move each JPG to dest
for jpg in all_jpgs:
    print(f"Moving {os.path.basename(jpg)} to {img_dest}")
    os.replace(jpg, img_dest + os.path.basename(jpg))
print(f"All JPGs have been moved to {img_dest}")

# Get all PNGs in Downloads
all_pngs = glob.glob(source + "*.png")

# Move each PNG to dest
for png in all_pngs:
    print(f"Moving {os.path.basename(png)} to {img_dest}")
    os.replace(png, img_dest + os.path.basename(png))
print(f"All PNGs have been moved to {img_dest}")

# Move all zip files to downloads/zip
all_zips = glob.glob(source + "*.zip")

if os.path.exists(source + "zip") == False:
    os.mkdir(source + "zip")
for zip in all_zips:
    os.replace(zip, source + "zip/"+ os.path.basename(zip) )
print(f"All ZIPs have been moved to {source}zip")

# Get all pdfs in Downloads
all_pdfs = glob.glob(source + "*.pdf")

# Check if destination exist, if not, create it
if os.path.exists(pdf_dest) == False:
    os.mkdir(pdf_dest)

# Move each pdf to dest
for pdf in all_pdfs:
    print(f"Moving {os.path.basename(pdf)} to {pdf_dest}")
    os.replace(pdf, pdf_dest + os.path.basename(pdf))
print(f"All pdfs have been moved to {pdf_dest}")

# This code handles every single file type
all_files = glob.glob(source + "*")
all_files = [f for f in all_files if os.path.isfile(f)]

for file in all_files:
    file_name, file_extension = os.path.splitext(file)
    # If a folder for given file_extension doesn't exist, then create one
    if os.path.exists(source + file_extension[1:]) == False:
        os.mkdir(source + file_extension[1:])
        print(f"Folder for extension doesn't exist, creating now.")
    # print( source + file_extension[1:] +"/"+ os.path.basename(file))
    os.replace(file, source + file_extension[1:] +"/"+ os.path.basename(file))

# Previous code that moves a specified file to a specified location

# if os.path.exists(source + file_name): 
#     print(f"File {file_name} found")
#     if os.path.exists(destination) == False:
#         print(f"{destination} does not exist, creating path")
#         os.mkdir(destination)
#     else:
#         print(f"{destination} exists, moving {file_name}")

#     os.replace(source + file_name, destination + file_name)

#     if os.path.exists(destination + file_name):
#         print(f"You have moved {file_name} from {source} to {destination}")
#     else:
#         print(f"Moving {file_name} from {source} to {destination} has FAILED")
# else:
#     print(f"File {file_name} not found, please correct this.")