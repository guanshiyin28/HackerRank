#include<bits/stdc++.h>

using namespace std;

//Define the structs Workshops and Available_Workshops.
//Implement the functions initialize and CalculateMaxWorkshops
struct Workshops{
    friend ostream &operator<<(ostream &os, const Workshops &obj);
    int start_time;
    int end_time;
    int duration;
    bool operator<(const Workshops &rhs){
    return (this->end_time < rhs.end_time);
    }
};
ostream &operator<<(ostream &os, const Workshops &obj){
    os << obj.start_time << ": " << obj.end_time << ": "
    << obj.duration << "\n";
    return os;
}
struct Available_Workshops{
    int n;
    vector<Workshops> vec;
};
Available_Workshops* initialize(int start_time[], int duration[], int num)
{
    Available_Workshops *avail = new Available_Workshops;
    avail->n = num;
    Workshops test;
    for(int i{0}; i < num; i++){
        test.start_time = start_time[i];
        test.duration = duration[i];
        test.end_time = start_time[i] + duration[i];
        avail->vec.push_back(test);
    }
    sort(avail->vec.begin(), avail->vec.end());
    return avail;
}
int CalculateMaxWorkshops(Available_Workshops *test){
    int w_count = 1;
    int test_end_time = test->vec.at(0).end_time;
    for(int i{1}; i < test->n; i++){
        if(test_end_time <= test->vec.at(i).start_time){
            w_count++;
            test_end_time = test->vec.at(i).end_time;
        }
    }
    return w_count;
}

int main(int argc, char *argv[]) {
    int n; // number of workshops
    cin >> n;
    // create arrays of unknown size n
    int* start_time = new int[n];
    int* duration = new int[n];

    for(int i=0; i < n; i++){
        cin >> start_time[i];
    }
    for(int i = 0; i < n; i++){
        cin >> duration[i];
    }

    Available_Workshops * ptr;
    ptr = initialize(start_time,duration, n);
    cout << CalculateMaxWorkshops(ptr) << endl;
    return 0;
}
