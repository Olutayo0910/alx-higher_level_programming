#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *h = list;
	listint_t *t = list;

	while (h && t && h->next)
	{
		t = t->next;
		h = h->next->next;

		if (h == t)
			return (1);
	}

	return (0);
}
