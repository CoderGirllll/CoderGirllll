#include <stdio.h>
int main(void){
    int n;
    do{
        printf("Enter the number of non-zeroes elements: ");
        scanf("%i", &n);
    } while ((n <= 0) && (n > 6));
    int spar[3][4];
    for (int i = 0; i < n; i++){
        int posx, posy, val;
        printf("Enter the position of %ith non-zeroes element: ", i+1);
        scanf("%i, %i", &posx, &posy);
        printf("Enter the value of the elements: ");
        scanf("%i", &val);  

        spar[posx][posy] = val;
    }    
    //Printing array
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 4; j++){
            if (spar[i][j] >= 0 && spar[i][j]<= 100)
                printf("%i ", spar[i][j]);
            else
                printf("0 ");
        }
        printf("\n");
    }
}