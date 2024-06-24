import json

# Начальный словарь с данными
initial_data = {
    'Россия': 'Москва',
    'Германия': 'Берлин',
    'Китай': 'Пекин',
    'США': 'Вашингтон',
    'Франция': 'Париж'
}

class CountryCapitalManager:
    """Класс для управления данными о странах и столицах в JSON файле."""

    def __init__(self, filename="countries_and_capitals.json"):
        """Инициализирует объект с именем файла."""
        self.filename = filename

    def _load_data(self):
        """Внутренний метод для загрузки данных из JSON файла."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}  # Возвращаем пустой словарь, если файл не найден

    def _save_data(self, data):
        """Внутренний метод для сохранения данных в JSON файл."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def add_entry(self, country, capital):
        """Добавляет страну и столицу в словарь."""
        data = self._load_data()
        data[country] = capital
        self._save_data(data)
        print(f"Добавлено: {country} - {capital}")

    def remove_entry(self, country):
        """Удаляет страну и столицу из словаря."""
        data = self._load_data()
        if country in data:
            del data[country]
            self._save_data(data)
            print(f"Удалено: {country}")
        else:
            print(f"Страна не найдена: {country}")

    def get_capital(self, country):
        """Возвращает столицу по заданной стране."""
        data = self._load_data()
        return data.get(country, None)  # Возвращает None, если страна не найдена

    def get_country(self, capital):
        """Возвращает страну по заданной столице."""
        data = self._load_data()
        for country, city in data.items():
            if city == capital:
                return country
        return None  # Возвращает None, если столица не найдена


if __name__ == "__main__":
    manager = CountryCapitalManager("countries_data.json")
    manager._save_data(initial_data)  # Сохраняем начальные данные

    print("Загруженные данные:", manager._load_data())

    manager.add_entry("Италия", "Рим")
    print("Данные после добавления:", manager._load_data())

    manager.remove_entry("США")
    print("Данные после удаления:", manager._load_data())

    print("Столица России:", manager.get_capital("Россия"))
    print("Страна с столицей Париж:", manager.get_country("Париж"))
