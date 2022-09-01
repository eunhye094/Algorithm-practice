#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

struct _STACK {
	int array[100001];
	int top;
} stack;

int main(void)
{
	char command[5] = "";
	int  command_count = 0;
	int  value = 0;
	stack.top = 0;

	scanf("%d", &command_count);
	fgetc(stdin);

	for (int idx = 0; idx < command_count; ++idx)
	{
		scanf("%s", command);
		fgetc(stdin);

		if (!strcmp(command, "push"))
		{
			scanf("%d", &value);
			stack.top = stack.top + 1;
			stack.array[stack.top] = value;
		}
		else if (!strcmp(command, "pop"))
		{
			if (stack.top == 0)
				printf("%d\n", -1);
			else
			{
				printf("%d\n", stack.array[stack.top]);
				stack.array[stack.top] == 0;
				stack.top = stack.top - 1;
			}
		}
		else if (!strcmp(command, "size"))
		{
			printf("%d\n", stack.top);
		}
		else if (!strcmp(command, "empty"))
		{
			if (stack.top == 0)
				printf("%d\n", 1);
			else
				printf("%d\n", 0);
		}
		else if (!strcmp(command, "top"))
		{
			if (stack.top == 0)
				printf("%d\n", -1);
			else
				printf("%d\n", stack.array[stack.top]);
		}
	}
	return 0;
}