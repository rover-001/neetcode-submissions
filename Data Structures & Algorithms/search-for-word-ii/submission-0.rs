use std::collections::HashMap;

#[derive(Default)]
struct TrieNode {
    children: HashMap<char, TrieNode>,
    word: Option<String>,
}

impl TrieNode {
    fn insert(&mut self, word: String) {
        let mut node = self;

        for ch in word.chars() {
            node = node.children.entry(ch).or_default();
        }

        node.word = Some(word);
    }
}

impl Solution {
    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let mut root = TrieNode::default();

        for word in words {
            root.insert(word);
        }

        let mut board = board;
        let mut result = Vec::new();

        let rows = board.len();
        let cols = board[0].len();

        for r in 0..rows {
            for c in 0..cols {
                Self::dfs(
                    &mut board,
                    r,
                    c,
                    &mut root,
                    &mut result,
                );
            }
        }

        result
    }

    fn dfs(
        board: &mut Vec<Vec<char>>,
        r: usize,
        c: usize,
        node: &mut TrieNode,
        result: &mut Vec<String>,
    ) {
        let ch = board[r][c];

        let Some(next) = node.children.get_mut(&ch) else {
            return;
        };

        if let Some(word) = next.word.take() {
            result.push(word);
        }

        board[r][c] = '#';

        let rows = board.len();
        let cols = board[0].len();

        if r + 1 < rows && board[r + 1][c] != '#' {
            Self::dfs(board, r + 1, c, next, result);
        }

        if r > 0 && board[r - 1][c] != '#' {
            Self::dfs(board, r - 1, c, next, result);
        }

        if c + 1 < cols && board[r][c + 1] != '#' {
            Self::dfs(board, r, c + 1, next, result);
        }

        if c > 0 && board[r][c - 1] != '#' {
            Self::dfs(board, r, c - 1, next, result);
        }

        board[r][c] = ch;
    }
}