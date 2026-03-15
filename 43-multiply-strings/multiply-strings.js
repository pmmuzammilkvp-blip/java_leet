function multiply(num1, num2) {
    if (num1 === "0" || num2 === "0") return "0";

    let m = num1.length;
    let n = num2.length;
    let result = new Array(m + n).fill(0);

    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            let mul = (num1[i] - '0') * (num2[j] - '0');
            let sum = mul + result[i + j + 1];

            result[i + j + 1] = sum % 10;
            result[i + j] += Math.floor(sum / 10);
        }
    }

    // Convert array to string
    let res = result.join('');

    // Remove leading zeros
    while (res[0] === '0') {
        res = res.substring(1);
    }

    return res;
}
