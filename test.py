import time

def sleeper():
    
    for i in range(0,5):
        print(i+1)
        time.sleep(1)


        
def directXType():


    from directkeys import PressKey,ReleaseKey
    from keys import KEY_W as W,KEY_A as A,KEY_S as S,KEY_D as D
    from keys_2 import w,a,s,d

    

    sleeper()

        
    print('W down')
    PressKey(W)
    PressKey(A)
    time.sleep(.1*60)
    print('W up')
    ReleaseKey(W)
    ReleaseKey(A)


def test2():    

    from pynput.keyboard import Key, Controller

    kb = Controller()
    sleeper()

    kb.press('W')
    time.sleep(.5*60)
    kb.release('W')


directXType()





