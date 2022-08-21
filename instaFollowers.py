import instaloader

L = instaloader.Instaloader()

# Login or load session
username = "nico.maes.run"
password = ""
L.login(username, password)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

# Print list of followers
follow_list = []
count = 0
for follower in profile.get_followees():
    follow_list.append(follower.username)
    file = open("following.txt", "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    count = count + 1
# (likewise with profile.get_followers())
