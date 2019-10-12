def digit_count(fulltext):
    num = [int(i) for i in fulltext if i.isdigit()]
    digitdict = {'Количество цифр в тексте': len(num)}
    return digitdict


def word_count(text6, thisnumberlist2):
    thisworddict = dict(zip(text6, thisnumberlist2))
    return thisworddict


def char_count(text3, thisnumberlist ):
    thischardict = dict(zip(text3, thisnumberlist))
    return thischardict


def text_stat(text, *args):
    textargs = ""
    textargs += "%s" % args
    fulltext = text + "" + textargs
    fulltext = fulltext.casefold()
    linecount = {"Количество строк": fulltext.count("\n")}
    text1 = list(fulltext)
    text2 = set(text1)
    text3 = list(text2)
    text3.sort()
    text3.remove("\n")

    thisnumberlist = []
    for x in text3:
        thisnumberlist.append(fulltext.count(x))

    text4 = ''.join([c for c in fulltext if c not in ('!', '?', '.', ',', '/', '\\', '>', '<', '|', ';', ':', '{', '}',
                                                      '[',']', '=', '+', '-', '(', ')', '*', '^', '%', '$', '`', '~',
                                                      "'", '"')])
    text4 = text4.replace("\n", " ")
    text4 = text4.replace("\t", " ")
    text4 = text4.split(" ")
    text5 = set(text4)
    text6 = list(text5)
    text6.sort()
    text6.remove("")

    thisnumberlist2 = []
    for x in text6:
        thisnumberlist2.append(text4.count(x))

    text_stat = {"digit_stat": digit_count(text4), "line_stat": linecount, "words_stat": word_count(text6,
                 thisnumberlist2), "chars_stat": char_count(text3, thisnumberlist)}

    return text_stat


if __name__ == '__main__':

    print("Программа подсчёта статистики теста!\nВведиет текс!:")

    text = ""
    stopword = ""
    while True:
        line = input()
        if line.strip() == stopword:
            break
        text += "%s\n" % line

    arg = input(str("АРГУМЕНТ ЧЁЁ ПОПУТАЛ?!"))
    digit = text_stat(text, arg).get("digit_stat")
    line_ = text_stat(text, arg).get("line_stat")
    char = text_stat(text, arg).get("chars_stat")
    word = text_stat(text, arg).get("words_stat")
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
