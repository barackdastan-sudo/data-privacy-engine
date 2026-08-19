import pandas as pd
import numpy as np

def anonymize_data(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Data Masking for Name & Email
    if 'Name' in df.columns:
        df['Name'] = df['Name'].astype(str).apply(lambda x: x.split()[0][0] + "*** " + x.split()[-1][0] + "***" if len(x.split()) > 1 else x[0] + "***")
    if 'Email' in df.columns:
        df['Email'] = df['Email'].astype(str).apply(lambda x: x.split("@")[0][0] + "***@" + x.split("@")[-1] if "@" in x else "masked@mail.com")
    if 'Phone' in df.columns:
        df['Phone'] = df['Phone'].astype(str).apply(lambda x: x[:3] + "****" + x[-3:])
    if 'National_ID' in df.columns:
        df['National_ID'] = "REDACTED-ID"
        
    # 2. Differential Privacy for Age (Adding Laplace noise)
    if 'Age' in df.columns:
        df['Age'] = df['Age'].apply(lambda x: int(max(18, min(90, x + np.random.laplace(0, 2)))))
        
    return df
