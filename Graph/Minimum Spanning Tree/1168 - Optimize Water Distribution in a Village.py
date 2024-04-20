# submitted on coding ninja

# logic: just we have to connect all the village with water.
# for this there are two ways: 1) either buliding wells at the village or 2) connecting by pipes through already connected village.

# since we have to connect all village with minimum cost then minimum spanning tree should come into mind.

# how to do?
# Ans: First we have to build well at any of the village then only we can connect other villages through it 
# otherwise we will build the wells at other villages also.

# Note: We don't know digging well at which village will give optimal ans, we can get starting from any village.
# so put cost of all building wells at all villages into heap and then after that totally same as mst.

import collections
import heapq

def supplyWater(n, k, wells, pipes):
	adj= collections.defaultdict(list)
	for s,d,c in pipes:
		adj[s].append((d, c))
		adj[d].append((s, c))
	minHeap= []
	for i in range(n):
		heapq.heappush(minHeap, (wells[i], i+1))
	visited= set()
	minCost= 0
	while minHeap:
		w1, n1= heapq.heappop(minHeap)
		if n1 in visited:
			continue
		visited.add(n1)
		minCost += w1
		if len(visited)== n:
			return minCost
		for n2,w2 in adj[n1]:
			if n2 not in visited:
				heapq.heappush(minHeap, (w2, n2))
	
