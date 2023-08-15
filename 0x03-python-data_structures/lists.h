#ifndef LIST_H
#define LIST_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head);
int compare_lists(listint_t **head1, listint_t **head2);
listint_t *reverse_list(listint_t **slow, listint_t *prev_slow);
void restore_list(listint_t *second_half,
		listint_t *slow, listint_t *prev_slow);

#endif /* LIST_H */
