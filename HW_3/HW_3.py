import os
import glob
import shutil
from os import path
filename=glob.glob("D:/Python/goit-python/goit-python/HW_3/Trash/*")
documents=['.pdf','.docx','.doc','.txt']
photo=['.jpeg','.jpg','.PNG']
media=['mp3', 'ogg', 'wav', 'amr']
video=['AVI', 'MP4', 'MOV']
setupFiles=['.exe','.msi']
compressedFiles=['.zip']
files=['.apk']
<<<<<<< Updated upstream
DocumentsLocation='D:/Python/goit-python/HW_3/Trash/documents'
mediaLocation='D:/Python/goit-python/HW_3/Trash/media'
photoLocation='D:/Python/goit-python/HW_3/Trash/media'
videoLocation='D:/Python/goit-python/HW_3/Trash/media'
setupFilesLocation='D:/Python/goit-python/HW_3/Trash/setupFiles'
compressedFilesLocation='D:/Python/goit-python/HW_3/Trash/compressedFiles'
FilesLocation='D:/Python/goit-python/HW_3/Trash/Files'
=======
DocumentsLocation='D:/Python/goit-python/goit-python/HW_3/Trash/documents'
mediaLocation='D:/Python/goit-python/goit-python/HW_3/Trash/media'
photoLocation='D:/Python/goit-python/goit-python/HW_3/Trash/media'
videoLocation='D:/Python/goit-python/goit-python/HW_3/Trash/media'
setupFilesLocation='D:/Python/goit-python/goit-python/HW_3/Trash/setupFiles'
compressedFilesLocation='D:/Python/goit-python/goit-python/HW_3/Trash/compressedFiles'
FilesLocation='D:/Python/goit-python/goit-python/HW_3/Trash/Files'
>>>>>>> Stashed changes
for file in filename:
    if os.path.splitext(file)[1] in documents:
        if(path.exists(DocumentsLocation)):
            shutil.move(file,DocumentsLocation)
        else:
            os.mkdir(DocumentsLocation)
            shutil.move(file,DocumentsLocation)
    if os.path.splitext(file)[1] in media:
        if(path.exists(mediaLocation)):
            shutil.move(file,mediaLocation)
        else:
            os.mkdir(mediaLocation)
            shutil.move(file,mediaLocation)
    if os.path.splitext(file)[1] in setupFiles:
        if(path.exists(setupFilesLocation)):
            shutil.move(file,setupFilesLocation)
        else:
            os.mkdir(setupFilesLocation)
            shutil.move(file,setupFilesLocation)
    if os.path.splitext(file)[1] in compressedFiles:
        if(path.exists(compressedFilesLocation)):
            shutil.move(file,compressedFilesLocation)
        else:
            os.mkdir(compressedFilesLocation)
            shutil.move(file,compressedFilesLocation)
    if os.path.splitext(file)[1] in files:
        if(path.exists(FilesLocation)):
            shutil.move(file,FilesLocation)
        else:
            os.mkdir(FilesLocation)
            shutil.move(file,FilesLocation)
    if os.path.splitext(file)[1] in video:
        if(path.exists(videoLocation)):
            shutil.move(file,videoLocation)
        else:
            os.mkdir(videoLocation)
            shutil.move(file,videoLocation)
    if os.path.splitext(file)[1] in photo:
        if(path.exists(photoLocation)):
            shutil.move(file,photoLocation)
        else:
            os.mkdir(photoLocation)
<<<<<<< Updated upstream
            shutil.move(file,photoLocation)
=======
            shutil.move(file,photoLocation)
>>>>>>> Stashed changes
