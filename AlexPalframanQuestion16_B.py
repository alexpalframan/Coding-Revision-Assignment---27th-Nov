l1 = [4, 5, 9, 8, 10, 17, 99, 77]

for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
 
print(l1)
n = len(l1)
if n % 2 == 0: 
    median1 = l1[n//2] 
    median2 = l1[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = l1[n//2]
    
print(median)