#include <stdio.h>

typedef enum {false, true} bool;

int plus(int a)
{
    int sum = 0;
    while( a > 0){
        sum += a % 10;
        a = a / 10;
    }
    return sum;
}

int Gen(int a){
    int self_num = true;
    int g;
    for (g = a -1; g > 0; g--){
        if ( a == (g+ plus(g))){
            self_num = false;
            break;
        }else {
            continue;
        }
    }
    return self_num? a : 0;
}

int main(){
    int a, b, i;
    int sum = 0;
    printf("sum : %d\n", sum);
    scanf("%d %d", &a, &b);
    for (i = a ; i <= b; i++){
        sum += Gen(i);
    }
    printf("sum : %d\n", sum);
    return 0;
}
