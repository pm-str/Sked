from gcm import GCM


def push_task():
    gcm = GCM("AIzaSyCNREuhmag35fb3Rn6e9C1rAJ6rU22yPLg")
    token = "cCX1n12_POM:APA91bF19khQZvB6PCf8Z_pl91tgyW-wDitX2HOFopwVvYf1FxsV4Wq2ahCRyXSbAvGx4sjEKhKJIhdomdKxeF-xZQCMbm866mg6u5CxY_NdcbC2Q3rNUQKIqkjAj2EHQWZtU8RuTK33"
    gcm.plaintext_request(registration_id=token, data={'title': 'asdfdfd'})
    print(" ***** The message was sent to {}\ntoken - {} ***** ".format('test', token))

push_task()