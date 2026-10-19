use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_maximized_capital(
        k: i32,
        w: i32,
        profits: Vec<i32>,
        capital: Vec<i32>,
    ) -> i32 {
        let mut projects: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();

        for i in 0..profits.len() {
            projects.push(Reverse((capital[i], profits[i])));
        }

        let mut available: BinaryHeap<i32> = BinaryHeap::new();
        let mut current = w;

        for _ in 0..k {
            while let Some(&Reverse((required, profit))) = projects.peek() {
                if required > current {
                    break;
                }

                projects.pop();
                available.push(profit);
            }

            if let Some(profit) = available.pop() {
                current += profit;
            } else {
                break;
            }
        }

        current
    }
}