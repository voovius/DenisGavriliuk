import os

def sort_files_by_extension(base_directory):
    """
    Сортирует файлы по папкам на основе их расширений.

    Если папка для данного расширения не существует, программа создаёт её.
    Обходит все поддиректории начальной директории для поиска файлов.

    :param base_directory: Путь к директории, где будут сортироваться файлы.
    """
    for root, _, files in os.walk(base_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lstrip(".").lower()  # Получаем расширение файла без точки

            if not file_extension:
                folder_name = "no_extension"
            else:
                folder_name = file_extension

            target_folder = os.path.join(base_directory, folder_name)

            # Создаём папку, если она не существует
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # Перемещаем файл в папку с соответствующим расширением
            target_path = os.path.join(target_folder, file)
            os.rename(file_path, target_path)


