#Кешко Маргарита
print("start code...")
import json #импортируем json
import os #импортируем json
filename = "cities.json"# Имя файла для хранения данных
operations_count = 0 # Счетчик операций
with open(filename, 'r', encoding='utf-8') as file:# Загрузка данных из файла
    data = json.load(file)
while True:
    print("\n" + "="*50)
    print("МЕНЮ УПРАВЛЕНИЯ ЗАПИСЯМИ О ГОРОДАХ5")
    print("="*50)
    print("1. Вывести все записи")
    print("2. Вывести запись по id")
    print("3. Добавить запись")
    print("4. Удалить запись по id")
    print("5. Выйти из программы")
    print("="*50) #добавили пункты
    try:
        choice = int(input("Выберите пункт меню (1-5): "))
    except ValueError:
        print("Ошибка: введите число от 1 до 5")
        continue
    # 1. Вывести все записи
    if choice == 1:
        operations_count += 1
        print("\n" + "-"*50)
        print("ВСЕ ЗАПИСИ О ГОРОДАХ")
        print("-"*50)
        if not data:
            print("Список городов пуст.")
        else:
            for idx, city in enumerate(data, 1):
                print(f"\nЗапись #{idx}:")
                print(f"  ID: {city['id']}")
                print(f"  Название города: {city['name']}")
                print(f"  Страна: {city['country']}")
                print(f"  Большой город (>100k): {'Да' if city['is_big'] else 'Нет'}")
                print(f"  Население: {city['people_count']:,} чел.")       
        input("\nНажмите Enter для продолжения...")
    # 2. Вывести запись по id
    elif choice == 2:
        operations_count += 1
        print("\n" + "-"*50)
        print("ПОИСК ЗАПИСИ ПО ID")
        print("-"*50)
        try:
            search_id = int(input("Введите ID города для поиска: "))
        except ValueError:
            print("Ошибка: ID должен быть числом")
            input("Нажмите Enter для продолжения...")
            continue  
        found = False
        for idx, city in enumerate(data):
            if city['id'] == search_id:
                print(f"\nЗапись найдена на позиции {idx + 1}:")
                print(f"  ID: {city['id']}")
                print(f"  Название города: {city['name']}")
                print(f"  Страна: {city['country']}")
                print(f"  Большой город (>100k): {'Да' if city['is_big'] else 'Нет'}")
                print(f"  Население: {city['people_count']:,} чел.")
                found = True
                break       
        if not found:
            print(f"\nПредупреждение: город с ID {search_id} не найден.")       
        input("\nНажмите Enter для продолжения...")    
    # 3. Добавить запись
    elif choice == 3:
        operations_count += 1
        print("\n" + "-"*50)
        print("ДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ")
        print("-"*50)        
        # Автоматическое определение нового ID
        if data:
            new_id = max(city['id'] for city in data) + 1
        else:
            new_id = 1        
        name = input("Введите название города: ")
        country = input("Введите название страны: ")        
        is_big_input = input("Это большой город (>100000 человек)? (да/нет): ").lower()
        is_big = is_big_input in ['да', 'yes', 'y', 'д']       
        try:
            people_count = int(input("Введите население города: "))
        except ValueError:
            print("Ошибка: население должно быть числом")
            input("Нажмите Enter для продолжения...")
            continue       
        # Создание новой записи
        new_city = {
            "id": new_id,
            "name": name,
            "country": country,
            "is_big": is_big,
            "people_count": people_count
        }        
        data.append(new_city)    
        # Сохранение в файл
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"\nЗапись успешно добавлена с ID: {new_id}")
        ("Нажмите Enter для продолжения...")    
    # 4. Удалить запись по id
    elif choice == 4:
        operations_count += 1
        print("\n" + "-"*50)
        print("УДАЛЕНИЕ ЗАПИСИ ПО ID")
        print("-"*50) 
        try:
            delete_id = int(input("Введите ID города для удаления: "))
        except ValueError:
            print("Ошибка: ID должен быть числом")
            input("Нажмите Enter для продолжения...")
            continue
        deleted = False
        for idx, city in enumerate(data):
            if city['id'] == delete_id:
                del data[idx]
                # Сохранение в файл
                with open(filename, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=2)               
                print(f"\nЗапись с ID {delete_id} успешно удалена.")
                deleted = True
                break
        if not deleted:
            print(f"\nПредупреждение: город с ID {delete_id} не найден.")
        input("Нажмите Enter для продолжения...")
    # 5. Выйти из программы
    elif choice == 5:
        print("\n" + "-"*50)
        print(f"За время работы выполнено операций: {operations_count}")
        print("Программа завершена.5")
        print("-"*50)
        break
    else:
        print("Ошибка: выберите пункт от 1 до 5")
print("end code...")