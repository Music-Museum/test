import pandas as pd
import os

# 配置文件路径
input_file = r"/Users/uu/Desktop/工作/KM. EBOM-结构.xlsm"  # 请替换为实际路径
output_file = r"/Users/uu/Desktop/11/11.csv"  # 目标CSV文件路径
sheet_name = "数据源"

def save_csv():
    # 检查目标文件是否已存在
    if os.path.exists(output_file):
        choice = input(f"文件 '{output_file}' 已存在，是否覆盖？(y/n): ").strip().lower()
        if choice != 'y':
            print("操作已取消。")
            return

    # 读取 Excel 文件
    try:
        df = pd.read_excel(input_file, sheet_name=sheet_name, dtype=str)  # 读取为字符串格式
        
        # 处理编码问题
        for col in df.columns:
            df[col] = df[col].apply(lambda x: x.encode('utf-8', errors='ignore').decode('utf-8') if isinstance(x, str) else x)
        
        # 保存为 CSV，添加 BOM 支持
        df.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"文件已成功保存至 {output_file}")
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    save_csv()
