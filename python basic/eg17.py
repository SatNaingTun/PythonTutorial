def setup():
    n=10
    print(n)

def main():
    global n
    n=5
    print(n)
    setup()
    print(n)

main()