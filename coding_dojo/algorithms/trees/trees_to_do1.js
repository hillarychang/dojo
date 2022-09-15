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


//     BST: Add
// Create an add(val) method on the BST object to add new value to the tree. This entails creating a BTNode with this value and connecting it at the appropriate place in the tree. Unless specified otherwise, BSTs can contain duplicate values.
    add(val) {
        // identify the largest value in the list

        //left side is smaller
        //right side is larger

        let new_node = new BTNode(val);
        let runner=this.root

        if(this.root != null) {

            while(runner !== null){
                if (new_node.val < runner.val){  //if val smaller than runner

                    if (runner.right != null){
                        runner = runner.right;    
                    }
                    else { //runner.right == null
                        runner.right = new_node;
                        return this;
                    }
                }

                else{  //if val larger than runner
                    if (runner.left != null){
                        runner = runner.left;    
                    }
                    else { //runner.right == null
                        runner.left = new_node;
                        return this;
                    }
                }

                }



        this.node = new_node;
        }

        }
    


    // BST: Contains
    // Create a contains(val) method on BST that returns whether the tree contains a given value. Take advantage of the BST structure to make this a much more rapid operation than SList.contains() would be.
    contains(val){

        var runner = this.root;
        while(runner !== null){
            if (new_node.val == runner.val){  //if val == runner
                return true;
            }
            else if (new_node.val < runner.val){
                if (runner.left == null){
                    return false;
                }
                runner = runner.left;    
            }
            else { //runner.right == null
                if (runner.left == null){
                    return false;
                }
                runner = runner.right;    
            }
        }
    }



    // BST: Min
    // Create a min() method on the BST class that returns the smallest value found in the BST.
    min(){ //go to most left        

        
        var runner = this.root;
        var min = this.root.val;

        while(runner.left !== null){

            if (min < runner.left.val){
                min  = runner.left.val;
            }
            runner = runner.left; 

        }
        return min;

    }



    // BST: Max
    // Create a max() BST method that returns the largest value contained in the binary search tree.
    max(){//go to most right

        var runner = this.root;
        var max = this.root.val;

        while(runner.right !== null){

            if (max > runner.right.val){
                max  = runner.right.val;
            }
            runner = runner.right; 

        }
        return max;

    }

    size() {
        if (this.root === null) {
            return 0;
        }
        function sizeHelp(runner) {
            if (!runner) {
                return 0;
            }
            return 1 + sizeHelp(runner.left) + sizeHelp(runner.right);
        }
        return sizeHelp(this.root);
    }

    

    isEmpty() {
        if(this.root != null) {
            return false
        }
        return true
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