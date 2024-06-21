var angkaAcak = [4, 6, 5, 1, 3, 2, 9, 7, 8, 10, 20, 50, 23, 43, 21, 35];
var maxSort = function (array) {
    var n = array.length;
    for (var i = 0; i < n - 1; i++) {
        var max = 0;
        for (var j = 0; j < n - i; j++) {
            if (array[j] > array[max]) {
                max = j;
            }
        }
        var temp = array[max];
        array[max] = array[n - 1 - i];
        array[n - 1 - i] = temp;
    }
    return array;
};
console.log(maxSort(angkaAcak));
