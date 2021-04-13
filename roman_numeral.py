def roman_numeral(number):
	result =0
	number_dict ={'I':1,'V':5,'X':10,'L': 50,'C' :100,'D' : 500, 'M' : 1000}
	
	for idx in range(0,len(number)):
		#print('idx1=',idx, result)
		num=number_dict[number[idx]]
		if idx+1< len(number) :
			nextNum = number_dict[number[idx+1]]
		if idx+1< len(number) and nextNum > result and result!=0:
			result =nextNum - result
			#print('idx1=',idx,num , result)
			idx+=2
			if idx ==len(number) :
				break
		elif idx+1< len(number) and nextNum > num :
			result +=nextNum - num
			#print('idx2=',idx, num,number[idx] , result)
			idx+=2
			if idx ==len(number) :
				break
		else :
			result += num
			#print('idx3=',idx,num,number[idx] , result)
	print(result)
