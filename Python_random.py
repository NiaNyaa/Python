import random

#random 1-10

data1 = random.randint(1,10)

print(data1)

#random memilih

isi = "batu","gunting","kertas"

data2 = random.choice(isi)

print(data2)

#random sampai komanya

data3 = random.uniform(50,60)

# tanpa pakai round

print(data3)

#komanya cuma 1

data3 = round(data3,1)

print(data3)

#random sample

huruf = "abcdefghijklmnopqrstuvwxyz"

#merandom 3 huruf dalam a-z

total = 3

data4 = "" .join(random.sample(huruf,total))

print(data4)
