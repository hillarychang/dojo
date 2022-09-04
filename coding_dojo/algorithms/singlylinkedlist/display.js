class Node {
    constructor(data) {
        this.data = data;
        this.next = null;              
    }
}


class LinkedList {
    constructor() {
        this.head = null;
    } 



    display() {
            // neatly display nodes in my list
            let runner = this.head;
            let arr = [];

            while (runner !== null){
                arr.push(runner.data);
                runner=runner.next;
            }

            return arr;
        }

    length() {
            // how many nodes are in my list?
            let runner = this.head
            let count = 0;
            
            while (runner !== null){
                
                count++
                runner=runner.next

            }


            return count;
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


    
    contains(num) {
        //We first have to tell our train attendant that we want them to start at the front of the train
        let runner=this.head
        let value=0
            //Since a Linked List does not know how many nodes is within it, we will not be able to use a for loop to             iterate, instead we'll use a while
            //Also we need to tell them when to stop otherwise they will just run off the end of the train
        while(runner !== null){
            //Since the runner is set to the current node, its value will be equal to the value of the node they                 are currently on
            value=runner.data
            //Tell our attendant to move to the next car
            if (value == num){
                return true;
            }
            runner=runner.next
        }
            return false;
    }



}

SLL1 = new LinkedList()
console.log("18",SLL1.addFront(18)) //=> Node { data: 18, next: null }
console.log("18",SLL1.addFront(18)) //=> Node { data: 18, next: null }
console.log("5",SLL1.addFront(5)) //=> Node { data: 5, next: Node { data: 18, next: null } }
console.log("73",SLL1.addFront(73)) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }
console.log("find",SLL1.display()) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }
