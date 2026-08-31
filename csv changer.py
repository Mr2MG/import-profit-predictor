# # import pandas as pd
# #
# # # 1. Load CSV using the auto-detected separator that worked in the debug script
# # try:
# #     df = pd.read_csv('importation-v1(not completed).csv', sep=None, engine='python', encoding='cp1256', skipinitialspace=True)
# # except Exception as e:
# #     print("Error reading file:", e)
# #     exit()
# #
# # # Drop empty columns caused by trailing pipes
# # df = df.dropna(axis=1, how='all')
# # # Clean column names
# # df.columns = df.columns.str.strip()
# #
# # print("Columns loaded successfully. Processing data...")
# #
# # # 2. Clean numeric columns (remove commas so math works)
# # for col in ['weight-kg', 'worth-usd']:
# #     if col in df.columns:
# #         df[col] = df[col].astype(str).str.replace(',', '', regex=False).str.strip()
# #         df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
# #
# # # 3. Add Short HS Names
# # def get_hs_name(hs_code):
# #     hs_str = str(hs_code).strip().split('.')[0]
# #     if hs_str.startswith('9887') or hs_str.startswith('9884'): return 'Vehicle/Chassis/Tractor Parts'
# #     if hs_str.startswith('8703'): return 'Passenger Vehicles'
# #     if hs_str.startswith('8708'): return 'Vehicle Parts & Accessories'
# #     if hs_str.startswith('8414'): return 'Compressors & Pumps'
# #     if hs_str.startswith('8479'): return 'Machines & Mechanical Appliances'
# #     if hs_str.startswith('8541') or hs_str.startswith('8542'): return 'Semiconductors & Solar Cells'
# #     if hs_str.startswith('8517') or hs_str.startswith('8528'): return 'Telecom & Display Equipment'
# #     if hs_str.startswith('72'): return 'Iron & Steel Products'
# #     if hs_str.startswith('73'): return 'Articles of Iron & Steel'
# #     if hs_str.startswith('39'): return 'Plastics & Polymers'
# #     if hs_str.startswith('40'): return 'Rubber & Tires'
# #     if hs_str.startswith('84'): return 'Industrial Machinery'
# #     if hs_str.startswith('85'): return 'Electrical Equipment'
# #     if hs_str.startswith('27'): return 'Mineral Fuels & Oils'
# #     if hs_str.startswith('38'): return 'Chemical Products'
# #     if hs_str.startswith('48'): return 'Paper & Paperboard'
# #     if hs_str.startswith('29'): return 'Organic Chemicals'
# #     return 'General Goods'
# #
# # df['HS-Short-Name'] = df['HS'].apply(get_hs_name)
# #
# # # 4. Create and Fill Distance, s-cost, and delivery-days
# # def get_distance(country):
# #     country_str = str(country).strip().lower()
# #     if country_str == 'china': return 10500
# #     if country_str == 'uae': return 400
# #     return 5000
# #
# # def get_delivery_days(country):
# #     country_str = str(country).strip().lower()
# #     if country_str == 'china': return 30
# #     if country_str == 'uae': return 5
# #     return 15
# #
# # def get_shipping_cost(row):
# #     weight = row['weight-kg']
# #     country = str(row['country']).strip().lower()
# #     if country == 'china': return weight * 0.15
# #     if country == 'uae': return weight * 0.08
# #     return weight * 0.12
# #
# # df['distance'] = df['country'].apply(get_distance)
# # df['delivery-days'] = df['country'].apply(get_delivery_days)
# # df['s-cost'] = df.apply(get_shipping_cost, axis=1).round(2)
# #
# # # 5. Create and Fill Tariff
# # def get_tariff(hs_code):
# #     hs_str = str(hs_code).strip().split('.')[0]
# #     if hs_str.startswith('9887') or hs_str.startswith('9884'): return '40%'
# #     if hs_str.startswith('8703'): return '45%'
# #     if hs_str.startswith('8708'): return '25%'
# #     if hs_str.startswith('27'): return '5%'
# #     if hs_str.startswith('72') or hs_str.startswith('73'): return '10%'
# #     if hs_str.startswith('84') or hs_str.startswith('85'): return '15%'
# #     if hs_str.startswith('39') or hs_str.startswith('40'): return '20%'
# #     if hs_str.startswith('48'): return '15%'
# #     if hs_str.startswith('29') or hs_str.startswith('38'): return '15%'
# #     return '20%'
# #
# # df['tariff'] = df['HS'].apply(get_tariff)
# #
# # # 6. Create and Fill VAT
# # df['VAT'] = '9%'
# #
# # # 7. Save to a new CSV
# # df.to_csv('importation-v1(COMPLETED).csv', index=False, sep=',', encoding='utf-8-sig')
# # print("\nSuccess! Your file has been processed and saved as 'importation-v1(COMPLETED).csv'")
# # import pandas as pd
# #
# # # Auto-detect if the file uses commas, pipes, or tabs
# # try:
# #     df = pd.read_csv('importation-v1(not completed).csv', sep=None, engine='python', encoding='cp1256', skipinitialspace=True)
# # except Exception as e:
# #     print("Error reading file:", e)
# #     exit()
# #
# # # Clean up empty columns
# # df = df.dropna(axis=1, how='all')
# #
# # print("====================")
# # print("COLUMNS DETECTED:")
# # print(df.columns.tolist())
# # print("====================")
# # print("FIRST ROW DATA:")
# # print(df.iloc[0].tolist())
# # print("====================")
# import pandas as pd
#
# file_path = 'importation-v1(not completed).csv'
# output_path = 'importation-v1(COMPLETED).csv'
#
# # 1. Auto-detect the correct encoding to prevent "????" in Persian text
# df = None
# encodings_to_try = ['utf-8-sig', 'utf-8', 'windows-1256', 'cp1256', 'latin1']
#
# for enc in encodings_to_try:
#     try:
#         df = pd.read_csv(file_path, sep=None, engine='python', encoding=enc, skipinitialspace=True)
#         print(f"Successfully read file using encoding: {enc}")
#         break
#     except Exception as e:
#         continue
#
# if df is None:
#     print("Could not read the file. Please check the file name and path.")
#     exit()
#
# # Drop empty columns and clean column names
# df = df.dropna(axis=1, how='all')
# df.columns = df.columns.str.strip()
#
# # 2. Clean numeric columns (remove commas like 11,179,099 -> 11179099 so math works)
# def clean_numeric(col_name):
#     if col_name in df.columns:
#         df[col_name] = df[col_name].astype(str).str.replace(',', '', regex=False).str.strip()
#         df[col_name] = pd.to_numeric(df[col_name], errors='coerce').fillna(0)
#
# clean_numeric('weight-kg')
# clean_numeric('worth-usd')
#
# # 3. Add Short HS Names
# def get_hs_name(hs_code):
#     hs_str = str(hs_code).strip().split('.')[0]
#     if hs_str.startswith('9887') or hs_str.startswith('9884'): return 'Vehicle/Chassis/Tractor Parts'
#     if hs_str.startswith('8703'): return 'Passenger Vehicles'
#     if hs_str.startswith('8708'): return 'Vehicle Parts & Accessories'
#     if hs_str.startswith('8414'): return 'Compressors & Pumps'
#     if hs_str.startswith('8479'): return 'Machines & Mechanical Appliances'
#     if hs_str.startswith('8541') or hs_str.startswith('8542'): return 'Semiconductors & Solar Cells'
#     if hs_str.startswith('8517') or hs_str.startswith('8528'): return 'Telecom & Display Equipment'
#     if hs_str.startswith('72'): return 'Iron & Steel Products'
#     if hs_str.startswith('73'): return 'Articles of Iron & Steel'
#     if hs_str.startswith('39'): return 'Plastics & Polymers'
#     if hs_str.startswith('40'): return 'Rubber & Tires'
#     if hs_str.startswith('84'): return 'Industrial Machinery'
#     if hs_str.startswith('85'): return 'Electrical Equipment'
#     if hs_str.startswith('27'): return 'Mineral Fuels & Oils'
#     if hs_str.startswith('38'): return 'Chemical Products'
#     if hs_str.startswith('48'): return 'Paper & Paperboard'
#     if hs_str.startswith('29'): return 'Organic Chemicals'
#     return 'General Goods'
#
# df['HS-Short-Name'] = df['HS'].apply(get_hs_name)
#
# # 4. Create and Fill Distance, s-cost, and delivery-days
# def get_distance(country):
#     country_str = str(country).strip().lower()
#     if country_str == 'china': return 10500
#     if country_str == 'uae': return 400
#     return 5000
#
# def get_delivery_days(country):
#     country_str = str(country).strip().lower()
#     if country_str == 'china': return 30
#     if country_str == 'uae': return 5
#     return 15
#
# def get_shipping_cost(row):
#     weight = row['weight-kg']
#     country = str(row['country']).strip().lower()
#     if country == 'china': return weight * 0.15
#     if country == 'uae': return weight * 0.08
#     return weight * 0.12
#
# df['distance'] = df['country'].apply(get_distance)
# df['delivery-days'] = df['country'].apply(get_delivery_days)
# df['s-cost'] = df.apply(get_shipping_cost, axis=1).round(2)
#
# # 5. Create and Fill Tariff and VAT
# def get_tariff(hs_code):
#     hs_str = str(hs_code).strip().split('.')[0]
#     if hs_str.startswith('9887') or hs_str.startswith('9884'): return '40%'
#     if hs_str.startswith('8703'): return '45%'
#     if hs_str.startswith('8708'): return '25%'
#     if hs_str.startswith('27'): return '5%'
#     if hs_str.startswith('72') or hs_str.startswith('73'): return '10%'
#     if hs_str.startswith('84') or hs_str.startswith('85'): return '15%'
#     if hs_str.startswith('39') or hs_str.startswith('40'): return '20%'
#     if hs_str.startswith('48'): return '15%'
#     if hs_str.startswith('29') or hs_str.startswith('38'): return '15%'
#     return '20%'
#
# df['tariff'] = df['HS'].apply(get_tariff)
# df['VAT'] = '9%'
#
# # 6. MATH: Convert Percentages to USD amounts and Calculate Total Cost
# # First, convert "40%" to 0.40 so we can do math with it
# def parse_percent(val):
#     if isinstance(val, str) and '%' in val:
#         return float(val.replace('%', '').strip()) / 100.0
#     return 0.0
#
# df['tariff_pct'] = df['tariff'].apply(parse_percent)
# df['vat_pct'] = df['VAT'].apply(parse_percent)
#
# # Calculate USD Amounts
# # Tariff is based on the item's worth
# df['Tariff-Amount-USD'] = (df['worth-usd'] * df['tariff_pct']).round(2)
#
# # VAT is usually calculated on (Item Worth + Tariff Amount)
# df['VAT-Amount-USD'] = ((df['worth-usd'] + df['Tariff-Amount-USD']) * df['vat_pct']).round(2)
#
# # Total Cost to Importer = Item Worth + Tariff Amount + VAT Amount + Shipping Cost
# df['Total-Import-Cost-USD'] = (df['worth-usd'] + df['Tariff-Amount-USD'] + df['VAT-Amount-USD'] + df['s-cost']).round(2)
#
# # Remove the temporary percentage columns to keep the CSV clean
# df = df.drop(columns=['tariff_pct', 'vat_pct'])
#
# # 7. Save to a new CSV
# df.to_csv(output_path, index=False, sep=',', encoding='utf-8-sig')
# print(f"\nSuccess! Your file has been processed and saved as '{output_path}'")
# print("New columns added: Tariff-Amount-USD, VAT-Amount-USD, Total-Import-Cost-USD")

