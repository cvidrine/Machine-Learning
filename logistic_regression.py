import math

def main():
	inputs, outputs, xlength, totalOuts = readFile('heart-train.txt')

	thetas = [0] * (xlength+1)
	#Compute Log Likelyhood
	step = 0.000001
	for k in range(0, 10000):
		gradients = [0] *(xlength+1)
		for i in range(0, totalOuts): #For each row
			z=thetas[0]
			for j in range(1, xlength+1): #for each trait xi
				z+=thetas[j]*inputs[i][j-1]
			sigmoidProduct = outputs[i] - (1/(1+math.exp(-z)))
			gradients[0] += sigmoidProduct
			for j in range(1, xlength+1):
				gradients[j]+=inputs[i][j-1] * sigmoidProduct
			for j in range(0, xlength+1):
				thetas[j]+= step * gradients[j]



	inputs, outputs, xlength, totalOuts = readFile('heart-test.txt')

	predictions = []
	for row in inputs:
		z = thetas[0]
		for i in range(1, xlength+1):
			z+=thetas[i]*row[i-1]


		p = 1/(1+math.exp(-z))
		if(p > 0.5):
			predictions.append(1)
		else:
			predictions.append(0)
	print predictions
	accuracyCheck(predictions, outputs, totalOuts)


def ComputeLikelyhood(thetas, inputs, outputs, totalOuts, xlength):
	likelyhood =0
	for i in range(0, totalOuts):
		z=thetas[0]
		for j in range(1, xlength+1): #for each trait xi
			z+=thetas[j]*inputs[i][j-1]
		likelyhood+=outputs[i]*math.log(1/(1+math.exp(-z))) + (1-outputs[i]) * math.log(1-(1/(1+math.exp(-z))))
	print 'likelyhood: ', likelyhood

def accuracyCheck(predictions, outputs, totalOuts):
	totalFalse = 0
	totalTrue = 0
	correctFalse = 0
	correctTrue = 0
	for i in range(0, totalOuts):
		if(outputs[i] == 0):
			totalFalse+=1
			if(predictions[i] == 0):
				correctFalse+=1
		if(outputs[i] == 1):
			totalTrue+=1
			if(predictions[i] == 1):
				correctTrue+=1

	print 'Class 0: tested {}, correctly classified {}'.format(totalFalse, correctFalse)
	print 'Class 1: tested {}, correctly classified {}'.format(totalTrue, correctTrue)
	print 'Overall: tested {}, correctly classified {}'.format(totalFalse+totalTrue, correctFalse+correctTrue)
	print 'Accuracy = {}'.format((correctTrue+correctFalse)/float(totalTrue+totalFalse))




def readFile(filename):
	inputMatrix = []
	outputArr = []
	xlength = 0
	numVects = 0
	with open(filename) as f:
		xlength = int(f.readline())
		numVects = int(f.readline())
		for line in f:
			a = line.split(': ') #Split into input & output
			inputstr = a[0].split(' ') #split input into list of string values
			outputArr.append(int(a[1])) #append output to list of outputs
			inputs = [] #Holds int values
			for i in inputstr: #Converts strings to ints
				inputs.append(int(i))
			inputMatrix.append(inputs) #Adds input vector to set of inputs
	return inputMatrix, outputArr, xlength, numVects


if __name__ == '__main__':
	main()