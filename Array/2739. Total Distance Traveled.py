# logic: After every 5 litre consumption we will add '1' more litre from additional only if additional will be present.

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if mainTank <= 4:
            return mainTank * 10
        ans = 0
        while mainTank >= 5 and additionalTank > 0:
            ans += 5 * 10
            mainTank = mainTank - 5 + 1
            additionalTank -= 1
        ans += mainTank * 10
        return ans


# METHOD 2: 
# very short . Before i was thinking in somewhat this way only.

# Logic: main tank me kitna extra fuel add hoga.
# Har 5 ke bad 1 litre means agar '5' litre use kiya to actual me main tank se '4' litre hi jayeya
#  kyonki hm 1 litre add kar denge except 1st time(isliye '-1').


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return (mainTank + min((mainTank -1)//4, additionalTank)) * 10

# similar q:
# 1) 3100. Water Bottles II