import requests, time  # requests 모듈과 시간 측정을 위한 time 모듈 임포트
import multiprocessing  # 병렬 처리를 위한 multiprocessing 모듈 임포트

session = None  # 전역 변수로 session을 None으로 초기화

def set_global_session():
    global session  # 전역 변수 session을 사용하겠다고 선언
    if not session:
        session = requests.Session()  # session이 None일 경우, requests의 Session 객체를 생성

def download_site(url):
    with session.get(url) as response:  # 전역 변수로 선언된 session을 사용하여 URL에 GET 요청
        name = multiprocessing.current_process().name  # 현재 프로세스의 이름을 얻음
        # 현재 프로세스 이름과, 응답받은 데이터의 길이, 요청한 URL을 출력
        print(f"{name}: Read {len(response.content)} from {url}")
        
def download_all_sites(sites):
    # multiprocessing.Pool을 사용하여 프로세스 풀 생성
    # processes=5는 동시에 실행될 프로세스의 수를 5로 설정
    # initializer에 set_global_session 함수를 지정하여 프로세스 풀의 각 프로세스가 시작할 때 실행되도록 함
    with multiprocessing.Pool(processes=5, initializer=set_global_session) as pool:
        pool.map(download_site, sites)  # sites 리스트의 각 요소를 download_site 함수에 병렬로 적용
        
if __name__ == "__main__":
    sites = [
        "https://home.sch.ac.kr/iot",
        "https://home.sch.ac.kr/bigdata"
    ] * 80  # 테스트를 위해 동일한 URL을 80번 반복하여 리스트 생성
    start_time = time.time()  # 작업 시작 시간 측정
    download_all_sites(sites)  # 사이트 다운로드 함수 호출
    duration = time.time() - start_time  # 작업 종료 시간 측정 및 총 소요 시간 계산
    # 다운로드한 사이트의 수와 총 소요 시간을 출력
    print(f"Downloaded {len(sites)} in {duration} seconds")

# 이 코드는 requests 모듈을 사용하여 여러 웹사이트의 컨텐츠를 병렬로 다운로드하는 예제입니다.
# multiprocessing.Pool을 사용하여 병렬 처리를 구현하고 있으며, 프로세스마다 독립적인 requests 세션을 사용하기 위해
# initializer 매개변수를 통해 프로세스가 생성될 때 set_global_session 함수를 호출합니다.
# 이를 통해 각 프로세스는 자신만의 네트워크 세션을 유지하게 되어, 네트워크 요청의 효율성을 높입니다.
