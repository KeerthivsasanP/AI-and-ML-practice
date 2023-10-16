class year:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        value = self.start
        if self.start < self.end:
                for i in range(self.start,self.end):
                    if self.start%4 != 0 or (self.start%100 == 0 and self.start%400 !=0):
                        self.start += 1
                    else:
                        value = self.start
                        self.start += 4
                        return value
        else:
            raise StopIteration
y = year(2009,2415)
yiter = iter(y)
for i in y:
    print(i)
