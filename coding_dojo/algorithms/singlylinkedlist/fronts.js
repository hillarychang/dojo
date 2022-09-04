// Add Front
// Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;              
    }
}

class SLL {

    constructor() {
        this.head = null;
    }


    addFront(val) {
        // Creating a new node object with the value provided
        let new_node = new Node(val);
        // Checking to see if the current list does not have a head node (if the list is empty)
        // If the list is empty, place the new node as the head 
        if(!this.head) {
            this.head = new_node;
            return this;
        }

        // If the list is not empty, assign the head to be the next node to the new node (Blue Arrow in picture above)
        new_node.next = this.head;
        // Then finally assign the new_node to be the new head of the list (Red Arrow in picture above)
        this.head = new_node;
        return this;
    }



    removeFront() {
        // If the list is empty, return the list 
        if(!this.head) {
            return this;
        }

        // If the list is not empty, assign the head to be the next node to the new node (Blue Arrow in picture above)
        this.head = this.head.next;
        // this.head.next = null;

        return this;
    }



    front() {
        if(!this.head) {
            return null;
        }

        return this.head.data;
    }




}

SLL1 = new SLL()
console.log("18",SLL1.addFront(18)) //=> Node { data: 18, next: null }
console.log("5",SLL1.addFront(5)) //=> Node { data: 5, next: Node { data: 18, next: null } }
console.log("73",SLL1.addFront(73)) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }
console.log("final",SLL1);
console.log("remove",SLL1.removeFront()) //=> Node { data: 5, next: Node { data: 18, next: null } }
console.log("remove",SLL1.removeFront()) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }
console.log("front",SLL1.front()) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }

