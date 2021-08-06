import datetime

# importing all colors from colors.py
from assets.colors import red,white,brightred,yellow,end


now = datetime.datetime.now()
today = now.strftime("%A, %d %B %Y")
# banners will be used for each option in tweely
def mainBanner():
	print("""
░▀█▀░█░█░█▀▀░█▀▀░█░░░█░█
░░█░░█▄█░█▀▀░█▀▀░█░░░░█░
░░▀░░▀░▀░▀▀▀░▀▀▀░▀▀▀░░▀░%s
https://github.com/rlyonheart
[%s Twitter Bot %s] %s%s

%s𝐏𝐑𝐎𝐅𝐈𝐋𝐄👤___________________________
1%s. My Info
%s2%s. My Timeline
%s3%s. Update Bio
%s4%s. Update Name
%s5%s. Update Location
%s6%s. Update Profile Photo
%s7%s. Update Cover Photo

%s𝐓𝐖𝐄𝐄𝐓 𝐎𝐏𝐓𝐈𝐎𝐍𝐒🐦___________________
8%s. Compose Tweet
%s9%s. Compose Tweet (with attachment)
%s10%s. Retweet
%s11%s. Unretweet
%s12%s. Delete Tweet
%s13%s. Like Tweet(s)
%s14%s. Unlike Tweet(s)
%s15%s. Like All (top recent tweets)
%s16%s. Unlike All (top recent tweets)

%s𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆👣___________________
17%s. Follow User(s)
%s18%s. Unfollow User(s)

%s𝐌𝐄𝐒𝐒𝐀𝐆𝐈𝐍𝐆✉️___________________
19%s. Send Direct Message
%s20%s. Delete Message(s)
%s21%s. Sent Message(s)

%s𝐁𝐋𝐎𝐂𝐊𝐈𝐍𝐆🚫_____________________
22%s. Block User(s)
%s23%s. Unblock User(s)
%s24%s. Blocked User(s)

%s𝐒𝐄𝐀𝐑𝐂𝐇𝐈𝐍𝐆🔎️___________________
25%s. Search Twitter
%s26%s. Search User(s)

%s𝐓𝐑𝐄𝐍𝐃𝐈𝐍𝐆🔥_____________________
27%s. Trending Topics (by place)

%s𝐒𝐓𝐑𝐄𝐀𝐌𝐈𝐍𝐆👀___________________
28%s. Stream Tweets

%s𝐎𝐓𝐇𝐄𝐑 𝐓𝐎𝐎𝐋𝐒🛠️_________________
29%s. Fetch User Info

%s99%s. %sAbout%s
%s00%s. %sQuit%s
 """ % (white,red,white,today,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,yellow,end,white,end,brightred,end))

def composeBanner():
	print("""
░█▀▀░█▀█░█▄█░█▀█░█▀█░█▀▀░█▀▀
░█░░░█░█░█░█░█▀▀░█░█░▀▀█░█▀▀
░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀%s
[%s Compose A Tweet %s] - Tweely
%s""" % (white,red,white,end))

def followBanner():
	print("""
░█▀▀░█▀█░█░░░█░░░█▀█░█░█
░█▀▀░█░█░█░░░█░░░█░█░█▄█
░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀%s
[%s Follow User(s)%s ] - Tweely
%s""" % (white,red,white,end))

def unfollowBanner():
	print("""
░█░█░█▀█░█▀▀░█▀█░█░░░█░░░█▀█░█░█
░█░█░█░█░█▀▀░█░█░█░░░█░░░█░█░█▄█
░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀%s
[%s Unfollow User(s) %s] - Tweely
%s""" % (white,red,white,end))

def likeTweetBanner():
	print("""
░█░░░▀█▀░█░█░█▀▀
░█░░░░█░░█▀▄░█▀▀
░▀▀▀░▀▀▀░▀░▀░▀▀▀%s
[%s Like Tweet(s)%s ] - Tweely
%s""" % (white,red,white,end))

def unlikeTweetBanner():
    print("""
░█░█░█▀█░█░░░▀█▀░█░█░█▀▀
░█░█░█░█░█░░░░█░░█▀▄░█▀▀
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀%s
[%s Unlike Tweet(s)%s ] - Tweely
%s""" % (white,red,white,end))

def likeRecentBanner():
    print("""
░█▀▄░█▀▀░█▀▀░█▀▀░█▀█░▀█▀
░█▀▄░█▀▀░█░░░█▀▀░█░█░░█░
░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░%s
[%s Like (all) Top Recent Tweets %s] - Tweely
%s""" % (white,red,white,end))

