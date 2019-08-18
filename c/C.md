# C
## GNU编译器
MinGW  
CYGWin  
linux默认有GCC  
> GCC 是由 GNU 组织开发的，最初只支持C语言，是一个单纯的C语言编译器， 后来 GNU 组织倾注了更多的精力，使得 GCC 越发强大，增加了对 C++、Objective-C、Fortran、Java 等其他语言的支持，  GCC 就成了一个编译器套件（套装），是所有编译器的总称

## IDE
VS
CLION

## 输入与输出
输入
> scanf()
> ```
> scanf("%f",&f);
> ```
> getchar()
> ```
> c = getchar( );
> ```
> gets()
> ```
> char a[10];     
> gets(a);     
> puts(a);
> ```

输出
> printf()
> ```
> printf("Value = %f", f);
> ```
> putchar( c );  
> puts() 

## 变量、常量
变量的定义
> 类型 变量名 = 值;  
> 变量的声明  
> 变量的初始化  
> 变量是可以重新赋值的  

常量
> 整数常量  
> 浮点常量  
> 布尔常量  
> 字符常量  
> 常量的值不可以重新赋值  
> 定义方式  
> ```
>   #define NUM 100
>   const int age=30;
> ```

数据类型
整数类型
> char 1 字节 -128 到 127 或 0 到 255  
> unsigned char 1 字节 0 到 255  
> signed char 1 字节 -128 到 127  
> int 2 或 4 字节 -32,768 到 32,767 或 -2,147,483,648 到 2,147,483,647  
> unsigned int 2 或 4 字节 0 到 65,535 或 0 到 4,294,967,295  
> short 2 字节 -32,768 到 32,767  
> unsigned short 2 字节 0 到 65,535  
> long 4 字节 -2,147,483,648 到 2,147,483,647  
> unsigned long 4 字节 0 到 4,294,967,295  

实型类型
> float 4 字节 1.2E-38 到 3.4E+38 6 位小数  
> double 8 字节 2.3E-308 到 1.7E+308 15 位小数  
> long double 16 字节 3.4E-4932 到 1.1E+4932 19 位小数  
> *在实型类型 进行运算的时候 会有精度丢失的问题*  
> *重要的数据 不可使用 实型类型（比如 钱 虚拟货币...）*

字符类型
> char 1 字节 -128 到 127 或 0 到 255  
> 单引号表示的字母 -> 字符  
> 大小写转变  
> > 小写->大写 -32  
> > 大写到小写 +32  

自定义类型
```
typedef int myInt;
```
格式化字符串(占位符)
> %d:int short char  
> %ld:long  
> %f:float double  
> > %.几f 精确到几位

> %Lf:long double  
> %c:char  
> %s:字符串  

## 运算符
(A = 10,B = 20)
算术运算符
> \+ 把两个操作数相加 A + B 将得到 30  
> \- 从第一个操作数中减去第二个操作数 A - B 将得到 -10  
> \* 把两个操作数相乘 A * B 将得到 200  
> / 分子除以分母 B / A 将得到 2  
> % 取模运算符，整除后的余数 B % A 将得到 0  
> ++ 自增运算符，整数值增加 1 A++ 将得到 11 自加减在前 先自加减 再赋值  
> -- 自减运算符，整数值减少 1 A-- 将得到 9  
  
关系运算符  
> == 检查两个操作数的值是否相等，如果相等则条件为真。 (A == B) 不为真。  
> != 检查两个操作数的值是否相等，如果不相等则条件为真。 (A != B) 为真。  
> \> 检查左操作数的值是否大于右操作数的值，如果是则条件为真。 (A > B) 不为真。  
> < 检查左操作数的值是否小于右操作数的值，如果是则条件为真。 (A < B) 为真。  
> \>= 检查左操作数的值是否大于或等于右操作数的值，如果是则条件为真。 (A >= B) 不为真。  
> <= 检查左操作数的值是否小于或等于右操作数的值，如果是则条件为真。 (A <= B) 为真。  
  
逻辑运算符  
> && 称为逻辑与运算符。如果两个操作数都非零，则条件为真。 (A && B) 为假。  
> || 称为逻辑或运算符。如果两个操作数中有任意一个非零，则条件为真。 (A || B) 为真。  
> ! 称为逻辑非运算符。用来逆转操作数的逻辑状态。如果条件为真则逻辑非运算符将使其为假。 !(A && B) 为真。  

## 分支结构
if 语句 
>一个 if 语句 由一个布尔表达式后跟一个或多个语句组成。

