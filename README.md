# 6기 머신러닝

이 저장소는 lab4dx KDT 과정의 머신러닝 수업 자료를 관리하는 공간입니다.

## 실습 환경 준비

본 과정의 실습은 **Python 3.10 기반 Conda 가상환경**을 기준으로 진행됩니다.  
Jupyter Notebook에서도 실습할 수 있지만, 파일 관리와 실행 환경 확인이 쉬운 **VS Code 사용을 권장**합니다.

Google Colab에서도 노트북을 실행할 수 있습니다. 다만 로컬 파일, 패키지 설치, 데이터 경로가 실습마다 달라질 수 있으므로 Colab을 사용할 경우 아래의 Colab 사용 방법을 먼저 확인해 주세요.

### 1. Anaconda 설치

Conda 기반 Python 가상환경을 사용하기 위해 Anaconda를 설치합니다.  
아래 공식 페이지에서 운영체제(Windows / macOS / Linux)에 맞는 설치 파일을 내려받아 설치해 주세요.

Anaconda 공식 다운로드 페이지:  
https://www.anaconda.com/download/success

### 2. Conda 가상환경 생성

Python 3.10 환경을 새로 만듭니다.

```bash
conda create -n py310 python=3.10
```

### 3. 가상환경 활성화

```bash
conda activate py310
```

### 4. 실습 패키지 설치

저장소 루트 디렉터리에서 `requirements.txt` 파일을 사용해 필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

### 5. VS Code 설치

VS Code는 필수는 아니지만 권장합니다.  
노트북 실행, 코드 수정, 파일 경로 확인, 터미널 사용을 한 화면에서 처리하기 쉽습니다.

VS Code 공식 다운로드 페이지:  
https://code.visualstudio.com/

VS Code에서 노트북을 실행할 때는 커널을 `py310` 가상환경으로 선택해 주세요.

### 6. Google Colab에서 사용하기

Colab에서는 저장소를 직접 복제하지 않아도 노트북을 열 수 있습니다.

1. https://colab.research.google.com/ 에 접속합니다.
2. 상단 메뉴에서 **파일 > 노트 열기**를 선택합니다.
3. **GitHub** 탭에서 저장소 주소를 입력하거나, **업로드** 탭에서 `.ipynb` 파일을 직접 업로드합니다.
4. 실행할 노트북을 선택합니다.

Colab에서 추가 패키지가 필요한 경우 `requirements.txt` 파일도 함께 업로드합니다.  
왼쪽 **파일** 패널에 `requirements.txt`를 업로드한 뒤, 노트북 첫 코드 셀에서 아래 명령을 실행합니다.

```python
%pip install -r requirements.txt
```

Colab 런타임이 초기화되면 설치한 패키지와 생성한 파일이 사라질 수 있습니다.  
런타임을 새로 시작한 경우 위 설치 명령을 다시 실행해 주세요.

## 저작권 및 문의

본 교육자료의 **무단 복제, 배포, 상업적 이용을 금지합니다.**  
교육자료의 사용 허가나 기타 문의사항은 아래로 연락 바랍니다.  

**문의:** `rlaalstn1504@naver.com`

---

> © 2026. lab4dx KDT 머신러닝(텍스트마이닝 포함) 교육자료  
> 본 자료는 lab4dx KDT 과정 전용으로 제작되었습니다.  
> All rights reserved.
