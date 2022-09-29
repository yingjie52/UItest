import logging

from core.case import create_case
from core.data import data_by_excel
from pathlib import Path

# data=data_by_excel(r'D:\AAxiangmu\uiautomator2\testcases\test_app.xlsx')
# TestA=create_case(data)

test_dir=Path(__file__).parent
logger=logging.getLogger(__name__)
_case_count=0
file_list=test_dir.glob('test_*.xlsx')


for file in file_list:
    data=data_by_excel(file)
    for case,suite_name in create_case(data,file):
        _case_count+=1
        globals()[f'Test_{_case_count}_{suite_name}']=case
logger.info('所有excel文件测试用例生成成功')

