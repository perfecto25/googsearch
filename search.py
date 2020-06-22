import os
from googlesearch import search 
import jinja2

# number of iterations to search thru
num_of_cases = 1200

def render_template(template, **kwargs):
    ''' renders a Jinja template into HTML '''
    # check if template exists
    if not os.path.exists(template):
        print('No template file present: %s' % template)
        return 'error'
    
    templateLoader = jinja2.FileSystemLoader(searchpath="/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    templ = templateEnv.get_template(template)
    return templ.render(**kwargs)


payload = {}

# digit count
for digit in range(num_of_cases):
    
    # for each digit, create list of results (hits)
    payload[digit] = []
    
    query = f"{digit} new cases"
    print(query)
    for j in search(query, tld="com", num=5, stop=5, pause=2): 
        payload[digit].append(j)

html = render_template(os.getcwd() + '/result.j2', payload=payload)

with open('output.html', 'w') as fh:
    fh.write(html)
 