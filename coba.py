# NilaiSiswa = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]

# def BubbleSortDescending (nilai) :
#   N = len(nilai)

#   for i in range(N) :
#     for j in range(0, N - i - 1) :
#       if nilai[j] < nilai[j + 1] :
#         temp = nilai[j]
#         nilai[j] = nilai[j + 1]
#         nilai[j + 1] = temp

#   return nilai

# urutNilaiDescending = BubbleSortDescending(NilaiSiswa)

# def TampilkanNilai (nilai) :
#   for i in range(len(nilai)):
#     if nilai[i] >= 90 :
#       predikat = 'A'
#       print(f'Mahasiswa No {i + 1} mendapatkan nilai {nilai[i]} dengan predikat {predikat}')
#     else : 
#       if nilai[i] >= 80 and nilai[i] <= 89 :
#         predikat = 'B'
#         print(f'Mahasiswa No {i + 1} mendapatkan nilai {nilai[i]} dengan predikat {predikat}')
#       else : 
#         predikat = 'C'
#         print(f'Mahasiswa No {i + 1} mendapatkan nilai {nilai[i]} dengan predikat {predikat}')
#   return ''

# print(TampilkanNilai(urutNilaiDescending))

# class Vehicle :
#   def __init__(self, color, merk, maxSpeed) :
#     self.color = color
#     self.merk = merk
#     self.maxSpeed = maxSpeed

#   def berjalan(self) :
#     return f"Mobil {self.merk} sedang berjalan"
  
#   def berhenti(self) :
#     return f"Mobil {self.merk} sedang berhenti"

# test = Vehicle('Biru', "Toyota", 200)

# print(test.color)


# import numpy
# import sys

# var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

# print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
# print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)

# matriks = [[1, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0],
#             [0, 0, 1, 0, 0],
#             [0, 0, 0, 1, 0],
#             [0, 0, 0, 0, 1]]
     
# print(matriks)

# matriks = [[1 for i in range(4)] for j in range(4)]
# print(matriks)

# varMath = [
#   [5,0],
#   [1,-2]
# ]

# defMath = [[0 for j in range(2)] for i in range(2)]

# for i in range(len(varMath)):
#   for j in range(len(varMath[0])) :
#     defMath[i][j] = varMath[i][j]*2

# print(defMath)

lagi = True

def hitungLuasPersegi(panjang, luas) :
  return panjang * luas

while(lagi) :
  print("Selamat datang di program kita")
  panjang = int(input("Masukkan Panjang : "))
  lebar = int(input("Masukkan Lebar : "))
  hasil = hitungLuasPersegi(panjang, lebar)
  print(f'hasilnya adalah : {hasil}')
  print()

  confirm = str(input('Lagi ? [y/t]'))
  if(confirm.lower() == 't' ) :
    lagi = False