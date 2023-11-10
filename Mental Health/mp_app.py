from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
from sklearn.ensemble import RandomForestClassifier
# Specify a static folder and disable directory listing
app.config['STATIC_FOLDER'] = 'static'
app.config['EXPLAIN_TEMPLATE_LOADING'] = False

with open("model.pkl", "rb") as model_file:
    model = RandomForestClassifier()
    
@app.route("/", methods=["GET"])
def hello_word():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    # Get form data from the request
    age = request.form['age']
    gender = request.form['gender']
    country = request.form['countries']
    state = request.form['states']
    self_employed = request.form['self-employed']
    family_history = request.form['family-history']
    work_interfere = request.form['Work-interfere']
    no_of_employees = request.form['no-of-employees']
    remote_work = request.form['remote_work']
    tech_company = request.form['tech-company']
    benefits = request.form['benefits']
    care_options = request.form['care_options']
    wellness_program = request.form['wellness_program']
    seek_help = request.form['seek_help']
    anonymity = request.form['anonymity']
    leave = request.form['leave']
    mental_health_consequence = request.form['mental-health-consequence']
    phys_health_consequence = request.form['phys-health-consequence']
    coworkers = request.form['coworkers']
    supervisor = request.form['supervisor']
    mental_health_interview = request.form['mental-health-interview']
    phys_health_interview = request.form['phys-health-interview']
    mental_vs_physical = request.form['mental-vs-physical']
    obs_consequence = request.form['obs-consequence']
    # Add more variables for other form fields

    # Perform any necessary data preprocessing

    # Make a prediction using your model
    # You need to adapt this based on your specific model and preprocessing steps
    # For simplicity, assuming you have a function `make_prediction` for making predictions
    prediction = model.predict(model, age, gender, country, state, self_employed,
                                family_history, work_interfere, no_of_employees,
                                remote_work, tech_company, benefits, care_options,
                                wellness_program, seek_help, anonymity, leave,
                                mental_health_consequence, phys_health_consequence,
                                coworkers, supervisor, mental_health_interview,
                                phys_health_interview, mental_vs_physical, obs_consequence)
    
    # Determine the result based on the prediction
    result = "Treatment Needed" if prediction == 1 else "No Treatment Needed"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
