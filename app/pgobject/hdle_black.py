from selenium.common.exceptions import NoSuchElementException



def handle_black(func):
    def wrapper(*args, **kwargs):
        _bolck_list = []
        from app.pgobject.pagebase import Pagebase
        instance: Pagebase = args[0]
        try:
            ele = func(*args, **kwargs)
            return ele
        except NoSuchElementException as e:
            if instance._error_count > instance._error_max_num:
                instance._error_count =0
                raise e
            instance._error_count += 1
            for ele in _bolck_list:
                eles = instance.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper


