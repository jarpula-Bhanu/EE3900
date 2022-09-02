#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>
#include <time.h>

complex *myfft(int n,complex *data){
	if(n==1) return data;
	complex *g = (complex *)malloc(n/2*sizeof(complex));
	complex *h = (complex *)malloc(n/2*sizeof(complex));
	for(int i=0;i<n;i++){
		if(i%2) h[i/2] = data[i];
		else g[i/2] = data[i];
	}
	g = myfft(n/2,g);
	h = myfft(n/2,h);
	for(int i=0;i<n;i++) data[i] = g[i%(n/2)] + cexp(-I*2*M_PI*i/n)*h[i%(n/2)];
	free(g);
	free(h);

	return data;
}

complex *myifft(int n,complex *data){
	if(n==1) return data;
	complex *g = (complex *)malloc(n/2*sizeof(complex));
	complex *h = (complex *)malloc(n/2*sizeof(complex));
	for(int i=0;i<n;i++){
	    if(i%2) h[i/2] = data[i];
	    else g[i/2] = data[i];
	}
	g = myifft(n/2 , g);
	h = myifft(n/2 , h);
	for(int i=0;i<n;i++){
		data[i] = g[i%(n/2)]+cexp(I*2*M_PI*i/n)*h[i%(n/2)];
		data[i] /= 2;
	}
	
	free(g);
	free(h);
	
	return data;
}

complex *convolve(complex *h,complex *x,int n){
	complex *dat = (complex *)calloc(n,sizeof(complex));
	for(int i=0;i<n;i++){
	   for(int j=0;j<=i;j++){
		dat[i] += h[j]*x[i-j];
	   }
	}

	return dat;
}
    
int main(){
    FILE *f1 = fopen("fft.txt","w");
    FILE *f2 = fopen("ifft.txt","w");
    FILE *f3 = fopen("conv.txt","w");

    for(int i=0;i<20;i++){
	srand(time(0));
	int n = 1 << i;
	complex *data = (complex *)malloc(sizeof(complex)*n);
	for(int j=0;j<n;j++) data[j] = random()/(1.0*RAND_MAX);
	clock_t fft_begin = clock();
	data = myfft(n,data);
	clock_t fft_end = clock();

	fprintf(f1,"%lf\n",1000*(double)(fft_end - fft_begin)/CLOCKS_PER_SEC);

	clock_t ifft_begin = clock();
	data = myifft(n,data);
	clock_t ifft_end = clock();

	fprintf(f2,"%lf\n",1000*(double)(ifft_end - ifft_begin)/CLOCKS_PER_SEC);

	free(data);

    }
    
    for(int i=0;i<1000;i++){
	int n=i;
	complex *h = (complex *)malloc(sizeof(complex)*n);
	complex *x = (complex *)malloc(sizeof(complex)*n);
	for(int j=0;j<n;j++) h[j] = random()/(1.0*RAND_MAX);
	for(int j=0;j<n;j++) x[j] = random()/(1.0*RAND_MAX);

	clock_t conv_begin = clock();
	complex *y = convolve(h,x,n);
	clock_t conv_end = clock();
	
	fprintf(f3,"%lf\n",1000*(double)(conv_end - conv_begin)/CLOCKS_PER_SEC);
	
	free(x),free(h);
    }

    fclose(f1);
    fclose(f2);
    fclose(f3);

    return 0;
}
