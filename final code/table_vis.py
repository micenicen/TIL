import os
import pandas as pd
import re
from konlpy.tag import Okt
from collections import Counter
import operator
import plotly.graph_objects as go

def process_text_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

    merged_text = ' '.join(df['Text'])
    df = pd.DataFrame({'Text': [merged_text]})
    df['Text'] = df['Text'].apply(lambda x: re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', x))

    okt = Okt()
    stop_words = ['지금', '상황', '경우', '안녕하세요', '안녕하십니까', '따라서', '지원', '우선', '일단', '얘기', '대해', '위해', '때문', '통해', '대한',
                  '생각', '또한', '으로', '이고', '로서', '에서', '에도', '하다', '입니다']
    df['Text'] = df['Text'].apply(
        lambda x: [word for word in okt.nouns(x) if word not in stop_words and len(word) >= 2])
    df['Sorted_Lemma_Frequencies'] = df['Text'].apply(
        lambda x: dict(sorted(Counter(x).items(), key=operator.itemgetter(1), reverse=True)))

    top_7_words = list(df['Sorted_Lemma_Frequencies'][0].keys())[:7]
    return top_7_words

def table_chart():
    # Base path for the files
    base_path = 'C:/Users/user/Downloads/Final_Project/'

    file_paths = ['pass_results_22.csv', 'pass_results_23.csv', 'pass_results_ex.csv']
    index_mapping = {'pass_results_22': '2022 합격자', 'pass_results_23': '2023 합격자', 'pass_results_ex': '본인'}

    # Combine the base path with file names to create full paths
    file_paths = [os.path.join(base_path, file_name) for file_name in file_paths]

    data = []

    for file_path in file_paths:
        top_words = process_text_data(file_path)
        if not top_words:
            continue
        index_value = index_mapping[os.path.basename(file_path).split('.')[0]]

        for rank, word in enumerate(top_words, 1):
            data.append((index_value, rank, word))

    if not data:
        print("No data to display.")
        return

    df = pd.DataFrame(data, columns=['File', 'Rank', 'Word'])
    pivot_df = df.pivot(index='Rank', columns='File', values='Word')

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['순위'] + pivot_df.columns.tolist(),
            fill_color='lightblue',
            align='center',
            font=dict(color='black', size=18),
            line_color='black',
            height=30
        ),
        cells=dict(
            values=[pivot_df.index] + [pivot_df[col].tolist() for col in pivot_df.columns],
            fill_color='white',
            align='center',
            font=dict(color='black', size=14),
            line_color='black',
            height=30
        )
    )])

    fig.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white'
    )

    return fig



# 분석결과

