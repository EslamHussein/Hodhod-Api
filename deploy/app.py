
# coding: utf-8

# In[1]:


import pickle
import flask
import os
import random
from cloudant import cloudant

app = flask.Flask(__name__)
port = int(os.getenv("PORT", 9099))

'''
{
  "apikey": "AeZ__chsijPGmC8o4Thw9klSlxKruMhtvLm-PgyXELM2",
  "host": "63893dc7-a257-4123-b7e8-314d086b0523-bluemix.cloudantnosqldb.appdomain.cloud",
  "iam_apikey_description": "Auto-generated for key a036f206-b604-40df-864f-c0b02bcc29d7",
  "iam_apikey_name": "Service credentials-1",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/e4d5b55044be43f0aebb08360e1764cc::serviceid:ServiceId-52db3217-c5d3-40be-aca1-78309d852bbf",
  "password": "f7ef0b9cb909f60e7c37c5d81e53c6b4f14e135de21651dda1212c813b03968c",
  "port": 443,
  "url": "https://63893dc7-a257-4123-b7e8-314d086b0523-bluemix:f7ef0b9cb909f60e7c37c5d81e53c6b4f14e135de21651dda1212c813b03968c@63893dc7-a257-4123-b7e8-314d086b0523-bluemix.cloudantnosqldb.appdomain.cloud",
  "username": "63893dc7-a257-4123-b7e8-314d086b0523-bluemix"
}
'''
'''
with cloudant("63893dc7-a257-4123-b7e8-314d086b0523-bluemix", "f7ef0b9cb909f60e7c37c5d81e53c6b4f14e135de21651dda1212c813b03968c", account=ACCOUNT_NAME) as client:
    # Context handles connect() and disconnect() for you.
    # Perform library operations within this context.  Such as:
    print client.all_dbs()
'''
# In[ ]:


model = pickle.load(open("linearmodel.pkl","rb"))


# In[ ]:


@app.route('/predict', methods=['POST'])
def predict():

    features = flask.request.get_json(force=True)['features']
    prediction = model.predict([features])[0,0]
    problems_map = {0:"MedicalAssistance",
    1:"FoodDistributors",
    2:"WaterIssues",
    3:"SurvivorsHandling",
    4:"RoadAndBridgeFixes",
    5:"CleanupOperations",
    }
    volunteers_map = {"MedicalAssistance":["Eslam","Mostafa","Eman"],
    "FoodDistributors":["Hussein","Yahia","Moamn"],
    "WaterIssues":["Ahmed","Magdy","Doaa"],
    "SurvivorsHandling": ["Mohamed","Ibrahiem"],
    "RoadAndBridgeFixes":["Abeer","Hend"],
    "CleanupOperations":["Salah","Dina"],
    }
    volunteers_list  = volunteers_map[problems_map[features[0]]]
    volunteer = random.choice(volunteers_list)
    response = {'volunteer': volunteer}

    return flask.jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

