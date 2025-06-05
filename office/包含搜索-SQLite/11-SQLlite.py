import pandas as pd
import sqlite3
from pathlib import Path

# 配置路径（与原脚本一致）
input_file = r"\\192.168.251.9\外贸价值链功能产品开发部\功能开发模块\结构工序\胡高高\KM. EBOM-结构.xlsm"
db_file = r"\\192.168.251.9\外贸价值链功能产品开发部\功能开发模块\结构工序\胡高高\11.db"  # 新数据库文件
sheet_name = "数据源"

def init_database():
    # 读取Excel（与原逻辑一致）
    df = pd.read_excel(input_file, sheet_name=sheet_name, dtype=str)
    
    # 创建数据库
    Path(db_file).unlink(missing_ok=True)  # 删除旧数据库（如果存在）
    conn = sqlite3.connect(db_file)
    
    # 导入数据（保留所有列）
    df.to_sql("products", conn, index=False, if_exists="replace")
    
    # 创建搜索索引（加速B/C列查询）
    conn.execute("CREATE INDEX idx_search ON products(物料号, 描述)")
    conn.close()
    print(f"数据库已初始化：{db_file}")

if __name__ == "__main__":
    init_database()
