# 편차가 큰 데이터에 대한 로그 변환
# 머신러닝에서 데이터 분석 시 log를 사용하면
# 1) 스케일 차이를 축소해준다. log(10) = 1, log(100) = 2, log(1000) = 3
# 2) 로그변환하면 치우친 데이터를 정규분포에 가깝게 변경 가능 (Skewness 완화)
# 3) 모델링에서 지수 관계를 선형 관계로 바꿔준다.  ax

import numpy as np
# suppress=True: 소수점을 지수 표현식(e+01 등) 대신 일반 실수로 출력
# precision=6: 소수점 아래 6자리까지만 표시
np.set_printoptions(suppress=True, precision=6)

def test():
    # 극단적으로 큰 값과 작은 값이 섞여 있는 배열 생성
    values = np.array([345, 34.5, 3.45, 0.345, 0.01, 0.1, 10, 100])
    
    # 각기 다른 밑(Base)을 가진 로그 함수들의 결과 비교
    print(np.log2(3.45), ' ', np.log10(3.45), ' ', np.log(3.45))
    print("원본 값 : ", values)
    
    # 상용로그(log10): 10을 몇 번 곱해야 해당 숫자가 되는지 계산 (스케일 축소에 효과적)
    log_values = np.log10(values)
    print("log_values : ", log_values)
    
    # 자연로그(ln): 밑이 e인 로그. 머신러닝 모델의 손실 함수 등에서 표준적으로 사용됨
    ln_values = np.log(values)
    print("ln_values : ", ln_values)

    # [정규화 (Normalization - Min-Max Scaling)]
    # 모든 데이터를 0 ~ 1 사이의 범위 내로 압축하여 데이터 간 상대적 위치를 표시함
    min_log = np.min(log_values)
    max_log = np.max(log_values)
    # 공식: (현재값 - 최소값) / (최대값 - 최소값)
    normalized = (log_values - min_log) / (max_log - min_log)
    print("정규화 결과 ", normalized)

class LogTrans:
    # 편차가 큰 데이터를 로그 스케일 변환하고 그 역변환을 제공하는 클래스
    # offset: 데이터에 0이 포함되어 있을 경우 log(0)은 정의되지 않으므로(무한대), 1.0 정도를 더해 안전하게 계산함
    def __init__(self, offset:float=1.0):
        self.offset = offset

    # 로그 변환 메서드 (Log Transformation)
    def transform(self, x:np.ndarray) -> np.ndarray:
        # x + 1.0을 해줌으로써 0 이상의 양수 데이터를 로그 변환 가능하게 만듦 (log1p와 유사한 개념)
        return np.log(x + self.offset)
    
    # 역변환 메소드 (Inverse Transformation)
    # 모델 예측 결과가 로그값일 때, 이를 다시 사람이 이해할 수 있는 원래 단위로 되돌림
    def inverse_trans(self, x_log:np.ndarray) -> np.ndarray:
        # 지수 함수(exp)를 취한 뒤 처음에 더했던 offset(1.0)을 다시 빼줌
        return np.exp(x_log) - self.offset


def main():
    print('***'*10)
    # 0.001부터 10000까지 10배씩 커지는 극단적인 편차의 데이터
    data = np.array([0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000], dtype = float)

    # 객체 생성 (기본 오프셋 1.0 설정)
    log_trans = LogTrans(offset=1.0)

    # 1. 원본 데이터를 로그 스케일로 변환
    data_log_scaled = log_trans.transform(data)
    # 2. 로그 변환된 데이터를 다시 원본 값으로 복구
    reversed_data = log_trans.inverse_trans(data_log_scaled)

    print("원본 :", data)
    # 변환 결과를 보면 10배씩 차이 나던 거리가 일정하게 좁혀진 것을 확인할 수 있음
    print("로그변환 : ", data_log_scaled)
    # 부동소수점 오차를 제외하고 원본과 거의 동일하게 복구됨
    print("역변환 : ", reversed_data)

if __name__ == "__main__":
    main()