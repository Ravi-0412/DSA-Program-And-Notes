# first  main tasks to identify the data structure for each function with minimal time complexity.

# 1) for 'follow' and 'unfollow' 
# we can make a hashmap wrt each user and store all the people whom the user follow in a list
# but in case if he unfollows then we will have to remove that user from the list of 'following person' and list will take O(n)
# so list will not work .
# then only think come into mind that can do the adding and removing thing in O(1) is set
# so hashset will work fine for this case

# Note: always remember when you have to add or delete(not from a fixed position) then 'set' should come into mind.

# 2) postTweet: we can take a hashmap and store the tweets done by user in a list, 
# the most recent tweets done by user will be at the end of the list.
# But to get the most recent feed we have to store the tweet done by a user with time also.
# Since we can use only minHeap so we will reduce the time each time by '1' instead of increment.

# 3)getNewsFeed:
# wo user jisko bhi follow kar rha, unlog ka 1o most recent tweet chahiye.
# for getting the most recent 10 tweets, we have to find the 10 most recent 
# from all the lists of tweets done by person whom user follow.
# Before adding into MinHeap, most recent tweet will be at last only.

# Vvi: Now the problem reduces to "merge k sorted array" for 'getNewsFeed'.
# Most recent tweet will be at the top for any person because we are storing in minHeap.

# Why using minHeap: Just to avoid adding '-ve' value in case of maxHeap. can do by maxHeap also.

# just compare the last tweet time of each person they follow
# and most efficient way to do this is add all the recent tweet done by all the person they follow into a minHeap.
# After that pop from minHeap to get the most recent one add that to the ans.

# for getNewsfeed ,time: O(10*logk)   # k : no of person a user is following, 10 times we have to heapify.
# And for remaining operation time: O(1).

import heapq
from collections import defaultdict
class Twitter:   
    def __init__(self):
        self.time= 0  # to keep track of timing of previous tweet.
        self.tweetMap=  defaultdict(list)  # contain the [time, tweetid] for each user
        self.followMap= defaultdict(set)   # contain the list of person a user is following. {user: person user follows}.
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1 # less time means most recent tweet, decr by '1' since in python only we can make minHeap
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res= []
        minHeap= []
        self.followMap[userId].add(userId)  # as we have to show tweets made by himself also.

        # get the last tweet done by each person user is following
        for followeeId in self.followMap[userId]:  # every person the user follows
            if followeeId in self.tweetMap: # if the person following has made atleast one tweet
                index= len(self.tweetMap[followeeId]) -1  # this will contain lastest tweet with time, latest tweet will be at the last
                time, tweetId= self.tweetMap[followeeId][index]      # getting the lastest tweet
                minHeap.append((time, tweetId, followeeId, index-1))  
                # heapq.heappush(minHeap,(time, tweetId, followeeId, index-1))
        
                # why 4 parameter. time: this will work as key to get the latest tweet. 
                # just same as 'merge k sorted array' i.e all varibles needed to get next most recent tweet.
                # Only one extra parameter here i.e 'time' to get the latest tweet.
                # tweetId: we have to add in the ans, followeeId: to get the next tweet done by this person
                # next tweet done by this person(followeeId) will be at 'index-1'
    
        # just same operation as 'merge k sorted array".    
        heapq.heapify(minHeap)  # to get the latest tweet
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index= heapq.heappop(minHeap)
            res.append(tweetId)  # most recent tweet will get added first
            if index >= 0: # means the followeeId has at least one more tweet left and that can be posted recnetly only.
                time, tweetId= self.tweetMap[followeeId][index]      # getting the lastest tweet
                heapq.heappush(minHeap, (time, tweetId, followeeId, index-1))
        return res
                
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Java
"""
import java.util.*;

class Twitter {
    private int time;
    private Map<Integer, List<int[]>> tweetMap; // userId -> list of tweets [time, tweetId]
    private Map<Integer, Set<Integer>> followMap; // followerId -> set of followeeIds

    /** Initialize your data structure here. */
    public Twitter() {
        time = 0;
        tweetMap = new HashMap<>();
        followMap = new HashMap<>();
    }
    
    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        tweetMap.putIfAbsent(userId, new ArrayList<>());
        tweetMap.get(userId).add(new int[]{time, tweetId});
        time ++;
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> res = new ArrayList<>();
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]); // max heap based on time
        
        followMap.putIfAbsent(userId, new HashSet<>());
        followMap.get(userId).add(userId); // include user's own tweets
        
        for (int followeeId : followMap.get(userId)) {
            if (tweetMap.containsKey(followeeId)) {
                List<int[]> tweets = tweetMap.get(followeeId);
                int index = tweets.size() - 1;
                if (index >= 0) {
                    int[] tweet = tweets.get(index);
                    minHeap.offer(new int[]{tweet[0], tweet[1], followeeId, index - 1});
                }
            }
        }
        
        while (!minHeap.isEmpty() && res.size() < 10) {
            int[] tweet = minHeap.poll();
            res.add(tweet[1]);
            int followeeId = tweet[2];
            int index = tweet[3];
            if (index >= 0) {
                int[] nextTweet = tweetMap.get(followeeId).get(index);
                minHeap.offer(new int[]{nextTweet[0], nextTweet[1], followeeId, index - 1});
            }
        }
        
        return res;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
        followMap.putIfAbsent(followerId, new HashSet<>());
        followMap.get(followerId).add(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
        followMap.putIfAbsent(followerId, new HashSet<>());
        followMap.get(followerId).remove(followeeId);
    }
}
"""
