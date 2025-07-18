// program to create a simple calculator

#include <stdio.h>

int main(){
	char operation;
	double n1, n2;
	
	printf("Enter an operator (+, -, *, /): ");
	scanf(" %c", &operation);
	printf("Enter two operations: ");
	scanf(" %lf %lf",&n1, &n2);
	
	switch(operation){
		case '+':
			printf(" %.1lf + %.1lf = %.1lf", n1, n2, n1+n2);
			break;
		case '-':
			printf(" %.1lf - %.1lf = %.1lf", n1, n2, n1-n2);
			break;
		case '*':
			printf(" %.1lf * %.1lf = %.1lf", n1, n2, n1*n2);
			break;
		case '/':
			printf(" %.1lf / %.1lf = %.1lf", n1, n2, n1/n2);
			break;
		// operator doesnt match any case constant +, -, *, /
		default:
			printf("Error! operator is not correct");
	}
	
	return 0;
}

