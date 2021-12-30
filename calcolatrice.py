import math  
m = 2 # ellevazione a potenza 
f = open("registro calcolatrice","w")
f.write('inizio registo calcolatrrice' ) 
f = open("registro calcoltrice","a")


print('cosa vuoi calcolare ipotenusa o cateti i/c')
risp = input('')
if risp == 'i':
    print('valore cateto 1')
    c1 = input("")
    print("valore cateto 2")
    c2 = input('')
    a =  pow(c1,m)
    b =  pow(c2,m)
    c =  a+b 
    i =  (math.sqrt(c))
    print(i)
    f.write('calcolo impotenusa')
    f.write('cateto 1 ', c1 )
    f.write('cateto 2', c2  )
    f.write('ipotenusa', i )
if risp ==  'c':
    print('valore  ipotenusa')
    I = input("")
    print('valore cateto')
    c3 = input('')
    z = pow(c3,m)
    x = pow(I,m) 
    o = x - z 
    c4 = (math.sqrt(o))
    print(c4)
    f.write('calcolo cateti')
    f.write('ipotenusa', I)
    f.write('cateto ', c3)
    f.write('cateto 2', c4  )
else : print('non hai scritto ne i ne c ')























