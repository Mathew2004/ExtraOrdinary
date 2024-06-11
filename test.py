import re
from flask import jsonify
input_string = "5x-3y+9=10y-10"
    
    # Extracting terms from the input string
terms = re.findall(r'([+-]?\d+)([a-zA-Z])?|=', input_string)


    
    # Dictionary to store variable values
variables = {}
c_value = 0
left = 1
for term in terms:
    # print(term[0],term[1])        
        # value = int(term[0])
    if term[0]=='':
        # print("=")
        # term[0] = "="
        left = 0
    else:
        value = int(term[0]) if left==1 else -int(term[0])
            
    variable = term[1] if (term[1] and term[0]) else 'C'
    
        
        
    if variable in variables:
        variables[variable] += value
    else:
        variables[variable] = value
    
    result = []
    
    for key, value in variables.items():
        result.append(f"Value of {key} = {value}")
    
    # return jsonify({'result': '\n'.join(result)})
    print(result)
   
    
    
        
    
        
    print(result)