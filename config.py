from pathlib import Path
import os

root = Path(__file__).resolve().parent.joinpath()



os.makedirs(f"{root}/dist", exist_ok=True)

if __name__ == "__main__":
    print(root)