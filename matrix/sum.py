# menjumlahkan dua buah matrix sama ordo
import numpy
import os

MatrixSatu = numpy.array([[5,4,5],
                          [2,3,2]])
MatrixDua = numpy.array([[1,2,1],
                        [5,4,3]])

print(f'Ini adalah` matriks 1 : \n {MatrixSatu}') 
print()
print(f'Ini adalah matriks 2 : \n {MatrixDua}')
print()

hasil = MatrixSatu + MatrixDua

for i in range(2) :
  print(f'{MatrixSatu[i]} + {MatrixDua[i]} = {hasil[i]}')

os.system('pause')

