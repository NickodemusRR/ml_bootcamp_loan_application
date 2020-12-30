from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route('/')
def hello_world():

    return  'Hello World!'

@app.route('/predict_application', methods=['GET', 'POST'])
def predict_loan_application():
    
    gender = request.form['gender']
    married = request.form['married']
    dependents = request.form['dependents']
    education = request.form['education']
    self_employed = request.form['self_employed']
    applicantincome = int(request.form['applicantincome'])
    coapplicantincome = int(request.form['coapplicantincome'])
    loanamount = int(request.form['loanamount'])
    loan_amount_term = int(request.form['loan_amount_term'])
    credit_history = int(request.form['credit_history'])
    property_area = request.form['property_area']

    genders_encoder = {'MALE':1,
                  'FEMALE':0}

    married_encoder = {'YES':1,
                    'NO':0}

    dependents_encoder = {'0':0,
                        '1':1,
                        '2':2,
                        '3+':3}

    education_encoder = {'GRADUATED':1,
                    'NOT GRADUATED':0}

    self_employment_encoder = {'YES':1,
                            'NO':0}                      

    property_area_encoder = {'RURAL':0,
                            'SEMIRURAL':1, 
                            'URBAN':2}

    gender = genders_encoder[gender]
    married = married_encoder[married]
    dependents = dependents_encoder[dependents]
    education = education_encoder[education]
    self_employed = self_employment_encoder[self_employed]
    property_area = property_area_encoder[property_area]

    response = jsonify({
        'estimated_price': utils.get_loan_status(gender, married, dependents, education, self_employed, applicantincome, coapplicantincome, loanamount, loan_amount_term, credit_history, property_area)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    utils.load_saved_artifacts()
    app.run(debug=True)