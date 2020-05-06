from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response
from admin import adminList
from patient import patientList
from provider import providerList
from transaction import transactionList

import pymysql,json,time

from flask_session import Session  #serverside sessions

app = Flask(__name__,static_url_path='')

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def welcome():
    return render_template('welcome.html', title='Kayshale Ortiz | IS437 Final Project', msg='Welcome!')

@app.route('/set')
def set():
    session['time'] = time.time()
    return 'set'

@app.route('/get')
def get():
    return str(session['time'])
'''
================================================================
START ADMIN LOGIN
=================================================================
'''
@app.route('/login',methods = ['GET','POST'])
def login():

    if request.form.get('username') is not None and request.form.get('password') is not None:
        a = adminList()
        if a.tryLogin(request.form.get('username'),request.form.get('password')):
            print('login ok')
            session['user'] = a.data[0]
            session['active'] = time.time()
            print(session['user'])
            return redirect('home') #redirecting to an html template in reponse valid to user input
        else:#INVALID VREDENTIALS
            print('login failed')
            return render_template('login.html', title='Login', msg='Incorrect login.')
    else:#THIS IS FOR AN INVALID SESSION NOT INVALID CREDENTIALS
        if 'msg' not in session.keys() or session['msg'] is None:
            m = 'Type your username and password to continue.'
        else:
            m = session['msg']
            session['msg'] = None
        return render_template('login.html', title='Login', msg=m)
'''
================================================================
END ADMIN LOGIN
=================================================================
'''
############MAIN MENU PAGE FOR ADMIN#############
@app.route('/home')
def main():
    if checkSession() == False:
        return redirect('login')
    userinfo = 'Hello, ' + session['user']['fname']
    return render_template('home.html', title='Main menu',msg = userinfo)
    print(session['user'])
def checkSession():
    if 'active' in session.keys():
        timeSinceAct = time.time() - session['active']
        print(timeSinceAct)
        if timeSinceAct > 500:
            session['msg'] = 'Your session has timed out.'
            return False
        else:
            session['active'] = time.time()
            return True
    else:
        return False

########################ADMIN LIST#########################
@app.route('/admins')
def admins():
    if checkSession() == False:
        return redirect('login')
    a = adminList()
    a.getAll()

    print(a.data)
    #return ''
    return render_template('admins.html', title='Admin List', admins=a.data)
'''
================================================================
START TRANSACTION PAGES:
=================================================================
'''
@app.route('/transactions')
def transactions():
    if checkSession() == False:
        return redirect('login')
    t = transactionList()
    t.getAll()

    print(t.data)
    #return ''
    return render_template('transaction/transactions.html', title='Transaction List', transactions=t.data)

@app.route('/transaction')
def transaction():
    if checkSession() == False:
        return redirect('login')
    t = transactionList()
    if request.args.get(t.pk) is None:
        return render_template('error.html', msg='No transaction id given.')

    t.getById(request.args.get(t.pk))
    if len(t.data) <= 0:
        return render_template('error.html', msg='Transaction not found.')

    print(t.data)
    return render_template('transaction/transaction.html', title='Transaction ',  transaction=t.data[0])

