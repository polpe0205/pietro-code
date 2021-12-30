
import math











print('questa e` una calcolatrice')
print('con cosa vuoi operare  :       /    *   +   -')
c = input('')


if c == '/' : 
    print('scrivi il primo fattore')
    fat1 = input('')
    print('scrivi il secondo')
    fat2 = input('')
    ris = fat1 / fat2
    print('questo e` il risultato')
    print(ris)
if c == '*' : 
    print('scrivi il primo fattore')
    fat3 = input('')
    print('scrivi il secondo')
    fat4 = input('')
    ris2 = fat3 * fat4 
    print(ris2)
if c == '+' :
    print('scrivi il primo fattore')
    fat5 =  input('')
    print('scrivi il secondo')
    fat6 =  input('')
    ris3 =  fat5 + fat6
if c == '-' : 
    print('scrivi il primo fattore')
    fat7 = input('')
    print('scrivi il secondo')
    fat8  = input('')
    ris4 = fat7 - fat8
else : 
    print('esmmdo che tu non hai scritto niente significa che vuoi ')
    print(' la radice quadrata o le potenze scegli ?')
    c2 = input('')
    
if c2  == 'raidice quadrata' : 
    print('fattore 1')
    fat9 = input('')
    print('vabene i radicando 2 ? s/n')
    risp = input('')
    if risp == 's' :
        op = (math.sqrt(fat9))
        print(op)
    if risp == 'n' : 
        print('indicare il radicando')
        rad = input('')
        op2 = pow(fat9,1/rad)
        print(op2)
if c2 ==  'potenze' : 
    print('fattore')
    fat10 = input('')
    print('vabene l esponente 2:  s/n')
    risp2 =  input('')
    if risp2 == 's' : 
        op3 = pow(fat10,2)
    if risp2 == 'n' : 
        print('quale esponente vuoi ?')
        esp  =  input('')
        if esp == 1 : 
            print('esponente non valido')
        if esp == 0 :
            print('esponente non valido')
        else :
            op4 =  pow(fat10,esp)
            print(op4)
else : 
    print('hai digitato qualcosa di non valido')
                

