list_alphabet = {
    1:"AEIOULNSTRАВЕИНОРСТ",
    2:"DGДКЛМПУ",
    3:"BCMPБГЁЬЯ",
    4:"FHVWYЙЫ",
    5:"KЖЗХЦЧ",
    8:"JXШЭЮ",
    10:"QZФЩЪ",}
word = input('Введите слово: '). upper()
mark = 0
for i in word:
    for c, z in list_alphabet.items():
        if i in z:
            mark += c
print(mark, 'балл(ов)')
