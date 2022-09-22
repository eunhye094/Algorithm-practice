#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

struct _STACK {
	char array[100001];
	int top;
} stack;

int main()
{
	int n;
	int count = 0;

	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		if (func() == 2)
			count++;
	}
	printf("%d", count);
}

int func()
{
	char* words=(char*)malloc(sizeof(char*)*100001);
	
	for (int i = 0; i < 100001; i++)
		words[i] = NULL;
	for (int i = 0; i < 100001; i++)
		stack.array[i] = NULL;
	stack.top = 0;

	scanf("%s", words);

	int idx = 0;
	
	while (words[idx] != NULL)
	{
		if (stack.array[stack.top] == words[idx])
			stack.array[stack.top--] = NULL;
		else
			stack.array[++stack.top] = words[idx];
		idx++;
	}
	if (stack.top == 0)
		return 2;

	free(words);
}