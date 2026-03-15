function myPow(x, n) {
    if (n === 0) return 1;

    let N = n;
    if (n < 0) {
        x = 1 / x;
        N = -n;
    }

    let result = 1;
    while (N > 0) {
        if (N % 2 === 1) {
            result *= x;
        }
        x *= x;
        N = Math.floor(N / 2);
    }

    return result;
}
