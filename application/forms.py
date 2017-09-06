from flask.ext.wtf import Form
from wtforms import TextField, validators

class EnterDBInfo(Form):
    name = TextField(label='Name', description="Enter Player Name", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Max 128 characters')]) 
    amount = TextField(label='Amount', description="Enter contribution")	   
    month = TextField(label='month', description="Enter Month")	
    year = TextField(label='Name', description="Enter year")	

class RetrieveDBInfo(Form):
    numRetrieve = TextField(label='Number of DB Items to Get', description="db_get", validators=[validators.required(), validators.Regexp('^\d{1}$',message=u'Enter a number between 1 and 10')])
