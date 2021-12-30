import math
import numpy as np
import matplotlib.pyplot as plt
from texttable import Texttable


def modulo_inverse_naive(n, m):
    if n == 1:
        return m
    else:
        if (float(n)).is_integer() and (float(m)).is_integer() and m > 0:
            if math.gcd(n, m) == 1:
                n_mod_m = n % m
                for x in range(1, m): 
                    if ((n_mod_m * x) % m) == 1:  #(np.mod((n_mod_m * x),m)  == 1):
                        return x
            
            else:
                return None
        else:
            return None
    return None


def problem1(cipherText, a, b):
    aInverse = modulo_inverse_naive(a, 26)
    plainText = ""
    for i in range(len(cipherText)):
        cipherChar = cipherText[i]
        if (cipherChar.isupper()):
            plainText += chr((aInverse*(ord(cipherChar) - 65) - b) % 26 + 65)
        elif (cipherChar.islower()):
            plainText += chr((a*(ord(cipherChar) - 97) - b) % 26 + 65) 
        else:
            plainText += cipherChar
    return plainText


def key_stream_gen(c, z_init, len_z, m):
    M = len(c)
    z = np.zeros(len_z)
    for ii in range(0,len_z):
        if ii < M: #Initial values of key
            z[ii] = int(np.round(z_init[ii]))
        else:
            z_tmp = 0
            for jj in range(0,M):
                z_tmp += c[jj]*z[ii-M+jj]           
            z_tmp = z_tmp % m
            z[ii] = int(np.round(z_tmp))
    return z


def problem6(list):
    len_z = 3
    z_init = list[0:4]
    for m in range(2, 10):
        c = [0] * (m-1)
        for val in range(m):
            for i in range(len(c)):
                c[i] = val
        listTemp = key_stream_gen(c, z_init, len_z, m)
        if (set(listTemp) == set(list)):
            return (m, c)
    return None        


def histogram(text,print_flag = 0):
    #A vector of length 26 (number of letters in English Alphabet)
    frequency = np.zeros(26)
    
    # Encrypting plain text using the key given by shift_key parameter 
    for ii in range(0,len(text)):
        text_char = text[ii]
        # Uppercase characters in text (Note: In ASCII table letter "A" is assigned 65)
        if (text_char.isupper()):
            text_char_index = ord(text_char) - 65
            frequency[text_char_index] += 1
        # Lowercase characters in text (Note: In ASCII table letter "a" is assigned 97)
        elif (text_char.islower()):
            text_char_index = ord(text_char) - 97
            frequency[text_char_index] += 1
        #Spaces, special characters such as ".","#",":", " " (space), etc... will not be encrypted
        
    hist = frequency/np.sum(frequency)
    
    if print_flag == 1:
        #Plotting the histogram 
        fig, ax = plt.subplots(figsize=(20, 10))

        # now, define the ticks (i.e. locations where the labels will be plotted)
        xticks = [ii for ii in range(26)]
    
        # create the histogram
        ax.bar(xticks, hist) # `align='left'` is used to center the labels

        # also define the labels we'll use (note this MUST have the same size as `xticks`!)
        xtick_labels = [chr(ii+65) for ii in range(26)]

        # add the ticks and labels to the plot
        ax.set_xticks(xticks)
        ax.set_xticklabels(xtick_labels)
        ax.set_ylabel('Normalized frequency', fontsize=30)
        ax.set_xlabel('Letters', fontsize=30)
        ax.tick_params(axis='both', which='major', labelsize=25)
        ax.tick_params(axis='both', which='minor', labelsize=25)

        plt.show()
        
        t1 = Texttable() #Creating an empty table
        t2 = Texttable() #Creating an empty table
    
        #Creating first table (Plain text from "a"(0) to "m"(12))
        t1_row_1 = xtick_labels[0:13]
        t1_row_1.insert(0,'Letters')
        t1.add_row(t1_row_1)
        t1_row_2 = hist[0:13].tolist()
        t1_row_2.insert(0,'Norm. freq.')
        t1.add_row(t1_row_2)
    
        #Creating second table (Plain text from "n"(13) to "z"(25))
        t2_row_1 = xtick_labels[13:]
        t2_row_1.insert(0,'Letters')
        t2.add_row(t2_row_1)
        t2_row_2 = hist[13:].tolist()
        t2_row_2.insert(0,'Norm. freq.')
        t2.add_row(t2_row_2)
        
        t1.set_cols_align(["c"]*14)
        t2.set_cols_align(["c"]*14)
        
        col_width = 5*np.ones(14)
        col_width[0] += 2.5
        t1.set_cols_width(col_width)
        t2.set_cols_width(col_width)
        
        #Draw two tables 
        print(t1.draw())
        print(t2.draw())

    
    return hist


