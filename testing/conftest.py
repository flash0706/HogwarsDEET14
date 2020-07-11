import pytest


@pytest.fixture(scope='session', params=['ure1', 'uer2'])
def login(request):
    print("loin")
    print(request.param)
    yield ['usename', 'password']
    print("teardown")


@pytest.fixture()
def self_setup(request):
    print(request.param, '开始计算')
    yield
    print(request.param, '计算结束')