#
# import pandas as pd
#
# file_path = 'importation-v1(not completed).csv'
# output_path = 'importation-v1(COMPLETED).csv'
#
# # 1. Auto-detect the correct encoding to prevent "????" in Persian text
# df = None
# encodings_to_try = ['utf-8-sig', 'utf-8', 'windows-1256', 'cp1256', 'latin1']
#
# for enc in encodings_to_try:
#     try:
#         df = pd.read_csv(file_path, sep=None, engine='python', encoding=enc, skipinitialspace=True)
#         print(f"Successfully read file using encoding: {enc}")
#         break
#     except Exception as e:
#         continue
#
# if df is None:
#     print("Could not read the file. Please check the file name and path.")
#     exit()
#
# # Drop empty columns and clean column names
# df = df.dropna(axis=1, how='all')
# df.columns = df.columns.str.strip()
#
# # 2. Clean numeric columns (remove commas like 11,179,099 -> 11179099 so math works)
# def clean_numeric(col_name):
#     if col_name in df.columns:
#         df[col_name] = df[col_name].astype(str).str.replace(',', '', regex=False).str.strip()
#         df[col_name] = pd.to_numeric(df[col_name], errors='coerce').fillna(0)
#
# clean_numeric('weight-kg')
# clean_numeric('worth-usd')
#
# # 3. Add Short HS Names
# def get_hs_name(hs_code):
#     hs_str = str(hs_code).strip().split('.')[0]
#     if hs_str.startswith('9887') or hs_str.startswith('9884'): return 'Vehicle/Chassis/Tractor Parts'
#     if hs_str.startswith('8703'): return 'Passenger Vehicles'
#     if hs_str.startswith('8708'): return 'Vehicle Parts & Accessories'
#     if hs_str.startswith('8414'): return 'Compressors & Pumps'
#     if hs_str.startswith('8479'): return 'Machines & Mechanical Appliances'
#     if hs_str.startswith('8541') or hs_str.startswith('8542'): return 'Semiconductors & Solar Cells'
#     if hs_str.startswith('8517') or hs_str.startswith('8528'): return 'Telecom & Display Equipment'
#     if hs_str.startswith('72'): return 'Iron & Steel Products'
#     if hs_str.startswith('73'): return 'Articles of Iron & Steel'
#     if hs_str.startswith('39'): return 'Plastics & Polymers'
#     if hs_str.startswith('40'): return 'Rubber & Tires'
#     if hs_str.startswith('84'): return 'Industrial Machinery'
#     if hs_str.startswith('85'): return 'Electrical Equipment'
#     if hs_str.startswith('27'): return 'Mineral Fuels & Oils'
#     if hs_str.startswith('38'): return 'Chemical Products'
#     if hs_str.startswith('48'): return 'Paper & Paperboard'
#     if hs_str.startswith('29'): return 'Organic Chemicals'
#     return 'General Goods'
#
# df['HS-Short-Name'] = df['HS'].apply(get_hs_name)
#
# # 4. Create and Fill Distance, s-cost, and delivery-days
# def get_distance(country):
#     country_str = str(country).strip().lower()
#     if country_str == 'china': return 10500
#     if country_str == 'uae': return 400
#     return 5000
#
# def get_delivery_days(country):
#     country_str = str(country).strip().lower()
#     if country_str == 'china': return 30
#     if country_str == 'uae': return 5
#     return 15
#
# def get_shipping_cost(row):
#     weight = row['weight-kg']
#     country = str(row['country']).strip().lower()
#     if country == 'china': return weight * 0.15
#     if country == 'uae': return weight * 0.08
#     return weight * 0.12
#
# df['distance'] = df['country'].apply(get_distance)
# df['delivery-days'] = df['country'].apply(get_delivery_days)
# df['s-cost'] = df.apply(get_shipping_cost, axis=1).round(2)
#
# # 5. Create and Fill Tariff and VAT
# def get_tariff(hs_code):
#     hs_str = str(hs_code).strip().split('.')[0]
#     if hs_str.startswith('9887') or hs_str.startswith('9884'): return '40%'
#     if hs_str.startswith('8703'): return '45%'
#     if hs_str.startswith('8708'): return '25%'
#     if hs_str.startswith('27'): return '5%'
#     if hs_str.startswith('72') or hs_str.startswith('73'): return '10%'
#     if hs_str.startswith('84') or hs_str.startswith('85'): return '15%'
#     if hs_str.startswith('39') or hs_str.startswith('40'): return '20%'
#     if hs_str.startswith('48'): return '15%'
#     if hs_str.startswith('29') or hs_str.startswith('38'): return '15%'
#     return '20%'
#
# df['tariff'] = df['HS'].apply(get_tariff)
# df['VAT'] = '9%'
#
# # 6. MATH: Convert Percentages to USD amounts and Calculate Total Cost
# def parse_percent(val):
#     if isinstance(val, str) and '%' in val:
#         return float(val.replace('%', '').strip()) / 100.0
#     return 0.0
#
# df['tariff_pct'] = df['tariff'].apply(parse_percent)
# df['vat_pct'] = df['VAT'].apply(parse_percent)
#
# # Tariff is based on the item's total worth
# df['Tariff-Amount-USD'] = (df['worth-usd'] * df['tariff_pct']).round(2)
#
# # VAT is calculated on (Item Worth + Tariff Amount)
# df['VAT-Amount-USD'] = ((df['worth-usd'] + df['Tariff-Amount-USD']) * df['vat_pct']).round(2)
#
# # Total Cost to Importer = Item Worth + Tariff Amount + VAT Amount + Shipping Cost
# df['Total-Import-Cost-USD'] = (df['worth-usd'] + df['Tariff-Amount-USD'] + df['VAT-Amount-USD'] + df['s-cost']).round(2)
#
# # 7. MATH: Calculate Profit Per KG
# # Assuming a realistic 25% profit margin on the total import cost
# profit_margin = 0.25
# df['Profit-Margin-Pct'] = '25%'
#
# # First find the cost per kg (Total Cost divided by Weight)
# # Using a lambda function to prevent Division by Zero errors if weight is 0
# df['Cost-per-kg-USD'] = df.apply(lambda row: (row['Total-Import-Cost-USD'] / row['weight-kg']) if row['weight-kg'] != 0 else 0, axis=1).round(2)
#
# # Profit per kg is simply the Cost per kg multiplied by the profit margin
# df['Profit-per-kg-USD'] = (df['Cost-per-kg-USD'] * profit_margin).round(2)
#
# # Remove the temporary percentage columns to keep the CSV clean
# df = df.drop(columns=['tariff_pct', 'vat_pct'])
#
# # 8. Save to a new CSV
# df.to_csv(output_path, index=False, sep=',', encoding='utf-8-sig')
# print(f"\nSuccess! Your file has been processed and saved as '{output_path}'")
# print("New columns added: Tariff-Amount-USD, VAT-Amount-USD, Total-Import-Cost-USD, Profit-Margin-Pct, Cost-per-kg-USD, Profit-per-kg-USD")

