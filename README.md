# Indonesian-Abusive-and-Hate-Speech-Twitter-Text-Analysis

![image](https://user-images.githubusercontent.com/102453318/209288004-ba191a2a-ad6c-417a-a1a8-91af1715eccc.png)


Hate speech is a form of expression that is done to eliminate hatred and commit acts of violence and against a person or group of people for various reasons. Cases of hate speech are very often found on social media, one of which is on Twitter.

In a report entitled 'Digital Civility Index (DCI)' published by Microsoft in 2020, Indonesia ranks lowest in Southeast Asia for the level of decency or ranks 29th out of 32 countries surveyed. Meanwhile, according to POLRI data, from April 2020 to July 2021 there were 937 reported cases with the highest number namely provocative cases, hateful content and hatred.

Based on this, I will analyze whether the tweet contains hate speech or abusive words.


## Objectives

- How many total or comparison of tweets that contain abusive words and hate speech from all the existing tweets?
- To whom are the hate speech tweets directed?
- What topics are most frequently discussed and what is the level of hate speech in tweets?
- How to make it easier to understand the intent of a tweet?

## Conclusions

- There are 56% negative tweets with compositions 13% containing abusive words, 17% hate speech, and 25% containing both
- Majority of tweets with hate speech are directed at certain individuals with a ratio 64%
- Topics of hate speech that are often discussed are general topic (Other), followed by negative tweets on the topic of religion. Likewise, from the level of hate speech discussed by the majority on general topics and followed by religion topic (Other)
- One way to make text data such as tweets easier to understand is by processing (cleansing) it with the help of the ReGex library. Then for a group of tweets in large numbers that are combined in one data, it can be cleaned relatively quickly by creating an API (Application Program Interface) using the Flask and Swagger libraries
