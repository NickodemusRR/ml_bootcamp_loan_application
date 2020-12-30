import json
import pickle

import numpy as np

__model = None
__data_columns = None

def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns
    global __model

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open('./artifacts/lr_model.pkl', 'rb') as f:
        __model = pickle.load(f)

    print("Loading saved artifacts... done")


def get_loan_status(gender, married, dependents, education, self_employed, applicantincome, coapplicantincome, loanamount, loan_amount_term, credit_history, property_area):

    
    x = np.array([[gender, married, dependents, education, self_employed, applicantincome, coapplicantincome, loanamount, loan_amount_term, credit_history, property_area]])

    return __model.predict([x])[0]

if __name__ == '__main__':
    load_saved_artifacts()