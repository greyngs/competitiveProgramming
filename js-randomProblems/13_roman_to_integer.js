var romanToInt = function(s) {
    table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000, 
    }

    sol = 0
    for (let i = 0; i < s.length; i++) {
        if (i < s.length - 1 && table[s[i]] < table[s[i + 1]]) {
            sol -= table[s[i]] 
        } else {
            sol += table[s[i]] 
        }
    }
    return sol;
};

