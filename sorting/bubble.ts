const angkaAcak : number[] = [4,6,5,1,3,2,9,7,8,10,20,50,23,43,21,35];

const bubbleSortAscending = (array : number[]) : number[] => {
  const n:number = array.length;

  for(let i = 0; i < n - 1; i++) {
    for(let j = 0; j < n - 1 - i; j++) {
      if(array[j] > array[j + 1]) {
        let temp : number = array[j]
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }

  return array;
}

console.log(bubbleSortAscending(angkaAcak));