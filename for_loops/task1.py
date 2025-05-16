# task1 make a fireworks countdown timer that counts down from 10 to 0 and explode in the end

from time import sleep

for i in range(10, 0, -1):
    print('' * i, end='\r')
    print(f'The fireworks gonna blow up in:{i} seconds')
    sleep(1)
print('🎇'* 20)