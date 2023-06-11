import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def get_clean_data():
    data = pd.read_csv("/home/pradejner/workspace/hd-diagnosis/data/heart.csv")
    # print(data.info())
    return data

def create_model(data):
    x = data.drop(['target'], axis=1)
    y = data['target']
    
    # scale the data
    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    # split data into training set and testing set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=88)

    # train
    model = LogisticRegression()
    model.fit(x_train, y_train)

    return model, scaler

# def test_model(model):

def main():
    data = get_clean_data()
    model, scaler = create_model(data)
    # test_model(model)


if __name__ == '__main__':
    main()