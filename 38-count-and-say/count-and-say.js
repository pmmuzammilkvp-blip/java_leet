var countAndSay = function(n) {

    let result = "1";

    for (let i = 2; i <= n; i++) {

        let current = "";
        let count = 1;

        for (let j = 1; j <= result.length; j++) {

            if (result[j] === result[j - 1]) {
                count++;
            } else {
                current += count + result[j - 1];
                count = 1;
            }
        }

        result = current;
    }

    return result;
};
