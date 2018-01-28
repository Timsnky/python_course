while True:
    try:
        x=int(raw_input('Enter Number: '))
        y=x/2
    except ValueError,e:
        print('Wrong Value'+str(e))
    except KeyboardInterrupt,e:
              print('Keyboard'+str(e))
    else:
        print(y)




