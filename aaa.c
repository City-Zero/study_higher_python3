#include <stdio.h>  
#include<string.h>  
  
int C(int x,int y)  
{  
    int i=y;  
    int temp=0;  
    int a,b;  
    a=b=1;  
    while(i && x)  
    {  
        a*=x;  
        i--;  
        x--;  
    }  
    while(y)  
    {  
        b*=y;  
        y--;  
    }  
    temp=a/b;  
    return temp;  
}  
//C(x,y)；是一个上层为y，下层为x的排列组合，x是指填充字符串的字母可能数量,y是指字符串的长度。   
int main()  
{  
    int n,i,j,start,sum,len;  
    char a[26];  
    while(~scanf("%d",&n))  
    {  
        getchar();  
        while(n--){  
            sum=0;  
            start=1;  
            gets(a);  
            len=strlen(a);  
            for(i=1;i<len;i++)  
                sum+=C(26,i);  
            //传递参数中i为字符串长度，此时每个字符串的可选择字母为26个字母都可以。 26不做变化   
            //长度小于已知字符串长度的所有数量。  
            for(j=len;j>0;j--){  
                //控制实际求取字符串的长度   
                for(i=start;i<a[len-j]-'a'+1;i++){  
                    //控制实际求取字符串的开头字母   
                    sum+=C(26-i,j-1);  
                // 第一个参数：因为字符串为递增，  
                    //所以字符串开头之后的位置填充（字母种类）为（总字母数量26）减去（开头字母之前的字母数量）   
                //第二个参数：因为开头字母已经人为确定，  
                    //所以此时实际应求数量的字符串长度为i-1（即应该填充的字母数量）    
                }  
                start=a[len-j]-'a'+2;  
                //因为实际字符数量求取过程已经完成，所以要进行下一位求取；  
            //因字符串为递增，所以可能情况为之前字母加1；而且要小于之后字母     
            }  
            printf("%d\n",sum+1);  
        }  
    }  
    return 0;  
} 
