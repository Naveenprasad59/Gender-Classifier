from flask import Flask
from app import views
app =Flask(__name__)

#url

app.add_url_rule('/index','index',views.index)
app.add_url_rule('/','faceapp',views.faceapp)
app.add_url_rule('/faceapp/gender','gender',views.gender,methods=['GET','POST'])

#run
if __name__ =="__main__":
    app.run(debug=True)
    