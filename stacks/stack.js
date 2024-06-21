class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items.push(item);
  }

  pop() {
    if(this.isEmpty()) {
      return 'Stack is empty';
    } 

    return this.items.pop()
  }

  peek() {
    if(this.isEmpty()) {
      return "Stack is empty"
    }

    return this.items[this.items.length - 1];
  }

  clear() {
    this.items = [];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }

  print() {
    console.log(this.items.join(''))
  }
}

const firstStack = new Stack();
firstStack.push(1)
firstStack.push(2);
firstStack.push(10);
console.log(firstStack.size())