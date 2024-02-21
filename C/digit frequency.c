#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int count[10] = {0};  
    char* num = (char*) malloc(1000 * sizeof(char)); 
    scanf("%s",num);
    num = (char*) realloc(num,strlen(num) + 1);
    for(int i = 0; i<strlen(num); i++){
        if(isdigit(*(num+i)))
            count[(int)(*(num+i))-48]++;
    }
    
    for(int i = 0;i<10;i++){
        printf("%d ",count[i]);
    }
    
    return 0;
}
