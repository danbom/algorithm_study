#include <stdio.h>

int main(){
    int A,B,C,sold;

    scanf("%d %d %d", &A, &B, &C);
    if (B >= C)
    {
        printf("-1");
        return 0;
    }
    sold = A/(C-B)+1;

    if (sold<=0) printf("-1");
    else printf("%d",sold);
}
