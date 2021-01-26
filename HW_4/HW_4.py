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
    folder = ['']
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
    folder_list = next(os.walk(adress))[1]
    for file in filename:
        if os.path.splitext(file)[1].lower() in otherfile:
            mainf = str(os.path.splitext(file)[1])
            if mainf == '':
                for m in folder_list:
                    a = str(m)
                    main_format.add(a)
            else:
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
            for y in folder_list:
                if y not in standard_folder:
                    folder_name = adress + str(y) + '/'
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
        print(f'Ducument: {os.listdir(DocumentsLocation)}')
    if path.exists(mediaLocation):
        print(f'media: {os.listdir(mediaLocation)}')
    if path.exists(photoLocation):
        print(f'photo:  {os.listdir(photoLocation)}')
    if path.exists(videoLocation):
        print(f'video:  {os.listdir(videoLocation)}')
    if path.exists(compressedFilesLocation):
        print(f'compressedFiles: {os.listdir(compressedFilesLocation)}')
    if path.exists(elseLocation):
        print(f'else:  {os.listdir(elseLocation)}')
    print(f'main format in folder: {main_format}')
    print(f'unknown format in folder: {unknown_format}')

folder_sort('D:/Python/goit-python/goit-python/HW_4/Trash/')
