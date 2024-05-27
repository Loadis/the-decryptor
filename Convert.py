from glob import glob
import time

print("convert v1.0\n")

format_file = '*.char'


BookA = '10000000'
BookB = '01000000'
BookC = '00100000'
BookD = '00010000'
BookE = '00001000'
BookF = '00000100'
BookG = '00000010'
BookH = '00000001'
BookI = '10000001'
BookJ = '01000001'
BookK = '00100001'
BookL = '00010001'
BookM = '00001001'
BookN = '00000101'
BookO = '00000011'
BookP = '10000111'
BookQ = '01000111'
BookR = '00100111'
BookS = '00010111'
BookT = '00001111'
BookU = '01010101'
BookV = '10101010'
BookW = '11110000'
BookX = '11001100'
BookY = '11100011'
BookZ = '00011100'
Probe = '00000000'
new_l = '10011001'


try:

    filePath = input("convert >> ")

    def _DEBUG_LOADER():
        global file, filePath, DebugFile

        with open(filePath, 'r') as file:
            for line in file:
                if BookA in line:
                    print('a', end='')
                elif BookB in line:
                    print('b', end='')
                elif BookC in line:
                    print('c', end='')
                elif BookD in line:
                    print('d', end='')
                elif BookE in line:
                    print('e', end='')
                elif BookF in line:
                    print('f', end='')
                elif BookG in line:
                    print('g', end='')
                elif BookH in line:
                    print('h', end='')
                elif BookI in line:
                    print('i', end='')
                elif BookJ in line:
                    print('j', end='')
                elif BookK in line:
                    print('k', end='')
                elif BookL in line:
                    print('l', end='')  
                elif BookM in line:
                    print('m', end='') 
                elif BookN in line:
                    print('n', end='')
                elif BookO in line:
                    print('o', end='') 
                elif BookP in line:
                    print('p', end='')
                elif BookQ in line:
                    print('q', end='')
                elif BookR in line:
                    print('r', end='')
                elif BookS in line:
                    print('s', end='') 
                elif BookT in line:
                    print('t', end='')
                elif BookU in line:
                    print('u', end='')
                elif BookV in line:
                    print('v', end='') 
                elif BookW in line:
                    print('w', end='')
                elif BookX in line:
                    print('x', end='') 
                elif BookY in line:
                    print('y', end='')  
                elif BookZ in line:
                    print('z', end='')
                elif Probe in line:
                    print(' ', end='')
                elif new_l in line:
                    print('\n')
                else:
                    print(filePath + ': error')
                
            input()
            
    if filePath in glob(format_file):
        _DEBUG_LOADER()
    else:
        print("wrong format file")

except:
    print("error")
