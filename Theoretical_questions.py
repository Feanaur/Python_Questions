# 1  Как получить список всех атрибутов объекта?
	dir()
# 2  Как получить список всех публичных атрибутов объекта? 
	print [arg for arg in dir(obj) if not arg.startswith('_')]
# 3  Как получить список методов объекта?
	[method for method in dir(object) if callable(getattr(object, method))]
# 4  В какой "магической" переменной хранится содержимое help?
	print obj.__doc__
# 5  Есть два кортежа, получить третий как конкатенацию первых двух?
	a = (1,2,3)
	b = (4,5)
	a+b
# 6  Есть два кортежа, получить третий как объединение уникальных элементов первых двух кортежей?
	set(a).intersection(b)
# 7  Почему если в цикле меняется список, то используется for x in lst[:], что означает [:]?
	# Ответ: создает копию списка
# 8  Есть два списка одинаковой длины, в одном ключи, в другом значения. Составить словарь.
	capitals = ["Moscow","London","Paris"]
	countries = ["Russia","England","France"]
	dict(zip(countries,capitals))
# 9  Есть два списка разной длины, в одном ключи, в другом значения. Составить словарь.
#    Для ключей, для которых нет значений использовать None в качестве значения.
#    Значения, для которых нет ключей игнорировать.
	capitals = ["Moscow","London"]
	countries = ["Russia","England","France","USA"]
	for k in countries:
		if countries.index(k)>len(capitals)-1:
			capitals.append("None")
	dict(zip(countries,capitals))
# 10 Есть словарь. Инвертировать его. Т.е. пары ключ: значение поменять местами — значение: ключ.
	inverse_dict = {v:k for k, v in map.items()}
# 11 Есть строка в юникоде, получить 8-битную строку в кодировке utf-8 и cp1251
	u"test".encode('utf-8')
	u"test".encode("cp1251")
# 12 Есть строка в кодировке cp1251, получить юникодную строку.
	unicode('test','cp1251')