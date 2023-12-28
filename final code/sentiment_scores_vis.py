import pandas as pd
from konlpy.tag import Okt
import plotly.graph_objects as go


# 감성 점수 계산 함수
# def get_sentiment_scores(sentence, sentiment_df):
#     okt = Okt()
#     words = okt.pos(sentence)
#
#     positive_score, negative_score, neutral_count = 0, 0, 0
#
#     for word, _ in words:
#         found = sentiment_df[sentiment_df['words'] == word]
#         if not found.empty:
#             polarity = found.iloc[0, 1]
#             if polarity > 0:
#                 positive_score += polarity
#             elif polarity < 0:
#                 negative_score += abs(polarity)
#             else:
#                 neutral_count += 3
#
#     return positive_score, negative_score, neutral_count

def get_sentiment_scores(sentence, sentiment_df):
    okt = Okt()
    words = okt.pos(sentence)

    positive_score, negative_score, neutral_count = 0, 0, 0

    for word, pos in words:
        found = sentiment_df[sentiment_df['words'] == word]    # 단어 검색
        if not found.empty:  # 단어가 존재하는 경우
            polarity = found.iloc[0, 1]  # 극성(긍정/부정) 확인
            if polarity > 0:
                positive_score += polarity
            elif polarity < 0:
                negative_score += abs(polarity)
            else:
                neutral_count += 1

    # 결과 계산 수정
    # positive_score = sum(score for _, score in positive_score)
    # negative_score = sum(score for _, score in negative_score)

    # 결과 계산
    if positive_score > negative_score:
        result = '긍정'
    elif positive_score < negative_score:
        result = '부정'
    else:
        result = '중립'

    return positive_score, negative_score, neutral_count, result

# 전체 데이터셋에 대한 감성 점수 계산 및 업데이트
def sentiment_scores(data_file, sentiment_file):
    df = pd.read_csv(data_file)
    sentiment_df = pd.read_csv(sentiment_file, delimiter='\t', header=None)
    sentiment_df.columns = ['words', 'sentiment_score']

    results = df['Text'].apply(lambda x: get_sentiment_scores(x, sentiment_df))
    df[['Positive_Score', 'Negative_Score', 'Neutral_Count', 'result']] = pd.DataFrame(results.tolist(), index=df.index)          # check

    df['Total_Score'] = df['Positive_Score'] + df['Negative_Score'] + df['Neutral_Count']
    df['Positive_Per'] = df['Positive_Score'] / df['Total_Score']
    df['Negative_Per'] = df['Negative_Score'] / df['Total_Score']
    df['Neutral_Per'] = df['Neutral_Count'] / df['Total_Score']

    df.drop('Total_Score', axis=1, inplace=True)

    return df

# 레이더 차트 생성 함수
def sentiment_radar_chart(df):
    categories = ['긍정 점수', '중립 점수', '부정 점수']

    # 전체 평균 점수 (예시 데이터)
    average_scores = [0.49, 0.17, 0.34, 0.49]  # 2023년 합격자 평균으로 적용

    fig = go.Figure()

    # 개인 점수 그래프 추가
    personal_scores = [df.iloc[0]['Positive_Per'], df.iloc[0]['Neutral_Per'], df.iloc[0]['Negative_Per'], df.iloc[0]['Positive_Per']]
    fig.add_trace(go.Scatterpolar(
        r=personal_scores,
        theta=categories + [categories[0]],
        fill='toself',
        name='본인',
        #line=dict(width=2)
    ))

    # 전체 평균 그래프 추가
    fig.add_trace(go.Scatterpolar(
        r=average_scores,
        theta=categories + [categories[0]],
        fill='toself',
        name='전체 평균',
        #line=dict(width=2, color='red'),
        opacity=0.3
    ))


    # 레이아웃 설정 및 눈금 조정
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 0.7],  # 최대값 1
                showticklabels=False
            ),
            angularaxis=dict(
                rotation=90, # 90도 회전
                direction='clockwise', # 시계방향으로 회전
            )
        ),
        showlegend=True,  # 범례 표시 여부
        plot_bgcolor='white',  # 배경색을 흰색으로 설정
        paper_bgcolor='white',  # 종이 배경색도 흰색으로 설정
        legend=dict(
            orientation="h",  # 범례를 수평
            yanchor="bottom",  # 범례의 y축 아래쪽
            y=-0.5,  # 범례의 y축 아래쪽
            xanchor="center",  # 범례의 x축 둠
            x=0.5  # 범례의 x축 위치
        )
    )
    return fig


# 감정 해석 함수 정의
def interpret_interview_sentiment(sentence, sentiment_df):

    df = pd.read_csv(sentence)
    sentiment_df = pd.read_csv(sentiment_df, delimiter='\t', header=None)
    sentiment_df.columns = ['words', 'sentiment_score']

    positive_score, negative_score, neutral_count, result = get_sentiment_scores(sentence, sentiment_df)

    total_score = positive_score + negative_score


    if result == '긍정':
        if positive_score >= 15:  # 긍정 감정이 강하게 나타날 때
            return "매우 긍정적인 답변이네요! 지원자의 자신감과 열정이 느껴집니다.\n훌륭한 긍정적인 에너지가 느껴집니다. 이런 자세는 팀에 긍정적인 영향을 미칠 것 같습니다."
        elif positive_score >= 7:  # 긍정 감정이 나타날 때
            return "긍정적인 측면이 있지만 좀 더 구체적인 예시가 있다면 더 좋겠네요.\n답변에 긍정적인 부분이 있지만 더 자세한 내용을 추가하면 더 강력해질 것 같습니다."
        else:  # 중립 감정
            return "좀 더 긍정적인 요소를 강조해보면 좋을 것 같습니다. 경험이나 성과 등을 강조해보세요."
    elif result == '부정':
        if negative_score >= 15:  # 부정 감정이 강하게 나타날 때
            return "답변에 부정적인 표현이 많이 느껴집니다. 개선의 여지가 있을 것 같습니다.\n부정적인 감정이 강하게 전달되는데, 이를 어떻게 극복할지 고민해보세요."
        elif negative_score >= 7:  # 부정 감정이 나타날 때
            return "일부 부정적인 표현이 있지만, 긍정적인 측면도 함께 강조해보세요.\n부정적인 면이 있지만, 개선 가능한 부분이라고 생각됩니다."
        else:  # 중립 감정
            return "부정적인 표현을 최소화하고 긍정적인 측면을 강조해보세요.\n좀 더 긍정적인 언어를 사용하면 더 좋을 것 같습니다."
    else:
        if neutral_count >= 15:  # 중립 감정이 강하게 나타날 때
            return "면접 대답에 중립적인 감정이 강하게 느껴집니다. 어떤 측면에서 더 강조할 수 있을까요?\n중립적인 표현이 강조되지만, 어떤 측면에서 더 독특하게 표현할 수 있을까요?"
        elif neutral_count >= 7:  # 중립 감정이 나타날 때
            return "면접 대답이 중립적으로 전달되었습니다. 어떤 측면에서 더 강조할 수 있을까요?\n중립적인 표현이 강조되지만, 어떤 측면에서 더 독특하게 표현할 수 있을까요?"
        else:  # 중립 감정
            return "면접 대답이 중립적으로 전달되었습니다. 어떤 측면에서 더 강조할 수 있을까요?\n중립적인 표현이 강조되지만, 어떤 측면에서 더 독특하게 표현할 수 있을까요?"
