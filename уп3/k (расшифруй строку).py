k1 = int(input())
abc = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',100:'j',110:'k',120:'l',
130:'m',140:'n',150:'o',160:'p',170:'q',180:'r',190:'s',200:'t',210:'u',220:'v',230:'w',
240:'x',250:'y',260:'z',}

for i in range (k1):
    k2 = int(input())
    shifr = int(input())
    slovo = ''
    while shifr > 0 :

        if shifr % 10 == 0:

            slovo = abc[shifr % 1000] + slovo
            shifr = shifr // 1000
        else:
            slovo = abc[shifr % 10] + slovo
            shifr = shifr // 10
    print(slovo)

