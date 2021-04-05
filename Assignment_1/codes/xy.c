#include <stdio.h>

float largest(float arr[], int n)
{
   
    float max = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > max)
            max = arr[i];
 
    return max;
}


int main() {   
    
	int k = 30;
	float x[6] = {1.0,2.0,1.0,4.0,3.0,3.0};
	float y[30] = {0};
	float x1[30];
	for(int j = 0; j < 30; j++){
		if(j<6){
			x1[j] = x[j];
		}
		else{
			x1[j] = 0;
		}
	}
	

	y[0] = x1[0];
	y[1] = -0.5*y[0]+x1[1];
	for(int i=2;i<k-1;i++){
		y[i] = -0.5*y[i-1]+x1[i]+x1[i-2];
	}
	

	printf("Upper bound of x(n) is %f\n", largest(x1,30));
	printf("Upper bound of y(n) is %f", largest(y,30));
	

    return 0;
}




