const angkaAcak = [4, 6, 5, 1, 3, 2, 9, 7, 8, 10, 20, 50, 23, 43, 21, 35];

const linearSearching = (array : number[], target : number) : any => {
  let indexAwal : number = 0;
  while(indexAwal < array.length) {
    if(target == array[indexAwal]) {
      return `${target} ada di dalam data`
    } else {
      return `${target} tidak ada di dalam data`; 
    }
  }
  indexAwal++
}

console.log(linearSearching(angkaAcak, 200));
