
import java.util.PriorityQueue;
import java.util.Collections;

class MedianFinder {

    PriorityQueue<Integer> small; // maxheap
    PriorityQueue<Integer> large; // minheap

    public MedianFinder() {
        small = new PriorityQueue<>(Collections.reverseOrder());
        large = new PriorityQueue<>();
    }

    public void addNum(int num) {
        small.offer(num);
        large.offer(small.poll());
        if (small.size() < large.size()) {
            small.offer(large.poll());
        }
    }

    public double findMedian() {
        if (small.size() > large.size()) {
            return small.peek();
        }

        return (small.peek() + (double) large.peek()) / 2;
    }
}
