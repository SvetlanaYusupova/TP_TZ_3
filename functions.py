def read_catalog(filename):     # чтение файла с данными
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            chislo = ''
            for word in range(len(line)):
                if line[word].isnumeric():
                    chislo += line[word]
                elif line[word] == '-' and chislo == '' and line[word + 1].isnumeric():
                    chislo += line[word]
                elif line[word] == '.' and line[word + 1].isnumeric():
                    chislo += line[word]
                elif chislo.isdigit():
                    data.append(int(chislo))
                    chislo = ''
                else:
                    try:
                        float(chislo)
                        if chislo[1:].isdigit():
                            data.append(int(chislo))
                            chislo = ''
                        else:
                            data.append(float(chislo))
                            chislo = ''
                    except ValueError:
                        chislo = ''
    return data


def minimal(data):  # нахождение минимального числа
    try:
        minchislo = data[0]
        for i in data:
            if i < minchislo:
                minchislo = i
        return minchislo
    except OverflowError:
        print("Too long numbers")


def maximum(data):  # нахождение максимального числа
    try:
        maxchislo = data[0]
        for i in data:
            if i > maxchislo:
                maxchislo = i
        return maxchislo
    except OverflowError:
        print("Too long numbers")


def summ(data):     # нахождение суммы чисел
    try:
        s = 0
        for i in data:
            s += i
        return s
    except OverflowError:
        print("Too long numbers")


def product(data):  # нахождение произведения чисел
    try:
        p = 1
        for i in data:
            p = p * i
        return p
    except OverflowError:
        print("Too long numbers")
