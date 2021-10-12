key=input('Digite sua senha:\n') 

Key2=('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

#Nums=list('0123456789')


for i1 in (Key2) :
    for i2 in (Key2) :
        for i3 in (Key2) :
            for i4 in (Key2) :
                for i5 in (Key2) :
                    for i6 in (Key2) :
                        for i7 in (Key2) :
                            for i8 in (Key2) :
                                Key3=(i1+i2+i3+i4+i5+i6+i7+i8)
                                print(Key3)
                                if(Key3==key) :
                                    #print('>>> {} <<<'.format(key))
                                    print('Encontrada')
                                    exit()