var isPalindrome = function(x) {
    if (x < 0) return false;
    const str = x.toString();

    let left = 0;
    let right = str.length - 1;

    while (left < right) {
        if (str[left] !== str[right]) {
        return false;
        }
        left++;
        right--;
    }

    return true;
};

