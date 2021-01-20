import pytest
import json
users = json.loads(open('./users.test.json', 'r').read())

class TestUserPasswordWithParam(object):
    @pytest.fixture(params=users)
    def user(self, request):
        return request.param

    def test_user_password(self, user):
        passwd = user['password']
        msg = "user %s has a weak password" % (user['name'])
        # fixture with params: it will loop through all params with checking every each assert, then return the final result
        assert len(passwd) >= 6
        assert passwd != 'password', msg
        assert passwd != 'password123', msg