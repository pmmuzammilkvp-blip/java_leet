var combinationSum2 = function(candidates, target) {

    candidates.sort((a, b) => a - b);

    let result = [];

    function backtrack(start, path, remaining) {

        if (remaining === 0) {
            result.push([...path]);
            return;
        }

        if (remaining < 0) return;

        for (let i = start; i < candidates.length; i++) {

            // skip duplicates
            if (i > start && candidates[i] === candidates[i - 1]) continue;

            path.push(candidates[i]);

            backtrack(i + 1, path, remaining - candidates[i]);

            path.pop(); // backtrack
        }
    }

    backtrack(0, [], target);

    return result;
};
