#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
    int a = 0;
    int o = 0;
    int x = 0;
    for(int i = 1; i<=n-1; i++){
        for(int j = i+1; j<=n; j++){
            if((i&j)<k && (i&j)>a)
                a = i&j;
            if((i|j)<k && (i|j)>o)
                o = i|j;
            if((i^j)<k && (i^j)>x)
                x = i^j;
        }
    }
    printf("%d \n", a);
    printf("%d \n", o);
    printf("%d \n", x);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
