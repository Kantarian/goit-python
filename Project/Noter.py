from pathlib import Path
import json


class Noter:

    FOLDER = "noter_data/"

    def scan(self):     #сканирует папку для записей на актуальное наличие файлов *.json
        try:
            self.folder = Path(Noter.FOLDER)
            self.content = []
            for item in self.folder.iterdir():
                self.extension = Path(item.name).suffix[1:].upper()
                if self.extension == "JSON":
                    self.content.append(item.name)
            return self.content
        except FileNotFoundError:
            self.folder.mkdir(exist_ok=True)
            return []

    def add(self, name, text: str, tag=None):     #создает заметку. Аргументы: 1 = имя, 2 = заметка, 3 = тэг(None по умолчанию)
        self.note = {text: tag}
        if f"{name}.json" in self.scan():
            return f"'{name}' is used. Choose another name"
        self.new_file_name = f"{str(Noter.FOLDER)}{name}.json"
        with open(self.new_file_name, "w") as f:
            json.dump(self.note, f)
        return f"Record '{name}' was successfully added"

    def show_content_by_text(self):     #сканирует папку и выводит актуальный словарь типа имя:заметка
        res_str = ""
        for item in Path(Noter.FOLDER).iterdir():
            extension = Path(item.name).suffix[1:].upper()
            if extension == "JSON":
                with open(item, "r") as f:
                    note = json.load(f)
                for key, value in note.items():
                    res_str += f"Name: {item.name[:-5]}\nText: {key}\n{'='*20}\n"
        if res_str:
            return res_str
        return f"There is nothing yet"

    def show_content_by_tag(self):      #сканирует папку и выводит актуальный словарь типа имя:тэг
        res_str = ""
        for item in Path(Noter.FOLDER).iterdir():
            extension = Path(item.name).suffix[1:].upper()
            if extension == "JSON":
                with open(item, "r") as f:
                    note = json.load(f)
                for key, value in note.items():
                    res_str += f"Name: {item.name[:-5]}\nText: {value}\n{'-'*20}\n"
        if res_str:
            return res_str
        return f"There is nothing yet"

    def delete(self, name):       #удаляет запись по имени
        file = Path(f"{Noter.FOLDER}{name}.json")
        try:
            file.unlink(missing_ok=False)
            return f"Record number '{name}' was successfully deleted"
        except FileNotFoundError:
            return f"Record number '{name}' doesn`t exist. Check content and try again"

    def show_note(self, name): # выводит заметку с тэгом по имени
        res_dic = {}
        file = Path(f"{Noter.FOLDER}{name}.json")
        try:
            with open(file, "r") as f:
                note = json.load(f)
            for key, value in note.items():
                name_f = key
                text = value
            return f"Name: {name_f}\nText: {text}"
        except FileNotFoundError:
            return f"Record '{name}' doesn`t exist. Check content and try again"

    def show_note_dict (self, name): # выводит заметку с тэгом по имени
        res_dic = {}
        file = Path(f"{Noter.FOLDER}{name}.json")
        try:
            with open(file, "r") as f:
                note = json.load(f)
            for key, value in note.items():
                name_f = key
                text = value
            return  {name_f:text}
        except FileNotFoundError:
            return f"Record '{name}' doesn`t exist. Check content and try again"

    def edit(self, name, text, tag):  # редактирует / перезаписывает заметку. Логика дозаписи: show_note() -> edit()
        res_dic = {}
        file = Path(f"{Noter.FOLDER}{name}.json")
        try:
            with open(file, "w") as f:
                res_dic[text] = tag
                json.dump(res_dic, f)
            return f"Record '{name}' was successfully edited"
        except FileNotFoundError:
            return f"Record '{name}' doesn`t exist. Check content and try again"

    def add_tag(self, name, tag):  # дописывает тэг
        pass


    def find_by_text(self, req):  # сканирует текст заметок на совпадение, выдает словарь типа имя:заметка
        res_str = ""
        for item in Path(Noter.FOLDER).iterdir():
            extension = Path(item.name).suffix[1:].upper()
            if extension == "JSON":
                with open(item, "r") as f:
                    note = json.load(f)
                for key, value in note.items():
                    if str(req) in key:
                        res_str += f"Name: {item.name[:-5]}\nText: {key}\n{'='*20}\n"
        if res_str:
            return res_str
        return f"There is no this text in notes"

    def sort_by_tag(self, req):  # сканирует имена и теги, выдает список фалов с совпадениями в алфавитном порядке
        res_list = []
        res_str = ""
        for file_name in self.scan():
            if req in file_name:
                res_list.append(file_name[:-5])
        for item in Path(Noter.FOLDER).iterdir():
            extension = Path(item.name).suffix[1:].upper()
            if extension == "JSON":
                with open(item, "r") as f:
                    note = json.load(f)
                for key, value in note.items():
                    if str(req) in str(value):
                        res_list.append(item.name[:-5])
        if res_list:
            res_list.sort()
            res_str = "The next files containe the request in their names or tags:\n"
            for rec in res_list:
                res_str += f" - '{rec}'\n"
            return res_str
        return f"There is no this text in tags and names"







noter = Noter()
#print(noter.scan())                       #сканирует папку для записей на актуальное наличие файлов *.json
#print(noter.add("bro2", "he is my brother too", "friend")) #создает заметку. Аргументы: 1 = имя, 2 = заметка, 3 = тэг(None по умолчанию)
#print(noter.show_content_by_text()) #сканирует папку и выводит актуальный словарь типа имя:заметка
#print(noter.show_content_by_tag())    #сканирует папку и выводит актуальный словарь типа имя:тэг
#print(noter.delete("cat"))                #удаляет запись по имени
#print(noter.show_note('car'))             # выводит заметку с тэгом по имени
print(noter.show_note_dict('car'))             # выводит заметку с тэгом по имени
print(noter.add_tag('dog ', 'friend')) # дописывает тэг
#print(noter.edit("car", "VV T-roc", "T")) # редактирует / перезаписывает заметку. Логика дозаписи: show_note() -> edit()
#print(noter.find_by_text("brot")) # сканирует текст заметок на совпадение, выдает словарь типа имя:заметка
#print(noter.sort_by_tag("friend"))  # сканирует имена и теги, выдает список фалов с совпадениями в алфавитном порядке