@app.route('/newtransaction',methods = ['GET', 'POST'])
def newtransaction():
    if checkSession() == False:
        return redirect('login')
    AllPatients = patientList()
    AllPatients.getAll()
    #print(AllPatients.data)
    AllProviders = providerList()
    AllProviders.getAll()
    #print(AllProviders.data)
    AllAdmins = adminList()
    AllAdmins.getAll()
    #print(AllAdmins.data)
    if request.form.get('TransactionID') is None:
        t = transactionList()
        t.set('TransactionID','')
        t.set('Date','')
        t.set('Amount','')
        t.set('Status','')
        t.set('Insurance','')
        t.set('Notes','')
        t.set('AdminID','')
        t.set('PatientID','')
        t.set('PCPID','')
        t.add()
        return render_template('transaction/newtransaction.html', title='New Transaction',  transaction=t.data[0], pl = AllPatients.data, prl = AllProviders.data, al = AllAdmins.data)
    else:
        t = transactionList()
        t.set('TransactionID',request.form.get('TransactionID'))
        t.set('Date',request.form.get('Date'))
        t.set('Amount',request.form.get('Amount'))
        t.set('Status',request.form.get('Status'))
        t.set('Insurance',request.form.get('Insurance'))
        t.set('Notes',request.form.get('Notes'))
        t.set('AdminID',request.form.get('AdminID'))
        t.set('PatientID',request.form.get('PatientID'))
        t.set('PCPID',request.form.get('PCPID'))
        t.add()
        if t.verifyNew():
            t.insert()
            print(t.data)
            return render_template('transaction/savedtransaction.html', title='Transaction Saved',  transaction=t.data[0],  pl = AllPatients.data, prl = AllProviders.data, al = AllAdmins.data)
        else:
            return render_template('Transaction/newtransaction.html', title='Transaction Not Saved',  transaction=t.data[0],msg=t.errorList,  pl = AllPatients.data, prl = AllProviders.data, al = AllAdmins.data)

@app.route('/savetransaction',methods = ['GET', 'POST'])
def savetransaction():
    if checkSession() == False:
        return redirect('login')
    t = transactionList()
    t.set('TransactionID',request.form.get('TransactionID'))
    t.set('Date',request.form.get('Date'))
    t.set('Amount',request.form.get('Amount'))
    t.set('Status',request.form.get('Status'))
    t.set('Insurance',request.form.get('Insurance'))
    t.set('Notes',request.form.get('Notes'))
    t.set('AdminID',request.form.get('AdminID'))
    t.set('PatientID',request.form.get('PatientID'))
    t.set('PCPID',request.form.get('PCPID'))
    t.add()
    t.update()
    #print(e.data)
    #return ''
    return render_template('transaction/savedtransaction.html', title='Transaction Saved',  transaction=t.data[0], pl = AllPatients.data, prl = AllProviders.data, al = AllAdmins.data)

'''
================================================================
END TRANSACTION PAGES
=================================================================
'''
'''
================================================================
START PATIENT PAGES:
=================================================================
'''
@app.route('/patients')
def patients():
    if checkSession() == False:
        return redirect('login')
    p = patientList()
    p.getAll()

    print(p.data)
    #return ''
    return render_template('patient/patients.html', title='Patient Roster', patients=p.data)

@app.route('/patient')
def patient():
    if checkSession() == False:
        return redirect('login')
    p = patientList()
    if request.args.get(p.pk) is None:
        return render_template('error.html', msg='No Patient id given.')

    p.getById(request.args.get(p.pk))
    if len(p.data) <= 0:
        return render_template('error.html', msg='Patient not found.')

    print(t.data)
    return render_template('patient/patient.html', title='Patient ',  patient=p.data[0])

@app.route('/newpatient',methods = ['GET', 'POST'])
def newpatient():
    if checkSession() == False:
        return redirect('login')
    AllProviders = providerList()
    AllProviders.getAll()
    if request.form.get('PatientID') is None:
        p = patientList()
        p.set('PatientID','')
        p.set('fname','')
        p.set('lname','')
        p.set('DOB','')
        p.set('SSN','')
        p.set('Notes','')
        p.set('PCPID','')
        p.add()
        return render_template('patient/newpatient.html', title='New Patient',  patient=p.data[0], prl = AllProviders.data)
    else:
        p = patientList()
        p.set('PatientID',request.form.get('PatientID'))
        p.set('fname',request.form.get('fname'))
        p.set('lname',request.form.get('lname'))
        p.set('DOB',request.form.get('DOB'))
        p.set('SSN',request.form.get('SSN'))
        p.set('Notes',request.form.get('Notes'))
        p.set('PCPID',request.form.get('PCPID'))
        p.add()
        if p.verifyNew():
            p.insert()
            print(p.data)
            return render_template('patient/savedpatient.html', title='Patient Saved',  patient=p.data[0], prl = AllProviders.data)
        else:
            return render_template('patient/newpatient.html', title='Patient Not Saved',  patient=p.data[0],msg=t.errorList, prl = AllProviders.data)

