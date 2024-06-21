# MEMBUAT ALGORITMA PROGRAM BUBBLE SORT DI PYTHON

def BubbleSortAscending (array) :
  N = len(array)
  for i in range(N) : # 0 - 9
    for j in range(0,  N - i - 1) : 
      if array[j] > array[j + 1] :
        temp = array[j]
        array[j] = array[j + 1]
        array[j + 1] = temp
  
  return array

ListNama = [1,4,2,5,7,3,6,9,8,10]

print(BubbleSortAscending(ListNama))

