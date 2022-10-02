from sqlalchemy import and_

from src import db
from src import models


def upload_email_for_user(contact_id, email):
    email = models.Email(contact_id=contact_id, email=email)
    db.session.add(email)
    db.session.commit()


def get_contact_emails(contact_id):
    return db.session.query(models.Email).filter(models.Email.contact_id == contact_id).all()


if __name__ == '__main__':
    contact_id = 1
    email = 'serdyuk0002@gmail.com'
    print(get_contact_emails(contact_id))

