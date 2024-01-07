#include "lists.h"

/**
 * add_nodeint_start - add element to start of a list
 * @head: ptr to head of list
 * @val: value to hold in pointer
 * Return: new head of list
 */
listint_t *add_nodeint_start(listint_t **head, int val)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (*head);

	new_node->n = val;
	new_node->next = *head;

	*head = new_node;
	return (*head);
}

/**
 * cmp_lists - compare two linked lists
 * @head1: head of first list
 * @head2: head of second list
 * Return: 0 if equal, list1 - list2 at node where things are different
 */
int cmp_lists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
			return (head1 - head2);
		head1 = head1->next;
		head2 = head2->next;
	}

	if (head1 == NULL && head2 == NULL)
		return (0);
	if (head2 == NULL)
		return (head1->n);
	return (-head2->n);
}

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head, *inverse = NULL;
	int size = 0, i = 0, odd = 0, mid = 0;

	while (curr != NULL)
	{
		size++;
		curr = curr->next;
	}

	curr = *head;
	odd = size % 2;
	mid = size / 2;
	while (i < mid)
	{
		add_nodeint_start(&inverse, curr->n);
		curr = curr->next;
		i++;
	}

	if (odd && curr)
		curr = curr->next;

	if (cmp_lists(curr, inverse) == 0)
	{
		free_listint(inverse);
		return (1);
	}

	free_listint(inverse);
	return (0);
}
