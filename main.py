documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people(docs, doc_number):
    for doc in docs:
        if doc["number"] == doc_number:
            return doc["name"]


def shelf(directories, doc_number):
    for dir_name, dir in directories.items():
        if doc_number in dir:
            return dir_name


def list(docs, dirs):
    print("Документы-----")
    for doc in docs:
        print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')
    print("Полки-----")
    for dir_number, dir_vol in dirs.items():
        print(f"{dir_number} -- > {dir_vol}")
    print()


def add_doc(docs, dirs, doc_number, doc_type, doc_owner, shelf_number):
    if shelf_number in dirs.keys():
        docs.append({"type": doc_type, "number": doc_number, "name": doc_owner})
        dirs[shelf_number].append(doc_number)
        return True


def delete_doc(docs, dirs, doc_number):
    for doc in docs:
        if doc["number"] == doc_number:
            docs.remove(doc)
            for dir in dirs.values():
                if doc_number in dir:
                    dir.remove(doc_number)
            return True


def add_shelf(dirs, shelf_number):
    if shelf_number not in dirs.keys():
        dirs[shelf_number] = []
        return True


def move(dirs, doc_number, shelf_number):
    for dir in dirs.values():
        if (doc_number in dir) and (shelf_number in dirs.keys()):
            dir.remove(doc_number)
            dirs[shelf_number].append(doc_number)
            return True


if __name__ == '__main__':
    while True:
        command = input("Введите команду (для выхода введите 'x'): ")

        if command == "p":
            doc_number = input("Введите номер документа: ")
            people_name = people(documents, doc_number)
            if people_name == None:
                print("Документа с таким номером нет в списке")
            else:
                print(f"Документ пренадлежит: {people_name}")
            print()

        elif command == "s":
            doc_number = input("Введите номер документа: ")
            shelf_name = shelf(directories, doc_number)
            if shelf_name == None:
                print("Документа с таким номером нет в списке")
            else:
                print(f"Документ на полке номер {shelf_name}")
            print()

        elif command == "l":
            list(documents, directories)

        elif command == "a":
            doc_number = input("Введите номер документа: ")
            doc_type = input("Введите номер тип документа: ")
            doc_owner = input("Введите имя владельца документа: ")
            shelf_number = input("Введите номер полки: ")
            if add_doc(documents, directories, doc_number, doc_type, doc_owner, shelf_number):
                print("Документ успешно добавлен")
            else:
                print("Нет полки с таким номером")
            print()

        elif command == "d":
            doc_number = input("Введите номер документа: ")
            if delete_doc(documents, directories, doc_number):
                print(f"Документ номер {doc_number} удален из списков")
            else:
                print("Номер не найден")
            print()

        elif command == "m":
            doc_number = input("Введите номер документа: ")
            shelf_number = input("Введите номер полки: ")
            if move(directories, doc_number, shelf_number):
                print(f"Документ номер {doc_number} перенесен на полку {shelf_number}")
            else:
                print("Нет такого документа или полки")
            print()

        elif command == "as":
            shelf_number = input("Введите номер полки: ")
            if add_shelf(directories, shelf_number):
                print(f"Полка номер {shelf_number} добавлена")
            else:
                print("Полка с таким номером уже существует")
            print()

        elif command == "x":
            print("Хорошего дня")
            break

        else:
            print("Введена некорректная команда")
            print()
        print(documents)
        print(directories)
