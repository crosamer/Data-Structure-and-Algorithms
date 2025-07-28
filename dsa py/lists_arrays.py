# membuat lists
# list kosong
a = []

# dengan nilai
b = [0, 1, 2, 3, 0, 8, 3]

# list dengan tipe data bervariasi
c = [1, "Adzka", 3.14, True]

# list methods
d = [0, 1, 2, 3, 0, 8, 3]
print(d)

# menambahkan pada akhir list
d.append(1)
print(d)

# mengurutkan list kecil ke besar
d.sort()
print(d)


# membuat algoritma
# mencari bilangan terbesar
arr = [0, 12, 30, 8, 3]
maxArr = arr[0]

for i in arr:
    if i > maxArr:
        maxArr = i

print('Bilangan terbesar:', maxArr)