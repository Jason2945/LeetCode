/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    // Find the amount it takes to become majority
    let n = nums.length / 2;
    // Sort the number into order
    nums.sort();
    // Start a counter to track how many time it appears
    let counter = 0;
    // If there is only 1 int, return that int
    if (nums.length === 1){
        return nums[0];
    }
    // Run through every single number
    for (let checkNum = 0; checkNum <= nums.length; checkNum++){
        // If the next number is the same as the current number, add a counter
        if (nums[checkNum] === nums[checkNum + 1]){
            counter ++;
            // If the current counter is greater or equal to the majority, return the current number
            if (counter >= n - 1){
                return nums[checkNum];
            }
        // Reset counter and start for the next number
        }else {
            counter = 0;
        }
    }
};