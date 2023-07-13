from flask_sqlalchemy import SQLAlchemy
from app import db

class Tenant(db.Model):
    __tablename__ = 'tenants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    code = db.Column(db.String)
    main_unit_no = db.Column(db.String)
    property_name = db.Column(db.String)
    general_contact = db.Column(db.String)
    telephone = db.Column(db.String)
    lease_start_date = db.Column(db.Date)
    lease_end_date = db.Column(db.Date)
    vacate_date = db.Column(db.Date)
    active = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Tenant(name={self.name}, code={self.code}, property={self.property})>'


class TenantTransaction(db.Model):
    __tablename__ = 'tenant_transactions'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))
    tenant = db.relationship('Tenant', backref=db.backref('transactions', lazy=True))
    transaction = db.Column(db.Integer)
    transaction_type = db.Column(db.String)
    transaction_date = db.Column(db.Date)
    amount = db.Column(db.Float)
    period= db.Column(db.String)
    tax= db.Column(db.Float)
    remarks=db.Column(db.String)
    exclusive=db.Column(db.Float)
    tax_amount=db.Column(db.Float)
    inclusive=db.Column(db.Float)
    def __repr__(self):
        return f'<TenantTransaction(tenant_id={self.tenant_id}, transaction_type={self.transaction_type}, amount={self.amount})>'
