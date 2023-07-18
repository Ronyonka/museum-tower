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
        for row in df.iterrows():
            if 'tenant' in str(row[0]).lower():
                # Create or update the Tenant model
                tenant = Tenant()
                tenant.name = row[1]
                tenant.code = row[3]
                tenant.main_unit_no = row[5]
                tenant.property_name = row[7]
                tenant.general_contact = row[9] if not pd.isnull(row[9]) and row[9] != "" else None
                tenant.telephone = row[11] if not pd.isnull(row[11]) and row[11] != "" else None
                tenant.lease_start_date = (
                    pd.to_datetime(row[13]).to_pydatetime() if not pd.isnull(row[13]) else None
                )
                tenant.lease_end_date = (
                    pd.to_datetime(row[15]).to_pydatetime() if not pd.isnull(row[15]) else None
                )
                tenant.vacate_date = (
                    pd.to_datetime(row[17]).to_pydatetime() if not pd.isnull(row[17]) else None
                )
                if row[7] == "":
                    tenant.active = True
                else:
                    tenant.active = False
                db.session.add(tenant)
                
                tenant_id = tenant.id
            else:
                if row[0] == 'Software supplied by: MDA Property Systems www.mdapropsys.com':
                    break
                transaction= TenantTransaction(
                    tenant_id = tenant_id,
                    period=row[0],
                    transaction_date=(
                    pd.to_datetime(row[1]).to_pydatetime() if not pd.isnull(row[1]) else None
                ),

                    transaction=row[2] if not pd.isnull(row[2]) and row[2] != "" else None,
                    transaction_type=row[3] if not pd.isnull(row[3]) and row[3] != "" else None,
                    tax=float(row[4]) if pd.notnull(row[4]) else None,
                    remarks=row[5] if not pd.isnull(row[5]) and row[5] != "" else None,
                    exclusive=float(row[6]) if pd.notnull(row[6]) else None,
                    tax_amount=float(row[7]) if pd.notnull(row[7]) else None,
                    inclusive=float(row[8]) if pd.notnull(row[8]) else None
                )
                db.session.add(transaction)

        db.session.commit()
        print("Data fully added to the database!")

file_path = './data/The Museum Tower Middle Block 201901-202212.xlsx'     
parse_excel_data(file_path)
