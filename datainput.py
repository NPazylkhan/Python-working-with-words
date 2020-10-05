symbols3 = (u"аәбвғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыіъэюяАӘБВҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЬЫІЪЭЮЯ",
           u"aabvgdeejzijkqlmnnooprstuuufhhcsss_yi_euaAABVGDEEJZIJKQLMNNOOPRSTUUUFHZCSS_YI_EUA")
symbols = ['а', 'ә', 'б', 'в', 'ғ', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'қ', 'л', 'м', 'н', 'ң', 'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ұ', 'ү', 'ф', 'х', 'һ', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'і', 'ъ', 'э', 'ю', 'я', 'А', 'Ә', 'Б', 'В', 'Ғ', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Қ', 'Л', 'М', 'Н', 'Ң', 'О', 'Ө', 'П', 'Р', 'С', 'Т', 'У', 'Ұ', 'Ү', 'Ф', 'Х', 'Һ', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'І', 'Ъ', 'Э', 'Ю', 'Я', ' ']
symbols2 = ['a', 'a', 'b', 'v', 'g', 'd', 'e', 'e', 'j', 'z', 'i', 'j', 'k', 'q', 'l', 'm', 'n', 'n', 'o', 'o', 'p', 'r', 's', 't', 'u', 'u', 'u', 'f', 'kh', 'h', 'c', 'ch', 'sh', 'sh', '_', 'y', 'i', '_', 'e', 'u', 'a', 'A', 'A', 'B', 'V', 'G', 'D', 'E', 'E', 'J', 'Z', 'I', 'J', 'K', 'Q', 'L', 'M', 'N', 'N', 'O', 'O', 'P', 'R', 'S', 'T', 'U', 'U', 'U', 'F', 'KH', 'H', 'C', 'CH', 'SH', 'SH', '_', 'Y', 'I', '_', 'E', 'U', 'A', ' ']
# for key in symbols: 
#     for value in symbols2: 
#         res[key] = value 
#         symbols2.remove(value) 
#         break
res = dict(zip(symbols,symbols2))
r = {**res}
# print(r)
# for word in r:
#     r[word] = r[word].split('; ')
#     print(r[word])
# tr = {ord(a):ord(b) for a, b in zip(*res)}

# for Python 2.*:
# tr = dict( [ (ord(a), ord(b)) for (a, b) in zip(*symbols) ] )

# text = u'Қазақша'
filename = r'C:\nlp\kz.txt'
f = open(filename, "r", encoding='UTF-8')
# print (text.translate(r))
t = list(f)
print(t)
# a= []
# for i in t:
#     a.append(res[i])
#     s = "".join(a)
# print(s)
# # s = 'аәбвғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыіъэюя'
# # upper = s.upper()
# # print(upper)
# # import re

# # import arcpy

# # cyrillic_substitution = re.compile(u'[\u0401-\u04f9]')

# # with arcpy.da.UpdateCursor(my_feature_class, column_with_cyrillic) as cur:
# #     for row in cur:
# #         row[0] = cyrillic_substitution.sub("", row[0])
# #         cur.updateRow(row)
