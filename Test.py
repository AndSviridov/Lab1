import pandas as pd

data = pd.read_csv('books-en.csv', delimiter=';', encoding='Latin_1')
output = pd.DataFrame()
popular = pd.DataFrame()
links = pd.DataFrame()

print('Enter a task in the field below')
print('Write "help" for the list of commands')

while 1:
    task = input('task: ')
    match task:
        case 'length':
            print(len(data))

        case 'find author':
            author = input('Author: ')
            year = input('Year: ')
            yearOrder = input('before or after: ')
            if yearOrder == 'before':
                output = data[(data['Book-Author'] == author) & (data['Year-Of-Publication'] <= int(year))]
            elif yearOrder == 'after':
                output = data[(data['Book-Author'] == author) & (data['Year-Of-Publication'] >= int(year))]
            else:
                print('Error, try again')

            name = author + ' ' + yearOrder + ' ' + year + '.csv'
            output.to_csv(name, index=False, sep=';')
            print('The answer to your request is in the file ', name)

        case 'title length':
            length = input('Lenght: ')
            lengthOrder = input('more or less: ')
            if lengthOrder == 'more':
                output = data[data['Book-Title'].str.len() > int(length)]
            elif lengthOrder == 'less':
                output = data[data['Book-Title'].str.len() < int(length)]
            else:
                print('Error, try again')

            name = 'title_length ' + lengthOrder + ' then ' + length + '.csv'
            output.to_csv(name, index=False, sep=';')
            print('The answer to your request is in the file ', name)

        case 'links':
            output = data.sample(20)
            links['Link'] = output['Book-Author'].astype(str) + ' . ' + output['Book-Title'].astype(str) + ' - ' + output['Year-Of-Publication'].astype(str)
            links.to_csv('links.txt', index=False, header=False)
            lines = []
            with open('links.txt') as l:
                i = 1
                for line in l:
                    lines.append(str(i) + ' ' + line)
                    i = i + 1
                l.close()
            with open('links.txt', 'w') as l:
                l.writelines(lines)
                l.close()
            print('The answer to your request is in the file links.txt')

        case 'popular':
            output = data.sort_values(by='Downloads', ascending=False)
            popular = output.head(20)
            popular.to_csv('popular.csv', index=False, sep=';')
            print('The answer to your request is in the file popular.csv')

        case 'publishers':
            pubs = data['Publisher'].tolist()
            for pub in pubs:
                i = pubs.count(pub)
                if i >= 2:
                    for j in range(1, i, 1):
                        pubs.remove(pub)
            with open('publishers.txt', 'w') as f:
                for pub in pubs:
                    f.write(pub)
                    f.write('\n')
                f.close()
            print('The answer to your request is in the file publishers.txt')

        case 'stop':
            break

        case 'help':
            print('Write "length" to get the number of notes in the file')
            print('Write "find author" to find a book by author')
            print('Write "title length" to filter notes by title length')
            print('Write "links" to get the list of bibliographic links')
            print('Write "links" to see the most popular books')
            print('Write "links" to get the list of bibliographic links')
            print('Write "links" to get the list of publishers')

        case _:
            print('Error, try again')
