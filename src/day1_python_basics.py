def analyze_number (x) :
    
    N = x ** 2
    print("square = %0.1f" %N)

    if N > 20 :
        print("Result is large")
    else :
        print("Result is small")

    return 0


x = float(input())
analyze_number(x)