def unlikeRecentBanner():
    print("""
░█▀▄░█▀▀░█▀▀░█▀▀░█▀█░▀█▀
░█▀▄░█▀▀░█░░░█▀▀░█░█░░█░
░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░%s
[%s Unlike (all) Top Recent Tweets%s ] - Tweely
%s""" % (white,red,white,end))

def userInfoBanner():
	print("""
░█░█░█▀▀░█▀▀░█▀▄░░░▀█▀░█▀█░█▀▀░█▀█
░█░█░▀▀█░█▀▀░█▀▄░░░░█░░█░█░█▀▀░█░█
░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀▀▀░▀░▀░▀░░░▀▀▀%s
[%s Get Public User(s) Info%s ] - Tweely
%s""" % (white,red,white,end))

def updateBioBanner():
	print("""
░█▀▄░▀█▀░█▀█
░█▀▄░░█░░█░█
░▀▀░░▀▀▀░▀▀▀%s
[%s Update Authenticated User Bio%s ] - Tweely
%s""" % (white,red,white,end))

def updateNameBanner():
	print("""
░█▀█░█▀█░█▄█░█▀▀
░█░█░█▀█░█░█░█▀▀
░▀░▀░▀░▀░▀░▀░▀▀▀%s
[%s Update Authenticated User Screen Name%s ] - Tweely
%s""" %s (white,red,white,end))

def updateLocationBanner():
	print("""
░█░░░█▀█░█▀▀░█▀█░▀█▀░▀█▀░█▀█░█▀█
░█░░░█░█░█░░░█▀█░░█░░░█░░█░█░█░█
░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░▀░▀%s
[%s Update Authenticated User Location%s ] - Tweely
%s""" % (white,red,white,end))

def searchUserBanner():
	print("""
░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░█░█
░▀▀█░█▀▀░█▀█░█▀▄░█░░░█▀█
░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀%s
[%s Search Username%s ] - Tweely
%s""" % (white,red,white,end))

def searchTwitterBanner():
	print("""
░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░█░█
░▀▀█░█▀▀░█▀█░█▀▄░█░░░█▀█
░▀▀▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀%s
[%s Try  searching for people, topics or keywords%s ] - Tweely
%s""" % (white,red,white,end))


def myInfoBanner():
	print("""
░█▄█░█░█░░░▀█▀░█▀█░█▀▀░█▀█
░█░█░░█░░░░░█░░█░█░█▀▀░█░█
░▀░▀░░▀░░░░▀▀▀░▀░▀░▀░░░▀▀▀%s
[%s Authenticated User Info%s ] - Tweely
%s""" % (white,red,white,end))

def viewTimelineBanner():
	print("""
░▀█▀░▀█▀░█▄█░█▀▀░█░░░▀█▀░█▀█░█▀▀
░░█░░░█░░█░█░█▀▀░█░░░░█░░█░█░█▀▀
░░▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀%s
[%s Authenticated User Timeline%s ] - Tweely
%s""" % (white,red,white,end))

def sendMessageBanner():
	print("""
░█▀▄░▀█▀░█▀▄░█▀▀░█▀▀░▀█▀
░█░█░░█░░█▀▄░█▀▀░█░░░░█░
░▀▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀░░▀░%s
[%s Send Direct Message%s ] - Tweely
%s""" % (white,red,white,end))

def viewMessageBanner():
	print("""
░█▀▀░█▀▀░█▀█░▀█▀
░▀▀█░█▀▀░█░█░░█░
░▀▀▀░▀▀▀░▀░▀░░▀░%s
[%s Sent Message(s)%s ] - Tweely
%s""" % (white,red,white,end))

def deleteMessageBanner():
    print("""
░█▀▄░█▀▀░█░░░█▀▀░▀█▀░█▀▀
░█░█░█▀▀░█░░░█▀▀░░█░░█▀▀
░▀▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀%s
[%s Delete Message(s)%s ] - Tweely
%s""" % (white,red,white,end))

def trendingTopicsBanner():
	print("""
░▀█▀░█▀▄░█▀▀░█▀█░█▀▄░▀█▀░█▀█░█▀▀
░░█░░█▀▄░█▀▀░█░█░█░█░░█░░█░█░█░█
░░▀░░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀%s
[%s Trending Topics By Place%s ] - Tweely
%s""" % (white,red,white,end))


