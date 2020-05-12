class Solution:
    def uniquePaths(self, m: int, n: int):
        
        max_right_moves= m-1
        max_down_moves= n-1
        summation=max_right_moves+max_down_moves
        factorial_right=factorial(max_right_moves)
        factorial_down=factorial(max_down_moves)
        factorial_sum=factorial(summation)
        possible_paths=int(factorial_sum/(factorial_right*factorial_down))
        
        return possible_paths 
      
   
    
    def factorial(number):

        i=1
        factorial=1    
        for i in range (number):
            
            factorial=factorial*i    
           
        return factorial
    
    
    
   
        
