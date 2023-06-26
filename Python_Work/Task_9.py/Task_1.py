import pandas as pd
hw9 = pd.read_csv('sample_data/california_housing_train.csv')
hw9['median_house_value'][(hw9['population'] >= 0) &
                          (hw9['population'] <= 500)].mean()
hw9['median_house_value'][(hw9['population'] >= 0) &
                          (hw9['population'] <= 500)].describe()
hw9[hw9['population'] == hw9['population'].min()]['households'].max()
hw9[hw9['population'] == hw9['population'].min()]


# Что то напутал походу малость непонял колаборатори
