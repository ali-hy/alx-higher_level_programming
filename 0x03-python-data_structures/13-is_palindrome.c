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
	listint_t *slow = *head, *fast = *head, *prev = NULL, *next_node;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next_node = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next_node;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
