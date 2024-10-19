class ExampleClass():
    def add(self,a,b):
        c=a+b
        return c
if __name__=="__main__":
        example=ExampleClass()
        d=int(input("Input value:"))
        e=int(input("Input second value:"))
        f=example.add(d,e)
        print(f)