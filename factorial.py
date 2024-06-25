
def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)



def list_factorial(n:list[int] ) -> list[int]:
    return [factorial(i) for i in n]
        

