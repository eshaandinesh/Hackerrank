#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;
void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    float p;
    float area[n];
    for(int i = 0; i < n; i++){
        p = (tr[i].a+tr[i].b+tr[i].c)/2.0;
        area[i] = sqrtf(p * (p - tr[i].a) * (p - tr[i].b) * (p - tr[i].c));
        //printf("%f ",area[i]);
    }
    float temp;
    for(int i = 0; i < n; i++){
        for(int j = i;j < n; j++){
            if(area[j]<area[i]){
                temp = area[j];
                area[j] = area[i];
                area[i] = temp;
                
                temp = tr[i].b;
                tr[i].b = tr[j].b;
                tr[j].b = temp;
                
                temp = tr[i].a;
                tr[i].a = tr[j].a;
                tr[j].a = temp;
                
                temp = tr[i].c;
                tr[i].c = tr[j].c;
                tr[j].c = temp;
            }    
        }
    }
    
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
