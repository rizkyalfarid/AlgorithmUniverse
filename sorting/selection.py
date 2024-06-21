angkaAcak = [4, 6, 5, 1, 3, 2, 9, 7, 8, 10, 20, 50, 23, 43, 21, 35]

def MaximumSort (array) :
  N = len(array)

  for i in range(N - 1) :
    max = 0
    for j in range(N - i) :
      if(array[j] < array[max]) :
        max = j

    temp = array[max]
    array[max] = array[N - i - 1]
    array[N - i - 1] = temp
  
  return array

print(MaximumSort(angkaAcak))
