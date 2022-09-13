#include <stdio.h>

int main(){
    float x[6]={1.0,2.0,3.0,4.0,2.0,1.0},y[20];
    int k=20;

    FILE* fp;
    fp = fopen("3.3.dat","w");


    y[0] = x[0];
    y[1] = -0.5*y[0]+x[1];

    for(int n=2;n<k-1;n++){
        if(n<6) y[n] = -0.5*y[n-1]+x[n]+x[n-2];
        else if(n > 5 && n < 8) y[n] = -0.5*y[n-1]+x[n-2];
        else y[n] = -0.5*y[n-1];
    }

    for(int i=0;i<20;i++){
        printf("%f\n",y[i]);
        fprintf(fp,"%f\n",y[i]);
    }

    fclose(fp);

    return 0;
    
}