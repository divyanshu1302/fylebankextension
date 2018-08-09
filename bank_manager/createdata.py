from bank_manager.models import BANK_COLLECTION


class Reading():

    def __init__(self, data, db=False):
        self.ifsc = data.get('ifsc')
        self.bank_id = data.get('bank_id')
        self.branch = data.get('branch')
        self.address = data.get('address')
        self.city = data.get('city')
        self.district = data.get('district')
        self.state = data.get('state')
        self.bank_name = data.get('bank_name')

        if db:
            BANK_COLLECTION.insert_one({
                'ifsc': self.ifsc, 'bank_id': self.bank_id,
                'branch': self.branch, 'address': self.address, 'city': self.city,
                'district': self.district, 'state': self.state, 'bank_name': self.bank_name
                })
