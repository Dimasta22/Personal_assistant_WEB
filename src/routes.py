import sqlalchemy.exc
from flask import render_template, request, flash, redirect, url_for, session, make_response
import pathlib
from . import app
from src.queries import contact, emails, addresses, phones


@app.route('/healthcheck', strict_slashes=False)
def healthcheck():
    return 'I am worhing'


@app.route('/', strict_slashes=False)
def index():
    #auth = True if 'username' in session else False
    return render_template('login.html', address='Cloud pictures')


@app.route('/registration', methods=['GET', 'POST'], strict_slashes=False)
def registration():
    #auth = True if 'username' in session else False
    if request.method == 'POST':
        if request.form.get('login'):
            return redirect(url_for('login'))

        nick = request.form.get('nickname')
        password = request.form.get('password')
        print(nick, password, contact.find_by_nick(nick))
        if contact.find_by_nick(nick) is None:
            registration_contact = contact.update_login_for_contact(nick, password)
            return redirect(url_for('login'))
        else:
            flash('User already exist')

    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    #auth = True if 'username' in session else False
    if request.method == 'POST':
        nick = request.form.get('nickname')
        password = request.form.get('password')
        login_data = contact.checkout_login_for_contact(nick, password)
        if login_data is None:
            flash('pass')
            return redirect(url_for('login'))

        session['contact_id'] = {'id': login_data.id}
        response = make_response(redirect(url_for('user_page')))
        return response
    return render_template('login.html')


@app.route('/page', strict_slashes=False)
def user_page():
    #auth = True if 'username' in session else False
    contact_first_name = contact.get_contact(session['contact_id']['id']).first_name
    contact_last_name = contact.get_contact(session['contact_id']['id']).last_name
    contact_birthday = contact.get_contact(session['contact_id']['id']).birthday
    contact_addresses = [address.address for address in addresses.get_contact_address(session['contact_id']['id'])]
    contact_phones = [phone.phone for phone in phones.get_contact_phone(session['contact_id']['id'])]
    contact_emails = [email.email for email in emails.get_contact_emails(session['contact_id']['id'])]
    print(contact_birthday)

    return render_template('index.html',
                           birthday=contact_birthday,
                           addresses=contact_addresses,
                           phones=contact_phones,
                           emails=contact_emails,
                           first_name=contact_first_name,
                           last_name=contact_last_name)


@app.route('/add_info', methods=['GET', 'POST'], strict_slashes=False)
def add_info():
    print(request.method)
    if request.method == 'POST':

        first_name = request.form.get('first_name')
        if first_name != '':
            contact.update_first_name(session['contact_id']['id'], first_name)

        last_name = request.form.get('last_name')
        if last_name != '':
            contact.update_last_name(session['contact_id']['id'], last_name)

        birthday = request.form.get('birthday')
        if birthday != '':
            contact.update_birthday(session['contact_id']['id'], birthday)

        contact_address = request.form.get('address')
        if contact_address != "":
            addresses.upload_address_for_user(session['contact_id']['id'], contact_address)

        contact_email = request.form.get('email')
        if contact_email != "":
            try:
                emails.upload_email_for_user(session['contact_id']['id'], contact_email)
            except sqlalchemy.exc.IntegrityError:
                flash('This email already added')

        contact_phone = request.form.get('phone')
        if contact_phone != "":
            phones.upload_phone_for_user(session['contact_id']['id'], contact_phone)

        print(f"{birthday}")

        response = make_response(redirect(url_for('user_page')))
        return response
    return render_template('add_info.html')
