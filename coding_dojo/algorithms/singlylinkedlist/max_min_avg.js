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



    max() {
        // identify the largest value in the list
        
        let runner = this.head;

        if (runner == null){
            return;
        }


        let current = runner.data;
        runner=runner.next;

        while (runner !== null){
            
            if (runner.data > current ){
                current = runner.data;
            }
            runner=runner.next;

        }


        return (current);

    }


    
    
    min() {
            // identify the smallest value in the list

            let runner = this.head;

            if (runner == null){
                return;
            }


            let current = runner.data;
            runner=runner.next;

            while (runner !== null){
                
                if (runner.data < current ){
                    current = runner.data;
                }
                runner=runner.next;
    
            }
    
    
            return (current);

        }

    
    average() {
            // what is the average value in my list?
        // how many nodes are in my list?
        let runner = this.head
        let sum = 0;
        let num = 0;
        let value=0;
        
        while (runner !== null){
            
            value=runner.data;
            sum+=value;
            num++;
            runner=runner.next;

        }


        return (sum/num);
            
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



}

SLL1 = new LinkedList()
console.log("18",SLL1.addFront(18)) //=> Node { data: 18, next: null }
console.log("18",SLL1.addFront(18)) //=> Node { data: 18, next: null }
console.log("5",SLL1.addFront(5)) //=> Node { data: 5, next: Node { data: 18, next: null } }
console.log("73",SLL1.addFront(73)) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }
console.log("avg",SLL1.average()) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }
console.log("min",SLL1.min()) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }
console.log("max",SLL1.max()) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }
