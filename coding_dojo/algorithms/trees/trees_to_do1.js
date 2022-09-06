class BTNode {
    constructor(value) {
        this.val = value;
        this.left = null;
        this.right = null;
        }
    }


class BST {
    constructor() {
    this.root = null;
    }


    9
    [6, 8,10,12 ]

//     BST: Add
// Create an add(val) method on the BST object to add new value to the tree. This entails creating a BTNode with this value and connecting it at the appropriate place in the tree. Unless specified otherwise, BSTs can contain duplicate values.
    add(val) {
        // identify the largest value in the list

        //left side is smaller
        //right side is larger

        let new_node = new BTNode(val);
        let runner=this.root

        if(!this.root) {
            this.root = new_node;
            return this;
        }


        while(runner !== null){
        if (new_node.val < runner.val){  //if larger than runner
            new_node.left = runner;
            runner.right = new_node;
            runner = new_node;
        }

        runner=runner.next

        }

    }


    // BST: Contains
    // Create a contains(val) method on BST that returns whether the tree contains a given value. Take advantage of the BST structure to make this a much more rapid operation than SList.contains() would be.
    contains(val){
        


    }



    // BST: Min
    // Create a min() method on the BST class that returns the smallest value found in the BST.
    min(){
        


    }



    // BST: Max
    // Create a max() BST method that returns the largest value contained in the binary search tree.
    max(){
        



    }





}


BST1 = new BST()
console.log("18",BST1.add(18)) //=> Node { data: 18, next: null }
console.log("18",BST1.add(18)) //=> Node { data: 18, next: null }
console.log("5",BST1.add(5)) //=> Node { data: 5, next: Node { data: 18, next: null } }
console.log("73",BST1.add(73)) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }
console.log("find",BST1.contains(73)) //=> Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }













// BST: Size
// Write a size() method that returns the number of nodes (values) contained in the tree.



// BST: Is Empty
// Create an isEmpty() method to return whether the BST is empty (whether it contains no values).