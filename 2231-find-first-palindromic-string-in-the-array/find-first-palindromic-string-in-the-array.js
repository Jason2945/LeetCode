/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    // Create a counter
    let counter = 0;
    // Make a while loop that goes through the length of the amount of words in the array
    while (counter <= words.length - 1){
        // Create a variable that holds the word backwords
        let reverseWord = [];
        words[counter].split("").map(word => reverseWord.unshift(word));
        // If the reverse word is a palindrome, return the word. If not increment counter and check next word.
        if (reverseWord.join("") === words[counter]){
            return words[counter];
        } else {
            counter ++;
        }
    }
    // If there are no matches at all, return blank string.
    return "";
};