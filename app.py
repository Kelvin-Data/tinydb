from flask import (Flask, render_template, redirect, 
                   url_for)
from form import ContactForm
from flask_ckeditor import CKEditor
from tinydb import TinyDB

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['CKEDITOR_PKG_TYPE'] = 'full-all'

ckeditor = CKEditor(app)
db = TinyDB('flask_ckeditor1/message.json')

################# Route ##################
@app.route('/')
def index():
    form = ContactForm()
    return render_template('contact.html', form=form)

@app.route('/message', methods=['GET','POST'])
def submit():
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subscribe = form.subscribe.data
        message = form.message.data
    
        db.insert({
            'name': name,
            'email': email,
            'subscribe': subscribe,
            'message': message
        })
        # print("Message saved to TinyDB:", {
        #     'name': name,
        #     'email': email,
        #     'message': message
        # })
        return redirect(url_for('thankyou'))
    
    return render_template('contact.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    
# python flask_ckeditor1/app.py