import plotly.graph_objects as go
import pandas as pd



def emotion_chart():
    # 데이터를 불러오고 처리
    emotion = pd.read_csv("C:/Users/user/Downloads/Final_Project/emotion_data.csv")
    emotion['Predicted_Emotion'] = emotion['Predicted_Emotion'].replace({
        "Angry": "화남",
        "Confident": "자신감",
        "Sad": "슬픔",
        "Happy": "행복",
        "Neutral": "침착",
        "Surprise": "놀람"
    })
    emotion_per = emotion['Predicted_Emotion'].value_counts(normalize=True).reset_index()
    emotion_per.columns = ['Predicted_Emotion', 'proportion']

    # 평균 비율 계산
    average_proportion = emotion_per['proportion'].mean()

    # 레이더 차트 생성
    fig = go.Figure()

    # 개별 감정 비율을 트레이스로 추가
    fig.add_trace(go.Scatterpolar(
        r=emotion_per['proportion'],
        theta=emotion_per['Predicted_Emotion'],
        fill='toself',
        name='개인'
    ))

    # 평균 비율을 다른 트레이스로 추가
    fig.add_trace(go.Scatterpolar(
        r=[average_proportion]*len(emotion_per),
        theta=emotion_per['Predicted_Emotion'],
        fill='toself',
        name='전체평균',
        opacity=0.3
    ))

    # 레이아웃 업데이트
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 0.6],
                showticklabels=False
            )
        ),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="center",
            x=0.5
        )
    )

    return fig


# 분석결과
def analyze_emotion_data():
    # 데이터 불러오기
    emotion = pd.read_csv("C:/Users/user/Downloads/Final_Project/emotion_data.csv")

    # 감정 데이터 변환
    emotion['Predicted_Emotion'] = emotion['Predicted_Emotion'].replace({
        "Angry": "화남",
        "Confident": "자신감",
        "Sad": "슬픔",
        "Happy": "행복",
        "Neutral": "침착",
        "Surprise": "놀람"
    })

    # 감정 비율 계산
    emotion_per = emotion['Predicted_Emotion'].value_counts(normalize=True)
    emotion_per = emotion_per.reset_index()

    # 가장 흔한 감정 파악
    most_common_emotion = emotion_per['Predicted_Emotion'][0]

    # 결과 문자열 생성
    result = f"{most_common_emotion} 감정이 가장 많이 나타납니다.<br>"

    if most_common_emotion == '화남':
        result += '화남 감정이 면접 결과에 부정적 영향을 미칠 수 있습니다. 면접 중 감정 조절에 주의해야 합니다.<br>'
    elif most_common_emotion == '슬픔':
        result += '슬픔 감정은 면접관에게 부정적인 인상을 줄 수 있으므로 긍정적 태도 유지가 중요합니다.<br>'
    elif most_common_emotion == '자신감':
        result += '자신감 있는 태도는 면접 결과에 긍정적인 영향을 미칩니다. 자신감을 유지하세요.<br>'
    elif most_common_emotion == '침착':
        result += '침착함은 면접관에게 긍정적인 인상을 줄 수 있습니다. 안정된 모습을 유지하세요.<br>'
    elif most_common_emotion == '행복':
        result += '행복한 감정은 긍정적인 에너지를 전달하며 면접 결과에 좋은 영향을 미칠 수 있습니다.<br>'
    elif most_common_emotion == '놀람':
        result += '놀람은 면접 중 예상치 못한 질문에 대한 반응으로 나타날 수 있습니다. 미리 준비하면 도움이 됩니다.<br>'
    else:
        result += '면접에서 감정 표현이 중요합니다. 각 상황에 맞는 적절한 감정 표현을 하세요.'

    return result
