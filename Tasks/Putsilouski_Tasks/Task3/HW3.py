# 1. Прочитать содержимое файла text.txt
# 2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 15
# 3. Отформатировать текст с учётом максимального количества символов, при этом если слово целиком не умещается в строке, оно должно быть перенесено на следующую, а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.
# (модуль textwrap использовать нельзя)


q = int(input("количество символов:\n"))
print(q)
# with open('text.txt', 'r') as text:
#     x = text.read()
#     print(x,"\n")
#     x = x.split("\n")
#     print(x,"\n")
#     for i in range(len(x)):
#         print(i,":"+ x[i])
#         string = x[i]
#         string = string.split(" ")
#         print(string)

string = ['Произнеся', 'всю', 'эту', 'ахинею,', 'Бенгальский', 'сцепил', 'обе', 'руки', 'ладонь', 'к', 'ладони', 'и', 'приветственно', 'замахал', 'ими', 'в', 'прорез', 'занавеса,', 'от', 'чего', 'тот,', 'тихо', 'шумя,', 'и', 'разошелся', 'в', 'стороны.']



for y in range(len(string)):
    string_new = ""
    if len(string_new) < q:
        string_new = string_new + string[y] + " "
    else:
        print(string_new)
        string_new = string_new.replace((" " + string[y - 1] + " ", "",1))


        dob = q-len(string_new)
        while dob > 0:
            z=0
            for i in range(len(string_new)):
                if dob == 0: break
                if string_new[i+z] == " " and string_new[i] == " ":
                    string_new[i+z] = "  "
                    i = i + 1
                    dob = dob - 1
                    continue












        print(string_new)


# for y in string:
#     if len(string_new)<q:
#         string_new = string_new+string[y]+" "
#     else:
#         print(string_new)
#         string_new = string_new.replace(" "+string[y-1]+" ","")
#
#     continue


# if string[q-1] == str(" "):
#     print(i,":"+string[q-1])


#
#
#     != " ":
# st_new = st[0:(q-1)]
# st.replace(st[0:(q-1)],"")
# print(st_new)


# for line in text:
#     line = line.split(" ")
#     print(line)


# for i in line:
#     print(i)
#     z = 0
#     if int(z) < int(q):
#         z = z+int(len(line[i]))+1
#     else:
#         for ns in (i-1):
#             line_new = line_new+line[i]+" "
#
#         with open("text2.txt", "w") as text2:
#             text2.write(line_new)


#
#
# for i in range(len(line)):
#     if i == q:
#         if line[i]==" ":
#             line[i] = "\n"
#         else:
#             for z in range ()
#
#         continue
#
#
#
