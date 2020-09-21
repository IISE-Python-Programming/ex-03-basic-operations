def str_to_int(string_number):
    """문자열 형태의 정수 string_number를 입력받아 integer 형태로 변환하는 함수입니다.

    Input:
        string_number: 문자열 형태의 정수

    Output:
        result: 정수 형태로 변환된 값

    Examples:
        >>> str_to_int("3")
        3
        >>> str_to_int("135")
        135
    """
    #===== write your code below =======

    result = None

    #===================================

    return result


def str_to_float(string_number):
    """문자열 형태의 실수 string_number를 입력받아 float 형태로 변환하는 함수입니다.

    Input:
        string_number: 문자열 형태의 실수

    Output:
        result: 실수 형태로 변환된 값

    Examples:
        >>> str_to_float("3")
        3.0
        >>> str_to_float("135.4567")
        135.4567
    """
    #===== write your code below =======

    result = None

    #===================================

    return result


def number_to_str(float_number):
    """실수 형태의 숫자 float_number를 입력받아 string 형태로 변환하는 함수입니다.

    Input:
        float_number: 실수

    Output:
        result: 문자열 형태로 변환된 값

    Examples:
        >>> number_to_str(3)
    	"3"
    	>>> number_to_str(-3.456)
    	"-3.456"
    """
    #===== write your code below =======

    result = None

    #===================================

    return result


def add_string_number(string, float_number):
    """문자열 string과 실수 float_number를 입력받아 string과 float_number가 연결된 
    하나의 문자열을 반환하는 함수입니다.
    
    Input:
        string: 문자열
        float_number: 실수

    Output:
        result: 문자열과 실수 값이 연결된 문자열

    Examples:
        >>> add_string_number("SeoulTech", 3)
    	"SeoulTech3"
    	>>> add_string_number("my", 14)
    	"my14"
    """
    #===== write your code below =======

    result = None

    #===================================
    
    return result


def add_string_string(str_1, str_2):
    """두 개의 문자열 str_1, str_2를 입력받아 두 문자열이 연결된 하나의 문자열을 반환하는 함수입니다.

    Input:
        str_1: 문자열
        str_2: 문자열
    
    Output:
        result: 두 문자열이 연결된 문자열
    
    Examples:
    	>>> add_string_string("3", "흐흐흐")
    	"3흐흐흐"
    	>>> add_string_string("135", "45.76")
    	"13545.76"
    """
    #===== write your code below =======

    result = None

    #===================================
    
    return result


def distributive_law(a, b, c):
    """세 개의 숫자 a, b, c를 입력받아 a * (b + c)를 계산하는 함수입니다.
    
    Input:
        a, b, c: 실수 형태의 숫자

    Output:
        result: 기술된 분배법칙이 적용되어 계산된 실수 값

    Examples:
        >>> distributive_law(3, 4, 5)
    	27
    """
    #===== write your code below =======

    result = None

    #===================================

    return result


def exponentiation(base, power):
    """두 실수 base, power를 입력받아 지수연산을 수행하는 함수입니다.
    
    Input:
        base: 밑
        power: 지수

    Output:
        result: 거듭제곱의 결과

    Examples:
    	>>> exponentiation(3, 4)
    	81
    """
    #===== write your code below =======

    result = None

    #===================================

    return result


def compute_average(a, b, c):
    """세 개의 실수 a, b, c를 입력받아 그 평균 값을 계산하는 함수입니다.

    Input:
        a, b, c: 실수 형태의 숫자

    Output:
        result: 평균 값

    Examples:
        >>> compute_average(3,1,6)
        3.3333333333333335
        >>> compute_average(1.5, 3, 4.5)
        3.0
    """
     #===== write your code below =======

    result = None

    #===================================

    return result



def main():
    print("str_to_int Test")
    print("\t", str_to_int("27") == 27)  # Expected Result: True
    print("str_to_int Test Closed \n")

    print("str_to_float Test")
    print("\t", str_to_float("3.4") == 3.4)  # Expected Result: True
    print("Str_to_float Test Closed \n")

    print("number_to_str Test")
    print("\t", number_to_str(4.751) == "4.751")  # Expected Result: True
    print("number_to_str Test Closed \n")

    print("add_string_number Test")
    print("\t", add_string_number("test", 4) == "test4")  # Expected Result: True
    print("add_string_number Test Closed \n")

    print("add_string_string Test")
    print("\t", add_string_string("파이썬", "수업") == "파이썬수업")  # Expected Result: True
    print("add_string_string Test Closed \n")

    print("distributive_law Test")
    print("\t", distributive_law(3, 4, 5) == 27)  # Expected Result: True
    print("distributive_law Test Closed \n")
    
    print("exponentiation Test")
    print("\t", exponentiation(2, 10) == 1024)  # Expected Result: True
    print("exponent Test Closed \n")

    print("compute_average Test")
    print("\t", compute_average(3, 1.5, 4.5) == 3.0)  # Expected Result: True
    print("compute_average Test Closed \n")

if __name__ == '__main__':
    main()
