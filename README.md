# Tweely
![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/tweely?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/tweely)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/tweely)
![Twitter](https://img.shields.io/twitter/follow/rly0nheart?&style=flat&logo=twitter)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/tweely/badge)

![Twitter URL](https://img.shields.io/twitter/url?color=grey&label=Twitter%20Developer%20Account&logo=twitter&style=flat&url=https%3A%2F%2Fdeveloper.twitter.com%2F)

*Tweely is a multi-function twitter bot written in python3*. 


# Features
**PROFILE👤**
* View Your Info
* View Your Timeline
* Update Bio
* Update Name
* Update Location
* Update Profile Photo
* Update Cover Photo

**TWEET OPTIONS🐦**
* Compose Tweet
* Compose Tweet With Attachment
* Retweet
* Unretweet
* Delete Tweet
* Like Tweet(s) 
* Unlike Tweet(s)
* Like All (top recent tweets) 
* Unlike All (top recent tweets) 

**FOLLOWING👣**
* Follow User(s)
* Unfollow User(s)

**MESSAGING✉️**
* Send Direct Message
* Delete Message(s) 
* Sent Message(s) 

**BLOCKING🚫**
* Block User(s) 
* Unblock User(s) 
* Blocked User(s)

**SEARCHING🔎**
* Search Twitter
* Search User(s)

**TRENDING🔥**
* Trending Topics (by place)

**STREAMING👀**
* Stream tweets

**OTHER TOOLS🛠️**
* Fetch User Info








# What You Will Need

* **Consumer API Key** (aka API key)

* **Secret API Key**

* **Access Key**

* **Secret Access Token**

>**Note**:
*You will have to apply for a twitter developer account to get the above credentials*.

You can apply for one [here](https://developer.twitter.com)

# Twitter Developer Account
A Twitter developer account gives access to the Twitter API. This opens up application layer and transport layer endpoints to perform various tasks such as tweeting, favoriting, retweeting, liking, direct messaging, and even more complex tasks like finding what is trending.

# Applying For A Developer Account

* Using a browser, Sign-in  to twitter with your existing account(If you don't have a twitter account, then you should create one).

* Now visit https://developer.twitter.com/ and apply for a developer account.

>**Note**:
*You will be asked to explain what your intentions are for wanting to use the api, you will have to share your real intentions and apply*.





* Once you have successfully applied for a developer account, it might take a while for your account to be approved (mine got approved immediately) if yours takes longer, you will need to be a little bit patient🙂.

* Once your developer account gets approved, you will need to configure your authentication details.



* Now navigate to the '**Apps**' option from the top menu bar and then click '**Create An App**'. Provide the details of your app and then click '**Create**'. 

* Once done, go to '**Permissions**' and see whether your new app has both reading as well as writing permissions. If it doesn't, you can edit it, and give permission for both reading and writing. as for full functionality Tweely will need all permissions.

* Lastly, navigate to '**Key and Tokens**' and generate your credentials, you should copy the generated

'**consumer key**'

'**consumer secret**' 

'**access token**'

'**access token secret**'

you will paste the keys in the **credentials.py** file (in their specified variables)

# Installation

**Clone the Tweely repo**:

> git clone https://github.com/rlyonheart/tweely

> cd tweely

> pip3 install -r REQUIREMENTS

# Usage
**Run**:

> python tweely
![Screenshot_20210622-030709](https://user-images.githubusercontent.com/74001397/122847033-5e953280-d307-11eb-9443-e0d2f78d8e90.jpg)


Alternatively you can give Tweely execution rights with **chmod +x tweely**



**Then run**:

> ./tweely
![Screenshot_20210622-030635](https://user-images.githubusercontent.com/74001397/122847051-6b198b00-d307-11eb-9bda-9e4b299fad75.jpg)


# Update
> New release (v1.5) has got the following new features;

**Change log:**
* Added *'Stream tweets'* option















