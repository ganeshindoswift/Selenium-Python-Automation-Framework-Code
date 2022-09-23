import string
import random
random_domain_list=['yahoo.com', 'gmail.com', 'hotmail.com', 'ril.com']
email_charater_length=10
total_noof_email=20
letters=string.ascii_lowercase
all_email=[]
for email in range(20):
    random_domain=random.choice(random_domain_list)
    random_string="".join(random.choice(letters) for i in range(email_charater_length))
    random_email=random_string +'@'+random_domain
    all_email.append(random_email)
print(all_email)