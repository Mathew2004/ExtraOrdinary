from flask import Flask, request, jsonify, render_template
from Solver import ExpressionSolver

app = Flask(__name__)

solver = ExpressionSolver()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    expression = data.get('input')
    
    if not expression:
        return jsonify({'result': 'No expression provided'}), 400

    n = expression.strip()
        
   
    Steps = None
    Solution = solver.solve(
        expression = n, 
        steps_return = solver.StepsReturnAsList
    )
        
    if len(Solution) > 1:
        Steps = Solution[1]
        Solution = Solution[0]
            
    print(f'{Solution = }')
    if Steps: 
        print(f'{Steps = }')
    else:
        Steps = 'InValid Equation'
    return jsonify({'result': '\n=>'.join(Steps)})


 

    
  
# For Coffitient of Variables  


# @app.route('/process', methods=['POST'])
# def process():
#     data = request.json
#     input_string = data.get('input')
    
#     # Extracting terms from the input string
#     terms = re.findall(r'([+-=]?\d+)([a-zA-Z])?|=', input_string)
    
#     # Dictionary to store variable values
#     variables = {}
#     c_value = 0
#     left = 1
#     for term in terms:
        
#         # value = int(term[0])
#         if term[0]=='':
#             print("=")
#             left = 0
#         else:
#             value = int(term[0]) if left==1 else -int(term[0])
            
#         variable = term[1] if term[1] else 'C'
        
#         if variable in variables:
#             variables[variable] += value
#         else:
#             variables[variable] = value
    
#     result = []
    
#     for key, value in variables.items():
#         result.append(f"Coff. of {key} = {value}")
    
#     return jsonify({'result': '\n'.join(result)})
