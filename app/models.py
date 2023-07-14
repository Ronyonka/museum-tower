from flask_sqlalchemy import SQLAlchemy
from app import db

class Tenant(db.Model):
    __tablename__ = 'tenants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=True)
    code = db.Column(db.String,nullable=True)
    main_unit_no = db.Column(db.String, nullable=True)
    property_name = db.Column(db.String, nullable=True)
    general_contact = db.Column(db.String, nullable=True)
    telephone = db.Column(db.String, nullable=True)
    lease_start_date = db.Column(db.Date, nullable=True)
    lease_end_date = db.Column(db.Date, nullable=True)
    vacate_date = db.Column(db.Date, nullable=True)
    active = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Tenant(name={self.name}, code={self.code}, property={self.property})>'


class TenantTransaction(db.Model):
    __tablename__ = 'tenant_transactions'

    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))
    tenant = db.relationship('Tenant', backref=db.backref('transactions', lazy=True))
    transaction = db.Column(db.String, nullable=True)
    transaction_type = db.Column(db.String, nullable=True)
    transaction_date = db.Column(db.Date, nullable=True)
    amount = db.Column(db.Float, nullable=True)
    period= db.Column(db.String, nullable=True)
    tax= db.Column(db.Float, nullable=True)
    remarks=db.Column(db.String, nullable=True)
    exclusive=db.Column(db.Float, nullable=True)
    tax_amount=db.Column(db.Float, nullable=True)
    inclusive=db.Column(db.Float, nullable=True)
    def __repr__(self):
        return f'<TenantTransaction(tenant_id={self.tenant_id}, transaction_type={self.transaction_type}, amount={self.amount})>'
