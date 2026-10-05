/*
* Check if nodes after dummy (prev.next) exists and nodes after dummy less than current node
* If true we change prev node till we find a node bigger than currentstore a pointer to current node's next node
* We assign current node's next node pointer to prev.next (so it's behind prev.next as it is smaller than it)
* We then add current node to end of prev node pointer
* Finally we let cur = nextNode
* Return head, which is node after dummy node
*/
    


public class insertionSortList {
    public static ListNode insertionSort(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode(0);
        ListNode cur = head;
        while (cur != null){
            ListNode prev = dummy;
            while (prev.next != null && prev.next.val < cur.val){
                prev = prev.next;
            }
            ListNode nextNode = cur.next;
            cur.next = prev.next;
            prev.next = cur;
            cur = nextNode;
        }
        return dummy.next;
    }


    // Implementation: e.g. 4 -> 2 -> 1 -> 3
    public static void main(String[] args){
        ListNode node2 = new ListNode(3);
        ListNode node3 = new ListNode(1, node2);
        ListNode node = new ListNode(2, node3);
        ListNode head = new ListNode(4, node);
        System.out.println("Before: ");
        ListNode cur = head;
        while (cur != null) {
            System.out.print(cur.val + " -> ");
            cur = cur.next;
        }
        System.out.println("null");

        System.out.println("After: ");
        ListNode sorted = insertionSort(head);
        while (sorted != null) {
            System.out.print(sorted.val + " -> ");
            sorted = sorted.next;
        }
        System.out.print("null");

    }
}
