#include <stdio.h>
#include "lists.h"

int main(void)
{
    dlistint_t *head = NULL;
    unsigned int i;

    for (i = 0; i < 5; i++)
        add_dnodeint_end(&head, i);

    printf("Original list:\n");
    print_dlistint(head);

    printf("\nDeleting node at index 2:\n");
    if (delete_dnodeint_at_index(&head, 2) == 1)
        print_dlistint(head);

    printf("\nDeleting head node:\n");
    if (delete_dnodeint_at_index(&head, 0) == 1)
        print_dlistint(head);

    printf("\nDeleting last node:\n");
    if (delete_dnodeint_at_index(&head, 2) == 1)
        print_dlistint(head);

    printf("\nTrying invalid index:\n");
    printf("Return: %d\n", delete_dnodeint_at_index(&head, 10));

    free_dlistint(head);

    return (0);
}

