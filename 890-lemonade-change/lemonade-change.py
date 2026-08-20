class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for i in bills :
            if i ==5:
                five+=1
            if i==10:
                if five>=1:
                    five-=1
                    ten+=1
                else:
                    return False
            if i==20:
                                    
                if five>=1 and ten>=1:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
            
        return True

