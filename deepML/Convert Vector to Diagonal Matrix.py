#https://www.deep-ml.com/problems/35?from=Linear%20Algebra

def make_diagonal(x):
	# Your code here
	result =[]
	for i in range(len(x)):
		arr=[0]*len(x)
		arr[i]=x[i]
		result.append(arr)
	
	return(result)
