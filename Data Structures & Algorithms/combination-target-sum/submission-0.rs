impl Solution {
    pub fn combination_sum(mut candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        candidates.sort();

        let mut result = Vec::new();
        let mut current = Vec::new();

        fn dfs(
            candidates: &Vec<i32>,
            start: usize,
            target: i32,
            current: &mut Vec<i32>,
            result: &mut Vec<Vec<i32>>,
        ) {
            if target == 0 {
                result.push(current.clone());
                return;
            }

            for i in start..candidates.len() {
                let num = candidates[i];

                if num > target {
                    break;
                }

                // Choose
                current.push(num);

                // `i`, not `i + 1`, because numbers can be reused
                dfs(candidates, i, target - num, current, result);

                // Undo choice
                current.pop();
            }
        }

        dfs(
            &candidates,
            0,
            target,
            &mut current,
            &mut result,
        );

        result
    }
}