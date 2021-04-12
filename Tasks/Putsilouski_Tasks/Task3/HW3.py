# 1. Прочитать содержимое файла text.txt
# 2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 15
# 3. Отформатировать текст с учётом максимального количества символов, при этом если слово целиком не умещается в строке, оно должно быть перенесено на следующую, а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
# (модуль textwrap использовать нельзя)


q = int(input("количество символов:\n"))

with open('text.txt', 'r') as text:
    x = text.read()
    print(x,"\n")
    x = x.split("\n")
    print(x,"\n")
    for i in range(len(x)):
        print(i,":"+ x[i])
        string = x[i]
        string = string.split(" ")
        print(string)

# string = ['Произнеся', 'всю', 'эту', 'ахинею,', 'Бенгальский', 'сцепил', 'обе', 'руки', 'ладонь', 'к', 'ладони', 'и', 'приветственно', 'замахал', 'ими', 'в', 'прорез', 'занавеса,', 'от', 'чего', 'тот,', 'тихо', 'шумя,', 'и', 'разошелся', 'в', 'стороны.']
        string_new = ""
        ostatok = ""
        for t in range(len(string)):
            if t == int(len(string) - 1):
                ostatok = ostatok + string[t]
                break
            ostatok = ostatok + string[t] + " "
            ostatok_dl = len(ostatok)

        while(ostatok_dl>q):
            print(ostatok_dl)
            print(string)
            string_new = ""

            for y in range(len(string)+1):
                if len(string_new) <= q:
                    string_new = string_new + string[y] + " "
                    print(string_new, q, len(string_new))
                else:
                    string_new = string_new.replace(" " + string[y - 1] + " ", "")
                    sp = string_new.split(" ")
                    string_new = ""
                    for c in range(len(sp)):
                        print(sp)
                        print(sp[c])
                        vrem = sp[c]
                        print(vrem)
                        print(string)
                        string.remove(vrem)
                    print("Строка после удаления записей", string)

                    ostatok = ""
                    for t in range(len(string)):
                        ostatok = ostatok + string[t] + " "
                        ostatok_dl = (len(ostatok)-1)
                    print("осталось1 в строке первоначальной", ostatok_dl)
















                    llen = 0
                    for z in range(len(sp)):
                        llen = llen + len(sp[z])
                    dob = q - llen
                    print("Добавляем  пробелов:", dob)
                    i = 0
        # Добавляем пробелы
                    while (dob):

                        if len(sp) == 1:
                            sp[0] = sp[0] + " "
                            dob = dob - 1
                        else:
                            sp[i] = sp[i] + " "
                            dob = dob - 1
                            i = i + 1
                            if i == (len(sp) - 1): i = 0
                        print(sp, type(sp))

        # Переводим строку и записываем
                    stroka = ""
                    for p in range(len(sp)):
                        stroka = stroka + sp[p]
                    with open('text2.txt', 'a') as text_new:
                        text_new.write(str(stroka) + "\n")
                        text_new.close()
                    break
        else:
            print("Осталось2", len(ostatok))
            strochka =""
            for r in range(len(string)):
                strochka=strochka+string[r]+" "
            with open('text2.txt', 'a') as text_new:
                text_new.write(strochka + "\n")
                text_new.close()








