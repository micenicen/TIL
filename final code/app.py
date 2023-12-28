import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from emotion_vis import (emotion_chart, analyze_emotion_data)
from stare_vis  import (stare_chart, analyze_stare_data)
from wordcloud_vis import wordcloud_chart
from sentiment_scores_vis import sentiment_scores, sentiment_radar_chart, interpret_interview_sentiment
from table_vis import table_chart
from datetime import datetime
import matplotlib.pyplot as plt
from PIL import Image
import io
import base64

# 현재 날짜를 문자열로 포매팅
current_date = datetime.now().strftime("%Y-%m-%d")

# 페이지 설정 (Streamlit 앱의 타이틀 및 레이아웃 설정)
st.set_page_config(page_title="INTERVIEW REPORT", layout="wide")

# CSS 스타일을 정의 (앱 전체에 적용될 스타일)
st.markdown(f"""
<style>
/* 페이지 전체에 적용되는 기본 스타일 설정 */
body {{
    font-family: 'Segoe UI', sans-serif;
    background-color: #000080;  /* 전체 페이지 배경을 흰색으로 설정 */
}}

/* 리포트의 메인 컨테이너 스타일. 모든 섹션을 감싸는 컨테이너에 적용됨 */
.report-container {{
    background-color: #FFFFFF;
    border-radius: 5px;
    margin: 10px 0px;
    padding: 20px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}}

/* 리포트 타이틀 스타일. 중앙 정렬된 헤더에 적용됨 */
.report-header h1 {{
    color:#0000FF; /* 네이비 색상 적용 */
    text-align: center;
}}

/* 이름과 검사일시를 포함하는 테이블 스타일. 각 셀의 너비를 50%로 설정하여 테이블이 반반으로 나뉘도록 함 */
.report-table {{
    width: 100%;
    table-layout: fixed;
}}
.report-table td {{
    width: 50%;
    text-align: left;
    padding: 10px;
}}

/* 카드 스타일. 각 섹션의 카드를 균등하게 배치 */
.cards-container {{
    display: flex;
    justify-content: space-around;
}}
.card {{
    flex-basis: 0;
    flex-grow: 1;
    margin: 10px;
    padding: 15px;
    border-radius: 5px;
    background-color: #FAFAFA;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: left;
}}

/* 진행바 컨테이너 및 진행바 스타일. 진행 상태를 시각화 */
.progress-bar-container {{
    background-color: #E0E0E0;
    border-radius: 5px;
    height: 20px;
    width: 100%;
    overflow: hidden;
    margin-top: 10px;
}}
.progress-bar {{
    height: 20px;
    border-radius: 5px;
    background-color: #76c893;
}}

/* 모바일 및 태블릿 뷰를 위한 반응형 디자인. 화면 크기가 작아질 때의 스타일 변경 */
@media (max-width: 768px) {{
    .cards-container {{
        flex-direction: column;
    }}
    .report-table td {{
        display: block;
        width: 100%;
        text-align: center;
    }}
}}
</style>
""", unsafe_allow_html=True)