import pandas as pd

file_path = 'importation-v1(not completed).csv'
output_path = 'importation-v1(COMPLETED).csv'

# 1. Auto-detect the correct encoding to prevent "????" in Persian text
df = None
encodings_to_try = ['utf-8-sig', 'utf-8', 'windows-1256', 'cp1256', 'latin1']

for enc in encodings_to_try:
    try:
        df = pd.read_csv(file_path, sep=None, engine='python', encoding=enc, skipinitialspace=True)
        print(f"Successfully read file using encoding: {enc}")
        break
    except Exception as e:
        continue

if df is None:
    print("Could not read the file. Please check the file name and path.")
    exit()

# Drop empty columns and clean column names
df = df.dropna(axis=1, how='all')
df.columns = df.columns.str.strip()

# 2. Clean numeric columns (remove commas like 11,179,099 -> 11179099 so math works)
def clean_numeric(col_name):
    if col_name in df.columns:
        df[col_name] = df[col_name].astype(str).str.replace(',', '', regex=False).str.strip()
        df[col_name] = pd.to_numeric(df[col_name], errors='coerce').fillna(0)

clean_numeric('weight-kg')
clean_numeric('worth-usd')

# 3. Add Short HS Names
def get_hs_name(hs_code):
    hs_str = str(hs_code).strip().split('.')[0]
    if hs_str.startswith('9887') or hs_str.startswith('9884'): return 'Vehicle/Chassis/Tractor Parts'
    if hs_str.startswith('8703'): return 'Passenger Vehicles'
    if hs_str.startswith('8708'): return 'Vehicle Parts & Accessories'
    if hs_str.startswith('8414'): return 'Compressors & Pumps'
    if hs_str.startswith('8479'): return 'Machines & Mechanical Appliances'
    if hs_str.startswith('8541') or hs_str.startswith('8542'): return 'Semiconductors & Solar Cells'
    if hs_str.startswith('8517') or hs_str.startswith('8528'): return 'Telecom & Display Equipment'
    if hs_str.startswith('72'): return 'Iron & Steel Products'
    if hs_str.startswith('73'): return 'Articles of Iron & Steel'
    if hs_str.startswith('39'): return 'Plastics & Polymers'
    if hs_str.startswith('40'): return 'Rubber & Tires'
    if hs_str.startswith('84'): return 'Industrial Machinery'
    if hs_str.startswith('85'): return 'Electrical Equipment'
    if hs_str.startswith('27'): return 'Mineral Fuels & Oils'
    if hs_str.startswith('38'): return 'Chemical Products'
    if hs_str.startswith('48'): return 'Paper & Paperboard'
    if hs_str.startswith('29'): return 'Organic Chemicals'
    return 'General Goods'

