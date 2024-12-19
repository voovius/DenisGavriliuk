import os


def sort_files_by_extension(base_directory):
    """
    Сортирует файлы в указанной директории и её поддиректориях по папкам, исходя из их расширений.

    :param base_directory: Путь к базовой директории, в которой будет происходить сортировка.
    """
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Игнорируем папки, которые уже созданы для расширений
            if root.startswith(base_directory) and root != base_directory:
                continue

            # Извлекаем расширение файла
            file_extension = os.path.splitext(file)[1].lower()

            # Если расширение есть (не пустое)
            if file_extension:
                # Папка для расширения (например, ".txt" -> "txt")
                extension_folder = os.path.join(base_directory, file_extension.strip("."))

                # Создаём папку для расширения, если она не существует
                if not os.path.exists(extension_folder):
                    os.makedirs(extension_folder)

                # Перемещаем файл в соответствующую папку
                new_file_path = os.path.join(extension_folder, file)
                os.rename(file_path, new_file_path)


if __name__ == "__main__":
    # Укажите путь к директории, которую нужно отсортировать
    directory = input("Введите путь к директории: ").strip()

    if os.path.exists(directory) and os.path.isdir(directory):
        sort_files_by_extension(directory)
        print("Файлы успешно отсортированы по папкам.")
    else:
        print("Указанная директория не существует или не является папкой.")