def auto_correlation(text_,m):
    
    text = ''
    for ii in range(0,len(text_)):
        text = text + text_[ii].replace('\n','')
        
    #print(text)
    text_len =len(text)
    letter_string = ''
    
    #Record cipher text letters
    for ii in range(0,text_len):
        char = text[ii]
        # Uppercase characters in plain text (Note: In ASCII table letter "A" is assigned 65)
        if (char.isupper()):
            letter_string = letter_string + char
        # Lowercase characters in plain text (Note: In ASCII table letter "a" is assigned 97)
        elif (char.islower()):
            letter_string = letter_string + chr(ord(char) - 97 + 65) #converting lowercase to uppercase letters
    
    letter_string_len = len(letter_string)
    
    sub_strings = []
    
    for ii in range(0,m):
        sub_strings.append('')
        
    jj = 0
    for ii in range(0,letter_string_len):
        sub_strings[jj] += letter_string[ii]
        jj += 1
        if jj == m:
            jj = 0
    
    hist_info  = []
    for ii in range(0,m):
        hist_data = histogram(sub_strings[ii],0) #To show hist
        #print(hist_data)
        hist_info.append(hist_data)
        
    
        
    auto_corr_info = []
    for ii in range(0,m):
        auto_corr_val = 0
        n = len(sub_strings[ii]) 
        for jj in range(0,26):
            auto_corr_val += hist_info[ii][jj]*n*(hist_info[ii][jj]*n-1)
            
        auto_corr_val_mod = 1/(n*(n-1))*auto_corr_val    
        auto_corr_info.append(auto_corr_val_mod)     
    
    return auto_corr_info, hist_info, sub_strings


def cross_correlation(hist_info):
    P = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.023, 0.001, 0.02, 0.001]
    m = len(hist_info)
    
    cross_corr_info = []
    for ii in range(0,m):
        sub_string_cross_info = []
        for KK in range(0,26):
            cross_corr_val = 0
            for jj in range(0,26):
                cross_corr_val += P[jj]*hist_info[ii][(jj+KK) % 26]
        
            sub_string_cross_info.append(cross_corr_val)
            
        cross_corr_info.append(sub_string_cross_info)
        
    return cross_corr_info    
        

def problem7(cipherText):
    relationshipMap = {"A": "b", "B": "s", "C": "e", "D": "v", "E": "r", "F": "a", "G": "l", "H": "n", "I": "t", "J": "o", "K": "p", "L": "y", "M": "w", "N": "h", "O": "f", "P": "m", "Q": "i", "R": "c", "T": "u", "U": "d"}
    result = ""
    for letter in cipherText:
        if (letter in relationshipMap):
            result += relationshipMap[letter]
        else:
            result += letter
    return result


def problem9(problem9aText):
    max_error = []
    for m in range(1,10):
        auto_corr_info, hist_info, sub_strings = auto_correlation(problem9aText,m)
        print('Key length:', m)
        #print('Average auto correlation value among '+str(m)+' sub strings: '+str(np.mean(auto_corr_info)))
        print('Auto correlation R(0) values corresponding to '+str(m)+' sub strings:')
        print([round(auto_corr_info[ii],3) for ii in range(0,len(auto_corr_info))],'\n')
        #Calculate max absolute error (wrt to 0.0656)
        max_error.append(max([abs(auto_corr_info[ii] - 0.0656) for ii in range(0,len(auto_corr_info))]))        
    keyLength = max_error.index(min(max_error))+1
    auto_corr_info, hist_info, sub_strings = auto_correlation(problem9aText,keyLength)
    cross_corr_info = cross_correlation(hist_info)
    Key = []
    for ii in range(0,m):
        print('Sub string', ii)
        fig, ax = plt.subplots(figsize=(20, 10))
        xticks = [ii for ii in range(26)]
        # create the histogram
        ax.bar(xticks, cross_corr_info[ii])
        ax.set_xticks(xticks)
        #ax.set_xticklabels(xtick_labels)
        ax.set_ylabel('C(k)', fontsize=30)
        ax.set_xlabel('k', fontsize=30)
        ax.tick_params(axis='both', which='major', labelsize=25)
        ax.tick_params(axis='both', which='minor', labelsize=25)

        plt.show()
        #print('\n',cross_corr_info[ii])
        max_val = max(cross_corr_info[ii])
        print('Cross correlation values C(k) for k = 0, 1, 2, ..., 25')
        print([round(cross_corr_info[ii][jj],3) for jj in range(0, len(cross_corr_info[ii]))])
        print('max C(k): ', round(max_val,3))
        max_index = cross_corr_info[ii].index(max_val)
        print('Key',ii,': ', max_index,'\n')
        Key.append(max_index)
    print(Key)


