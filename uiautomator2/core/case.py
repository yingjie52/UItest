import time
from pathlib import Path
import allure
import pytest
from core.kdt import KeyWord
import logging
import uiautomator2 as u2
logger = logging.getLogger(__name__)

d = u2.connect_usb('emulator-5554')


def create_case(test_suite:dict,file):

    file_path=Path(file)
    filename=file_path.name


    for suite_name, case_dict in test_suite.items():
        @allure.suite(filename)
        class Test:

            @pytest.mark.parametrize("case",case_dict.items(),ids=case_dict.keys())
            def test_(self,case):
                name=case[0]
                step_list=case[1]
                logger.warning('测试用例开始执行:{suite_name}.{name}')
                kw=KeyWord()
                try:
                    for step in step_list:
                        key=step[2]
                        args=step[3:]
                        logger.info(f'执行关键字：{key=},{args=}')
                        f=kw.get_kw_method(key)

                        with allure.step(step[1]):
                            f(*args)

                            kw.allure_screenshot()

                        logger.debug('关键字执行成功')
                    logger.info(f'测试用例执行完毕:{suite_name}.{name}:测试通过')
                except Exception as e:
                    logger.error(f'测试用例执行完毕:{suite_name}.{name}:测试失败',exc_info = True)
                    raise e

        logger.info(f'生成了测试用例{suite_name}')
        yield Test,suite_name
















