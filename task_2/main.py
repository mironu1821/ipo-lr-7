#кешко маргарита
print("start code...")
import json
def main():
    try:
        with open('dump.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("[Python] Ошибка: Файл dump.json не найден")
        return
    except json.JSONDecodeError:
        print("[Python] Ошибка: Неверный формат JSON в файле")
        return
    qualification_number = input("Введите номер квалификации: ").strip()
    found_qualifications = []
    for item in data:
        if item.get('model') == 'data.skill':
            fields = item.get('fields', {})
            code = fields.get('code', '')
            if code.startswith(qualification_number):
                name = fields.get('name', 'Неизвестно')
                found_qualifications.append((code, name))
    found_qualifications.sort(key=lambda x: x[0])
    print("[Python] Поиск квалификации")
    if found_qualifications:
        print("===================== Найдено =================")
        for code, name in found_qualifications:
            print(f"{code} >> {name}")
    else:
        print("===================== Не найдено =================")
print("end code...")