if __name__ == '__main__':
    with open("sampleACAD.txt", "r") as inputFile:
        with open("Khoa_Tran_shift_affine_output.txt", "w") as outputFile:
            cipherText = inputFile.read()
            plainText = problem1(cipherText, 9, -17)
            outputFile.write(plainText)
            print("Answer to problem 1b ii: " + plainText[30:40])
    list6a = [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    list6b = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1]
    problem6(list6a)
    problem6(list6b)
    problem7Text = "BCDCEFG BCHFIJEB KECBBCU LCGGCH JH MNCINCE INC OCUB CFBL PJHCL KJGQRQCB MCEC OTCGQHV FBBCI ATAAGCB INFI RJTGU INECFICH INC BLBICP."
    print("Answer to problem 7: " + problem7(problem7Text))
    problem9aText = "KTSVFVMHMCHJUBFDYLMGRWZXNHMVDSVNUBJOJULFZNAQILXSXOJYOROEFJTDXWCNERALABFMLVJFFSEFVXLUJQBORDKMLFBVGYNXLSNJQDWARDXQHAMBRHUPGTYXVVUYXEXHAQJVMLJEZFZBVQPBYPQMPBCUJHBUDSKQFOTVTFGKYXNPDWXJQYVOWLJDUJNJHBUUFUPFOFUTCLWKFJWMKDMOLYNZSQBVBJJHWEEQHLLWTWTORYZXXDYZXOVFPMIHXBMEHSSHZRZKXORYWAPSTZNURNUEFVYPWTRZAQBIWPLBQXLLVUNARFVNNJWHFZCBUYVOBVYVWJVMTNOWFJLVVYVVFGFZRXDXAXIRQTNTVHBAJRZZOBFZSCJHXAQJVXBMEHSPWUUZZRPQNUCPPDTXTWNUCJPFANUKTBPIWXDJTXYANSODPWFAUSRDDGSN"
    problem9bText = "KSQRAUHSQGGBFDQSXOIXMRWCSYFWAAPPOSELGYQGWZGLDCXVFZZIHLCAXILVRTEWGSJPFLWWCWUXAJOWNEFKGHTMUOVLHIUVBYQGLLRETIEDWETEFVHSQVSUREAEKZIXQEEVBRFLWWCHQVKVTETIWHFETXZLGPBEJHHPMRVLEFMPKAOEUSFACHTMUOHSQPSDGZRRSAICQEFKCQZELBFPEKGKSYFMLSSETIEHRPOIFAFPETWJHEAXZLCAURAVBDAJEHBVURVYSBGMJLGETELAVPKWZVIWPHWJZLDILOSNMYKLGHTMUOWXBIDAVPYXGAVPEIHHFLFMGU"
    problem9cText = "GGAMGHUMEDWXUFFAOQLYYSALSHUMEDDXPDVUMAKREIKLAZFEMJQHKKBYKQKYSHVRQFATXMMSFBAHZBXHXHQCGOLERXXTOPPYFBMFRPNVFPZULZWTFQBIYQTHLRTVCAVSKFTWKZFLJGKNXNUVFALYLFRSIXVUHOVJWHVLGOLOHSXTPQFVMQGHVNRQRKTQLXEVGPRCLZBKXWGZEFWFHLVPREVJRQRNWJPHAVDZBSESFFGPVZMTQPVERTHFBHEACKNSFEBXSUEOLWAAZWEEJFPHSSHWMIJJFJYKIYECCILZPEBSGAWARZATXXXJFVBMZUWJGWCKALSMMYERMPGOHFWTRDVQNYNQMBIPMKRZZQLNRIJBPYFBMTKGCMUPJMELSGKQUTZFAJQHGIILZNNYMCUQRHKQQUPDKQJLHWGJWHGPVUATXNVXOMYLTQGYEIKLALCQGYLDWDUAOQZTEAJXFILQGYLTUXZLATXRIIJLQZHZWYIRJKVXBQLTJRTVCAHZTQCHKPUHCQVMECIBQKYMLYMRCIYFATKTYVJQULOULYSGALSJYKIYSVTXCOFMWFTIKKTAVUGHVTCPVUNOKDTIQDEHWTBHGDOMYLEUMDVPPDVUNRKTQIJBCLUMGITPRBETLFATHHQCGOLBTXXIJOBBNTFFGWKKRZSUDJXWGYEPAULMFDOYRZHZWHSAQPFBZOHRTJVBEZHFUQIIEEYLFBTWOXPTBYSPPFVXKQBAOQFFXWGJNAPOTQPNCAIHUOXIGDOMHALDBEISUZULTQLTJIJBCYLEXSXBGQUVKEYTVQTBNRPZZRSSGOAJYKIYSHAPGLTEHKXTPFACVXOJWDNSVUNOTWIUWIYFJAGXXGWZGLKBKTFAGJFPUBNWIBCQULTMMNGHVERILEMPRDYKOLPZZNRIGDRYMMVYSGKWNAPAG"
    problem9(problem9aText)
    problem9(problem9bText)
    problem9(problem9cText)