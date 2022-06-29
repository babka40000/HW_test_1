from main import add_doc, delete_doc, people, shelf
import pytest


class TestSomething:
    def test_add_doc(self):
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        ]

        documents_result = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "pasport", "number": "12345", "name": "Галадриель"}
        ]

        directories = {
            '1': ['2207 876234', '11-2', '5455 028765']
        }

        directories_result = {
            '1': ['2207 876234', '11-2', '5455 028765', '12345']
        }

        #Добавим один элемент, элемент должен добавится, потому что номер полки - существует
        add_doc(documents, directories, '12345', 'pasport', 'Галадриель', '1')
        assert documents == documents_result
        assert directories == directories_result

        # Добавим еще один элемент, элемент не добавится, потому что номер полки - не существует
        add_doc(documents, directories, '3456', 'bilet', 'Мария', '5')
        assert documents == documents_result
        assert directories == directories_result

    def test_delete_doc(self):
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        ]

        documents_result = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "pasport", "number": "12345", "name": "Галадриель"}
        ]

        directories = {
            '1': ['2207 876234', '11-2', '5455 028765']
        }

        directories_result = {
            '1': ['2207 876234', '11-2', '5455 028765', '12345']
        }

        # Удалим один элемент, элемент должен удалиться, потому что номер документа существует в списках
        delete_doc(documents_result, directories_result, '12345')
        assert documents == documents_result
        assert directories == directories_result

        # Удалим еще один элемент, элемент не удалится, потому что номер документа не существует в списках
        delete_doc(documents_result, directories_result, '3456')
        assert documents == documents_result
        assert directories == directories_result

    def test_people(self):
        documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        ]

        assert people(documents, '2207 876234') == 'Василий Гупкин'
        assert people(documents, '543543') is None

    def test_shelf(self):
        directories = {
            '1': ['2207 876234', '11-2', '5455 028765']
        }

        assert shelf(directories, '11-2') == '1'
        assert shelf(directories, '11---2') is None
