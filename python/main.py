from fastapi import FastAPI
from pydantic import BaseModel  # リクエストbodyを定義するために必要
from typing import List  # ネストされたBodyを定義するために必要
import pandas as pd
import os, asyncio
import config
app = FastAPI()

# リクエストbodyを定義
class Data(BaseModel):
    test: int
    name: str

# @app.get("/")
# def home():
#     return {"test"}

# シンプルなJSON Bodyの受け取り
@app.post("/upload/")
# 上で定義したUserモデルのリクエストbodyをuserで受け取る
# user = {"user_id": 1, "name": "太郎"}
async def create_user(user: Data):

    df_old = pd.read_csv(f'{config.root}/data/old_price_data.csv')
    df_new = pd.read_csv(f'{config.root}/data/new_price_data.csv')

    print(df_old)
    count = 0
    for new_index, new_row in df_new.iterrows():
        new_JAN = new_row['商品コード']
        new_PRICE = new_row['商品単価']

        for old_index, old_row in df_old.iterrows():
            old_JAN = old_row["商品コード"]
            old_PRICE = old_row["商品単価"]

            if old_JAN == new_JAN:
                df_old.loc[old_index, "商品単価"] = new_PRICE
                count += 1
                print(f"{count}---{old_PRICE} -> {new_PRICE} | {old_JAN}={new_JAN}")

    print("done")

    os.makedirs(f"{config.root}/dist", exist_ok=True)

    df_old.to_csv(f'{config.root}/dist/smaregi_upload_data.csv', encoding = 'shift_jis', index=False)

    print("ACTIVE")
    # レスポンスbody
    return {"res": "ok", "ID": user.test, "名前": user.name}

"""
# ネストされたJSON Bodyの受け取り
@app.post("/users/")
# 上で定義したUserモデルのリクエストbodyをリストに入れた形で受け取る
# users = [{"user_id": 1, "name": "太郎"},{"user_id": 2, "name": "次郎"}]
def create_users(users: List[User]):
    new_users = []
    for user in users:
        new_users.append({"res": "ok", "ID": user.user_id, "名前": user.name})
    # 整形したデータをレスポンスbodyを送信
    return new_users
"""