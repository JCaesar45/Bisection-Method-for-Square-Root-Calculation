def square_root_bisection(num, tolerance=1e-7, max_iter=100):
    if num < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    # Handle special cases directly
    if num == 0:
        print(f"The square root of 0 is 0")
        return 0
    if num == 1:
        print(f"The square root of 1 is 1")
        return 1

    # Set initial bounds
    low = 0
    high = max(1, num)

    for i in range(max_iter):
        guess = (high + low) / 2
        squared_guess = guess * guess

        # Check if the current bounds are within the tolerance
        if (high - low) <= tolerance:
            print(f"The square root of {num} is approximately {guess}")
            return guess

        # Narrow the bounds
        if squared_guess > num:
            high = guess
        else:
            low = guess

    # If max iterations reached without convergence
    print(f"Failed to converge within {max_iter} iterations")
    return None
