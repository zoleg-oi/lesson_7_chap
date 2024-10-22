#Найдёт везде
import re
import os.path
class WordsFinder():
    ''' Класс WordsFinder
    ищет заданные слова в заданных файлах, не учитывая регистр,
    если файл не найден, то выдается соответствующее сообщение
    атрибуты:
    file_name - содержит список наименований файлов для исследования
    методы:
    get_all_word
        данный метод изучает переданные файлы и создает словарь где ключом является наименование файла,
        а значением является список, состоящий из слов, записанных в файл
        при создании списка удаляются заданные символы препинания и тире, а так же слова переводятся в нижний регистр
    find
        данный метод ищет первое вхождение слова в списке файлов и возвращает словарь, где
        ключом является наименование файла, а значением первое вхождение искомого слова в файл
        регистр не учитывается
    count
        данный метод количество вхождений искомого слова в файле, возвращает словарь, где ключом является
        наименование файла, а значение количество вхождений искомого слова
        регистр не учитывается
        '''
    file_name = []

    def __init__(self,*files):
        for fl in files:
            if os.path.exists(fl): # файл найден
                self.file_name.append(fl)
            else:
                print(f'Файл {fl} не найден!')

    def get_all_words(self):
        all_words = {}
        for n_file in self.file_name:
            with open(n_file, encoding='utf-8') as n_file:
                line_str = ''
                for line in n_file:
                    line_str += line.lower()
            ls_ = line_str.replace(' - ', ' ') #для удаления тире вида ' - '
            ls = re.sub(r'[\,\.\=\!\?\;\:]',' ',ls_) # для удаления, указанных знаков препинания
            all_words[n_file.name] = ls.split()
        return all_words

    def find(self,word):
        all_w = self.get_all_words()
        output = {}
        for keys in all_w:
            word_output = all_w[keys]
            if word.lower() in word_output:
                output[keys] = word_output.index(word) + 1
            else:
                output[keys] = f'{word}, нет такого слова в файле'
        return output
    def count(self,word):
        all_w = self.get_all_words()
        output = {}
        for keys in all_w:
            word_count = all_w[keys]
            word_c = word_count.count(word.lower())
            output[keys] = word_c
        return output
'''cl = WordsFinder('test_file.txt')
print(cl.get_all_words())
print(cl.finde('the'))
print(cl.count('the'))'''

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))