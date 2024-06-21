angkaAcak = [4, 6, 5, 1, 3, 2, 9, 7, 8, 10, 20, 50, 23, 43, 21, 35]

# subrutin search sequential tanpa sentinel
def sequentianSearchNoSentinel (array) :
  dataCari = int(input("Masukkan Data Yang Ingin Dicari : "))
  i = 0

  while i < len(array) and dataCari != array[i] :
    i = i + 1

  if i < len(array)  :
    print(f'{dataCari} ditemukan pada indeks {i + 1}')
  else : 
    print(f'{dataCari} TIDAK DI TEMUKAN') 

  return ' '

print(sequentianSearchNoSentinel(angkaAcak))
