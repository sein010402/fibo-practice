import math

def binet_fibonacci(n):
  """
  Binet의 공식을 사용하여 n번째 피보나치 수를 계산합니다.
  """
  phi = (1 + math.sqrt(5)) / 2
  # psi = (1 - math.sqrt(5)) / 2 # psi 항은 매우 작아져서, n이 클 경우 0으로 수렴합니다.
  # 따라서 아래와 같이 간단하게 계산할 수 있습니다.
  result = (phi**n) / math.sqrt(5)
  return round(result)

# 예시
print(binet_fibonacci(10))
