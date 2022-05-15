from functools import partial
from datetime import datetime
import winsound


numE1 = "Введите целое число >= 0."
numE2 = "Размер слова не может быть меньше 0."

fileE1 = "Проверьте наличие файла text.txt."
fileE2 = "В файле нет ни одного слова."
fileE3 = "В файле нет ни одного предложения."
fileE4 = "В файле нет ни одного слова с заданной длиной."
fileE5 = "В файле нет ни одного предложения с нечётным кол-вом слов с заданной длиной."


endOfSentence = ".!?"
endOfWord = " -.,!?\n"


def process(k: int):
    try: # попытка открыть файл
        with open("text.txt") as f: # открытие файла
            start = datetime.now() # время начала выполнения
            sentence = ""  # временная переменная для предложения
            word = ""      # временная переменная для слова
            count = 0      # временная переменная для кол-ва слов длины k

            countSymbols = 0    # кол-во символов в файле

            countWords = 0      # кол-во слов в файле
            countSentences = 0  # кол-во предложений в файле

            countTargetWords = 0      # кол-во слов длины k в файле
            countTargetSentences = 0  # кол-во предложений с нечётным кол-вом слов длины k в файле

            # цикл по всем символам в файле
            for char in iter(partial(f.read, 1), ''):
                countSymbols += 1                   # увеличение счётчика
                if char in endOfWord and word:      # если символ - конец слова и слово не пусто
                    word = word.strip()             # обрезка пробелов в начале и конце слова
                    if len(word) > k:               # если длина слова > k
                        count += 1                  # увеличение счётчика
                        countTargetWords += 1       # увеличение счётчика
                    countWords += 1                 # увеличение счётчика
                    sentence += word + " "          # добавление слова в предложение
                    word = ""                       # обнуление слова
                else:                               # иначе
                    word += char                    # добавление символа в слово
                if char in endOfSentence:           # если символ - конец предложения
                    if not count % 2 == 0:          # если слов длины k нечётное кол-во
                        countTargetSentences += 1   # увеличение счётчика
                        sentence = sentence.strip() # обрезка пробелов в начале и конце слова
                        print(f"{sentence}{char}")  # печать предложения
                    countSentences += 1             # увеличение счётчика
                    sentence = ""                   # обнуление предложения
                    count = 0                       # обнуление счётчика

            # проверка на содержание в файле
            if countWords == 0:
                print(fileE2)
            elif countTargetWords == 0:
                print(fileE4)
            if countSentences == 0:
                print(fileE3)
            elif countTargetSentences == 0:
                print(fileE5)

            winsound.Beep(1500, 300)

            end = datetime.now() - start # время выполнения программы
            print(f"Время выполнения: {end}")
            print(f"Символов в файле: {countSymbols}")
            print(f"Слов в файле:     {countWords}")
    except: # вывод ошибки открытия файла
        print(fileE1)


if __name__ == "__main__":
    while True: # цикл для ввода числа
        try: # попытка прочитать число
            k = int(input("Введите размер слова (K): "))
        except: # обработка ошибки ввода числа
            print(numE1)
            continue # следующая итерация цикла

        input()

        if k >= 0: # если число > 0
            process(k) # обработка файла
            break # конец цикла
        else: # обработка ошибки числа
            print(numE2)
