import pandas as pd
import re
from konlpy.tag import Okt
from wordcloud import WordCloud
from collections import Counter
from PIL import Image
import numpy as np

def wordcloud_chart():
    # 데이터 파일과 폰트 경로 직접 지정
    csv_file = 'C:/Users/user/Downloads/Final_Project/pass_results_23.csv'
    font_path = r'C:\Windows\Fonts\batang.ttc'
    mask_path = "C:/Users/user/Downloads/Final_Project/cloud1.jpg"

    # 데이터 파일 읽기
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {csv_file}")
        return None

    # 여러 행을 하나의 행으로 합치기
    merged_text = ' '.join(df['Text'])
    # 새로운 데이터프레임 생성
    df = pd.DataFrame({'Text': [merged_text]})


    # 불용어 리스트
    stop_words = ['안녕하세요', '안녕하십니까', '따라서', '지원', '우선', '일단', '얘기', '대해', '위해', '때문', '통해', '대한', '생각', '또한', '으로', '이고', '로서', '에서', '에도', '하다', '입니다']

    # 텍스트 전처리
    okt = Okt()
    df['Text'] = df['Text'].apply(lambda x: re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', x))
    df['Text'] = df['Text'].apply(lambda x: ' '.join([word for word in okt.nouns(x) if word not in stop_words and len(word) > 1]))

    # 단어 빈도수 계산
    word_counts = Counter(" ".join(df['Text']).split())

    # 상위 30개 단어 선택
    top_words = dict(list(word_counts.items())[:100])

    # 원하는 크기로 조정 (예: 기본 크기의 70%)
    wordcloud_width = int(375 * 0.5)
    wordcloud_height = int(300 * 0.5)

    # 이미지 마스크 로드
    mask = np.array(Image.open(mask_path))


    wordcloud = WordCloud(
        font_path=font_path,
        background_color='white',
        #width=wordcloud_width,
        #height=wordcloud_height,
        mask=mask  # 이미지 마스크 사용
    ).generate_from_frequencies(top_words)  #100개만

    return wordcloud