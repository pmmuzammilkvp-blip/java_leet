var nextPermutation = function(nums) {

    let n = nums.length;
    let i = n - 2;

    // Step 1: find first decreasing element
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }

    // Step 2: swap with next larger element
    if (i >= 0) {
        let j = n - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        [nums[i], nums[j]] = [nums[j], nums[i]];
    }

    // Step 3: reverse the rest
    let left = i + 1;
    let right = n - 1;

    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]];
        left++;
        right--;
    }
};
