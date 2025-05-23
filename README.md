# DS_assign3
 feature similar to 'searchNearby' used in google maps

We assume that you have used the ‘search nearby’ feature of Google maps to search for restaurants close to you. (Use it and party with your friends over the upcoming weekend.) How should Google store the locations of restaurants so that it can answer such queries fast? A na ̈ıve idea is use a list and, given a query, scan the list and return the subset of nearby restaurants. This requires time O(n) on a list of n locations. How can we speed this up in practice? Note that the list of restaurants remains fairly unchanged over time, while ‘search nearby’ queries are much more frequent. Therefore, it makes sense to pre-process the list of restaurants and create an appropriate data structure that enables processing ‘search nearby’ queries much faster than a brute-force search (assuming the number of “nearby” restaurants is much smaller than the total number of restaurants, which is typically the case).

Problem Statement
The l∞-distance between two points – p1 = (x1, y1) and p2 = (x2, y2), denoted by ∥p1 − p2∥∞, is defined as max(|x1 − x2|, |y1 − y2|). Given a list S of n data points in R2, a query point q ∈ R2, and a non-negative numberd,we wish to find the set{p∈S|∥p−q∥∞ ≤d},thesetofallpointsinSthatareatmostan l∞-distance d away from the point q. You are required to design and program an appropriate data structure, which we call PointDatabase, to store a set of data points that admits the following.
1. An algorithm which, given a list S of data points, outputs an object R(S) of PointDatabase which is a “representation” of S.
2. An algorithm which, given the object R(S) of PointDatabase, a query point q, and a distance d, outputstheset{p∈S|∥p−q∥∞ ≤d}.
More specifically, your task is to implement a Python class PointDatabase with the following methods.
• init (self, pointlist): A constructor which, given a list pointlist of pairs of numbers, creates an object of PointDatabase. This method must run in time O(nlogn), where n is the number of points in pointlist.
• searchNearby(self, q, d): An accessor method which, given a point q and distance d, returns the list of all points, in the set that self represents, that are at l∞-distance at most d from q (arranged in an arbitrary order). This method must run in time O(m + log2 n), where n is the cardinality of the set of points that self represents, and m is the number of points returned.
For simplicity, you may assume the following.
1. The coordinates of all points involved are integers (thus, avoiding floats and the resulting errors).
2. In the list pointlist from which a PointDatabase object is constructed, no two data points have the
same x-coordinate, and no two data points have the same y-coordinate.
3. No data point is at l∞-distance exactly d from the query point q.


