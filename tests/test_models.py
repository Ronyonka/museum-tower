import unittest
from app import app, db, db_host, db_name, db_user, db_password
from app.models import Tenant, TenantTransaction

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test environment
        app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Use the existing SQLAlchemy instance from your Flask app
        # db.init_app(app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Clean up after the test
        with app.app_context():
            db.drop_all()

    def test_tenant_model(self):
        # Create a test tenant
        tenant = Tenant(
            name='John',
            code='001',
            main_unit_no='A-101',
            property_name='Tower A',
            general_contact='John Doe',
            telephone='123-456-7890',
            lease_start_date='2022-01-01',
            lease_end_date='2023-12-31',
            vacate_date=None,
            active=True
        )

        with app.app_context():
            # Add the tenant to the session and commit the changes
            db.session.add(tenant)
            db.session.commit()

            # Retrieve the tenant from the database
            retrieved_tenant = Tenant.query.first()

            # Perform assertions to verify the correctness of the retrieved tenant
            self.assertEqual(retrieved_tenant.name, 'John')
            self.assertEqual(retrieved_tenant.code, '001')
            self.assertEqual(retrieved_tenant.main_unit_no, 'A-101')
            self.assertEqual(retrieved_tenant.property_name, 'Tower A')
            self.assertEqual(retrieved_tenant.general_contact, 'John Doe')
            self.assertEqual(retrieved_tenant.telephone, '123-456-7890')
            self.assertEqual(str(retrieved_tenant.lease_start_date), '2022-01-01')
            self.assertEqual(str(retrieved_tenant.lease_end_date), '2023-12-31')
            self.assertIsNone(retrieved_tenant.vacate_date)
            self.assertTrue(retrieved_tenant.active)

    def test_tenant_transaction_model(self):
        # Create a test tenant
        tenant = Tenant(
            name='John',
            code='001',
            main_unit_no='A-101',
            property_name='Tower A',
            general_contact='John Doe',
            telephone='123-456-7890',
            lease_start_date='2022-01-01',
            lease_end_date='2023-12-31',
            vacate_date=None,
            active=True
        )

        with app.app_context():
            # Add the tenant to the session and commit the changes
            db.session.add(tenant)
            db.session.commit()

            # Create a test tenant transaction
            tenant_transaction = TenantTransaction(
                tenant_id=tenant.id,
                transaction_type='Rent',
                transaction_date='2022-01-05',
                amount=1000.0
            )

            # Add the transaction to the session and commit the changes
            db.session.add(tenant_transaction)
            db.session.commit()

            # Retrieve the tenant transaction from the database
            retrieved_transaction = TenantTransaction.query.first()

            # Perform assertions to verify the correctness of the retrieved tenant transaction
            self.assertEqual(retrieved_transaction.tenant_id, tenant.id)
            self.assertEqual(retrieved_transaction.transaction_type, 'Rent')
            self.assertEqual(str(retrieved_transaction.transaction_date), '2022-01-05')
            self.assertEqual(retrieved_transaction.amount, 1000.0)

if __name__ == '__main__':
    unittest.main()