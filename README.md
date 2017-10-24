# PERMUTATIONS
```
Permutations are all the different ways that you can arrange N objects. Given N objects, there are N! permutations. This algorithm returns all the sets for numbers 0 to N-1. For example given input 5, it outputs permutations such as 0,1,2,3,4  ,  1,0,2,3,4  , 1,3,2,4,0 etc.
This algorithm is very usefull for anadroms, keys creation-algorithms and generally when you want to get the permutation of a set of objects in an array.
```

## How it works
```
The algorithm works recursively. It creates a recusion tree, that has a depth of N nodes. And looks like this for input 3:
```

```



				                                                                          {length=3, curr=[],res }            
				                             /     									                 |                       	\	 
				                            0     			    					                 1                           2
				                           /                    					                 |                            \
				                          /                     					                 |                             ...
				 	   {length=3, curr=[0],res}                                         {length=3, curr=[1],res}                    
				       /                     \                                           /                     \ 
					  1                       2                                         2                       3 
	                 /                         \                                       /                         \ 
	{length=3, curr=[0,1],res}         {length=3, curr=[0,2],res}        {length=3, curr=[1,2],res}         {length=3, curr=[1,3],res}
                  |                                |                                |                                |
                  2                                1                                3                                2
                  |                                |                                |                                |
    {length=3, curr=[0,1,2],res}       {length=3, curr=[0,2,1],res}     {length=3, curr=[1,2,3],res}       {length=3, curr=[1,3,2],res}
                  ||                               ||                               ||                               ||           
                  ||                               ||                               ||                               ||                
         res.append [0,1,2]                 res.append [0,2,1]               res.append [1,2,3]                 res.append [1,3,2]















 
```                                                                                                                                                                                                                                