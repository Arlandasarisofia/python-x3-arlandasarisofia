# konversi bilangan biner ke desimal

biner = input('Input nilai biner : ')
desimal = 0
pangkat = len(biner)-1

for i in range(len(biner)):
    idesimal = int(biner[i]) * 2 ** pangkat
    desimal += idesimal
    pangkat -= 1

print("Desimalnya adalah : ", desimal)