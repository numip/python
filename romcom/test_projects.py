import pandas


class Analysis:
    def __init__(self, fail):
        read = pandas.read_csv(fail, sep=';', index_col=0)
        self.pd = pandas.DataFrame(read)
        self.pd['Рейтинг'] = self.pd['Рейтинг'].apply(lambda i: float(i.split()[0].replace(',', '.')))
        pandas.set_option('display.max_columns', 100)
        pandas.set_option('display.max_rows', 100)
        pandas.set_option('display.precision', 3)

    # вывод полного документа
    def print_fail(self):
        print(self.pd)
        print()

    # вывод краткой информации по документу
    def info(self):
        print(f'\nИнформация по файлу:\n')
        print(self.pd.info())
        print(f'\nСтатистика по числовым столбцам:\n')
        print(self.pd.describe())
        print(f'\nСтатистика по нечисловым столбцам:\n')
        print(self.pd.describe(include=['object']))

    # поиск по столбцу
    def search(self):
        print(self.pd.columns)
        colum = input(f'\nВведите название столбца: ')
        draft = list(set(self.pd[colum]))
        print(*draft, sep='\n')
        if self.pd[colum].dtypes == object:
            prod = input(f'\nВыберите из списка: ')
        elif self.pd[colum].dtypes == int:
            prod = int(input(f'\nВыберите из списка: '))
        else:
            prod = float(input(f'\nВыберите из списка: '))
        ind = self.pd[self.pd[colum] == prod].index - 1
        print(self.pd.iloc[ind])

    # создание сводной таблицы
    def crosstab(self):
        print('Создание сводной таблицы')
        colum1 = input(f'\nВведите название первого столбца: ')
        colum2 = input(f'\nВведите название второго столбца: ')
        print(pandas.crosstab(self.pd[colum1], self.pd[colum2]))


class Go:
    def __init__(self):
        self.file = 'test3.csv'
        self.analysis = Analysis(self.file)
        self.running = True
        self.func = True

    def run(self):
        while self.running:
            print('Выберете подборку фильмов: r - ромкомы, f - семейные')
            number = input('Введите обозначение выбранной подборки: ')

            if number == 'r' or number == 'R':
                self.running = False
            elif number == 'f' or number == 'F':
                self.file = 'test2.csv'
                self.analysis = Analysis(self.file)
                self.running = False
            else:
                print('Ошибка')
                continue
        while self.func:
            print(f'\nЧто вы хотите сделать?')
            var = int(
                input(f'1 - Вывести данные файла\n2 - Вывести краткую информацию о файле\n3 - Поиск информации по '
                      f'столбцу\n4 - Создать сводную таблицу\nЕсли хотите выйти нажмите - 0\n'))
            if var == 1:
                print(self.analysis.print_fail())
                continue
            elif var == 2:
                print(self.analysis.info())
                continue
            elif var == 3:
                print(self.analysis.search())
                continue
            elif var == 4:
                print(self.analysis.crosstab())
                continue
            elif var == 0:
                self.func = False
            else:
                print('Ошибка')
                continue


if __name__ == '__main__':
    go = Go()
    go.run()
