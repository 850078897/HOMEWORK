def is_prime(n):
    for i in range(2, n):
        if i % n ==0:
            print("maybe be multiple")
            return False
        return True
