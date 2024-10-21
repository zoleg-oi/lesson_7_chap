# Записать и запомнить
__FILE_NAME = 'test.txt'


def custom_write(__FILE_NAME, strings):
    output_data = {}
    file = open(__FILE_NAME, 'w', encoding='utf-8')
    number_str = 0
    for str_list in strings:
        number_str += 1
        output_data[number_str, file.tell()] = str_list
        file.write(str_list + '\n')
    file.close()
    return output_data


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write(__FILE_NAME, info)

for elem in result.items():
    print(elem)
