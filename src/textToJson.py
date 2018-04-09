import json



#This function is used to write input to a file (input to be given in JSON format)
def writeToFile(input):
    file = open('../resources/ingredientsTagged.json', 'w')
    file.write(input)
    file.close()



#This function gathers the data from a file and return them in categorized arrays
def dataToCategorizedArrays():
    with open('../resources/ingredients.txt') as ingredients:
        all = [line.strip() for line in ingredients]

    vegetableindex = all.index("VEGETABLES")
    herbspicecindex = all.index("HERBS AND SPICES")
    fruitindex = all.index("FRUITS")


    vegetables = all[vegetableindex:herbspicecindex]
    herbsspices = all[herbspicecindex:fruitindex]
    fruits = all[fruitindex:]

    categorizedAll = vegetables, herbsspices, fruits
    return categorizedAll




#This function converts categorized arrays into JSON data and writes it to a file
def arrayToJson(arrays):
    """
    :param :arrays: a collection of categorized arrays
    """
    data = []

    for array in arrays:
        for item in array:
            if array[0] not in array[array.index(item)]:
                text = array[array.index(item)]
                tag = array[0].lower()
                data.append({'text': text, 'tag': tag})

    json_data = json.dumps(data)
    writeToFile(json_data)





arrayToJson(dataToCategorizedArrays())
