# just similar to LIS only.
# logic: Har dimension bda hona chahiye and sbko rotate bhi kar sakte h like agar kisi ka width lete h then other ka uske uper length or height bhi rakh ke try kar sakte h
# agar wo fit baith jaye kisi bhi tarah se tb.
# isliye hmko har ek internal cube ko bhi sort karna hoga taki rotation wala condition automaticaly handle ho jaye.

# internally sort karne ke bad pure cuboid ko sort kar rhe taki smallest dimension (either width, length or height) phle aa jaye and max dimension(either width, length or height) wala piche chla jaye.
# isse hmko easily pta chal jayega ki kisko hm include kar sakte h and kisko nhi.


# traversing from right to left be more logical.
# it is just like we are trying to put smaller one above larger one since larger one will be on right side only.
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # first sorting all the internal cubes
        for cube in cuboids:
            cube.sort()
        cuboids.sort()
        # we are just doing opposite
        LIS= [cube[2] for cube in cuboids]  # every cube will contribute equal to its height.
        # 'LIS[i]' is denote the height when last added cuboid is 'i' from the last.
        for i in range(len(cuboids)-1, -1, -1):
            for j in range(i +1, len(cuboids)):
                if cuboids[i][0] <= cuboids[j][0] and cuboids[i][1] <= cuboids[j][1] and cuboids[i][2] <= cuboids[j][2]:
                # if all(cuboids[j][k] <= cuboids[i][k] for k in range(3)):   # we can also write like this.
                    LIS[i] = max(LIS[i], LIS[j] + cuboids[i][2])   # we are adding 'i'th cuboid so add its height with LIS[j] (instead of LIS[j] + 1 in case of LIS)
        return max(LIS)     
    
# from left to right.
# here we are placing larger one above smaller one but we will get the correct ans only.
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # first sorting all the internal cubes
        for cube in cuboids:
            cube.sort()
        cuboids.sort()
        LIS= [cube[2] for cube in cuboids]  # every cube will contribute equal to its height.
        for i in range(len(cuboids)):
            for j in range(i):
                if cuboids[j][0] <= cuboids[i][0] and cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                    LIS[i] = max(LIS[i], LIS[j] + cuboids[i][2])
        return max(LIS)