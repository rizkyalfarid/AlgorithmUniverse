import os

angkaAcak = [4, 6, 5, 1, 3, 2, 9, 7, 8, 10, 20, 50, 23, 43, 21, 35]

ulang = True

while ulang : 
  dataUser = int(input("Masukkan Data Yang Mau Di Cari : "))
  ketemu = False

  for i in range(len(angkaAcak)) :
    if dataUser == angkaAcak[i] :
      os.system('cls')
      print(f'{dataUser} ada di dalam data')
      ketemu = True
      
  if not ketemu :
    os.system('cls')
    print(f'{dataUser} tidak ada di dalam data')

  lagi = input('Mau Cari Lagi [y/t]').lower()
  if lagi != 'y' : 
    ulang = False
