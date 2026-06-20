import csv
import os

# def rubify(s):
#     kanji = False
#     res = []
#     c = '.'

#     for char in s[::-1]:
#         if 0x4E00 <= ord(char) <= 0x9FFF:
#             kanji = True
#             res += char
#             continue
#         if kanji:
#             if not 0x4E00 <= ord(char) <= 0x9FFF:
#                 kanji = False
#                 res += c
#         res += char
    
#     if 0x4E00 <= ord(res[-1]) <= 0x9FFF :
#         res.append(c)

#     res.reverse()
#     return ''.join(res).replace('.', '<ruby>').replace('[', '<rt>').replace(']', '</rt></ruby>')

# filename = "n3.txt"
# filelist = []
# with open(os.path.join(filename), encoding="utf-8") as f:
#     for num, row in enumerate(f):
#         # r = row.replace("\t", '$').replace('$$', '$')
#         # r = r.split(',')
#         r = rubify(row)
#         filelist.append(r)

# with open(os.path.join("a" + filename), 'w', encoding="utf-8") as f:
#     f.write(''.join(filelist))

for c in [str(x) + "all.csv" for x in range(1, 11)]:
    vocab = []
    print(c)
    with open(os.path.join("vocab", "core_original", c), encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            roww = row.copy()
            d1 = '<div class="hint">'
            output = roww[0] + d1 + roww[2] + "</div>"
            roww[0] = output
            print(', '.join(row))
            vocab.append(','.join(roww))

    with open(os.path.join("vocab", "core", c), 'w', encoding="utf-8") as f:
        f.write('\n'.join(vocab))
        