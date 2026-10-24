# Fix My Code Challenge

## 4. Double Linked List

### Description

This task focuses on debugging a C implementation of a doubly linked list. The main issue was in the `delete_dnodeint_at_index` function, which removes a node at a specified index.

### Implementation

The function `delete_dnodeint_at_index` handles the following cases:

* Deleting the first node and updating the head pointer.
* Deleting a node from the middle of the list.
* Deleting the last node.
* Returning `-1` when the list is empty or the index is invalid.
* Freeing the memory allocated to the deleted node.

### Files

* `lists.h`: Defines the doubly linked list structure and function prototypes.
* `main.c`: Contains tests for the deletion function.
* `add_dnodeint_end.c`: Adds a node to the end of the list.
* `print_dlistint.c`: Prints the list.
* `free_dlistint.c`: Frees the list.
* `delete_dnodeint_at_index.c`: Deletes a node at a specified index.

### Compilation

Compile the program using:

```bash
gcc -Wall -pedantic -Werror -Wextra -std=gnu89 main.c free_dlistint.c print_dlistint.c add_dnodeint_end.c delete_dnodeint_at_index.c -o delete_dnodeint
```

### Run

Execute the program:

```bash
./delete_dnodeint
```

### Testing

The program was tested for:

* Deleting a node from the middle.
* Deleting the head node.
* Deleting the last node.
* Attempting to delete a node at an invalid index.

All tested cases produced the expected results.

