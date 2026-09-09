impl Solution {
        pub fn min_extra_char(s: String, dictionary: Vec<String>) -> i32 {
        let words: HashSet<String> = dictionary.into_iter().collect();

        fn dfs(i: usize, s: &String, words: &HashSet<String>) -> i32 {
            if i == s.len() {
                return 0;
            }

            let mut res = 1 + dfs(i + 1, s, words);

            for j in i + 1..=s.len() {
                let sub = &s[i..j];

                if words.contains(sub) {
                    res = res.min(dfs(j, s, words));
                }
            }

            res
        }

        dfs(0, &s, &words)
    }      
}
