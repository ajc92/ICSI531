import matplotlib.pyplot as plt, os
os.chdir("tweet_data")
data = []
for line in open('antalya.data').readlines():
	items = []
	for item in line.split(','):
		if item.isdigit():# check if this is an integer
			items.append(int(item))
		else:
			try:
				f = float(item)
				items.append(f)
			except:
				# if it goes to here, it means it is neither integer nor float
				if item == 'hot':
					items.append(1)
				if item == 'cold':
					items.append(2)
				if item == 'rainy':
					items.append(3)
				if item == 'snowy':
					items.append(4)
				if item == 'humid':
					items.append(5)
				if item == 'freezing':
					items.append(6)
				if item == 'sunny':
					items.append(7)
				if item == 'windy':
					items.append(8)
				if item == 'cloudy':
					items.append(9)
				if item == 'sleet':
					items.append(10)
				if item == 'ice':
					items.append(11)
	data.append(items)
weather = []
for i in range(len(data)):
	for j in range(len(data[i])):
		if j % 2 != 0:
			for k in range(int(data[i][j])):
				weather.append(i+1)
plt.hist(weather, normed = True, bins=11, color='b', label='1 = Hot\n2 = Cold\n3 = Rain\n4 = Snow\n5 = Humid\n6 = Freezing\n7 = Sunny\n8 = Windy\n9 = Cloudy\n10 = Sleet\n11 = Ice')
plt.title("Weather in Antalya")
plt.xlabel("Condition")
plt.ylabel("Quantity")
plt.legend()
plt.show()
