/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    // Sort the number from lowest to greatest
    nums = nums.sort();
    let curr = 0;
    // Check through each number
    while(curr < nums.length){
        // If it is the last number or only number, return it
        if (nums[curr] === nums.length -1){
            return nums[curr];
        // If the current number doesnt equal the previous or next number, return it
        }else if (nums[curr] !== nums[curr + 1] && nums[curr] !== nums[curr - 1]){
            return nums[curr];
        }
        curr ++;
    }
};