use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct MedianFinder {
    small: BinaryHeap<i32>,
    large: BinaryHeap<Reverse<i32>>,
}

impl MedianFinder {
    pub fn new() -> Self {
        Self {
            small: BinaryHeap::new(),
            large: BinaryHeap::new(),
        }
    }

    pub fn add_num(&mut self, num: i32) {
        self.small.push(num);

        if let Some(Reverse(smallest_large)) = self.large.peek() {
            if self.small.peek().unwrap() > smallest_large {
                let largest_small = self.small.pop().unwrap();
                self.large.push(Reverse(largest_small));
            }
        }

        if self.small.len() > self.large.len() + 1 {
            let largest_small = self.small.pop().unwrap();
            self.large.push(Reverse(largest_small));
        } else if self.large.len() > self.small.len() {
            let smallest_large = self.large.pop().unwrap().0;
            self.small.push(smallest_large);
        }
    }

    pub fn find_median(&self) -> f64 {
        if self.small.len() > self.large.len() {
            *self.small.peek().unwrap() as f64
        } else {
            (*self.small.peek().unwrap() as f64
                + self.large.peek().unwrap().0 as f64)
                / 2.0
        }
    }
}