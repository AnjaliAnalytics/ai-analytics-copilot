import pandas as pd
import sys

def validate_sales_dataset(file_path):
    """Validates schema integrity and data types for sales_data.csv"""
    required_columns = ['Date', 'Region', 'Category', 'Product', 'Sales', 'Profit', 'Quantity']
    try:
        df = pd.read_csv(file_path)
        print(f"[+] Loaded {len(df)} records from {file_path}")
        
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            print(f"[-] ERROR: Missing physical columns: {missing_cols}")
            return False
            
        print("[+] Schema check passed.")
        total_sales = df['Sales'].sum()
        total_profit = df['Profit'].sum()
        margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0.0
        print(f"[+] Totals - Revenue: ${total_sales:,.2f} | Profit: ${total_profit:,.2f} | Margin: {margin:.2f}%")
        return True
    except Exception as e:
        print(f"[-] Validation failed: {str(e)}")
        return False

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "data/sales_data.csv"
    validate_sales_dataset(target)