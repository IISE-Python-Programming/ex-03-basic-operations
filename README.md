# Exercise 03. Basic Operations

세 번째 과제입니다. 이번 과제는 두 번째 과제와 아주 유사합니다.

두 번째 과제와 마찬가지로 어떤 연산을 수행한 후 그 결과를 `result` 변수에 할당하면 됩니다. 이 과제에서 작성할 함수들은 아래와 같습니다.

* 문자열 형태의 정수를 입력받아 정수 형태로 변환하는 `str_to_int` 함수
* 문자열 형태의 실수를 입력받아 실수 형태로 변환하는 `str_to_float` 함수
* 실수 형태의 숫자를 입력받아 문자열 형태로 변환하는 `number_to_str` 함수
* 문자열과 실수를 입력받아 연결된 하나의 문자열을 반환하는 `add_string_number` 함수
* 두 개의 문자열을 입력받아 연결된 하나의 문자열을 반환하는 `add_string_string` 함수
* 세 개의 숫자를 입력받아 분배법칙에 따라 계산하는 `distributive_law` 함수
* 두 실수 (밑, 지수) 를 입력받아 거듭제곱 연산을 수행하는 `exponentiation` 함수
* 세 개의 숫자를 입력받아 그 평균 값을 계산하는 `compute_average` 함수

템플릿 코드를 보면 각 함수에 대한 설명과 예시가 주석으로 적혀 있으니 참고하세요. 템플릿 코드에서 여러분들이 작성해야 하는 부분은 아래와 같습니다.

``` python
    #===== write your code below =======

    result = None

    #===================================
```

위에서 `None`에 해당되는 부분을 작성하면 됩니다. 두 번째 숙제와 마찬가지로 입력에 해당되는 정보는 Input에 해당되는 변수에 미리 들어있다고 생각하면 됩니다. 예를 들어, `str_to_int` 함수는 `string_number`라는 이름의 변수를 Input으로 가지는데, 이 `string_number` 변수에 어떤 값이 이미 들어있다고 생각하고 `None` 부분을 수정하면 됩니다. `result =` 부분이 이미 작성되어 있으니 우변의 결과가 `result`라는 이름의 변수에 할당된다는 얘기겠죠?

템플릿 코드의 마지막 부분을 보면 아래와 같은 `main` 함수 코드가 있습니다.

``` python
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
```

역시 위의 `main` 함수 코드는 여러분들이 터미널에서 아래와 같이 입력하면 자동으로 실행됩니다.
``` bash
> python basic_operations.py
```
출력된 테스트 결과가 모두 `True`라면 맞게 작성한 걸로 볼 수 있습니다. 여러분들이 직접 다른 테스트 코드를 추가하여 확인해보세요.