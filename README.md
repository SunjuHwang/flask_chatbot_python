# 파이썬 챗봇 만들기!!

### 카카오톡 플러스친구 관리자 센터 접속

- 플러스 친구 생성 후 공개 설정(공개 안되면 검색 불가)
- 스마트 채팅 API형 사용

### C9 개발

- 우측 상단의 톱니바퀴에 들어가서 python 3로 설정 변경
- `sudo pip3 install flask` 플라스크 설치

### keyboard

``` python
from flask import Flask
import os
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return '챗봇 페이지입니다!!!'

@app.route('/keyboard')
def keyboard():
    keyboard = {
                "type" : "buttons",
                "buttons" : ["메뉴", "로또", "고양이", "영화"]
                }
    json_keyboard = json.dumps(keyboard)            
    return json_keyboard
                    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

```

### API

- request
    - url : 어떤 경로로 보낼 것인가
    - method : 어떤 방법으로 보낼 것인가
    - parameter : 어떤 정보를 담을 것인가
    - 
- response
    - data type : 어떤 형식으로 답할 것인가
    - 