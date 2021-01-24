from twill.commands import *
#     raise TwillException('no field matches "%s"' % (fieldname,))
# twill.errors.TwillException: no field matches "usernamdhjfjkasdjjkjj"
go('https://www.douban.com/')

fv("1", "username", "yourEmail")
fv("1", "password", "yourPass")

submit('0')
code(200)  # make sure form submission is correct!
