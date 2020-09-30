class Point:
    def __init__(self, x, y):  # конструктор класса с параметрами
        self.coord = (x, y)

    def __repr__(self):
        return "Point(%s, %s)" % self.coord

class Figure:
   # переменная класса. сколько всего элементов создано
   count = 0

   # конструктор класса. вызывается при создании экземпляра
   def __init__(self, name):
       # переменные экземпляра класса. их значения доступны только объекту

       self.name = name
       
       # увеличиваем значение переменной класса
       Figure.count += 1

   def info(self):
       print('Имя: ', self.name,
            '\nВсего фигур: ', Figure.count)
