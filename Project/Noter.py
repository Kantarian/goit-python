from pathlib import Path
import json
import pickle
import difflib


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
        res_dic = {}
        file = Path(f"{Noter.FOLDER}{name}.json")
        try:
            with open(file, "r") as f:
                res_dic = json.load(f)
                for key in res_dic.keys():
                    k = key
                res_dic[k] = tag
            with open(file, "w") as f:
                json.dump(res_dic, f)
            return f"Tag '{tag}' was added to '{name}'"
        except FileNotFoundError:
            return f"Record '{name}' doesn`t exist. Check content and try again"


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



if __name__ == "__main__":
    commands = ["add", "exit", "delete", "show", "find"]
    prediction_experience = {}
    noter = Noter()
    try:
        with open("experience.dat", "rb") as f:
            prediction_experience = pickle.load(f)
    except FileNotFoundError:
        prediction_experience = {}
    while True:
        command = str(input("Enter command:>> ")).lower()
        if not command in commands:
            answer = ""
            while answer != "y":
                if command in commands:
                    break
                for key, value in prediction_experience.items():
                    if command in key:
                        print(f"(d)Perhaps you mean {prediction_experience[key]}")
                        answer = str(input("Answer (Y/N): ")).lower()
                        if answer == "n":
                            command = str(input("Command input error, try again: ")).lower()
                        elif answer == "y":
                            command = prediction_experience[key]
                            break
                if not command in commands:
                    result = str(difflib.get_close_matches(command, commands, cutoff=0.1, n=1))[2:-2]
                    print(f"Perhaps you mean {result}")
                    answer = str(input("Answer (Y/N): ")).lower()
                    if answer == "n":
                        command = str(input("Command input error, try again: ")).lower()
                    elif answer == "y":
                        prediction_experience[command] = result
                        command = result
        if command == "add":
            print("Creating a note...")
            name = str(input("Enter name:> "))
            text = str(input("Enter text:> "))
            answer = str(input("Do you need tags recording now (Y/N):> ")).lower()
            if answer == "y":
                tags = str(input("Enter tags:> "))
                print(noter.add(name, text, tags))
            elif answer == "n":
                print(noter.add(name, text))
            else:
                print("Incorrect answer. Default mode is a new note without tag")
                print(noter.add(name, text, tags))
        if command == "show":
            print("Choosing the note to show...")
            name = str(input("Enter name:> "))
            print(noter.show_note(name))
        if command == "exit":
            print("Good buy!")
            with open("experience.dat", "wb") as f:
                pickle.dump(prediction_experience, f)
            break







noter = Noter()
    # print(noter.scan())                       #сканирует папку для записей на актуальное наличие файлов *.json
# print(noter.add("Helen2", "he is my sister2", "family2")) #создает заметку. Аргументы: 1 = имя, 2 = заметка, 3 = тэг(None по умолчанию)
    # print(noter.show_content_by_text()) #сканирует папку и выводит актуальный словарь типа имя:заметка
    # print(noter.show_content_by_tag())    #сканирует папку и выводит актуальный словарь типа имя:тэг
    # print(noter.delete("cat"))                #удаляет запись по имени
# print(noter.show_note('Helen'))             # выводит заметку с тэгом по имени
    # print(noter.add_tag('bfff', 'fr')) # дописывает тэг
    # # print(noter.edit("car", "VV T-roc", "T")) # редактирует / перезаписывает заметку. Логика дозаписи: show_note() -> edit()
    # print(noter.find_by_text("brot")) # сканирует текст заметок на совпадение, выдает словарь типа имя:заметка
    # print(noter.sort_by_tag("friend"))  # сканирует имена и теги, выдает список фалов с совпадениями в алфавитном порядке
