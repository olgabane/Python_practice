import os
import re 

def main():
    path = "/Users/Olga/Desktop/google-python-exercises/babynames"
    os.chdir(path)

    for filename in os.listdir(path):
        if filename.endswith(".html"):
            #get year
            year = re.search(r'\d\d\d\d', filename)
            year = year.group()
        
            #open file, read in line by line
            f = open(filename, 'r')
        
            #pull out ranks and names, delete surrounding characters
            names = re.findall(r'<td>\w+</td>', f.read())
            for i in range(0, len(names)):
                names[i] = names[i].replace('<td>','')
                names[i] = names[i].replace('</td>','')
        
            #populate list
            list = [year]
            for i in range(0, len(names), 3):
                rank = names[i]
                string1 = '%s %s' %(names[i+1], rank)
                string2 = '%s %s' %(names[i+2], rank)
                list.append(string1)
                list.append(string2)
        
            print sorted(list)
            
            continue
        else:
            continue
        return
        
if __name__ == '__main__':
  main()