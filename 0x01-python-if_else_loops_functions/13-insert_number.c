#include "lists.h"

/**
 * insert_node - ...
 * @head: ...
 * @number: ...
 * Return: ...
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)),
			  *prev = NULL,
			  *i = *head;
	new_node->n = number;
	new_node->next = NULL;

	while ((i != NULL) && (i->n < number))
	{
		prev = i;
		i = i->next;
	}

	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	prev->next = new_node;
	new_node->next = i;
	return (new_node);
}
