#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person{
    public:
        string name;
        int age;
    public:
        Person():name(""), age(0){}
        Person(string& name, int age):name(name), age(age){}
        virtual void getdata(){
            cin >> name >> age;
        }
        virtual void putdata(){
            cout << name << " " << age << " ";
        }
};

class Student: public Person{
    private:
        vector<int> arr;
        static int cur_id;
    public:
        Student():Person(), arr(6, 0){}
        Student(string&name, int age, vector<int>& arr, int cur_id):Person(name, age), arr(arr){}
        void getdata()
        {
            Person::getdata();
            for(int i = 0; i < arr.size(); i++)
            {
                cin >> arr[i];
            }
        }
        void putdata()
        {
            Person::putdata();
            int total = 0;
            for(int i = 0; i < arr.size(); i++)
            {
                total += arr[i];
            }
            cout << total << " " << ++cur_id << endl;
        }
};

class Professor: public Person{
    private:
        int publicatios;
        static int cur_id;
    public:
        Professor():Person(), publicatios(0){}
        Professor(string& name, int age, int publications, int cur_id):Person(name, age), publicatios(publications){}
        void getdata()
        {
            Person::getdata();
            cin >> publicatios;
        }
        void putdata()
        {
            Person::putdata();
            cout << publicatios << " " << ++cur_id << endl;
        }
    
};
int Professor::cur_id = 0;
int Student::cur_id = 0;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