df['HS-Short-Name'] = df['HS'].apply(get_hs_name)

# 4. Create and Fill Distance, s-cost, and delivery-days
def get_distance(country):
    country_str = str(country).strip().lower()
    if country_str == 'china': return 10500
    if country_str == 'uae': return 400
    return 5000

def get_delivery_days(country):
    country_str = str(country).strip().lower()
    if country_str == 'china': return 30
    if country_str == 'uae': return 5
    return 15

def get_shipping_cost(row):
    weight = row['weight-kg']
    country = str(row['country']).strip().lower()
    if country == 'china': return weight * 0.15
    if country == 'uae': return weight * 0.08
    return weight * 0.12

df['distance'] = df['country'].apply(get_distance)
df['delivery-days'] = df['country'].apply(get_delivery_days)
df['s-cost'] = df.apply(get_shipping_cost, axis=1).round(2)

# 5. Create and Fill Tariff and VAT
def get_tariff(hs_code):
    hs_str = str(hs_code).strip().split('.')[0]
    if hs_str.startswith('9887') or hs_str.startswith('9884'): return '40%'
    if hs_str.startswith('8703'): return '45%'
    if hs_str.startswith('8708'): return '25%'
    if hs_str.startswith('27'): return '5%'
    if hs_str.startswith('72') or hs_str.startswith('73'): return '10%'
    if hs_str.startswith('84') or hs_str.startswith('85'): return '15%'
    if hs_str.startswith('39') or hs_str.startswith('40'): return '20%'
    if hs_str.startswith('48'): return '15%'
    if hs_str.startswith('29') or hs_str.startswith('38'): return '15%'
    return '20%'

