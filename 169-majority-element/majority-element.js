/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let n = nums.length / 2;
    nums.sort();
    let counter = 0;
    if (nums.length === 1){
        return nums[0];
    }
    for (let checkNum = 0; checkNum <= nums.length; checkNum++){
        if (nums[checkNum] === nums[checkNum + 1]){
            counter ++;
            if (counter >= n - 1){
                return nums[checkNum];
            }
        }else {
            counter = 0;
        }
    }
};