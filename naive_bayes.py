
import math

def main():
	inputs, outputs, xlength, totalOuts = readFile('heart-train.txt') #Creates input Matrix and output Array.
	laplace = False #MLE
	laplace = True #LE
	xProb, yProb = readTrainingData(inputs, outputs, xlength, totalOuts, laplace)





	inputs, outputs, xlength, totalOuts = readFile('heart-test.txt')

	predictions = []
	for row in inputs:
		y0 = BayesCalc(row, xProb, yProb, xlength, 0)
		y1 = BayesCalc(row, xProb, yProb, xlength, 1)
		prediction = -1
		if(y0 > y1):
			prediction = 0
		elif(y1 > y0):
			prediction = 1
		predictions.append(prediction)
	accuracyCheck(predictions, outputs, totalOuts)


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




def BayesCalc(row, xProb, yProb, xlength, yval):
	totalProb = 0
	for i in range(0, xlength):
		temp = 0
		if(row[i] == 0):
			temp = math.log(xProb[i][0+yval*2]+.0001) + math.log(yProb[yval])
		if(row[i] == 1):
			temp = math.log(xProb[i][1+yval*2]+.0001) + math.log(yProb[yval])
		totalProb+=temp
	return totalProb

def readTrainingData(inputs, outputs, xlength, totalOuts, laplace):
	trueOuts = 0
	xCount = [] #Holds Amount of times x=1 when y=0 or when y=1
	startVal = 0

	for i in range(0, xlength):
		temp = [0] * 2
		xCount.append(temp)


	for i in range(0, totalOuts): #Loop through all data
		mod = outputs[i] #0 if y=0, 1 if y=1
		for j in range(0, xlength):
			if(inputs[i][j] == 1):
				xCount[j][mod]+=1
		trueOuts+=mod

	mod = 0
	if(laplace):
		mod = 1
		totalOuts+=2



	falseOuts = totalOuts-trueOuts
	xProb = []
	for row in xCount:
		x1y0 = float(row[0]+mod)/totalOuts
		x1y1 = float(row[1]+mod)/totalOuts
		x0y0 = float(falseOuts-row[0]+mod)/totalOuts
		x0y1 = float(trueOuts-row[1]+mod)/totalOuts  #true Outs
		xProb.append([x0y0, x1y0, x0y1, x1y1])

	falseProb = float(falseOuts)/totalOuts
	trueProb = float(trueOuts)/totalOuts
	yProb = [falseProb, trueProb]

	return xProb, yProb

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
