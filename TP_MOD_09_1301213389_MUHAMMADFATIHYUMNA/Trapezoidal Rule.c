#include <stdio.h>

float func(float x) {
    // Fungsi yang diintegrasikan
    return x * x;
}

float trapezoidalRule(float a, float b, int n) {
    float h = (b - a) / n;
    float result = 0.5 * (func(a) + func(b));

    for (int i = 1; i < n; ++i) {
        result += func(a + i * h);
    }

    return h * result;
}

int main() {
    float a, b;
    int n;

    printf("Enter the lower limit of integration: ");
    scanf("%f", &a);

    printf("Enter the upper limit of integration: ");
    scanf("%f", &b);

    printf("Enter the number of subintervals: ");
    scanf("%d", &n);

    float integral = trapezoidalRule(a, b, n);

    printf("The estimated integral is: %f\n", integral);

    return 0;
}
