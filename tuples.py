#tuples hash 

n = int(input())
print("Numbers:",n)

data = input().split()
print("data", data)


num_list = list(map(int, data))
print(num_list)

t = tuple(num_list)
print(t)

result = hash(t)
print(result)