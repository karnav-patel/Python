import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('agro-servicecenter-firebase-adminsdk-zikwb-f3b24f9228.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

users_ref = db.collection(u'CustomerData')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))