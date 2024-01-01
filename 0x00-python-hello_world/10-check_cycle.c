#include "lists.h"

/**
 * check_cycle - ...
 * @list: first node in the list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr;

	if (list == NULL)
		return (0);

	curr = list->next;

	while (curr != NULL)
	{
		if (curr == list)
			return (1);
		curr = curr->next;
	}

	return (0);
}
