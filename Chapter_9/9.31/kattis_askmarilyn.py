from random import choice
doors = ['A','B','C']
for _ in range(1000): # 1000 reounds
    inital = choice(doors)
    print(inital, flush=True)
    
    res = input()
    res = res.split()
    
    if res[1] == '1':
        print(res[0], flush=True)
    else:
        for door in doors:
            if door != res[0] and door != inital:
                print(door, flush=True)
                break
    
    res = input()
