#include "lists.h"

/**
 * check_cycle - ...
 * @list: first node in the list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list->next;
	fast = slow ? slow->next : NULL;

	while (fast != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next ? fast->next->next : NULL;
	}

	return (0);
}
