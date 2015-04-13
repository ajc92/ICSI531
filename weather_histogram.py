import matplotlib.pyplot as plt, os
os.chdir("tweet_data")
data = []
for line in open('san_juan.data').readlines():
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
for i in range(rows):
	for j in range(columns):
		data[i][j]
weather = [items[0] for items in data]
print weather
plt.hist(weather, bins=11, color='b', label='Weather')
plt.title("Weather")
plt.xlabel("Condition")
plt.ylabel("Quantity")
plt.legend()
#plt.show()
