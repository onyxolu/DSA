# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):

    # Write your code here.
    newLinkedList = LinkedList(0)
	new = newLinkedList
    carry = 0
    curr1 = linkedListOne
    curr2 = linkedListTwo
    
	while curr1 or curr2 or carry:
		sum = carry
		if curr1:
			sum += curr1.value
			curr1 = curr1.next
		if curr2:
			sum += curr2.value
			curr2 = curr2.next
		carry = sum//10
		if sum > 9:
			sum = sum%10
		
		new.next = LinkedList(sum)
		new = new.next
	return newLinkedList.next