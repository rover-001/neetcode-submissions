
impl Solution {
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        fn dfs(i: usize, total: i32, nums: &[i32]) -> i32 {
            if i == nums.len() {
                return total;
            } else {
                return dfs(i + 1, total ^ nums[i], nums) + dfs(i + 1, total, nums);
            }
        }

        return dfs(0, 0, &nums);
    }
}