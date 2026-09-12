
impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        let mut subset = Vec::new();

        fn dfs(i: usize, nums: &Vec<i32>, subset: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
            if i == nums.len() {
                res.push(subset.clone());
                return;
            }

            subset.push(nums[i]);
            dfs(i + 1, nums, subset, res);

            subset.pop();
            dfs(i + 1, nums, subset, res);
        }

        dfs(0, &nums, &mut subset, &mut res);

        res
    }
}
