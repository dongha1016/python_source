li = [7, 10, -23, 20, 50, 31]

def find_max(a, b):
    if b == 1:
        return a[0]
    else: 
        return max(a[b-1], find_max(a, b-1))
    
print(find_max(li, len(li)))

print('*'*100)

print(list(filter(lambda a:a<5, range(10))))