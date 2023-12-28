
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

# 시선차트
def stare_chart():
    # 데이터 분석 및 차트 생성 코드
    stare = pd.read_csv('C:/Users/user/Downloads/Final_Project/stare_data.csv')
    stare['Timestamp'] = pd.to_datetime(stare['Timestamp'])
    stare1 = stare.groupby(['Timestamp', 'Predicted_Emotion']).size().unstack(fill_value=0)
    stare1.reset_index(inplace=True)
    stare1['second'] = stare1.index + 1

    # 그래프 생성
    fig = go.Figure()

    # 'Stare O'의 선 그래프 추가
    fig.add_trace(go.Scatter(x=stare1['second'], y=stare1['Stare O'], mode='lines', name='Stare O'))

    # 'Stare X'의 선 그래프 추가
    fig.add_trace(go.Scatter(x=stare1['second'], y=stare1['Stare X'], mode='lines', name='Stare X'))

    # 레이아웃 설정
    fig.update_layout(
        #title='Stare over Time',
        xaxis=dict(
            title='Seconds',  # x축의 타이틀을 'Seconds'로 변경
            showgrid=True,
            tickangle=45,
            tickvals=stare1['second'],  # x축에 표시될 눈금의 위치 설정
            ticktext=[str(val) for val in stare1['second']]  # 눈금에 표시될 텍스트 설정
        ),
        yaxis=dict(title='Values', showgrid=True, range=[0, 12]),
        showlegend=True,
        plot_bgcolor='white',  # 배경색을 흰색으로 설정
        paper_bgcolor='white',  # 종이 배경색도 흰색으로 설정
        legend = dict(
        orientation="h",  # 범례를 수평
        yanchor="bottom",  # 범례의 y축 아래쪽
        y=-0.5,  # 범례의 y축 아래쪽
        xanchor="center",  # 범례의 x축 둠
        x=0.5  # 범례의 x축 위치
    ))

    # 애니메이션 생성
    frames = [go.Frame(data=[
        go.Scatter(x=stare1['second'][:k+1], y=stare1['Stare O'][:k+1], mode='lines', name='Stare O'),
        go.Scatter(x=stare1['second'][:k+1], y=stare1['Stare X'][:k+1], mode='lines', name='Stare X')],
        name=str(k+1)) for k in range(len(stare1))]

    # 애니메이션 설정
    fig.update(frames=frames)

    # 애니메이션 제어 버튼 추가
    fig.update_layout(
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "args": [None, {
                            "frame": {"duration": 1000, "redraw": True},  # 1초 간격으로 설정
                            "fromcurrent": True,
                            "transition": {"duration": 1500}  # 부드러운 전환을 위한 설정
                        }],
                        "label": "Play",  # 재생 버튼
                        "method": "animate"
                    },
                    {
                        "args": [[None], {
                            "frame": {"duration": 0, "redraw": False},
                            "mode": "immediate"
                        }],
                        "label": "Pause",  # 일시정지 버튼
                        "method": "animate"
                    }
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 90},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }
        ]
    )

    return fig


# 시선결과
def analyze_stare_data():
    # 파일 경로를 문자열 변수로 지정
    file_path = 'C:/Users/user/Downloads/Final_Project/stare_data.csv'

    # 데이터 불러오기 및 타임스탬프 변환
    stare = pd.read_csv(file_path)
    stare['Timestamp'] = pd.to_datetime(stare['Timestamp'])

    # 'Predicted_Emotion' 컬럼을 이용하여 'Stare O'와 'Stare X'의 횟수를 계산
    stare_res = stare.pivot_table(index='Timestamp', columns='Predicted_Emotion', aggfunc='size', fill_value=0)
    stare_res['Time_Diff'] = stare_res.index.to_series().diff().dt.total_seconds().fillna(0)

    # 'Stare O'와 'Stare X'의 총합 계산
    total_stare_o = stare_res['Stare O'].sum()
    total_stare_x = stare_res['Stare X'].sum()
    total = total_stare_o + total_stare_x

    # 'Stare O'의 비율 계산
    stare_o_ratio = total_stare_o / total * 100

    # 결과 문자열 생성
    result = ""
    if stare_o_ratio >= 90:
        result += "시선 처리가 매우 좋습니다.<br>"
    elif stare_o_ratio >= 80:
        result += "시선 처리가 양호합니다.<br>"
    elif stare_o_ratio >= 70:
        result += "시선 처리에 주의가 필요합니다.\<br>"
    else:
        result += "시선 처리가 불충분합니다.<br>"

    # 집중력 관련 결과
    attention_periods = []
    distraction_periods = []
    current_duration = 0

    for index, row in stare_res.iterrows():
        if row['Stare X'] > row['Stare O']:
            if current_duration == 0:
                start_time = index
            current_duration += row['Time_Diff']
            if current_duration >= 3 and current_duration < 5:
                attention_periods.append(start_time)
            if current_duration >= 5:
                distraction_periods.append(start_time)
        else:
            current_duration = 0

    # 집중력 결과 추가
    #result += "\n집중력 분석 결과:\n"
    if attention_periods:
        result += f"집중력 주의구간(3초이상응시X): {len(attention_periods)}번<br>"
    else:
        result += "집중력 주의구간이 발견되지 않았습니다.<br>"

    if distraction_periods:
        result += f"집중력 부족구간(5초이상응시X): {len(distraction_periods)}번\n"
    else:
        result += "집중력이 뛰어납니다.<br>"

    return result