df['tariff'] = df['HS'].apply(get_tariff)
df['VAT'] = '9%'

# 6. MATH: Convert Percentages to USD amounts and Calculate Total Cost
def parse_percent(val):
    if isinstance(val, str) and '%' in val:
        return float(val.replace('%', '').strip()) / 100.0
    return 0.0

df['tariff_pct'] = df['tariff'].apply(parse_percent)
df['vat_pct'] = df['VAT'].apply(parse_percent)

# Tariff is based on the item's total worth
df['Tariff-Amount-USD'] = (df['worth-usd'] * df['tariff_pct']).round(2)

# VAT is calculated on (Item Worth + Tariff Amount)
df['VAT-Amount-USD'] = ((df['worth-usd'] + df['Tariff-Amount-USD']) * df['vat_pct']).round(2)

# Total Cost to Importer = Item Worth + Tariff Amount + VAT Amount + Shipping Cost
df['Total-Import-Cost-USD'] = (df['worth-usd'] + df['Tariff-Amount-USD'] + df['VAT-Amount-USD'] + df['s-cost']).round(2)

# 7. MATH: Calculate Profits
# Assuming a realistic 25% profit margin on the total import cost
profit_margin = 0.25
df['Profit-Margin-Pct'] = '25%'

# First find the cost per kg (Total Cost divided by Weight)
df['Cost-per-kg-USD'] = df.apply(lambda row: (row['Total-Import-Cost-USD'] / row['weight-kg']) if row['weight-kg'] != 0 else 0, axis=1).round(2)

# Profit per kg is simply the Cost per kg multiplied by the profit margin
df['Profit-per-kg-USD'] = (df['Cost-per-kg-USD'] * profit_margin).round(2)

# NEW: Total Profit for the whole shipment = Total Import Cost * Profit Margin
df['Total-Import-Profit-USD'] = (df['Total-Import-Cost-USD'] * profit_margin).round(2)

# Remove the temporary percentage columns to keep the CSV clean
df = df.drop(columns=['tariff_pct', 'vat_pct'])

# 8. Save to a new CSV
df.to_csv(output_path, index=False, sep=',', encoding='utf-8-sig')
print(f"\nSuccess! Your file has been processed and saved as '{output_path}'")
print("New columns added: Tariff-Amount-USD, VAT-Amount-USD, Total-Import-Cost-USD, Profit-Margin-Pct, Cost-per-kg-USD, Profit-per-kg-USD, Total-Import-Profit-USD")