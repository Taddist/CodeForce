#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
   int i ,a ,b,sum,g,c,k , j , t ;

cin>>t;

for  (i=0;i<t;i++){
    
    cin>>a;
	cin>>b;
	sum=0 ;
	g=0 ;
	int T[b];
	for (j=0;j<b;j++){
	    cin>>T[j];
	}
	sort(T, T+b, greater<int>());

	c=0;
	for (k=b-1;k>-1;k--){
	    if(c==0){
			sum=sum+T[k];
			g=g+1;
	    }

		if(sum>=a){
			c=1;
		}
	
	} 
cout << g << "\n" << endl;	

} 
}