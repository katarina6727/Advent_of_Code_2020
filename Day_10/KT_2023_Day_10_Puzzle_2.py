# initialize variables
adaptersList = []
adapterPaths = 0

# open the file and put all of the adapters input into a list before closing the file
f = open('adapters_input.txt')

for line in f.readlines():
    if (line.find("\n") != -1):
        data = int(line[:len(line)-1])
    else:
        data = int(line)
    adaptersList.append(data)

f.close()

# add my device's adapter to the adapter list
adaptersList.append(max(adaptersList)+3)
# sort the list so the numbers are ordered lowest to highest
adaptersList = sorted(adaptersList)

# solution code
paths = {0:1}
for adapter in adaptersList:
    paths[adapter] = 0
    if adapter - 1 in paths:
        paths[adapter] += paths[adapter-1]
    if adapter - 2 in paths:
        paths[adapter] += paths[adapter-2]
    if adapter - 3 in paths:
        paths[adapter] += paths[adapter-3]

# print the result  
print(paths[max(adaptersList)])
