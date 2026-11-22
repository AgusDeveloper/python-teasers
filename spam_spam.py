from email.message import EmailMessage

msg = EmailMessage()
msg['From'] = 'xyz@someCompany.com'
msg['To'] = 'ABC <abc@privateCompany.com>'
msg.set_content('''\
Dear Sir.

I'm here to learn Python.
...
''')
print(msg)