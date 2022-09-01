#include <stdio.h>

int main() {
	int a;
	int x = 0;
	scanf("%d", &a);
	for (int i = 1; i <= a; i++) {
		x += i;
	}
	printf("%d", x);
	return 0;
}