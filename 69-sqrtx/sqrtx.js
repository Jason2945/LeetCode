/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    let num1 = 0;
    while (num1 <= x){
        if (num1 * num1 === x){
            return num1;
        }else if (num1 * num1 > x){
            return num1 - 1;
        }
        num1++;
    }
};