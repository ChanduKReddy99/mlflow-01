
import os

p1s= range(2,4)
p2s= range(0,2)

for p1 in p1s:
    for p2 in p2s:
        print(f'params: p1:{p1}, p2:{p2}')
        os.system(f'python test.py -p1 {p1} -p2 {p2}')

