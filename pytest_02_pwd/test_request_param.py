import pytest
import smtplib

@pytest.fixture(scope="module",
                params=["smtp.gmail.com", "mail.python.org"])
def smtp(request):
    smtp = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp
    print ("finalizing %s" % smtp)
    smtp.close()