# 리포트 헤더 HTML (리포트의 타이틀 및 사용자 정보를 포함하는 섹션)
st.markdown(f"""
<div class="report-container">
    <div class="report-header">
        <h1 style="color: #0000FF;">INTERVIEW REPORT</h1>
    </div>
    <table class="report-table">
        <tr>
            <td><b>이름:</b> 이상진</td>
            <td><b>검사일시:</b> {current_date} </td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# AI 얼굴관리 분석 섹션
cols = st.columns(3)
with cols[0]:
    st.markdown("""
  <div class="card">
        <h4>전체 면접 역량 평가</h4>
        <p> <b>최우수</b> (1/100) &nbsp;&nbsp; <b>상위</b>(1%)</p>
        <div class="progress-bar-container">
            <div class="progress-bar" style="width: 50%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
    <div class="card">
        <h4>전체전형 신뢰성 평가 </h4>
        <p> <b>신뢰가능</b> &nbsp;&nbsp; (지원동기, 면접인터뷰 안정정으로 진행) </p>
        <div class="progress-bar-container">
            <div class="progress-bar" style="width: 80%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with cols[2]:
    st.markdown("""
    <div class="card">
        <h4>면접시간</h4>
        <p> <b>46:00</b> </p>
        <div class="progress-bar-container">
            <div class="progress-bar" style="width: 90%;"></div>        
    </div>
    """, unsafe_allow_html=True)


# 결과 해석 섹션
st.markdown("""
<div class="report-container">
    <h3 class="section-title"> 면접역량 해석</h3>
    <table class="report-table">
        <tr>
            AI 면접 결과분석은 기본면접/ 상황면접을 통해 AI가 응사자의 답변내용 및 태도 등을 평가한 결과가 제시합니다.<br>
            이때, 평가에 활용되는 항목은 응사자의 면접 태도를 안면분석, 음성분석, AI자연어 처리, 어휘분석을 한 데이터가 포함 됩니다.<br>
            이러한 결과는 지원자 간의 상대평가에 따른 것으로, 절대적인 기준은 아니며 참고용 자료로 활용됩니다.<br>
            또한, 결과내용은 응사자의 변동 및 AI의 지속적인 딥러닝을 통해 수시로 변동될 수 있습니다.<br>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# 통계적 분석 섹션 시작
st.markdown("""
<div class="report-container">
    <h4 class="section-title">2. 면접분석</h4>
</div>
""", unsafe_allow_html=True)

# 감정분석과 시선분석을 위한 컬럼 정의
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h5>감정분석</h5>", unsafe_allow_html=True)
    fig1 = emotion_chart()  # Make sure this function returns a Plotly figure
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("<h5>시선분석</h5>", unsafe_allow_html=True)
    fig2 = stare_chart()  # Make sure this function returns a Plotly figure
    st.plotly_chart(fig2, use_container_width=True)

# 추가 컬럼
cols = st.columns(2)
with cols[0]:
    emotion_analysis_result = analyze_emotion_data()
    st.markdown(f"""
    <div class="card" style="border:1px solid #ccc; padding:10px;">
        <p>{emotion_analysis_result}</p>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    # analyze_stare_data 함수가 문자열을 반환하도록 수정해야 함
    stare_analysis_result = analyze_stare_data()
    st.markdown(f"""
    <div class="card" style="border:1px solid #ccc; padding:10px;">
        <p>{stare_analysis_result}</p>
    </div>
    """, unsafe_allow_html=True)

# 통계적 분석 섹션 종료
st.markdown("""
</div>
""", unsafe_allow_html=True)

# 통계적 분석 섹션 시작
st.markdown("""
<div class="report-container">
    <h4 class="section-title">언어분석</h4>
</div>
""", unsafe_allow_html=True)

# 언어분석 섹션
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h5>긍정/부정/중립</h5>", unsafe_allow_html=True)
    # 데이터 파일 경로 설정
    data_file = 'C:/Users/user/Downloads/Final_Project/pass_results_ex.csv'
    sentiment_file = 'C:/Users/user/Downloads/Final_Project/SentiWord_Dict.txt'

    df = sentiment_scores(data_file, sentiment_file)
    # 첫 번째 행의 결과 사용
    positive, neutral, negative = df.iloc[0]['Positive_Per'], df.iloc[0]['Neutral_Per'], df.iloc[0]['Negative_Per']
    radar_chart = sentiment_radar_chart(df)
    st.plotly_chart(radar_chart, use_container_width=True)

with col2:
    st.markdown("<h5>단어빈도수</h5>", unsafe_allow_html=True)
    fig3 = table_chart()  # Make sure this function returns a Plotly figure
    st.plotly_chart(fig3, use_container_width=True)

# 워드 클라우드 생성 및 표시
st.markdown("<h5>워드클라우드</h5>", unsafe_allow_html=True)
wordcloud = wordcloud_chart()
st.set_option('deprecation.showPyplotGlobalUse', False)  # 경고 메시지 숨기기
plt.figure(figsize=(7, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout()  # 여백 최적화
st.pyplot()

interpret_interview_sentiment_result = interpret_interview_sentiment(data_file, sentiment_file)
st.markdown(f"""
<div class="card" style="border:1px solid #ccc; padding:10px;">
    <p>{interpret_interview_sentiment_result}</p>
</div>
""", unsafe_allow_html=True)

# st.markdown("""
#     <div class="card">
#         <p>결과해석부분</p>
#     </div>
# """, unsafe_allow_html=True)




# 결과 해석 섹션
st.markdown("""
<div class="report-container">
    <h3 class="section-title">면접역량 해석</h3>
    <p>AI 면접 결과분석은 기본면접/ 상황면접을 통해 AI가 응사자의 답변내용 및 태도 등을 평가한 결과가 제시합니다.</p>
</div>
""", unsafe_allow_html=True)


# # 추가 컬럼
# cols = st.columns(2)
# with cols[0]:
#     st.markdown("""
#     <div class="card">
#         <p>결과해석부분</p>
#     </div>
#     """, unsafe_allow_html=True)
#
# with cols[1]:
#     st.markdown("""
#     <div class="card">
#         <p>결과해석부분</p>
#     </div>
#     """, unsafe_allow_html=True)


# Close the div for 통계적 분석 섹션
st.markdown("""
    </div>
</div>
""", unsafe_allow_html=True)





