from assets.colors import *

def mainBanner():
	print("""
░▀█▀░█░█░█▀▀░█▀▀░█░░░█░█
░░█░░█▄█░█▀▀░█▀▀░█░░░░█░
░░▀░░▀░▀░▀▀▀░▀▀▀░▀▀▀░░▀░%s
[%s Twitter Bot %s] - https://github.com/rlyonheart%s

%sPROFILE👤____________________
1%s. My Info
%s2%s. My Timeline
%s3%s. Update Bio
%s4%s. Update Name
%s5%s. Update Location
%s6%s. Update Profile Photo
%s7%s. Update Cover Photo

%sTWEET OPTIONS🐦________________________
8%s. Compose Tweet
%s9%s. Retweet
%s10%s. Compose Tweet (with attachment)
%s11%s. Delete Tweet
%s12%s. Like Tweet(s)
%s13%s. Unlike Tweet(s)
%s14%s. Like All (top recent tweets)
%s15%s. Unlike All (top recent tweets)

%sFOLLOWING👣____________
16%s. Follow User(s)
%s17%s. Unfollow User(s)

%sMESSAGING✉️________________
18%s. Send Direct Message
%s19%s. Delete Message(s)
%s20%s. Sent Message(s)

%sBLOCKING🚫_____________
21%s. Block User(s)
%s22%s. Unblock User(s)
%s23%s. Blocked User(s)

%sOTHER TOOLS🛠️_________
24%s. Search User(s)
%s25%s. Fetch User Info

%s99%s. %sAbout%s
%s00%s. %sQuit%s
 """ % (white,red,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,white,end,yellow,end,white,end,brightred,end))

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

