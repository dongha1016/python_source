# 예외처리 : 파일, 네트워크, DB작업, 실행에러 등의 에러 처리


def divide(a, b):
    return a/b

try:    # 실행문(예외 발생 가능 구문)
    c = divide(5, 2)
    print(c) 

    aa = [1,2]
    print(aa[0])
    # print(aa[3])

except ZeroDivisionError:   # 예외 종류 관련 클래스
    print('두번째 값은 0이 안됨')   # 예외 발생 처리 구문
except IndexError as e:     # as ~ 변수 : 에러 종류를 별명으로 저장하고 출력
    print('참조범위 오류 : ', e)
except Exception as e:     # 에러에 대한 최상위
    print('에러 원인은 : ', e)   # 전체 에러에 대해 출력해주는 구문
finally:    # 무조건 수행하는 구문
    print('에러 유무의 상관없이 반드시 수행')

print('end')