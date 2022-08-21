
# import pandas with shortcut 'pd'
import pandas as pd

# read_csv function which is used to read the required CSV file
data = pd.read_csv('coralieFollowersP.csv')

# drop function which is used in removing or deleting rows or columns from the CSV files
data.drop('pk', inplace=True, axis=1)
data.drop('full_name', inplace=True, axis=1)
data.drop('is_private', inplace=True, axis=1)
data.drop('profile_url', inplace=True, axis=1)
data.drop('profile_pic_url', inplace=True, axis=1)
data.drop('profile_pic_id', inplace=True, axis=1)
data.drop('is_verified', inplace=True, axis=1)
data.drop('follow_friction_type', inplace=True, axis=1)
data.drop('has_anonymous_profile_picture', inplace=True, axis=1)
data.drop('account_badges', inplace=True, axis=1)
data.drop('latest_reel_media', inplace=True, axis=1)
data.drop('is_favorite', inplace=True, axis=1)

data.to_csv(r'coralieFollowersPtries.csv', index=None)
