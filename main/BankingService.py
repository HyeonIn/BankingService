def deposit():
  #입금
  #입금 금액 입력 
  #금액 확인 메세지 출력
  #통장 잔고에 더하기 
  #완료메세지 후 초기화면 or 로그아웃 선택, 5초 후 자동 로그아웃
  pass
def withdraw():
  #출금
  #출금 금액 입력
  #계좌 비밀번호 입력
  #잔고 확인
  #출금 완료 안내 or 출금 불가능 안내 후 초기화면
  pass
def transfer():
  #계좌 이체
  #이체할 계좌 입력
  #받는 분 성함과 금액 안내
  #계좌 비밀번호 입력
  #이체 완료 메세지
  pass
def openAccount():
  #계좌 개설
  #성명, 생년월일, 휴대폰 번호 기입
  #계좌번호는 휴대폰 번호로 개설된다고 알림
  #계좌 비밀번호 설정을 위해 입력, 재입력
  #계좌 개설 완료 메세지
  pass


def main():
  while True:
    print("원하시는 기능의 숫자를 입력하세요.")
    print("1. 입금 2. 출금 3. 이체 4. 계좌 개설 5. 종료")
    command = int(input())
    if command == 1:
      deposit()
    elif command == 2:
      withdraw()
    elif command == 3:
      transfer()
    elif command == 4:
      openAccount()
    elif command == 5:
      print("서비스를 종료합니다. 감사합니다.")
      break
    else:
      print("숫자를 잘못 입력하셨습니다.")
    

if __name__ == "__main__":
  #로그인 필요
  main()