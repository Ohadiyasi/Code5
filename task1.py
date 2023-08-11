
lineOdd="#*"
lineEven="*#"

def Print(n , m ):
    for i in range(n) :
        for j in range(m):
            if i%2==0:
                print(lineOdd , end="")
            else:
                print(lineEven , end="")
        print()
def main():
    n=int(input("number of rows = "))
    m=(int(input("number of cols = ")))
    Print(n , m)
    
main()
    