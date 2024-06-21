var angkaAcak = [4, 6, 5, 1, 3, 2, 9, 7, 8, 10, 20, 50, 23, 43, 21, 35];
var BubblesortAscending = function (array) {
    var n = array.length;
    var i = 0;
    while (i < n - 1) {
        var j = 0;
        while (j < n - i - 1) {
            if (array[j] > array[j + 1]) {
                var temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
            j++;
        }
        i++;
    }
    return array;
};
console.log(BubblesortAscending(angkaAcak));
