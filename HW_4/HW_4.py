import os
import glob
import shutil
from os import path



def folder_sort(adress):
    filename = glob.glob(adress+'*')
    documents = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
    photo = ['.jpeg', '.png', '.jpg', '.svg']
    media = ['.mp3', '.ogg', '.wav', '.amr']
    video = ['.avi', '.mp4', '.mov', '.mkv']
    compressedFiles = ['.zip', '.gz', '.tar']
    folder = ['',' ','_']
    standard_folder = ['documents','photo','media','video','compressedFiles','elseLocation']
    otherfile = documents + photo + media + video + compressedFiles + folder
    DocumentsLocation = 'D:/Python/goit-python/goit-python/HW_4/Trash/documents'
    mediaLocation = 'D:/Python/goit-python/goit-python/HW_4/Trash/media'
    photoLocation = 'D:/Python/goit-python/goit-python/HW_4/Trash/photo'
    videoLocation = 'D:/Python/goit-python/goit-python/HW_4/Trash/video'
    compressedFilesLocation = 'D:/Python/goit-python/goit-python/HW_4/Trash/compressedFiles'
    elseLocation = 'D:/Python/goit-python/goit-python/HW_4/Trash/elseLocation'
    main_format = {'None'}
    unknown_format = {'None'}
    x = next(os.walk('D:/Python/goit-python/goit-python/HW_4/Trash'))[1]
    for file in filename:
        if os.path.splitext(file)[1].lower() in otherfile:
            mainf = str(os.path.splitext(file)[1])
            if mainf == '':
                for m in mainf:
                    a = str(m)
                    main_format.add(a)
            if mainf != '':
                main_format.add(mainf)
            if os.path.splitext(file)[1].lower() in documents:
                if(path.exists(DocumentsLocation)):
                    shutil.move(file,DocumentsLocation)
                else:
                    os.mkdir(DocumentsLocation)
                    shutil.move(file,DocumentsLocation)
            if os.path.splitext(file)[1].lower() in photo:
                if(path.exists(photoLocation)):
                    shutil.move(file,photoLocation)
                else:
                    os.mkdir(photoLocation)
                    shutil.move(file,photoLocation)
            if os.path.splitext(file)[1].lower() in media:
                if(path.exists(mediaLocation)):
                    shutil.move(file,mediaLocation)
                else:
                    os.mkdir(mediaLocation)
                    shutil.move(file,mediaLocation)
            if os.path.splitext(file)[1].lower() in video:
                if (path.exists(videoLocation)):
                    shutil.move(file, videoLocation)
                else:
                    os.mkdir(videoLocation)
                    shutil.move(file, videoLocation)
            if os.path.splitext(file)[1].lower() in compressedFiles:
                if (path.exists(compressedFilesLocation)):
                    shutil.move(file, compressedFilesLocation)
                else:
                    os.mkdir(compressedFilesLocation)
                    shutil.move(file, compressedFilesLocation)
            for y in x:
                if y not in standard_folder:
                    folder_name = adress + str(y) + '/'
                    print(folder_name)
                    folder_sort(folder_name)
        else:
            unknown = str(os.path.splitext(file)[1])
            unknown_format.add(unknown)
            if(path.exists(elseLocation)):
                shutil.move(file,elseLocation)
            else:
                os.mkdir(elseLocation)
                shutil.move(file,elseLocation)
    if path.exists(DocumentsLocation):
        print(os.listdir(DocumentsLocation))
    if path.exists(mediaLocation):
        print(os.listdir(mediaLocation))
    if path.exists(photoLocation):
        print(os.listdir(photoLocation))
    if path.exists(videoLocation):
        print(os.listdir(videoLocation))
    if path.exists(compressedFilesLocation):
        print(os.listdir(compressedFilesLocation))
    if path.exists(elseLocation):
        print(os.listdir(elseLocation))
    print(main_format)
    print(unknown_format)

folder_sort('D:/Python/goit-python/goit-python/HW_4/Trash/')