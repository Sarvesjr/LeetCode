/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null) {
            return null;
        }
        if (left == right) {
            return head;
        }
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        ListNode curr = head;
        int count = 1;
        while (curr != null) {
            if (count >= left && count <= right) {
                stack.push(curr.val);
            }
            curr = curr.next;
            count++;
        }
        curr = head;
        count = 1;
        while (curr != null && !stack.isEmpty()) {
            if (count >= left && count <= right) {
                curr.val = stack.pop();
            }
            curr = curr.next;
            count++;
        }
        return head;
    }
}