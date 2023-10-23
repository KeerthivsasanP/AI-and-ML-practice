def leapyear(start,end):
    count = 1
    for i in range(start,end):
        if i%4 == 0 and (i%100 != 0 or i%400==0):
            yield (count)
            count += 1
            yield (i)
            
    

start = 2000
end = 2019
gen = leapyear(start,end)
print(gen)
for i in range(start,end):
    try:
        print(next(gen))
    except StopIteration:
        break


while True:
    try:
        year = next(gen)
        print(year)
    except StopIteration:
        break
