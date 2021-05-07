class Solution(object):
            
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
        result = []
        lookUpTable = {}
        for i in range (0, len(nums)):
            if nums[i] not in lookUpTable:
                lookUpTable[nums[i]] = []                            
            lookUpTable[nums[i]].append(i)
                    
        for i in range (0, len(nums)):            
            if len(lookUpTable[nums[i]]) > 0:                
                lookUpTable[nums[i]].pop(0)                
                targetTwoSum = 0 - nums[i]                
                for k in lookUpTable.keys():
                    if len(lookUpTable[k]) > 0:                        
                        lookUpNumb = targetTwoSum - k
                        if lookUpNumb in lookUpTable:
                            if (lookUpNumb != k and len(lookUpTable[lookUpNumb]) > 0) or (lookUpNumb == k and len(lookUpTable[lookUpNumb]) > 1):      
                                
                                foundDuplicateTriplex = False
                                for tempResult in result:
                                    if (nums[i] == k and k == lookUpNumb):
                                        if (nums[i] == tempResult[0] and tempResult[0] == tempResult[1] and tempResult[2] == tempResult[1]): 
                                            foundDuplicateTriplex = True
                                            break
                                    elif (nums[i] in tempResult and k in tempResult and lookUpNumb in tempResult):
                                        foundDuplicateTriplex = True                                        
                                        break
                                        
                                if not foundDuplicateTriplex:                                
                                    result.append([nums[i], k, lookUpNumb])                               
              
        return result
                    
        
        
                
            
