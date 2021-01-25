#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
    return strcmp((char *)a, (char *)b);
}

int main(void)
{
    char str[200][100];
    int n;
    while (scanf("%d", &n) != EOF)
    {
        for (int i = 0; i < n; i++)
        {
            scanf("%s", str[i]);
        }
        qsort(str, n, sizeof(str[0]), cmp);
        for (int k = 0; k < n; k++)
        {
            printf("%s\n", str[k]);
        }
    }
    return 0;
}