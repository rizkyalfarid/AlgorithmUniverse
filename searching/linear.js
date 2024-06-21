var angkaAcak = [4, 6, 5, 1, 3, 2, 9, 7, 8, 10, 20, 50, 23, 43, 21, 35];
var linearSearching = function (array, target) {
    var indexAwal = 0;
    while (indexAwal < array.length) {
        if (target == array[indexAwal]) {
            return "".concat(target, " ada di dalam data");
        }
        else {
            return "".concat(target, " tidak ada di dalam data");
        }
    }
    indexAwal++;
};
console.log(linearSearching(angkaAcak, 200));
