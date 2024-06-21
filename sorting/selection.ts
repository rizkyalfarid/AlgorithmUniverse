let angkaAcak = [4, 6, 5, 1, 3, 2, 9, 7, 8, 10, 20, 50, 23, 43, 21, 35];
const maxSort = (array : number[]) : number[] =>  {
  const n : number = array.length;

  for(let i = 0; i < n - 1; i++) {
    let max : number = 0;

    for(let j = 0; j < n - i; j++) {
      if(array[j] > array[max]) {
        max = j;
      }
    }

    let temp : number = array[max];
    array[max] = array[n - 1 - i];
    array[n - 1 - i] = temp
  }

  return array;
}

console.log(maxSort(angkaAcak))