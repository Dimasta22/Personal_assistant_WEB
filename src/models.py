from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from src import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(30), nullable=True, unique=True)
    hash = db.Column(db.String(255), nullable=True)
    contacts = relationship('Contact', back_populates='user')


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    birthday = db.Column(db.String(30), nullable=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', cascade='all, delete', back_populates='contacts')
    emails = relationship('Email', back_populates='contact')
    addresses = relationship('Address', back_populates='contact')
    phones = relationship('Phone', back_populates='contact')


'''
class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(30), nullable=False, unique=True)
    hash = db.Column(db.String(255), nullable=False)
    contact_id = db.Column(db.Integer, ForeignKey('contacts.id'), nullable=False)
    contact = relationship('Contact', cascade='all, delete', back_populates='login')
'''


class Email(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=True, unique=True)
    contact_id = db.Column(db.Integer, ForeignKey('contacts.id'), nullable=False)
    contact = relationship('Contact', cascade='all, delete', back_populates='emails')


class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(250), nullable=True)
    contact_id = db.Column(db.Integer, ForeignKey('contacts.id'), nullable=False)
    contact = relationship('Contact', cascade='all, delete', back_populates='addresses')


class Phone(db.Model):
    __tablename__ = 'phones'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=True)
    contact_id = db.Column(db.Integer, ForeignKey('contacts.id'), nullable=False)
    contact = relationship('Contact', cascade='all, delete', back_populates='phones')
