


def test_yield():
    for i in range( 5 ):
        yield check_yield, i, i+1


def check_yield( a, b ):
    assert ( a+b < 10 )


def je_teste_tout():
    assert True
0
    
def ce_test_existe():
    assert True


def ceci_est_un_test():
    assert True


# def test_test( a, b, c ):
#     assert a == b
#     assert b == c

