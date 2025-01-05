# PetFriends API Tests (HW-24.7.2)

Это проект для тестирования API сервиса PetFriends. Проект содержит различные тесты для проверки функциональности API, включая создание, обновление, удаление питомцев и другие операции.

## Установка

1. Клонируйте репозиторий на свой компьютер:
   git clone https://github.com/Darimo4ka08/PetFriends-24.7.2.git

2. Перейдите в директорию проекта:
cd PetFriends-24.7.2

3. Установите виртуальное окружение:
python -m venv .venv

4. Активируйте виртуальное окружение:
На Windows:
.venv\Scripts\activate
На MacOS/Linux:
source .venv/bin/activate

5. Установите зависимости:
pip install -r requirements.txt

## Конфигурация
Создайте файл .env в корне проекта и добавьте в него следующие переменные:

VALID_EMAIL=your_email@example.com
VALID_PASSWORD=your_password

## Запуск тестов
Для запуска тестов выполните следующую команду:
pytest tests/

## Функциональность
Проект содержит следующие тесты:
1) Получение API ключа (get_api_key_for_valid_user)
2) Получение списка всех питомцев (get_all_pets_with_valid_key)
3) Добавление нового питомца (add_new_pet)
4) Обновление информации о питомце (update_pet_info)
5) Удаление питомца (delete_pet)
6) Добавление нового питомца без фото (create_pet_simple)
7) Добавление фото питомца (set_photo_pet)
8) Удаление питомца с неверным API ключом (delete_pet_with_invalid_auth_key)
9) Добавление нового питомца с неверным API ключом (create_pet_with_invalid_auth_key)
10) Добавление нового питомца без фото с пустыми данными (create_pet_simple_empty_data)
11) Добавление нового питомца без фото с отрицательным возрастом (create_pet_simple_negative_age)
12) Удаление несуществующего питомца (delete_nonexistent_pet)
13) Обновление информации о несуществующем питомце (update_nonexistent_pet_info)
14) Добавление фото несуществующему питомцу (set_photo_nonexistent_pet)
15) Добавление нового питомца без фото с длинным именем (create_pet_simple_long_name)
16) Добавление нового питомца без фото с типом животного, содержащим специальные символы (create_pet_simple_special_char_animal_type)
17) Получение списка питомцев с неверной категорией (get_pets_invalid_category)



