# Задание 7 Разработать класс «Студенческая группа». Предусмотреть
# возможность работы с переменным числом студентов, поиска записи по
# какому-либо признаку (фамилия, дата рождения, номер телефона и .д.),
# добавление и удаление записей, сортировки по разным полям.

class studgroup():
    students=[]
    def __init__(self):
        pass
    def Zanis(self):
        Name=input('Фамилия')
        DR=input('Дата рождения')
        Nomer=input('Номер телефона')
        a=[Name,DR,Nomer]
        self.students.append(a)
    def removeZapis(self):
        NameNaYdal=input("Введите фамилию на удаление")
        for i in self.students:
            if NameNaYdal in i:
                self.students.remove(i)
                print('Удалено')
            else:
                print('Такого студента нет')
    def FindName(self):
        NameFind=input('Каво найти, насяника?')
        for i in self.students:
            if NameFind in i:
                print(i[0]+'\t'+i[1]+'\t'+i[2]+'\n')
            else:
                print('Такой записи нет')
    def sorting(self):
        self.kniga.sort()
    def see(self):
        for i in self.students:
            print(i[0]+'\t'+i[1]+'\t'+i[2]+'\n')

Spisok=studgroup()
Spisok.Zanis()
Spisok.Zanis()
Spisok.Zanis()
Spisok.see()
