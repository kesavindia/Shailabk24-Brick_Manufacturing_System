''''''
'''
Decimal to Binary:
===================
Integer  : 137
Convepy to binary===>  2| 137
                       2| 68 - 1
                       2| 34 - 0
                       2| 17 - 0 
                       2|  8 - 1 
                       2|  4 - 0
                       2|  2 - 0
                        |  1 - 0           Binary format -    1000 1001
 
 
Binary to Decimal:
=================== 
Given binary  number                :  1  0  0  0  1  0  0  1 
                                       -----------------------
position(0-7) right to left :          7  6  5  4  3  2  1  0   : Indexing
                                      2  2  2  2  2  2  2  2  
Where ever 1 exists, calculate power: ------------------------   
                                      128  0  0  0  8  0  0  1  
                                        ==> sum => 137                              
                                      -------------------------            

Textfile/Zipfile/Image/Audio/Video: Binary Format
                                            
'''