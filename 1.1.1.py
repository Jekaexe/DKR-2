from random import randint
arr=[i for i in range(0,4)]
for i in arr:
    arr[i]=randint(-20,20)
    print(arr[i])
print('raznost max and min', abs(max(arr)- min(arr)))