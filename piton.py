import random
from nose import nose

def run():
    print("Bombardeen ubisoft")
    Nro = random.randint(1, 16)
    Ep01 = [1,3,6,9]
    Ep02 = [2,5,8,10]
    Ep03 = [4,7,11,12]
    Ep04 = [13,14,15,16]
    if Nro in Ep01:
        print("Qwen haces tus momos en leage of legends")
    elif Nro in Ep02:
        print("Bombardeen Ubisoft")
    elif Nro in Ep03:
        print("I believe in Rei chiquita Supremacy")
    elif Nro in Ep04:
        print("ASFSFSDfedsa")

    print(Nro)
    nose(Nro)