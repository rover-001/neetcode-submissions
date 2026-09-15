impl Solution {
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        let mut current: Vec<i32> = Vec::new();

        fn backtrack(start: i32, n: i32, k: i32, res: &mut Vec<Vec<i32>>, current: &mut Vec<i32>) {
            if current.len() == k as usize {
                res.push(current.clone());
                return;
            }

            let needed = k as usize - current.len();

            for i in start..=(n - needed as i32 + 1) {
                current.push(i);

                backtrack(i + 1, n, k, res, current);

                current.pop();
            }
        }

        backtrack(1, n, k, &mut res, &mut current);

        res
    }
}
