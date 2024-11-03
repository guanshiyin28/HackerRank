#include<bits/stdc++.h>

using namespace std;

class Box{
//for people who are learning
    private:
    int l;
    int b;
    int h;
    
    public:
//Getter functions for Box object attributes
    int getLength() const { //const shows it does not modify object
        return l;
    }
    int getBreadth() const {
        return b;
    }
    int getHeight() const {
        return h;
    }
    //volume calculation
    long long CalculateVolume() const {
/*
We use the static_cast method to prevent overflow,
just in case the volume exceeds the interger range.
Note we dont place l * b * h inside the static_cast parameters
as that causes the multiplication to take place first.
*/
        return static_cast<long long>(l) * b * h;
    }
// Constructors - Topic overloading constructors with differerent parameters
    Box(int length, int breadth, int height): l(length), b(breadth), h(height){}
    Box(Box& X): l(X.l), b(X.b), h(X.h){}
    Box():l(0), b(0), h(0) {}
    
// overloading the '<' operator
    bool operator<(const Box& other) const { //again const shows we are not modifying either obj
        if (l < other.l) return true;
        if (l == other.l && b < other.b) return true;
        if (l == other.l && b == other.b && h < other.h) return true;
        return false;
    }
//Declare friend function for opp<< that exists outside the class.
    friend ostream& operator<<(ostream& out, const Box& B); 
};   

// The friend we refered to in the class
ostream& operator<<(ostream& out,const Box& B){
//its our friend so it can see our privates :p
        out << B.l <<' '<< B.b <<' '<<B.h;
        return out;
}



void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}
