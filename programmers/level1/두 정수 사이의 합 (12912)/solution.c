#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    int min, max;
    long long answer = 0;
    if (a == b) {
        answer = a;
        return answer;
    }
    else if (a > b) {
        max = a;
        min = b;
    }
    else {
        max = b;
        min = a;
    }
    for (int i = min; i <= max; i++) {
        answer += i;
    }
    return answer;
}