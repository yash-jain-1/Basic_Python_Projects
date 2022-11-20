def gen():
    import random
    lower_case = "abcdefghijklmnopqrstuvxyz "
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    number = '1234567890'
    special = '!@#$%^&*<>?/+_-'
    use = lower_case+upper_case+number+special
    leng = 8
    password =''.join(random.sample(use,leng))
    return "generated password:"+password

print(gen())




