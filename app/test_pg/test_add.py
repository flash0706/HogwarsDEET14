import pytest

from app.test_pg.testbase import Testbase



class Test_add(Testbase):
    file_add ='../data/file_add.yaml'
    file_dele ='../data/file_dele.yaml'
    @pytest.mark.parametrize('gender,num,name', Testbase().yaml(file_add))
    def test_case(self, gender, num, name):
        ele = self.app.start().go_MainActivity().click_cont().add_num().add_manually().add_gender(gender).add_mobynum(num).add_name(name).save().get_toast()
        assert '成功' in ele.text

    @pytest.mark.parametrize('name', Testbase().yaml(file_dele))
    def test_case1(self, name):
        print(name)
        flag =self.app.start().go_MainActivity().click_cont().click_screch().editText(name).clickmore().clickedit().detele().isexistence(name)
        assert flag == False