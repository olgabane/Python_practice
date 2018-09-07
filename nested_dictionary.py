#Nested dictionary practice

people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for k, v in people.items():
    print "Key: ", k, "\n", "Value: ", v, "\n"

#prints dictionary values
for k in people.values():
    print k

#also prints dictionary values
for k, v in people.items():
    print v

#iterate over nested dictionary
for k, v in people.items():
    print "Key: ", k, "\n", "Value: ", v, "\n"
    
    for k1, v1 in v.items():
        print k1+":", v1
