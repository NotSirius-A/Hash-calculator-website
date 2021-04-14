import hashlib

def calculate_hashes(string):
    rv = {
        'md-5': '',
        'SHA-1': '',
        'SHA-256': '',
    }

    #return an empty dict when string is empty
    if not string or string == None:
        return rv 

    encoded_string = bytes(string, 'utf-8')

    m = hashlib.sha1()
    m.update(encoded_string)
    rv.update({
        'SHA-1': m.hexdigest()
        })

    n = hashlib.sha256()
    n.update(encoded_string)
    rv.update({
        'SHA-256': n.hexdigest()
        })

    p = hashlib.md5()
    p.update(encoded_string)
    rv.update({
        'md-5': p.hexdigest()
        })

    return rv

