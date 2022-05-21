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
        with open("text.txt") as f:    # открытие файла
            start = datetime.now()      # время начала выполнения
            sentence = ""               # временная переменная для предложения
            sentenceFull = ""           # временная переменная для полного предложения (включая все символы)
            word = ""                   # временная переменная для слова
            count = 0                   # временная переменная для кол-ва слов длины k

            countSymbols = 0    # кол-во символов в файле

            countWords = 0      # кол-во слов в файле
            countSentences = 0  # кол-во предложений в файле

            countTargetWords = 0      # кол-во слов длины k в файле
            countTargetSentences = 0  # кол-во предложений с нечётным кол-вом слов длины k в файле

            # цикл по всем символам в файле
            for char in iter(partial(f.read, 1), ''):
                countSymbols += 1                   # увеличение счётчика
                sentenceFull += char                # добавляем символ к текущему предложению
                if char.isalpha():                  # если символ является буквой (то есть частью слова)
                    word += char                    #   - то продолжаем слово
                else:                               # иначе если символ - конец слова
                    if word:                        #   - то если слово не пусто
                        if len(word) > k:           #       - если длина слова > k
                            count += 1              #           -увеличение счётчика
                            countTargetWords += 1   #           -увеличение счётчика
                        countWords += 1             #       - увеличение счётчика
                        sentence += word + " "      #       - добавление слова в предложение
                        word = ""                   #       - обнуление слова
                if char in endOfSentence:           # если к тому же символ - конец предложения
                    if count % 2:                   #   - если слов длины k нечётное кол-во
                        countTargetSentences += 1   #       - увеличение счётчика
                                                    #       - обрезка пробелов в начале и конце слова
                        sentenceFull = sentenceFull.strip()
                        print(f"{sentenceFull}")    #       - печать предложения
                    countSentences += 1             #   - увеличение счётчика
                    sentence = ""                   #   - обнуление предложения
                    sentenceFull = ""               #   - обнуление предложения
                    count = 0                       #   - обнуление счётчика

            # Если последний символ в файле - НЕ конец, предложения, то нужно рассмотреть последнее предложение отдельно
            if char not in endOfSentence:
                if count % 2:  # - если слов длины k нечётное кол-во
                    countTargetSentences += 1  # - увеличение счётчика
                    #       - обрезка пробелов в начале и конце слова
                    sentenceFull = sentenceFull.strip()
                    print(f"{sentenceFull}")  # - печать предложения
                countSentences += 1  # - увеличение счётчика

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
