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
                                                  ']', '=', '+', '-', '(', ')', '*', '^', '%', '$', '`', '~', "'", '"')]
                    )
    text4 = text4.replace("\n", " ")                                                  #&
    text4 = text4.split(" ")
    text5 = set(text4)
    text6 = list(text5)
    text6.sort()
    text6.remove("")

    thisnumberlist2 = []
    for x in text6:
        thisnumberlist2.append(text4.count(x))

    text_stat = {**digit_count(text6), **linecount, "words_stat": word_count(text6,thisnumberlist2), "chars_stat":
                 char_count(text3, thisnumberlist)}

    return text_stat

text = ""
stopword = ""
while True:
    line = input()
    if line.strip() == stopword:
        break
    text += "%s\n" % line

print(''.join(['%s = %s \n' % (key, value) for (key, value) in text_stat(text).items()]))
