'''
Author : Prateek Chanda(@prateekiiest)
Problem Link: https://www.facebook.com/hackercup/problem/656203948152907/
Explanation: Under explanation folder
'''

t = int(input())

for test in range(t):
	st = input()
	
	no_of_dots = st.count(".")
	no_of_b_s = st.count("B")
	result = ""
	if no_of_dots >= 1 and no_of_b_s >= no_of_dots:
		result = "Y"
	else:
		result = "N"
		
	case = "Case #"
	print( case + str(test+1) + ": "+result)
