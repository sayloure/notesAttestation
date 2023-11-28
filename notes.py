import csv
from datetime import datetime

# Класс Note для предоставления заметки с полями "Идентификатор, заголовок, тело заметки и дата/время создания последнего изменения"
class Note:
    def __init__(self, id, title, body, timestamp):
        self.id = id
        self.title = title
        self.body = body
        self.timestamp = timestamp

# Класс NoteService для выполнения операций с заметками
class NoteService:
    def __init__(self):
        self.notes = []

    # ... остальные методы ...

    # Функция сброса заметок
    def reset(self):
        self.notes = []
        print("Заметки сброшены.")

    # Функция добавления заметки
    def addNote(self, note):
        for existing_note in self.notes:
            if existing_note.id == note.id:
                print(f"Ошибка: Заметка с ID {note.id} уже существует.")
                return

        self.notes.append(note)
        print("Заметка добавлена.")

    # Функция редактирования заметки
    def editNote(self, id, title, body):
        if not self.notes:
            print("Нет заметок для редактирования.")
            return

        for note in self.notes:
            if note.id == id:
                note.title = title
                note.body = body
                note.timestamp = datetime.now()
                print("Заметка отредактирована.")
                return
        print("Заметка с указанным ID не найдена.")

    # Функция удаления заметки
    def deleteNote(self, id):
        if not self.notes:
            print("Нет заметок для удаления.")
            return

        for i, note in enumerate(self.notes):
            if note.id == id:
                del self.notes[i]
                print("Заметка удалена.")
                return
        print("Заметка с указанным ID не найдена.")

    # Функция чтения заметки
    def readNote(self, id):
        if not self.notes:
            print("Нет заметок для прочтения.")
            return

        for note in self.notes:
            if note.id == id:
                print("Заметка найдена:")
                print("ID:", note.id)
                print("Заголовок:", note.title)
                print("Тело заметки:", note.body)
                print("Дата/время последнего изменения:", note.timestamp)
                return
        print("Заметка с указанным ID не найдена.")

    # Функция сохранения заметок
    def saveNotes(self, filename):
        filename_csv = filename if filename.endswith('.csv') else f"{filename}.csv"
        with open(filename_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['id', 'title', 'body', 'timestamp'])
            for note in self.notes:
                writer.writerow([note.id, note.title, note.body, note.timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')])
        print(f"Заметки сохранены в файл {filename_csv}.")

    # Функция загрузки заметок
    def loadNotes(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=';')
                next(reader)
                loaded_notes = []
                for row in reader:
                    if len(row) == 4:
                        id = int(row[0])
                        title = row[1]
                        body = row[2]
                        timestamp = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f')
                        loaded_notes.append(Note(id, title, body, timestamp))

                if loaded_notes:
                    print("\nЗагруженные заметки:")
                    for note in loaded_notes:
                        print(f"ID: {note.id}, Заголовок: {note.title}")
                    self.notes.extend(loaded_notes)
                else:
                    print("Файл не содержит заметок.")

            print("Заметки загружены из файла", filename)
        except FileNotFoundError:
            print("Файл не найден. Новая коллекция заметок создана.")

if __name__ == "__main__":
    note_service = NoteService()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Прочитать заметку")
        print("5. Показать все ID и заголовки заметок")
        print("6. Сохранить заметки в файл")
        print("7. Загрузить заметки из файла")
        print("8. Сбросить заметки")
        print("0. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            id = int(input("Введите ID: "))
            title = input("Введите заголовок: ")
            body = input("Введите тело заметки: ")
            new_note = Note(id, title, body, datetime.now())
            note_service.addNote(new_note)

        elif choice == "2":
            id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок: ")
            body = input("Введите новое тело заметки: ")
            note_service.editNote(id, title, body)

        elif choice == "3":
            id = int(input("Введите ID заметки для удаления: "))
            note_service.deleteNote(id)

        elif choice == "4":
            id = int(input("Введите ID заметки для прочтения: "))
            note_service.readNote(id)

        elif choice == "5":
            if note_service.notes:
                print("\nID и заголовки заметок:")
                for note in note_service.notes:
                    print(f"ID: {note.id}, Заголовок: {note.title}")
            else:
                print("Нет заметок для отображения.")

        elif choice == "6":
            filename = input("Введите имя файла для сохранения заметок: ")
            note_service.saveNotes(filename)

        elif choice == "7":
            filename = input("Введите имя файла для загрузки заметок: ")
            note_service.loadNotes(filename)
            
        elif choice == "8":
            note_service.reset()

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите действие снова.")