#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error

#path to the csv files
PATH = 'data/'

train_filename = os.path.join(PATH, 'train.csv')
test_filename = os.path.join(PATH, 'test.csv')
turns_filename = os.path.join(PATH, 'turns.csv')
game_filename = os.path.join(PATH, 'games.csv')

#read the csv files
train_df = pd.read_csv(train_filename)
test_df = pd.read_csv(test_filename)
turns_df = pd.read_csv(turns_filename)
game_df = pd.read_csv(game_filename)

# print the head of every csv file
# print(f'Train data:\n{train_df.head()}')
# print(f'Test data:\n{test_df.head()}')
# print(f'Turns data:\n{turns_df.head()}')
# print(f'Game data:\n{game_df.head()}')

#selecting features
concat_df = pd.concat([train_df, test_df], axis=0)
concat_df = concat_df.sort_values(['game_id'])
bots = ['BetterBot', 'STEEBot', 'HastyBot']

user_df = concat_df[~concat_df['nickname'].isin(bots)]
user_df = user_df.rename(columns={
      'nickname': 'username', 
      'score': 'user_score',
      'rating': 'user_rating',
})

bot_df = concat_df[concat_df['nickname'].isin(bots)]
bot_df = bot_df.rename(columns={
      'nickname': 'bot',
      'score': 'bot_score',
      'rating': 'bot_rating'
})

main_df = pd.merge(user_df, bot_df, on='game_id')
print(main_df.head())

main_df['user_freq'] = main_df.groupby('username')['username'].transform('count')
encode_bots          = LabelEncoder()
main_df['bot']  = encode_bots.fit_transform(main_df['bot'])
main_df.head()

#split data
train_df = main_df[~main_df['user_rating'].isna()].reset_index(drop=True)
# print(X.head())

test_df = main_df[main_df['user_rating'].isna()].reset_index(drop=True)
# print(y.head())

x = train_df.drop(['username', 'user_rating'], axis = 1)
y = train_df['user_rating'].copy()

#split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)

#predict
y_pred = model.predict(x_test)
print(y_pred)

MSE  = mean_squared_error(y_pred, y_test)
RMSE = np.sqrt(MSE)
print(f'RMSE: {RMSE}')

#save results in csv file
model = LinearRegression()
model.fit(x, y)
test_df['user_rating'] = model.predict(test_df.drop(['username', 'user_rating'], axis = 1))
sub = test_df[['game_id', 'user_rating']]
sub = sub.rename(columns={'user_rating': 'rating'})
sub.to_csv('submission.csv', index=False)
