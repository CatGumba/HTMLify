from os.path import exists
import re

path = input('File: ')
if not path.endswith('.txt'):
    input('Error:\nFile must end with .txt')
    exit()

htmlpath = path.replace('.txt','.html')



with open(htmlpath, 'a'):
    pass

def htmlify():
    size = 'auto'
    googlefont = ''
    html = ''
    font = 'sans-serif'
    align = 'auto'
    margin = '1px'
    if exists(path):
        with open(path) as f:
            for line in f:
                result = re.search('{(.*)}', line)
                link = ''
                if not result == None:
                    link = result.group(1)
                    linkarray = link.split(',')
                    print(linkarray)
                    try:
                        linkarray[2]
                        line = line.replace('{'+link+'}',f'<a href={linkarray[0]} target="_blank">{linkarray[1]}</a>')
                    except:   
                        line = line.replace('{'+link+'}',f'<a href={linkarray[0]}>{linkarray[1]}</a>')
                    
                line = line.replace('\n', '')

                if line.startswith('-'):
                    line = line[1:]
                    if line.startswith('c'):
                        align = 'center'
                        continue
                    if line.startswith('ln'):
                        html += f"\n<hr>"
                        continue
                    if line.startswith('l'):
                        align = 'left'
                        continue
                    if line.startswith('r'):
                        align = 'right'
                        continue
                    if line.startswith('br'):
                        html += f"\n<br>"
                        continue
                    if line.startswith('m'):
                        margin = line[2:]
                        continue
                    if line.startswith('s'):
                        size = ''
                        line = line[2:]
                        for char in line:
                            if not char == ' ':
                                size += char
                                continue
                            break
                        line = line[len(size)+1:]
                
                if line.startswith('###'):
                    line = line[3:]
                    html += f'\n<h3 style="font-size: {size}; text-align: {align}; margin: {margin};">{line}</h3>'
                    continue 
                    
                if line.startswith('##'):
                    line = line[2:]
                    html += f'\n<h2 style="font-size: {size}; text-align: {align}; margin: {margin};">{line}</h2>'
                    continue

                if line.startswith('#'):
                    line = line[1:]
                    html += f'\n<h1 style="font-size: {size}; text-align: {align}; margin: {margin};">{line}</h1>'
                    continue
                
                if line.startswith('*'):
                    line = line[1:]
                    html += f'\n<img src={line} alt={line} style="text-align: {align}; margin: {margin}; max-width: {size}; display: block;">'
                    continue

                if line.startswith('~~'):
                    line = line[2:]
                    googlefont = f'https://fonts.googleapis.com/css?family={line.replace(" ","+")}'
                    font = line
                    continue

                if line.startswith('~'):
                    line = line[1:].replace(' ','-')
                    font = line
                    continue

                
                
                if line.startswith('!'):
                    line = line[1:]
                    html += f'\n<p style="font-size: {size}; text-align: {align}; margin: {margin};">{line}</p>'
                    continue
                
                if bool(line):
                    html += f'\n<p style="font-size: {size}; text-align: {align}; margin: {margin};">{line}</p>'

            if bool(googlefont):
                print(googlefont)
                html = f'<link rel="stylesheet" href="{googlefont}">\n{html}'
            html = f'<body style="font-family: {font};">{html}\n</body>'
            return html

html = htmlify()


print(html)

with open(htmlpath, "w") as f:
    f.write(html)