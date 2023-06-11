import pandas as pd

def get_clean_data():
    data = pd.read_csv("/home/pradejner/workspace/hd-diagnosis/data/heart.csv")
    print(data.info())
    return data

def main():
    data = get_clean_data()


if __name__ == '__main__':
    main()