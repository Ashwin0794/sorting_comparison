#!/usr/bin/python3

lists = []
for i in range(20, 0, -1):
    lists.append(i)

def generate_list(n, percent):
    value = int((n * percent) / 100)   
    result = lists[value:]
    rest = lists[:value]
    rest.reverse()
    result = result + rest
    print(f'for {percent} is {result}')

generate_list(20, 40)
generate_list(20, 60)
generate_list(20, 80)
generate_list(20, 10)


