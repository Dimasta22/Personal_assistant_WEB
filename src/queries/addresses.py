from sqlalchemy import and_

from src import db
from src import models


def upload_address_for_user(contact_id, address):
    address = models.Address(contact_id=contact_id, address=address)
    db.session.add(address)
    db.session.commit()


def get_contact_address(contact_id):
    return db.session.query(models.Address).filter(models.Address.contact_id == contact_id).all()


if __name__ == '__main__':
    contact_id = 1
    print(get_contact_address(contact_id)[0].phone)
