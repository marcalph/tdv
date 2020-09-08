## Context

everything is in java

### source
```
public class A{
    private String attribute;
    public String getAttribute() {
        return attribute;
    }
}

public class B extends A{
    private int id;
    public int getId() {
        return id;
    }
}

public class C extends A{
    private String id;
    public String getId() {
        return attribute;
    }
}
```

### declarations
```
B b = new B();
A a = new A();
A aa = new A();
C c = new C();
Object o = new C();
```

### questions

```
String att = b.getAttribute();  #1
a = b;                          #2
int i = a.getId;                #3
c = aa;                         #4
o = a;                          #5
```

### solutions
1 - OK b is a reference to a B object which inherits method from parent class A because method is public  
2 - OK reference a  which is a A instance is assigned reference b which is a B instance, it works because B class extends A class, so every B is an A instance so you can cast B to A (casting works if you affect a child class)  
3 - KO will fail at compile time, to fix it we should cast a as B so that compiler know that reference
4 - KO not every A is a C, also there is no implicit casting possible so there is no fix
5 - OK everything inherits from the object class