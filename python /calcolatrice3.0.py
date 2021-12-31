








while 'true' : 
    
    
    
    
    
    print('''
    ciao questa e` una calcoltrice 
    scegliere op :
    /    
    *
    +
    -

    or type s for the hidden mode 
    ''')
    c = input("")
    if c == 'esc' :
        print('l app è chiusa ')
        break    
    
    
    if c == '/' :
        a = float(input( 'num 1 ->  '))                 
        b = float(input('num 2 ->'))                     
        print('il risultato e` : '  + str(a / b ) )           
    if c == '*'  :
        a = float(input('num 1 ->  '))
        b = float(input('num 2 ->'))
        print('il risultato e` : '  + str(a * b) )
    if c == '+' : 
        a = float(input('num 1 ->  '))
        b = float(input('num 2 ->'))
        print('il risultato e` : '  + str(a + b) )
    if c == '-' : 
        a = float(input('num 1 ->  '))
        b = float(input('num 2 ->'))
        print('il risultato e` : '  + str(a - b) )
    if c == 's':
        print('soryy work in progress')
    print('true')

    

    


































