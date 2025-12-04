import json

def update_config(config_path, new_settings):
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
            config.update(new_settings)
            with open(config_path, 'w', encoding='utf-8') as file:
                json.dump(config, file, indent=4)
    except FileNotFoundError:
        with open(config_path, 'w', encoding='utf-8') as file:
            json.dump(new_settings, file, indent=4)
            config = new_settings
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in file.")
    return config


# Пример использования
# Создайте файл config.json с начальными данными
settings_to_update = {'font_size': 16, 'show_notifications': False}
try:
    updated_config = update_config('config.json', settings_to_update)
    print("Конфигурация обновлена:", updated_config)
except ValueError as e:
    print(e)