def updateProfilePicBanner():
	print("""
░█▀█░█▀▄░█▀█░█▀▀░▀█▀░█░░░█▀▀░░░█▀█░▀█▀░█▀▀
░█▀▀░█▀▄░█░█░█▀▀░░█░░█░░░█▀▀░░░█▀▀░░█░░█░░
░▀░░░▀░▀░▀▀▀░▀░░░▀▀▀░▀▀▀░▀▀▀░░░▀░░░▀▀▀░▀▀▀%s
[%s Update Authenticated User Profile Picture%s ] - Tweely
%s""" % (white,red,white,end))

def updateCoverPhotoBanner():
    print("""
░█▀▀░█▀█░█░█░█▀▀░█▀▄
░█░░░█░█░▀▄▀░█▀▀░█▀▄
░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀%s
[%s Update Authenticated User Cover Photo%s ] - Tweely
%s""" % (white,red,white,end))

def retweetBanner():
	print("""
░█▀▄░█▀▀░▀█▀░█░█░█▀▀░█▀▀░▀█▀
░█▀▄░█▀▀░░█░░█▄█░█▀▀░█▀▀░░█░
░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░░▀░%s
[%s Retweet%s ] - Tweely
%s""" % (white,red,white,end))

def unRetweetBanner():
    print("""
░█░█░█▀█░█▀▄░█▀▀░▀█▀░█░█░█▀▀░█▀▀░▀█▀
░█░█░█░█░█▀▄░█▀▀░░█░░█▄█░█▀▀░█▀▀░░█░
░▀▀▀░▀░▀░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░░▀░%s
[%s Unretweet%s ] - Tweely
%s""" % (white,red,white,end))

def viewFollowersBanner():
    print("""
░█▀▀░█▀█░█░░░█░░░█▀█░█░█░█▀▀░█▀▄░█▀▀
░█▀▀░█░█░█░░░█░░░█░█░█▄█░█▀▀░█▀▄░▀▀█
░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀%s
[%s User(s) Followers%s ] - Tweely
%s""" % (white,red,white,end))

def deleteTweetBanner():
    print("""
░█▀▄░█▀▀░█░░░█▀▀░▀█▀░█▀▀
░█░█░█▀▀░█░░░█▀▀░░█░░█▀▀
░▀▀░░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀%s
[%s Delete Tweet%s ] - Tweely
%s""" % (white,red,white,end))

def blockUsersBanner():
    print("""
░█▀▄░█░░░█▀█░█▀▀░█░█
░█▀▄░█░░░█░█░█░░░█▀▄
░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀%s
[%s Block User(s)%s ] - Tweely
%s""" % (white,red,white,end))

def unblockUsersBanner():
    print("""
░█░█░█▀█░█▀▄░█░░░█▀█░█▀▀░█░█
░█░█░█░█░█▀▄░█░░░█░█░█░░░█▀▄
░▀▀▀░▀░▀░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀%s
[%s Unblock User(s)%s ] - Tweely
%s""" % (white,red,white,end))

def blockedUsersBanner():
	print("""
░█▀▄░█░░░█▀█░█▀▀░█░█░█▀▀░█▀▄
░█▀▄░█░░░█░█░█░░░█▀▄░█▀▀░█░█
░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀░%s
[%s Blocked Users%s ] - Tweely
%s""" % (white,red,white,end))

def streamingBanner():
	print("""
░█▀▀░▀█▀░█▀▄░█▀▀░█▀█░█▄█░▀█▀░█▀█░█▀▀
░▀▀█░░█░░█▀▄░█▀▀░█▀█░█░█░░█░░█░█░█░█
░▀▀▀░░▀░░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀%s
[ %sStream Twitter Data%s ] - Tweely
%s""" % (white,red,white,end))

def aboutBanner():
    print("""
░█▀█░█▀▄░█▀█░█░█░▀█▀ 
░█▀█░█▀▄░█░█░█░█░░█░ 
░▀░▀░▀▀░░▀▀▀░▀▀▀░░▀░%s
[%s About Tweely%s ]
%s
Tweely is a multi-function twitter bot written in python3.
Check the README.md file for more information.
    	
%sAUTHOR✍️________________%s
%sName(s)%s: Richard Mwewa
%sOther Name(s)%s: Ritchie
%sAlias(es)%s: rly0nheart
    	
%sSOCIAL MEDIA💬_____________________________%s
%sTwitter%s: https://twitter.com/rly0nheart
%sTelegram%s: https://t.me/rlyonheart
%sFacebook%s: https://fb.me/rly0nheart
%sInstagram%s: https://instagram.com/rlyonheart
    	
    	           %s©2021%s


""" % (white,yellow,white,end,white,end,yellow,end,yellow,end,yellow,end,white,end,yellow,end,yellow,end,yellow,end,yellow,end,red,end))

