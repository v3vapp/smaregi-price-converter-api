import pandas as pd

df_old = pd.read_csv('old_price_data.csv')
df_new = pd.read_csv('new_price_data.csv')

count = 0
for new_index, new_row in df_new.iterrows():
    new_JAN = new_row['JAN']
    new_PRICE = new_row['PRICE']

    for old_index, old_row in df_old.iterrows():
        old_JAN = old_row["商品コード"]
        old_PRICE = old_row["商品単価"]

        if old_JAN == new_JAN:
            df_old.loc[old_index, "商品単価"] = new_PRICE
            count += 1
            print(f"{count}---{old_PRICE} -> {new_PRICE} | {old_JAN}={new_JAN}")

print("done")
df_old.to_csv('dist/SmaregiNewPriceData.csv', encoding = 'shift_jis', index=False) 