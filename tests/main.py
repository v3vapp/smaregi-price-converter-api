from fastapi import FastAPI
from pydantic import BaseModel  # リクエストbodyを定義するために必要
from typing import List  # ネストされたBodyを定義するために必要
import  pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent.joinpath('data/testdata.csv'))

print(df)