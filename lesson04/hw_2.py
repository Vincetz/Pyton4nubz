def digitline_count():
    num = [int(i) for i in text if i.isdigit()]
    digitdict = {'Количество цифр в тексте': len(num)}
    thislinedict = dict.fromkeys(['Количество строк'], thisnumberlist[0])
    seprdict = {'=': '=== Начало = Словаря = Символов ======='}
    digitdict.update(thislinedict)
    digitdict.update(seprdict)
    return digitdict

def word_count():
    thisworddict = dict(zip(text6, thisnumberlist2))
    return thisworddict


def char_count():
    thischardict = dict(zip(text3, thisnumberlist))
    return thischardict


def text_stat():
    seprdict2 = {'==': '=== Конец = Словаря = Символов ===='}
    seprdict3 = {'===': '=== Начало = Словаря = Слов ===='}
    seprdict4 = {'====': '=== Конец = Словаря = Слов ===='}
    ndic = {**digitline_count(), **char_count(), **seprdict2, **seprdict3,**word_count(), **seprdict4}
    return ndic

text = ""
stopword = ""
while True:
    line = input()
    if line.strip() == stopword:
        break
    text += "%s\n" % line

thisnumberlist = []
thisnumberlist2 = []

text = text.casefold()                          # text case fold
text1 = list(text)                              # text1 необходим для функции digit_count
text2 = set(text1)                              # text 2 множество
text3 = list(text2)                             # text 3 список
text3.sort()                                    # text 3 сортирований список

text4 = text.replace("\n", " ")                 # text 4 строка без спец символов
text4 = text4.split(" ")                        # text 4 список слов
text4.remove("")                                # text 4 убрали пустую строку
text5 = set(text4)                              # text 5 множество слов
text6 = list(text5)                             # text 6 список слов
text6.sort()                                    # text 6 Сортированый список слов

for x in text3:
    thisnumberlist.append(text.count(x))

for x in text6:
    thisnumberlist2.append(text4.count(x))

print(''.join(['%r = %s \n' % (key, value) for (key, value) in text_stat().items()]))

# Код написан с Варбанцом, есть не ясные моменты реализации, выясним на уроке с преподователем
