filepath = 'counter.txt'

def readnumber():
    try:
        with open(filepath, 'tr') as fp:
            contents = int(fp.read())
            return contents
    except FileNotFoundError:
        # with open(filepath, 'xt') as fp:
        #     fp.write('0')
        return 0

number = readnumber()
number += 1

def writenumber(number):
    with open(filepath, 'tw') as fp:
        fp.write(str(number))
        print(number)

writenumber(number)