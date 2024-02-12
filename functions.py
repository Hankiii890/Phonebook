import csv
def read_from_csv(page_number, page_size):
    """Вывод записей по странично на экран"""
    with open("data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        data = list(reader)
        start_index = (page_number - 1) * page_size
        end_index = min(start_index + page_size, len(data))
        return data[start_index:end_index], fieldnames


def add_data(new_data, fieldnames):
    """Добавление новой записи в справочник"""
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(new_data)


def edit_data(key, new_data):
    """Реализация редактирования записей в справочнике"""
    updated_data = []
    found_record = False

    with open("data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        for record in reader:
            if record["Lastname"] == key:
                record.update(new_data) # Обновление записи
                found_record = True
            updated_data.append(record)

    if found_record:
        with open("data.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_data)
        print("Запись успешно отредактирована!")
    else:
        print("Запись не найдена. Редактирование невозможно.")


def search_data(criteria, fieldnames):
    """Поиск записей по характеристике"""
    results = []
    with open("data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Lastname"] == criteria["Lastname"]:  # Проверка по фамилии
                results.append(row)
    return results


if __name__ == "__main__":
    try:
        while True:
            print("1. Прочитать данные CSV файла")
            print("2. Добавить Данные в CSV")
            print("3. Редактирование записи CSV")
            print("4. Поиск записей по определенным критериям")
            print("5. Завершение")

            choice = input("Введите свой выбор: ")

            if choice == "1":
                page_number = int(input("Введите номер страницы: "))
                page_size = int(input("Введите размер страницы: "))
                data, fieldnames = read_from_csv(page_number, page_size)
                for entry in data:
                    for field in entry.values():
                        print(field)
                    print()

            elif choice == "2":
                with open("data.csv", mode="r") as file:
                    reader = csv.DictReader(file)
                    fieldnames = reader.fieldnames
                    # Создание словаря, для ввода значения каждого поля из списка fieldnames
                    new_data = {fieldname: input(f'Введите значение поля {fieldname}: ') for fieldname in fieldnames}
                    add_data(new_data, fieldnames)

            elif choice == "3":
                key = input("Введите фамилию человека, запись которого вы хотите изменить: ")

                with open("data.csv", mode="r") as file:
                    reader = csv.DictReader(file)
                    fieldnames = reader.fieldnames
                    print("Доступные поля для изменений: ", fieldnames)

                print("Введите номер поля, которое вы ходите изменить: ".format(len(fieldnames)))
                field_choice = int(input())

                if field_choice == 0:
                    print("Редактирование завершено.")
                elif field_choice < 1 or field_choice > len(fieldnames):
                    print("Некорректный выбор поля!")
                else:
                    field_to_edite = fieldnames[field_choice - 1]
                    new_value = input("Введите новое значение для поля: ".format(field_to_edite))
                    new_data = {field_to_edite: new_value}
                    edit_data(key, new_data)


            elif choice == "4":
                search_criteria = {}
                with open("data.csv", mode="r") as file:
                    reader = csv.DictReader(file)
                    fieldnames = reader.fieldnames
                    search_criteria["Lastname"] = input("Введите фамилию для поиска: ")
                    results = search_data(search_criteria, fieldnames)
                    if results:
                        for entry in results:
                            print(entry)
                    else:
                        print("Записей по указанной фамилии не найдено!")

            elif choice == "5":
                print("Завершение программы...")
                break

            else:
                print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
    except KeyboardInterrupt:
        print("Программа прервана пользователем!")