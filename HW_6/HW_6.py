import os
import glob
import shutil
from os import path
from zipfile import ZipFile





def folder_sort(adress):


    def normalize(string):
        string = str(string)
        dictionary = {
            ord('а'): 'a',
            ord('б'): 'b',
            ord('в'): 'v',
            ord('г'): 'g',
            ord('д'): 'd',
            ord('е'): 'e',
            ord('ё'): 'yo',
            ord('ж'): 'zh',
            ord('з'): 'z',
            ord('и'): 'i',
            ord('й'): 'y',
            ord('к'): 'k',
            ord('л'): 'l',
            ord('м'): 'm',
            ord('н'): 'n',
            ord('о'): 'o',
            ord('п'): 'p',
            ord('р'): 'r',
            ord('с'): 's',
            ord('т'): 't',
            ord('у'): 'u',
            ord('ф'): 'f',
            ord('х'): 'h',
            ord('ц'): 'ts',
            ord('ч'): 'ch',
            ord('ш'): 'sh',
            ord('щ'): 'shch',
            ord('ъ'): 'y',
            ord('ы'): 'y',
            ord('ь'): "'",
            ord('э'): 'e',
            ord('ю'): 'yu',
            ord('я'): 'ya',

            ord('А'): 'A',
            ord('Б'): 'B',
            ord('В'): 'V',
            ord('Г'): 'G',
            ord('Д'): 'D',
            ord('Е'): 'E',
            ord('Ё'): 'Yo',
            ord('Ж'): 'Zh',
            ord('З'): 'Z',
            ord('И'): 'I',
            ord('Й'): 'Y',
            ord('К'): 'K',
            ord('Л'): 'L',
            ord('М'): 'M',
            ord('Н'): 'N',
            ord('О'): 'O',
            ord('П'): 'P',
            ord('Р'): 'R',
            ord('С'): 'S',
            ord('Т'): 'T',
            ord('У'): 'U',
            ord('Ф'): 'F',
            ord('Х'): 'H',
            ord('Ц'): 'Ts',
            ord('Ч'): 'Ch',
            ord('Ш'): 'Sh',
            ord('Щ'): 'Shch',
            ord('Ъ'): 'Y',
            ord('Ы'): 'Y',
            ord('Ь'): "'",
            ord('Э'): 'E',
            ord('Ю'): 'Yu',
            ord('Я'): 'Ya',
        }
        t_string = string.translate(dictionary)
        f_string = ''
        for st in t_string:

            if st.isalpha() or st.isnumeric() or st == "'":
                f_string = f_string + st
            else:
                st = '_'
                f_string = f_string + st
        return t_string


    filename = glob.glob(adress+'*')
    documents = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
    photo = ['.jpeg', '.png', '.jpg', '.svg']
    media = ['.mp3', '.ogg', '.wav', '.amr']
    video = ['.avi', '.mp4', '.mov', '.mkv']
    compressedFiles = ['.zip', '.gz', '.tar']
    folder = ['']
    standard_folder = ['documents', 'photo', 'media', 'video', 'compressedFiles', 'elseLocation']
    otherfile = documents + photo + media + video + compressedFiles + folder
    DocumentsLocation = adress+'documents'
    mediaLocation = adress+'media'
    photoLocation = adress+'photo'
    videoLocation = adress+'video'
    compressedFilesLocation = adress+'compressedFiles'
    elseLocation = adress+'elseLocation'
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
                if path.exists(DocumentsLocation):
                    for file_name in os.listdir(adress):
                        if file_name.endswith(os.path.splitext(file)[1]):
                            new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                            os.rename(adress + file_name, adress + new_name)
                            shutil.move(adress[:-1] + '\\' + new_name, DocumentsLocation)
                else:
                    os.mkdir(DocumentsLocation)
                    for file_name in os.listdir(adress):
                        if file_name.endswith(os.path.splitext(file)[1]):
                            new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                            os.rename(adress + file_name, adress + new_name)
                            shutil.move(adress[:-1] + '\\' + new_name, DocumentsLocation)

            if os.path.splitext(file)[1].lower() in photo:
                if path.exists(photoLocation):
                    for file_name in os.listdir(adress):
                        if file_name.endswith(os.path.splitext(file)[1]):
                            new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                            os.rename(adress + file_name, adress + new_name)
                            shutil.move(adress[:-1] + '\\' + new_name, photoLocation)
                else:
                    os.mkdir(photoLocation)
                    for file_name in os.listdir(adress):
                        if file_name.endswith(os.path.splitext(file)[1]):
                            new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                            os.rename(adress + file_name, adress + new_name)
                            shutil.move(adress[:-1] + '\\' + new_name, photoLocation)
            if os.path.splitext(file)[1].lower() in media:
                if path.exists(mediaLocation):
                    for file_name in os.listdir(adress):
                        if file_name.endswith(os.path.splitext(file)[1]):
                            new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                            os.rename(adress + file_name, adress + new_name)
                            shutil.move(adress[:-1] + '\\' + new_name, mediaLocation)
                else:
                    os.mkdir(mediaLocation)
                    for file_name in os.listdir(adress):
                        if file_name.endswith(os.path.splitext(file)[1]):
                            new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                            os.rename(adress + file_name, adress + new_name)
                            shutil.move(adress[:-1] + '\\' + new_name, mediaLocation)
            if os.path.splitext(file)[1].lower() in video:
                if path.exists(videoLocation):
                    for file_name in os.listdir(adress):
                        if file_name.endswith(os.path.splitext(file)[1]):
                            new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                            os.rename(adress + file_name, adress + new_name)
                            shutil.move(adress[:-1] + '\\' + new_name, videoLocation)
                else:
                    os.mkdir(videoLocation)
                    for file_name in os.listdir(adress):
                        if file_name.endswith(os.path.splitext(file)[1]):
                            new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                            os.rename(adress + file_name, adress + new_name)
                            shutil.move(adress[:-1] + '\\' + new_name, videoLocation)
            if os.path.splitext(file)[1].lower() in compressedFiles:
                if path.exists(compressedFilesLocation):
                    for file_name in os.listdir(adress):
                        if file_name.endswith(os.path.splitext(file)[1]):
                            new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                            os.rename(adress + file_name, adress + new_name)
                            shutil.move(adress[:-1] + '\\' + new_name, compressedFilesLocation)
                            with ZipFile(compressedFilesLocation + '\\' + new_name, 'r') as zipObj:
                                zipObj.extractall(compressedFilesLocation + '/' + normalize(file_name.replace(os.path.splitext(file)[1], '')))
                else:
                    os.mkdir(compressedFilesLocation)
                    for file_name in os.listdir(adress):
                        if file_name.endswith(os.path.splitext(file)[1]):
                            new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                            os.rename(adress + file_name, adress + new_name)
                            shutil.move(adress[:-1] + '\\' + new_name, compressedFilesLocation)
                            with ZipFile(compressedFilesLocation + '\\' + new_name, 'r') as zipObj:
                                zipObj.extractall(compressedFilesLocation + '/' + normalize(file_name.replace(os.path.splitext(file)[1], '')))
            for folder_random in folder_list:
                if folder_random not in standard_folder:
                    new_name_folder = normalize(str(folder_random))
                    os.rename(adress + str(folder_random),adress + str(new_name_folder))
                    try:
                        folder_name = adress + str(new_name_folder) + '/'
                        os.rmdir(folder_name)
                    except OSError as e:
                        folder_name = adress + str(new_name_folder) + '/'
                        folder_sort(folder_name)
        else:
            unknown = str(os.path.splitext(file)[1])
            unknown_format.add(unknown)
            if path.exists(elseLocation):
                for file_name in os.listdir(adress):
                    if file_name.endswith(os.path.splitext(file)[1]):
                        new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                        os.rename(adress + file_name, adress + new_name)
                        shutil.move(adress[:-1] + '\\' + new_name, elseLocation)
            else:
                os.mkdir(elseLocation)
                for file_name in os.listdir(adress):
                    if file_name.endswith(os.path.splitext(file)[1]):
                        new_name = normalize(file_name.replace(os.path.splitext(file)[1], '')) + os.path.splitext(file)[1]
                        os.rename(adress + file_name, adress + new_name)
                        shutil.move(adress[:-1] + '\\' + new_name, elseLocation)
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


folder_sort('D:/Python/goit-python/goit-python/HW_6/Trash/')
