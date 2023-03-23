class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        remaining_money= money- children   #After giving one to each children
        # to make maximum of '8' we need maximum multiple of '7' from remaining money
        possibleAns= remaining_money //7   # this much combination of '8' we can form.
        if possibleAns > children:  # then to one children we have to give extra dollar
            return children -1
        if possibleAns== children and remaining_money % 7 == 0:  # just same as money/children= 8 then we can simply return 'children' also.
            return possibleAns 
        if possibleAns== children and remaining_money % 7!= 0:
            return possibleAns -1
        # now we have to distribute remainder and to get max '8' we will try to give it to only remaining children other than ans if possible.
        # it's possible to give only to one people except case when remainder== 3 since it will lead total money ='4'.
        if remaining_money % 7 != 3:
            return possibleAns
        peopleWithOneDollar= children- possibleAns
        if peopleWithOneDollar >=2:   # we can distribute '3' dollar among more than one children with dollar '1'.
            return possibleAns
        if peopleWithOneDollar == 1:   # we have to distribute '3' to more than one people so that no person get '4'. But remaining people is only one so we will take one more people from ans.
            return possibleAns -1
