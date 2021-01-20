import pytest
import json

class TestUserPassword(object):
    @pytest.fixture
    def users(self):
        return json.loads(open('./users.test.json', 'r').read())

    def test_user_password(self, users):

        for user in users:
            passwd = user['password']
            msg = "user %s has a weak password" % (user['name'])
            # if failed at the 1st assert then break
            assert len(passwd) >= 6
            assert passwd != 'password', msg
            assert passwd != 'password123', msg



