import math
import time

def problem3a_gcd(a, b):
    while (b):
        temp = b
        b = a % b
        a = temp
    return a


def problem3b(a, b, c, number):
    firstGCD = problem3a_gcd(b, c)
    print(number + " problem in 3b: " + str(problem3a_gcd(a, firstGCD)))


def modulo_inverse_naive(n, m, print_flag=0):
    if n == 1:
        if print_flag == 1:
            print('Inverse of 1 in mod ' + str(m) + ' is 1')
        return 1
    else:
        if (float(n)).is_integer() and (float(m)).is_integer() and m > 0:
            if math.gcd(n, m) == 1:
                n_mod_m = n % m
                for x in range(1, m):
                    if (n_mod_m * x) % m == 1:
                        if print_flag == 1:
                            print('Inverse of ' + str(n) + ' in mod ' + str(m) + ' is ' + str(x))
                        return x
            else:
                print('ERROR: gcd(n,m) is not 1. Inverse does not exist for n mod m')
        else:
            print('ERROR: n and m both must be integers. m should be positive')


def problem3d(n, m):
    start_time = time.time()
    modulo_inverse_naive(n, m, 1)
    end_time = time.time()
    print("Run time in seconds (s):", (end_time - start_time))


def problem5b(text, key):
    m = 8
    decryptionKey = [0] * m
    resultList = []
    splitText = []
    resultString = ""
    for i in range(0, len(text), m):
        splitText.append(text[i:i+m])
    for i in range(len(key)):
        decryptionKey[key[i]-1] = i
    for word in splitText:
        string = [None]*m
        for j in range(len(decryptionKey)):
            string[j] = word[decryptionKey[j]]
        resultList.append(string)
    for item in resultList:
        resultString += "".join(item)
    return resultString


def problem6(text, key):
    plainText = ""
    for i in range(len(text)):
        textChar = text[i]
        if (textChar.isupper()):
            plainText += chr((ord(textChar) - key - 65) % 26 + 65)
        elif (textChar.islower()):
            plainText += chr((ord(textChar) - key - 97) % 26 + 65)
        else:
            plainText += textChar
    return plainText

if __name__ == '__main__':
    print("Answer to 3b:")
    problem3b(-144, 2058, 302526, "First")
    problem3b(3674160, -243, 51030, "Second")
    problem3b(-733, -21379, 46782, "Third")
    print("")
    print("Answer to 3d:")
    problem3d(777, 26)
    print("")
    problem3d(-37, 512)
    print("")
    problem3d(24865, 4096)
    print("")
    problem3d(-256789, 56789)
    print("")
    problem3d(-1900757, 770077)
    print("")
    print("Problem 5b: " + problem5b("TGEEMNELNNTDROEOAAHDOETCSHAEIRLM", [4, 1, 6, 2, 7, 3, 8, 5]))
    print("")
    print("Problem 6:")
    inputFile = open("sampleFICT.txt", "r")
    outputFile = open("Khoa_Tran_shift_output.txt", "w")
    cipherText = inputFile.read()
    plainText = problem6(cipherText, 15)
    outputFile.write(plainText)
    characterOutput = cipherText[30:40]
    print(problem6(characterOutput, 15))
    inputFile.close()
    outputFile.close()
