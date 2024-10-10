#Учёт товаров
import os.path

class Product:
    '''
    данный клас предназначен для создания наименования продукта
    атрибуты
    name - наименование товара
    weght - вес товара
    catecory - категория товара
    метод
    __str__ выводит информацию о товаре (name, weght.category
    '''
    def __init__(self,name,wetght,category):
        self.name = name
        self.weght = wetght
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weght}, {self.category}'

class Shop:
    ''' Данный класс осуществляет запись в файл товара
    если товар имеется в файле, то запись не производится
    генерируется сообщение о наличие данного товара
    атрибуты
    _FILE_NAME - содержит название и путь к файлу
    методы
    get_products
        выводит информацию о содержимом файла, если файла не существует выводит
        соответствующее сообщение
    add
        производит запись товара в файл, если товар имеется в файле,
        то выводится сообщение о наличие товара
    '''


    __FILE_NAME = 'product.txt'
    def get_products(self):
        if os.path.exists(self.__FILE_NAME):
            file = open(self.__FILE_NAME,'r')
            shop_product = file.read()
            file.close()
            return shop_product
        else:
            return f'файл - {self.__FILE_NAME} не существует'
    def add(self,*product):
#        file = open(self.__FILE_NAME,'a')
        list_product = self.get_products()

        for i in range(0,len(product)):
            n_p = str(product[i])
            name_product = n_p[0:n_p.find(', ')]
            if name_product in list_product:
                print(f'Продукт {product[i]} существует в магазине')
            else:
                file = open(self.__FILE_NAME,'a')
                file.write(str(product[i]))
                file.write('\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())