@app.route('/savepatient',methods = ['GET', 'POST'])
def savepatient():
    if checkSession() == False:
        return redirect('login')
    p = patientList()
    p.set('PatientID',request.form.get('PatientID'))
    p.set('fname',request.form.get('fname'))
    p.set('lname',request.form.get('lname'))
    p.set('DOB',request.form.get('DOB'))
    p.set('SSN',request.form.get('SSN'))
    p.set('Notes',request.form.get('Notes'))
    p.set('PCPID',request.form.get('PCPID'))
    p.add()
    p.update()
    #print(e.data)
    #return ''
    return render_template('patient/savedpatient.html', title='Patient Saved',  patient=p.data[0],msg=t.errorList, prl = AllProviders.data)

'''
================================================================
END PATIENT PAGES
=================================================================
'''
'''
================================================================
START PROVIDER PAGES:
=================================================================
'''
@app.route('/providers')
def providers():
    if checkSession() == False:
        return redirect('login')
    pr = providerList()
    pr.getAll()

    print(pr.data)
    #return ''
    return render_template('provider/providers.html', title='List of Providers', providers=pr.data)

@app.route('/provider')
def provider():
    if checkSession() == False:
        return redirect('login')
    pr = providerList()
    if request.args.get(pr.pk) is None:
        return render_template('error.html', msg='No Provider ID given.')

    pr.getById(request.args.get(pr.pk))
    if len(pr.data) <= 0:
        return render_template('error.html', msg='Provider not found.')

    print(pr.data)
    return render_template('provider/provider.html', title='Provider ',  providers=pr.data[0])

@app.route('/newprovider',methods = ['GET', 'POST'])
def newprovider():
    if checkSession() == False:
        return redirect('login')
    if request.form.get('PCPID') is None:
        pr = providerList()
        pr.set('PCPID','')
        pr.set('DOH','')
        pr.set('Name','')
        pr.set('SSN','')
        pr.set('Specialty','')
        pr.add()
        return render_template('provider/newprovider.html', title='New Provider',  providers=pr.data[0])
    else:
        pr = providerList()
        pr.set('PCPID',request.form.get('PCPID'))
        pr.set('DOH',request.form.get('DOH'))
        pr.set('Name',request.form.get('Name'))
        pr.set('SSN',request.form.get('SSN'))
        pr.set('Specialty',request.form.get('Specialty'))
        pr.add()
        if pr.verifyNew():
            pr.insert()
            print(pr.data)
            return render_template('provider/savedprovider.html', title='Provider Saved', providers=pr.data[0])
        else:
            return render_template('provider/newprovider.html', title='Provider Not Saved',  providers=pr.data[0])

@app.route('/saveprovider',methods = ['GET', 'POST'])
def saveprovider():
    if checkSession() == False:
        return redirect('login')
    pr = providerList()
    pr.set('PCPID',request.form.get('PCPID'))
    pr.set('DOH',request.form.get('DOH'))
    pr.set('Name',request.form.get('Name'))
    pr.set('SSN',request.form.get('SSN'))
    pr.set('Specialty',request.form.get('Specialty'))
    pr.add()
    pr.update()
    #print(pr.data)
    #return ''
    return render_template('provider/savedprovider.html', title='Provider Saved',  provider=pr.data[0],msg=pr.errorList)

'''
================================================================
END PROVIDER PAGES
=================================================================
'''
@app.route('/logout',methods = ['GET','POST'])
def logout():
    del session['user']
    del session['active']
    return render_template('login.html', title='Login', msg='Logged out.')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
   app.secret_key = '1234'
   app.run(host='127.0.0.1',debug=True)
