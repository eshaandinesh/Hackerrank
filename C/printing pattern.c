#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    for(int i=0;i<2*n-1;i++){
        for(int j = 0;j<2*n-1;j++){
            for(int k = 0;k<n;k++){
                if(i==k || j==k || i==2*n-2-k || j==2*n-2-k){
                    printf("%d ",n-k);
                    break;
                }
            }
        }
        printf("\n");
    }
    return 0;
}
