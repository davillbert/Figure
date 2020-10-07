{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Point:\n",
    "    def __init__(self, x, y):  # конструктор класса с параметрами\n",
    "        self.x, self.y = (x, y)\n",
    "\n",
    "    def __repr__(self):\n",
    "        return \"Point(%s, %s)\" % (self.x, self.y)\n",
    "\n",
    "class Figure:\n",
    "   # переменная класса. сколько всего элементов создано\n",
    "   count = 0\n",
    "\n",
    "   # конструктор класса. вызывается при создании экземпляра\n",
    "   def __init__(self, name):\n",
    "       # переменные экземпляра класса. их значения доступны только объекту\n",
    "        self.list_of_coords = []\n",
    "        self.name = name\n",
    "       \n",
    "       # увеличиваем значение переменной класса\n",
    "        Figure.count += 1\n",
    "        def push(self, p):\n",
    "            list_of_coords.append(p)\n",
    "        def info(self):\n",
    "            print('Имя: ', self.name)\n",
    "        def QuantityOfFigure(self):            \n",
    "            print('\\nВсего фигур: ', Figure.count)\n",
    "\n",
    "class Edge:\n",
    "    def __init__(self, p1, p2):\n",
    "        # переменные экземпляра класса. их значения доступны только объекту\n",
    "        self.p1, self.p2 = (p1, p2)\n",
    "    def __repr__(self):\n",
    "        return \"Edge(%s, %s)\" % (self.p1, self.p2)\n",
    "    def info(self):\n",
    "        print(\"Edge(%s, %s; %s, %s)\" % (self.p1.x, self.p1.y, self.p2.x, self.p2.y))\n",
    "    def on_edge(self, x,y):\n",
    "        if(x <= max(p1.x, p2.x)) and (x >= min(p1.x, p2.x)) and (y <= max(p1.y, p2.y)) and (y >= min(p1.y, p2.y)):\n",
    "            return true\n",
    "        else:\n",
    "            return false\n",
    "    def move_first(self, p):\n",
    "        self.p1 = p\n",
    "    def move_second(self, p):\n",
    "        self.p2 = p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Point(1, 2)\n",
      "Edge(Point(1, 2), Point(2, 4))\n",
      "Edge(Point(3, 6), Point(2, 4))\n"
     ]
    }
   ],
   "source": [
    "p = Point(1,2)\n",
    "P = Point(2,4)\n",
    "print(p)\n",
    "e = Edge(p,P)\n",
    "print(e)\n",
    "p_n = Point(3,6)\n",
    "e.move_first(p_n)\n",
    "print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
