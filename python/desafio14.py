# loop com o break
print("\nloop loop com break")  
i = 0
for i in range(1, 11):
    print(i) 
    if i == 5:
        break

# loop com o continue
print("\nloop loop com continue")  
i = 0
for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(i)