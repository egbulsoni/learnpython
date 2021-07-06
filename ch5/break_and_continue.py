count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
         break

print("funfou 1")

for x in range(10):
    # doesn't happen
    if x % 2 == 0:
        continue
    print(x)

print("funfou 2")

for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("""this is not printed because for loop
    is terminated because of break but not due to
    fail in condition""")

print("funfou 3")

numbers = [
951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507,
725, 547, 544]

for number in numbers:
    if(number % 2 == 0):
        continue
    else:
        print(number)

#for n in numbers:
#    print(n)