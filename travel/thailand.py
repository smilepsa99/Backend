class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":  # 모듈 직접실행을 위한 코드
                            # [참고글1] https://velog.io/@mjk3136/if-name-main%EC%9D%80-%EC%99%9C-%ED%95%84%EC%9A%94%ED%95%9C%EC%A7%80%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90
                            # [참고글2] https://codealone.tistory.com/47
                            # [참고글3] https://lovelydiary.tistory.com/297
                            # __name__테스트 파일 참고!
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행됩니다.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
