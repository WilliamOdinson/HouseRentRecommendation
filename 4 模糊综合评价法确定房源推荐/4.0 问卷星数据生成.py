import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(9)

# Number of responses
num_responses = 182

# Survey data simulation

num_responses = 182

data = {
    '性别': np.random.choice(['男', '女'], num_responses, p=[0.55, 0.45]),
    '考研租房意向': np.random.choice(['完全没意向', '有意向', '在考虑'], num_responses, p=[0.1, 0.6, 0.3]),
    '第几次考研': np.random.choice(['1', '2', '2次以上'], num_responses, p=[0.5, 0.4, 0.1]),
    '租房倾向': '整租',
    '与学校距离': np.random.choice(range(3, 6), num_responses, p=[0.2, 0.3, 0.5]),
    '交通便利程度': np.random.choice(range(3, 6), num_responses, p=[0.02, 0.1, 0.88]),
    '附近商场': np.random.choice(range(1, 3), num_responses, p=[0.12, 0.88]),
    '附近医院': np.random.choice(range(1, 6), num_responses, p=[0.01, 0.01, 0.12, 0.3, 0.56]),
    '附近便利店': np.random.choice(range(1, 6), num_responses, p=[0.01, 0.01, 0.12, 0.13, 0.73]),
    '是否旁边需要地铁': np.random.choice(range(2, 6), num_responses, p=[0.05, 0.15, 0.25, 0.55]),
    '是否旁边需要公交车': np.random.choice(range(1, 4), num_responses, p=[0.15, 0.13, 0.72]),
    '周围环境安静程度': np.random.choice(range(4, 6), num_responses, p=[0.1, 0.9]),
    '户型重视度': np.random.choice(range(1, 4), num_responses, p=[0.1, 0.13, 0.77]),
    '所处楼层重视度': np.random.choice(range(1, 4), num_responses, p=[0.5, 0.3, 0.2]),
    '房间面积重视度': np.random.choice(range(2, 5), num_responses, p=[0.2, 0.3, 0.5]),
    '房间朝向重视度': np.random.choice(range(2, 5), num_responses, p=[0.01, 0.03, 0.96]),
    '房屋装修重视度': np.random.choice(range(3, 6), num_responses, p=[0.1, 0.2, 0.7]),
    '空调是否必要': np.random.choice(range(2, 6), num_responses, p=[0.01, 0.04, 0.15, 0.8]),
    '热水器是否必要': np.random.choice(range(1, 6), num_responses, p=[0.01, 0.04, 0.15, 0.23, 0.57]),
    '暖气是否必要': np.random.choice(range(1, 6), num_responses, p=[0.01, 0.04, 0.05, 0.13, 0.77]),
    '床是否必要': np.random.choice(range(1, 6), num_responses, p=[0.01, 0.04, 0.05, 0.13, 0.77]),
    '网络是否必要': np.random.choice(range(1, 6), num_responses, p=[0.01, 0.04, 0.15, 0.2, 0.6]),
    '租金价格重视度': np.random.choice(range(1, 6), num_responses, p=[0.01, 0.04, 0.25, 0.4, 0.3]),
    '押金价格重视度': np.random.choice(range(1, 6), num_responses, p=[0.01, 0.04, 0.25, 0.4, 0.3]),
    '房源真实程度重视度': np.random.choice(range(1, 6), num_responses, p=[0.01, 0.04, 0.25, 0.4, 0.3]),
    '预计租房时长': np.random.choice(['3个月以内', '3～6个月', '6～12个月', '一年及以上'], num_responses, p=[0.1, 0.3, 0.4, 0.2]),
    '租房预算': np.random.choice(['500以下', '500～1000', '1000～1500', '1500～2000', '2000～3000', '3000～5000', '5000以上'], num_responses, p=[0.01, 0.08, 0.8, 0.08, 0.01, 0.01, 0.01]),
}

# Create DataFrame
survey_survey = pd.DataFrame(data)

csv_file = './input/survey_data1.csv'
survey_survey.to_csv(csv_file, index=False, encoding='utf-8')
