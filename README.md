2023.02  
2023년 2월 말, stable-diffusion 모델에 관심이 생겨 진행한 프로젝트다.  

AI 모델을 컴퓨터에서 직접 실행해보는 건 처음이라 실행 환경을 맞추느라 며칠 동안 애를 많이 먹었던 기억이 난다.
결국 어떻게 성공해서 이런 그림을 그렸다.
<img width="2560" height="1272" alt="image" src="https://github.com/user-attachments/assets/ad5b6799-2266-494a-b392-1300336097ea" />
<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/8153c8e6-a919-470a-bcee-253a5a861bcc" />

이후 'Stable Diffusion Model을 활용한 주가의 대략적 향방 예측'프로젝트를 잠깐 시도해봤다.

당시 모델 학습을 위해 주가 데이터를 차트 이미지로 저장하고, 같은 비율로 정규화하는 프로그램(DMPredict/savechart, InvokeAI-main/resize_512)을 작성했다.
krx에서 KOSPI200에 속한 종목의 1년치 일별 종가 데이터를 크롤링하고 정규화해서 총 1413개의 이미지 파일을 확보했다.

이 자료를 활용해 Stable-Diffusion을 파인튜닝해서 나름 이미지를 뽑아 봤으나,
<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/cd0f2cea-6e93-488f-9ce1-f1a65846bf33" />
나름 주가 비슷한 게 나오긴 했으나 썩 시원찮았다.

그 당시엔 이 정도로 만족하고 끝냈던 것 같다.

이후 이 아이디어를 차용해서 DB금융경제공모전에 '현재 주가 차트를 이용한 과거 유사 차트 검색 시스템 제안'이라는 아이디어를 제출했고, 예선 통과했다.
