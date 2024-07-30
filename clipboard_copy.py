import pyperclip
import pyautogui
import time

# Функция для копирования текста в буфер обмена и получения содержимого буфера
def copy_clipboard():
    # Симулируем нажатие Ctrl+C
    pyautogui.hotkey('ctrl', 'c')
    # Задердка для того, чтобы операция завершилась
    time.sleep(0.5)
    # Получаем содержимое буфера обмена
    clipboard_content = pyperclip.paste()
    return clipboard_content

# Пример использования
if __name__ == '__main__':
    print("Пожалуйста, выделите текст и нажмите Enter")
    input()
    result = copy_clipboard()
    print("Содержимое буфера обмена:")
    print(result)