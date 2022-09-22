#include <stdio.h>

int main() {
	int x, y, a, b, c;
	scanf("%d %d", &x, &y);
	a = y / 100;
	b = (y % 100) / 10;
	c = (y % 100) % 10;
	printf("%d\n%d\n%d\n%d", x * c, x * b, x * a, x * y);
	return 0;
}