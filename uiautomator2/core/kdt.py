import uiautomator2 as u2
import allure
import os


d = u2.connect_usb('emulator-5554')
vars={}

class KeyWord:

    def get_kw_method(self,key):
        f=getattr(self,f'key_{key}',None)
        if not f:
            raise AttributeError(f'不存在关键字：{key}')
        return f

    def key_start_app(self, str):
        d.app_start(str)

    def key_xpath_click(self, ele):
        d.xpath(ele).click()

    def key_click(self,ele):
        d(resourceId=ele).click()

    def key_save_vars(self,ele,a):
        text = d(resourceId = ele).get_text()
        vars[a]=text
        print(vars[a])

    def key_input_vars(self,ele,a):
        value=vars[a]
        print(value)
        d(resourceId = ele).set_text(value)


    def allure_screenshot(self):

        picture_file = os.path.join(os.getcwd(), './reports/report/temp123.png')
        # 截图
        d.screenshot(picture_file)
        allure.attach(open(picture_file, 'rb').read(),
                        '截图',
                        attachment_type = allure.attachment_type.PNG)



