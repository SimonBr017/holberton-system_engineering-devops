#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - loop infinite
 * Return: returns zero
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - 5 zombie process
 * Return: infitie loop
 */

int main(void)
{
	__pid_t zombie;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (0);
}
