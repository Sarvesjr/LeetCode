/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        dummy.next = head;

        ListNode cur = head;

        while (cur != null && cur.next != null) {
            if (cur.next.val >= cur.val) {
                cur = cur.next;
            } else {
                ListNode tmp = cur.next;
                cur.next = tmp.next;

                ListNode pre = dummy;

                while (pre.next.val < tmp.val) {
                    pre = pre.next;
                }

                tmp.next = pre.next;
                pre.next = tmp;
            }
        }

        return dummy.next;
    }
}