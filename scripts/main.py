import csv
import pandas as pd
import numpy as np 
import string


class SimplexAlgorithm:

    def __init__(self, profit , constraints , bounds ):
        self.profit = profit 
        self.constraints = constraints 
        self.bounds = bounds 
        self.tableau = []
        self.used_length = len( profit )+1
        self.visited_pivots = [] 
        self.convert_to_tableau()


    def last_index_has_negative ( self ):
        for elements in self.tableau[-1]:
            if elements < 0:
                return True
        return False


    def convert_to_tableau( self ):
        for count,const in enumerate(self.constraints):
            zeroes  = [0]*self.used_length
            zeroes[count] = 1 
            self.tableau.append( const+zeroes+[self.bounds[count]] )
        last_row = [i*-1 for i in self.profit] + [0]*self.used_length + [0]
        last_row[-2] = 1 
        self.tableau.append( last_row )


    def finding_pivot( self ):
        minimum_value = min( self.tableau[-1] )
        lowest_index_profit = self.tableau[-1].index( minimum_value )
        pivot =  [ None , lowest_index_profit ]
        find_lowest_bound = 100000000000
        for count,const in enumerate(constraints):
            compute = self.bounds[count]/const[pivot[-1]] 
            if find_lowest_bound > compute:
                find_lowest_bound = compute 
                pivot[0]= count 
        # self.visited_pivots.append( pivot[0] )
        return  pivot 

        
    def row_operations( self , pivot ):
        pivot_value = self.tableau[pivot[0]][pivot[1]]
        for count,consts in enumerate(self.tableau[pivot[0]]):
            self.tableau[pivot[0]][count] = consts*(1/ pivot_value )

    def column_operations( self, pivot ):
        for count,consts in enumerate(self.tableau):
            value = consts[ pivot[1] ] 
            if  count != pivot[0]  and value != 0:
                self.tableau[count] = [  (value*-1)*(self.tableau[pivot[0]][count])+ const  for count,const in enumerate(self.tableau[count]) ] 
               
    def printing_tableu(self):
        for i in self.tableau:
            print(i)
        print("-"*10)


    def main(self, *args , **kwargs ):
        self.printing_tableu()
        while self.last_index_has_negative():
            pivot = self.finding_pivot()
            self.row_operations( pivot )
            self.column_operations( pivot )
            self.printing_tableu()
        print( [i[-1] for i in self.tableau] )






if __name__ == '__main__':
    profit = [5,4] 
    constraints  = [ [3,5], [4,1] ]
    bounds  = [ 78, 36 , 0 ] 

    # profit = [3,4,1] 
    # constraints  = [ [3,10,5], [5,2,8], [8,10,3] ]
    # bounds  = [ 120, 6 , 105, 0 ]  
    
    simplex = SimplexAlgorithm( profit,constraints,bounds ) 
    simplex.main()