import numpy
import pandas

read = pandas.read_csv('test3.csv', sep=';', index_col=0)

pd = pandas.DataFrame(read)

print(pd)
print()

pandas.set_option('display.max_columns', 100)
pandas.set_option('display.max_rows', 100)
print()
# смотрим, какая информация содержится в каждой колонке
print(pd.columns)
print()
# узнаем типы данных, находящихся в каждой колонке
print(pd.dtypes)
# преобразуем тип 'Рейтинг' в float
pd['Рейтинг'] = pd['Рейтинг'].apply(lambda x: float(x.split()[0].replace(',', '.')))
print(pd['Рейтинг'])
print()
# находим самый высокий рейтинг
max_rat = pd['Рейтинг'].max()
print(max_rat)
print()
# выводим фильм с самым высоким рейтингом
print(pd.loc[pd['Рейтинг'] == max_rat])
print()
# находим самый низкий рейтинг
min_rat = pd['Рейтинг'].min()
print(min_rat)
print()
# выводим фильм с самым низким рейтингом
print(pd.loc[pd['Рейтинг'] == min_rat])
print()
# средняя оценка фильмов в данной подборке
print(pd['Рейтинг'].mean())
print()
# выводим название фильмов с рейтингом по убыванию
print(pd.sort_values(by='Рейтинг', ascending=False)[['Рейтинг', 'Название']])
print()
# все фильмы с оценкой выше 8
print(pd.loc[pd['Рейтинг'] >= 8])
print()
# все фильмы с оценкой ниже 8
print(pd.loc[pd['Рейтинг'] < 8])
print()
# Выводим всех представленных режиссеров в подборке (без повторений)
draft = []
for i in pd['Режиссер']:
    if i not in draft:
        draft.append(i)
print(*draft, sep='\n')
print()
# Поиск фильмов по режиссеру
prod = input('Введите режиссера из списка: ')
ind = pd[pd['Режиссер'] == prod].index - 1
print(pd.iloc[ind])
print()
# фильм с самым большим количеством оценок
max_pr = pd['Количество оценок'].max()
print(pd.loc[pd['Количество оценок'] == max_pr])
print()
# фильм с самым маленьким количеством оценок
min_pr = pd['Количество оценок'].min()
print(pd.loc[pd['Количество оценок'] == min_pr])
print()
# среднее количество оценок в подборке
print(pd['Количество оценок'].mean())
# общее количество оценок в подборке
print(pd['Количество оценок'].sum())
# выводим название фильмов с рейтингом по убыванию
print(pd.sort_values(by='Количество оценок', ascending=False))
print()
# сортировка фильмов по алфавиту
print(pd.sort_values(by='Название'))
print()
# создаем новую колонку с долей количества оценок одного фильма в общей массе количества оценок
pd['Доля количества оценок (%)'] = pd['Количество оценок'] / pd['Количество оценок'].sum() * 100
print(pd)
print()
# переименовываем колонку
pd = pd.rename(columns={'Доля количества оценок (%)': 'Доля %'})
print(pd)
print()
# удаление колонки
pd.drop(['Доля %'], axis=1, inplace=True)
print(pd)
print()
# выводим 5 фильмов с самым большим количеством оценок
print(pd.nlargest(5, 'Количество оценок'))
print()
# выводим 5 фильмов с самым маленьким количеством оценок
print(pd.nsmallest(5, 'Количество оценок'))
print()
# числовые статистики по всему pd
print(pd.describe())
print()
# нечисловые статистики
print(pd.describe(include=['object']))
print()
# частота повторений стран в подборке
print(pd.Страна.value_counts())
print()
# топ 3 стран чаще всего встречающихся в подборке
print(pd.Страна.value_counts()[:3])
print()
# информация по pd
print(pd.info())
# сортировка по Рейтингу и Количеству оценок
print(pd.sort_values(by=['Рейтинг', 'Количество оценок'], ascending=[False, False]).head(5))
print()
# группируем данные по столбцу Страна и смотрим максимальный год фильмов разных стран
print(pd.groupby(by='Страна')['Год'].max())
print()
# смотрим данные по станам: максимальный и минимальный год выходов фильмов
print(pd.groupby(by='Страна')['Год'].agg([numpy.min, numpy.max]))
print()
# сводная таблица: количество фильмов выпущенное разными странами в разные года представленные в подборке
print(pandas.crosstab(pd['Страна'], pd['Год']))
print()
