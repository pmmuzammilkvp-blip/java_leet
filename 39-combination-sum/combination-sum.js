var combinationSum = function(candidates, target) {

    let result = [];

    function backtrack(start, current, remaining) {

        if (remaining === 0) {
            result.push([...current]);
            return;
        }

        if (remaining < 0) return;

        for (let i = start; i < candidates.length; i++) {

            current.push(candidates[i]);

            backtrack(i, current, remaining - candidates[i]); // reuse same number

            current.pop(); // backtrack
        }
    }

    backtrack(0, [], target);

    return result;
};
