import pandas as pd
from app.models import Tenant, TenantTransaction
from datetime import datetime
from app import app, db





def parse_excel_data(file_path):
    with app.app_context():

        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path)
        print("Give me a moment to Normalize this Data!")

        # Loop through each row in the DataFrame
        for index, row in df.iterrows():
            if 'tenant' in str(row[0]).lower():
                # Create or update the Tenant model
                tenant = Tenant()
                tenant.name = row[1]
                tenant.code = row[3]
                tenant.main_unit_no = row[5]
                tenant.property_name = row[7]
                tenant.general_contact = row[9]
                tenant.telephone = row[11]
                tenant.lease_start_date =row[13]
                tenant.lease_end_date = row[15]
                tenant.vacate_date = row[17]
                if row[7] == "":
                    tenant.active = True
                else:
                    tenant.active = False
                db.session.add(tenant)
                
                tenant_id = tenant.id

            else:
                transaction= TenantTransaction(
                    tenant_id = tenant_id,
                    period=row[0],
                    transaction_date=row[1],
                    transaction=row[2],
                    transaction_type=row[3],
                    tax=row[4],
                    remarks=row[5],
                    exclusive=row[6],
                    tax_amount=row[7],
                    inclusive=row[8]
                )
                db.session.add(transaction)
            if str(row[0]).lower() == 'software supplied by: mda Property systems www.mdapropsys.com':
                break

file_path = './data/The Museum Tower Middle Block 201901-202212.xlsx'     
with app.app_context():
    parse_excel_data(file_path)
    db.session.commit()
    print("Completed Normalizing of the Data!")
# Specify the file path of the Excel file


# Call the parse_excel_data function with the file path