if...else 语句 
>一个 if 语句 后可跟一个可选的 else 语句，else 语句在布尔表达式为假时执行。

嵌套 if 语句 
> 可以在一个 if 或 else if 语句内使用另一个 if 或 else if 语句。

switch 语句 
>一个 switch 语句允许测试一个变量等于多个值时的情况。

嵌套 switch 语句 
>可以在一个 switch 语句内使用另一个 switch 语句。

? : 运算符(三元运算符)

## 循环
while 循环 
>当给定条件为真时，重复语句或语句组。它会在执行循环主体之前测试条件。

for 循环 
>多次执行一个语句序列，简化管理循环变量的代码。

do...while 
>循环 除了它是在循环主体结尾测试条件外，其他与 while 语句类似。

嵌套循环 
>可以在 while、for 或 do..while 循环内使用一个或多个循环。

循环控制语句
> break 语句 
>>终止循环或 switch 语句，程序流将继续执行紧接着循环或 switch 的下一条语句。

> continue 语句 
> >告诉一个循环体立刻停止本次循环迭代，重新开始下次循环迭代。

> goto  
> >语句 将控制转移到被标记的语句。 但是不建议在程序中使用 goto 语句。
> > ```
> > mark:     printf("1");     
> > goto mark;
> > ```
> > ```
> > LABEL:     scanf("%d",&sex);     
> > printf("yahahah!\n");     
> > if (sex>5){         
> >     goto LABEL;     
> > }
> > ```

## 函数
公式
```
return_type function_name( parameter list ) {    body of the function }
```
作用域  
> 在函数或块内部的局部变量  
> 在所有函数外部的全局变量  
> 在形式参数的函数参数定义中    
main函数的功能
```
int main(int arg,char **args){
    printf("%s",args[0]) 
} 
```
> 默认有一个编译好,可执行文件的路径  
可变参数
> 通过...来表示 可变参数
> ```
> //使用可变参数 -> 获取参数 -> 导入stdarg 
> \#include <stdarg.h>
> void fun9(int arg,...){ 
>     //    声明参数列表    
>     va_list args;    
>     va_start(args,arg); //   获取参数值 
>     for (int i = 0; i < arg; ++i) {
>         printf("%d\n",va_arg(args, int)); 
>     }
>     printf("%d\n",va_arg(args, int));     
>     printf("%d\n",va_arg(args, int));    
>     printf("%d\n",va_arg(args, int));    
>     va_end(args); 
> }
> ```

## 数组

## 字符串
连接
```
strcat(s1, s2);
```
复制字符串 s2 到字符串 s1
```
strcpy(s1, s2);
```
返回字符串 s1 的长度。
```
strlen(s1);
```
字符串比较
```
strcmp(s1, s2);
```
> 如果 s1 和 s2 是相同的，则返回 0  
> 如果 s1 < s2 则返回小于 0  
> 如果 s1 > s2 则返回大于 0  

字符串截取
```
strchr(s1, ch);
printf("%s",strchr(msg,'h'));
```


## 枚举
enum　枚举名　{枚举元素1,枚举元素2,……};
```
enum LOGIN_TYPE {
    QQ=10,     
    Wechat=0,     
    Sina,     
    Dingding 
}loginType;
```
```
enum SEASON {     
    Spring,     
    Summer,     
    Autumn,     
    Winter 
};  
enum SEASON season;
```

## 指针 pointer
符号
> & 取地址符  
> %p 打印地址  
> * 取值/声明指针变量  

运算
> ++  
> \-\-  
> +=  
> \-=  

指针的长度
```
sizeof(int *)
```
创建指针对象
```
int num = 30; int *a = &num;
int *a = malloc(4);
```
free 释放指针对象  

函数指针
函数 也是一个(对象)      
声明:returnType funName(parms);      

## 预编译
头文件的重复引入
```
#ifdef
#pragma once
```
宏定义  
> 宏函数
> ```
> #define MAX(a,b) a>=b?a:b  
> #define ENUMTER(len,content) \     
>     for (int i=0;i<len;++i)content
> ```
> 宏定义 
> ```
> //#define 宏名字 宏代表的值 
> #define FFF 0 
> #define VVV() 2+3 
> #define KKK(a) a%2 
> #define PPP(a,b) printf("%d\n%d",a,b)
> printf("%d\n",VVV()); 
> printf("%d\n",KKK(3));  
> PPP(22,33);
> #define ANDROID "1"
> #define ANDROID 1
> ```