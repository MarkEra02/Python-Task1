from itertools import permutations

print('Enter letters: ')

arr = input().split()

print('Result: ')

for letter in permutations(arr, ):
    print(letter)
