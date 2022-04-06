#['jeans', 'corduroy  trousers', 'shorts']
#['denim shirt', 'lace top', 'T-shirt']
#['sneakers', 'leather boots', 'sandals']
#create all the possible outfit combinations using each list above
myCompleteList = []
pantolones = ['jeans', 'corduroy  trousers', 'shorts']
camisas = ['denim shirt', 'lace top', 'T-shirt']
zapatos = ['sneakers', 'leather boots', 'sandals']
for pant in pantolones:
    for top in camisas:
        for shoe in zapatos:
           # print(top, pant, shoe)
            myList  = []
            myList.append(top)
            myList.append(pant)
            myList.append(shoe)
            myCompleteList.append(myList)
print(myCompleteList)