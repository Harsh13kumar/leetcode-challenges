class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode(0)   # Create a starting node to make building easier
        current = dummy       # current will point to the last node in our merged list

        while list1 and list2:   # Continue until one list becomes empty
            
            if list1.val <= list2.val:
                current.next = list1      # Attach list1's node
                list1 = list1.next        # Move list1 forward
            
            else:
                current.next = list2      # Attach list2's node
                list2 = list2.next        # Move list2 forward
            
            current = current.next        # Move current to the node we just added

        # One list is empty now, attach the remaining list
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next   # Skip the empty starting node

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna