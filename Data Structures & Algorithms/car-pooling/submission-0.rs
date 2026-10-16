use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn car_pooling(trips: Vec<Vec<i32>>, capacity: i32) -> bool {
        let mut trips = trips;
        trips.sort_unstable_by_key(|trip| trip[1]);

        let mut heap = BinaryHeap::new();
        let mut passengers = 0;

        for trip in trips {
            let num = trip[0];
            let from = trip[1];
            let to = trip[2];

            while let Some(Reverse((drop_off, count))) = heap.peek().copied() {
                if drop_off > from {
                    break;
                }

                heap.pop();
                passengers -= count;
            }

            passengers += num;

            if passengers > capacity {
                return false;
            }

            heap.push(Reverse((to, num)));
        }

        true
    }
}