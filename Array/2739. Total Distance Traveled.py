# logic: After every 5 litre consumption we will add '1' more litre.

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
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return (mainTank + min((mainTank -1)//4, additionalTank)) *10
