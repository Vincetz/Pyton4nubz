def digit_count(text6):
    num = [int(i) for i in text6 if i.isdigit()]
    digitdict = {'Количество цифр в тексте': len(num)}
    return digitdict


def word_count(text6, thisnumberlist2):
    thisworddict = dict(zip(text6, thisnumberlist2))
    return thisworddict


def char_count(text3, thisnumberlist ):
    thischardict = dict(zip(text3, thisnumberlist))
    return thischardict


def text_stat(text):
    text = text.casefold()
    linecount = {"Количество строк": text.count("\n")}
    text1 = list(text)
    text2 = set(text1)
    text3 = list(text2)
    text3.sort()
    text3.remove("\n")

    thisnumberlist = []
    for x in text3:
        thisnumberlist.append(text.count(x))

    text4 = ''.join([c for c in text if c not in ('!', '?', '.', ',', '/', '\\', '>', '<', '|', ';', ':', '{', '}', '[',
                                                  ']', '=', '+', '-', '(', ')', '*', '^', '%', '$', '`', '~', "'", '"',
                                                  '\n')])
    text4 = text4.replace("\n", " ")
    text4 = text4.split(" ")
    text5 = set(text4)
    text6 = list(text5)
    text6.sort()
    text6.remove("")

    thisnumberlist2 = []
    for x in text6:
        thisnumberlist2.append(text4.count(x))

    text_stat = {"digit_stat": digit_count(text6), "line_stat": linecount, "words_stat": word_count(text6,
                 thisnumberlist2), "chars_stat": char_count(text3, thisnumberlist)}

    return text_stat


print("Программа подсчёта статистики теста!\nВведиет текс!:")

text = ""
stopword = ""
while True:
    line = input()
    if line.strip() == stopword:
        break
    text += "%s\n" % line

digit = text_stat(text).get("digit_stat")
line_ = text_stat(text).get("line_stat")
char = text_stat(text).get("chars_stat")
word = text_stat(text).get("words_stat")
print("="*40, "\n")
print(''.join(['%s = %s \n' % (key, value) for (key, value) in digit.items()]))
print(''.join(['%s = %s \n' % (key, value) for (key, value) in line_.items()]))
print("="*40)
print("===== Начало = Словаря = Символов =====")
print(''.join(['%r = %s \n' % (key, value) for (key, value) in char.items()]))
print("====== Конец = Словаря = Символов ======")
print("="*40,)
print("======= Начало = Словаря = Слов =======")
print(''.join(['%r = %s \n' % (key, value) for (key, value) in word.items()]))
print("======== Конец = Словаря = Слов ========")
