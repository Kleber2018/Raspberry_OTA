
def atualizar_firmware():
    import subprocess
    try:
        subprocess.run(["sudo", "python3", "/home/update_firmware.py"])
        return 1
    except Exception as e :
        print('erro na atualização', e)
        return 0


#fazer uma lógica sua apra executar essa linha e atualizar/parear com o github
atualizar_firmware()



try:

    tempFile = open( '/etc/loader/load/cloud.conf')
    jwt_user = tempFile.read()
    tempFile.close()
    tempVFile = open( '/etc/loader/loader/version.conf')
    version_local = tempVFile.readlines()
    tempVFile.close()
    us = auth.verify_and_decode_jwt(jwt_user)
    user = auth_fire.sign_in_with_email_and_password(us['user'], us['key'])
except Exception as e:
    capture_exception(e)
    print('erro de autenticação', e)