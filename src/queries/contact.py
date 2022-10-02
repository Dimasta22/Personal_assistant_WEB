from src import db
from src import models
import bcrypt


def update_login_for_contact(nick, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=10))
    contact = models.Contact(nick=nick, hash=hashed)
    db.session.add(contact)
    db.session.commit()
    return contact


def checkout_login_for_contact(nick, password):
    contact = find_by_nick(nick)
    if not contact:
        return None
    if not bcrypt.checkpw(password.encode('utf-8'), contact.hash):
        return None
    return contact


def find_by_nick(nick):
    user = db.session.query(models.Contact).filter(models.Contact.nick == nick).first()
    return user


def get_contact(contact_id):
    user = db.session.query(models.Contact).filter(models.Contact.id == contact_id).first()
    return user


def update_first_name(contact_id, first_name):
    user_contact = get_contact(contact_id)
    user_contact.first_name = first_name
    db.session.commit()


def update_last_name(contact_id, last_name):
    user_contact = get_contact(contact_id)
    user_contact.last_name = last_name
    db.session.commit()


def update_birthday(contact_id, birthday):
    user_contact = get_contact(contact_id)
    user_contact.birthday = birthday
    db.session.commit()


if __name__ == '__main__':
    nick = 'Dimas'
    password = '123456'
    id = 1
    birthday  = '22.01.2000'
    #print(update_login_for_contact(nick, password))
    #print(checkout_login_for_contact(nick, password))
    print(update_birthday(id, birthday))