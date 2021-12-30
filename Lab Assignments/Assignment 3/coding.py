import math
import sympy
import numpy as np
import sympy.ntheory as nt 
import math
import random

def problem2a(n):
    x = []
    temp = n
    while n % 2 == 0:
        x.append(2)
        n = n / 2
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            x.append(int(i))
            n = n / i
    if n > 2:
        x.append(int(n) % temp)
    return x

def problem2b(c, a, n):
    e = 1
    l = int(math.log(a, 2))
    for i in range(l-1, -1, -1):
        e = (e**2) % n
        if ((a & (1 << i)) >> i) == 1:
            e = (e * c) % n
    return e


def modulo_inverse_naive(n,m):
    if n == 1:
        return 1
    else:
        if (float(n)).is_integer() and (float(m)).is_integer() and m > 0:
            if math.gcd(n,m) == 1:
                n_mod_m = n%m
                for x in range(1, m): 
                    if (n_mod_m * x)%m  == 1:
                        return x

def problem2c(inputVal):
    n = 31313
    text = "abcdefghijklmnopqrstuvwxyz"
    factors = problem2a(n)
    b = 4913
    totient = 0
    for i in range(1, n):
        if (math.gcd(i, n) == 1):
            totient += 1
    a = modulo_inverse_naive(b, totient)
    l = int(math.log(inputVal, 26))
    result = ""
    for i in range(l,-1,-1):
        letter = inputVal / 26**i
        result += text[int(letter)]
        inputVal = inputVal - (letter * 26**i)
    return result
        


def problem4(val):
    text = "abcdefghijklmnopqrstuvwxyz"
    charMap = dict()
    for i in range(len(text)):
        charMap[(i**25) % 18721] = text[i]
    return charMap[val]


def Euclidean_Algorithm(a,b):
    if (float(a)).is_integer() and (float(b)).is_integer() and a > 0 and b > 0:
        if a < b:
            tmp = a
            a = b
            b = tmp
        #Euclidean Algorithm
        r = []
        r.append(a)
        r.append(b)
        k = 1
        while r[k] != 0:
            q = np.floor((r[k-1]/r[k]))
            r.append(r[k-1] - q*r[k])
            k += 1
        d = r[k-1]
        return int(d)


def problem7():
    factor = problem2a(37069139875071)
    n = 985739879 * 1388749507
    left = 1
    right = n - 1
    while (left < right):
        if (left != right) and ((left**2) % n) == ((right**2) % n):
            x = left
            y = right
        left += 1
        right -= 1
    result = []
    if (math.gcd(x-y), n) in factor:
        result.append(math.gcd(x-y), n)
    if (math.gcd(x+y), n) in factor:
        result.append(math.gcd(x-y), n)
    return result


def problem6b():
    a = 1567886
    b = 2288233
    factor1 = Euclidean_Algorithm(a,b)
    factor2 = b / factor1
    print(factor1, factor2)


def problem9():
    alpha = 5
    beta = 18074
    p = 31847
    a = 7899
    factor = problem2b(alpha, beta, p)
    print(factor)


if __name__ == '__main__':
    print(problem2a(31313))
    problem2Table = "6340 8309 14010 8936 27358 25023 16481 25809 \
23614 7135 24996 30590 27570 26486 30388 9395 \
27584 14999 4517 12146 29421 26439 1606 17881 \
25774 7647 23901 7372 25774 18436 12056 13547 \
7908 8635 2149 1908 22076 7372 8686 1304 \
4082 11803 5314 107 7359 22470 7372 22827 \
15698 30317 4685 14696 30388 8671 29956 15705 \
1417 26905 25809 28347 26277 7897 20240 21519 \
12437 1108 27106 18743 24144 10685 25234 30155 \
23005 8267 9917 7994 9694 2149 10042 27705 \
15930 29748 8635 23645 11738 24591 20240 27212 \
27486 9741 2149 29329 2149 5501 14015 30155 \
18154 22319 27705 20321 23254 13624 3249 5443 \
2149 16975 16087 14600 27705 19386 7325 26277\
19554 23614 7553 4734 8091 23973 14015 107 \
3183 17347 25234 4595 21498 6360 19837 8463 \
6000 31280 29413 2066 369 23204 8425 7792 \
25973 4477 30989"
    problem2List = problem2Table.split(" ")
    problem2Result = ""
    for num in problem2List:
        problem2Result += problem2c(int(num)) + " "
    print(problem2Result)
    problem4List = [365,0,4845,14930,2608,2608,0]
    problem4Result = ""
    for item in problem4List:
        problem4Result += problem4(item)
    print(problem4Result)
    problem6b()
    problem7()
    problem9Text = "(3781, 14409) (31552, 3930) (27214, 15442) (5809, 30274)\
(54000, 31486) (19936, 721) (27765, 29284) (29820, 7710)\
(31590, 26470) (3781, 14409) (15898, 30844) (19048, 12914)\
(16160, 3129) (301, 17252) (24689, 7776) (28856, 15720)\
(30555, 24611) (20501, 2922) (13659, 5015) (5740, 31233)\
(1616, 14170) (4294, 2307) (2320, 29174) (3036, 20132)\
(14130, 22010) (25910, 19663) (19557, 10145) (18899, 27609)\
(26004, 25056) (5400, 31486) (9526, 3019) (12962, 15189)\
(29538, 5408) (3149, 7400) (9396, 3058) (27149, 20535)\
(1777, 8737) (26117, 14251) (7129, 18195) (25302, 10248)\
(23258, 3468) (26052, 20545) (21958, 5713) (346, 31194)\
(8836, 25898) (8794, 17358) (1777, 8737) (25038, 12483)\
(10422, 5552) (1777, 8737) (3780, 16360) (11685, 133)\
(25115, 10840) (14130, 22010) (16081, 16414) (28580, 20845)\
(23418, 22058) (24139, 9580) (173, 17075) (2016, 18131)\
(198886, 22344) (21600, 25505) (27119, 19921) (23312, 16906)\
(21563, 7891) (28250, 21321) (28327, 19237) (15313, 28649)\
(24271, 8480) (26592, 25457) (9660, 7939) (10267, 20623)\
(30499, 14423) (5839, 24179) (12846, 6598) (9284, 27858)\
(24875, 17641) (1777, 8737) (18825, 19671) (31306, 11929)\
(3576, 4630) (26664, 27572) (27011, 29164) (22763, 8992)\
(3149, 7400) (8951, 29435) (2059, 3977) (16258, 30341)\
(21541, 19004) (5865, 29526) (10536, 6941) (1777, 8737)\
(17561, 11884) (2209, 6107) (10422, 5552) (19371, 21005)\
(26521, 5803) (14884, 14280) (4328, 8635) (28250, 21321)\
(28327, 19237) (15313, 28649)"
    problem9Table = problem9Text.split(")")
    print(problem9Table)
    problem9()
     