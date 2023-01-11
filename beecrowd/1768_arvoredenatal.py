while True:
    try:
        n = int(input())
        for i in range(1, n + 2,2):
            k = n - i
        
            r = (k//2)*" " + (i*'*')
            p = str(r)
            print(p)
        
        k = n - 1
        l =  (k//2)*" " + (1*'*')
        a = str(l)
        r = ((n-3)//2)*" " + 3*'*'
        y = str(r)
        
        print(a)
        print(y)
        print('')
    except EOFError:
        break
