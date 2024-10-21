with open('text.txt', 'r') as file:
    text = file.read()
    print(f'Количество слов в тексте: {len(text.split())}')