# first we main task s to identify the data structure for each function with minimla time complexity

# 1) for 'follow' and 'unfollow' 
# we can make a hashmap wrt each user and store all the people whom the user follow in a list
# but in case if he unfollows then we will have to remove that user from the list of 'following person' and list will take O(n)
# so list will not work .
# then only think come into mind that can do the adding and removing thing in O(1) is set
# so hashset will work fine for this case

# Note: always remember when you have to add or delete(not from a fixed position) then 'set' should come into mind

# 2) postTweet: we can take a hashmap and store the tweets done by user in a list
# the most recent tweets done by user will be at the end of the list
# but to get the most recent feed we have to store the tweet done by a user with time also
# since we can use only minHeap so we will reduce the time each time by '1' instead of incr
# so tweet with minimum time will be the most recent tweets

# 3)getNewsFeed:
# wo user jisko bhi follow kar rha, unlog ka 1o most recent tweet chahiye
# tweet done by a person, we have stored in a list and tweet at last of the list will be the most recent one
# for getting the most recent 10 tweets, we haveto find the most recent from all the lists of tweets that they user follow

# for this take the last tweet done by each person they follow including themselves and take the tweet with minimum time
# now the problem reduces to merge k sorted array

# just compare the last tweet time of each person they follow
# and most efficient way to do this is add all the recent tweet done by all the person they follow into a minHeap
# after that pop from minHeap to get the most recent one add that to the ans 
# after that add the next recent tweet done by person you included intoi ans as same work might have done all the recent tweets

# time: O(10*logk)   # k : no of person a user is following
# 10 times we have to heapify 

class Twitter:   
    def __init__(self):
        self.time= 0
        self.tweetMap=  defaultdict(list)  # contain the [time, tweetid] for each user
        self.followMap= defaultdict(set)   # contain the list of person a user is following
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time-= 1 # less time means most recent tweet, decr by '1' since in python only we can make minHeap
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res= []
        minHeap= []
        self.followMap[userId].add(userId)  # as this person itself has made recent tweets
        for followeeId in self.followMap[userId]:  # every person the user follows
            if followeeId in self.tweetMap: # if the person following has made atleast one tweet
                # get the last tweet done by each person user is following
                index= len(self.tweetMap[followeeId]) -1  # this will contain lastest tweet with time, latest tweet will be at the last
                time, tweetId= self.tweetMap[followeeId][index]      # getting the lastest tweet
                minHeap.append((time, tweetId, followeeId, index-1))  
                # heapq.heappush(minHeap,(time, tweetId, followeeId, index-1))
                # why 4 parameter. time: this will work as key to get the latest tweet
                # tweetId: we have to add in the ans, followeeId: to get the next tweet done by this person
                # next tweet done by this person(followeeId) will be at 'index-1'
        
        heapq.heapify(minHeap)  # to get the latest tweet
        while minHeap and len(res)< 10:
            time, tweetId, followeeId, index= heapq.heappop(minHeap)
            res.append(tweetId)  # most recent tweet will get added first
            if index>= 0: # means the followeeId has at least one more tweet left
                time, tweetId= self.tweetMap[followeeId][index]      # getting the lastest tweet
                heapq.heappush(minHeap, (time, tweetId, followeeId, index-1))
        return res
                
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        