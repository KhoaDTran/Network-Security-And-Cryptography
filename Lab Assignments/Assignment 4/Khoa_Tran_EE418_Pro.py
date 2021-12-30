import numpy as np


def problem7(m, t, K1, K2, IV):
    splitBlock = []
    for i in range(0, int(len(m)/t), 1):
        splitBlock.append(m[i*t: t+i*t])
    outputString = ''
    for block in splitBlock:
        cString = ''
        for j in range(0, t):
            cString += str((int(IV[j]) + int(block[j])) % 2)
        if (int(cString, 2) % 2 == 0):
            for k in range(0, int(len(block)/4), 1):
                cBlock = ''
                cBlock += cString[k*4: k*4+4]
                vec = np.array(list(cBlock), dtype=int) * K1
                for val in vec:
                    for character in val:
                        outputString += str(character)
        else:
            for m in range(0, t):
                outputString += str((int(cString[m]) + int(K2[m])) % 2)
    return outputString


if __name__ == '__main__':
    K1 = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    K2 = '1001001111001001'
    IV = '1010000011111010'
    t = 16
    m = '100110010011100011000101000111101100111110101010010110110101100001101110010101111000000010001001'
    print(problem7(m, t, K1, K2, IV))
    print(problem7(m, t, K1, K2, IV)[
          len(problem7(m, t, K1, K2, IV)) - 16: len(problem7(m, t, K1, K2, IV))])
