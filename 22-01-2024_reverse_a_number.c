/*
Given a number N reverse the number and print it.

Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

Input Format

123

Constraints

N <= 1000

Output Format

321

Sample Input 0

123
Sample Output 0

321
Sample Input 1

2341
Sample Output 1

1432
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int q,e,m=0,f[100000];
    scanf("%d",&q);
    while(q>0){
        e=q%10;
        f[m++]=e;
        q/=10;
    }
    for(int i=0;i<m;i++){
        printf("%d",f[i]);
    }
}