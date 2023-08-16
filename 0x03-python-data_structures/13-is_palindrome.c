#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev_slow = NULL;
	listint_t *second_half, *midnode = NULL;
	int is_palindrome = 1; /* Assume it's a palindrome */

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome); /* Empty list or single element list */

	/* Use fast and slow pointers to find the middle of the list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	is_palindrome = compare_lists(head, &slow);

	second_half = reverse_list(&slow, prev_slow);

	restore_list(second_half, slow, prev_slow);

	return (is_palindrome);
}

/**
 * compare_lists - Compares two linked lists.
 * @head1: Double pointer to the first linked list.
 * @head2: Double pointer to the second linked list.
 * Return: 0 if not equal, 1 if equal.
 */
int compare_lists(listint_t **head1, listint_t **head2)
{
	listint_t *temp1 = *head1, *temp2 = *head2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n != temp2->n)
			return (0);
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	return (1);
}

/**
 * reverse_list - Reverses the second half of a linked list.
 * @slow: Double pointer to the second half of the linked list.
 * @prev_slow: Pointer to the node before the second half.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t **slow, listint_t *prev_slow)
{
	listint_t *second_half = *slow, *midnode = NULL;

	prev_slow->next = NULL; /* Terminate the first half */
	while (second_half != NULL)
	{
		listint_t *next_node = second_half->next;

		second_half->next = midnode;
		midnode = second_half;
		second_half = next_node;
	}

	return (midnode);
}

/**
 * restore_list - Restores the original linked list.
 * @second_half: Pointer to the reversed second half of the linked list.
 * @slow: Pointer to the end of the first half.
 * @prev_slow: Pointer to the node before the second half.
 */
void restore_list(listint_t *second_half, listint_t *slow,
		listint_t *prev_slow)
{
	while (second_half != NULL)
	{
		listint_t *next_node = second_half->next;

		second_half->next = slow;
		slow = second_half;
		second_half = next_node;
	}
	prev_slow->next = slow; /* Restore the first half */
}
