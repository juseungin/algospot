#include <iostream>

using namespace std;

class Dummy{
public:
    static int n;
    Dummy() {n++;};
    bool istime(Dummy& param);

};

int Dummy::n = 0;

class CVector {
public:
    int x,y;
    CVector () {}
    CVector (int a, int b) : x(a), y(b) {}
    CVector& operator= (const CVector& );
};

bool Dummy::istime(Dummy& param)
{
    if (&param == this) return true;
    else return false;
}

CVector& CVector::operator= (const CVector& param){
    x = param.x;
    y = param.y;
    return *this;
}

class MyClass{
public:
    int x;
    MyClass(int val) : x(val) {}
    const int& get() const {return x;}
};

template <class T>
class mypair{
    T a,b;
  public:
    mypair (T first, T second)
    { a = first; b = second; }
    T getmax ();
};

template <class T>
T mypair<T>::getmax(){
    T retval;
    retval = a>b? a : b;
    return retval;
}

template <class T>
class mycontainer{
    T element;
  public:
    mycontainer (T arg) {element = arg;}
    T increase() {return ++element;}
};

template <>
class mycontainer <char> {
    char element;
  public:
    mycontainer (char arg) {element = arg;}
    char uppercase() {
        if((element >= 'a') && (element <= 'z'))
            element += 'A' - 'a';
        return element;
    }
};

int main(){
    mycontainer<int> myint (7);
    mycontainer<char> mychar ('j');

    cout << myint.increase() << endl;
    cout << mychar.uppercase() << endl;

/*
    mypair <int> myobject(100, 75);
    cout << myobject.getmax() << endl;

    const MyClass foo(10);
    cout << foo.get() << endl;


    Dummy a;
    Dummy b[5];

    cout << a.n << endl;
    Dummy *c = new Dummy;
    cout << Dummy::n << endl;
    delete c;

    Dummy* b = &a;

    CVector foo(1,2);
    CVector bar;
    bar = foo;
    cout << bar.x << ", " << bar.y << endl;

    if (b->istime(a))
        cout << "&a is b \n";
*/
    return 0;
}
