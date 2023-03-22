# translations function
def translation(photons, detectors):
    message = ""
    for n in range(len(photons)):
        if (photons[n] == 'H') and (detectors[n] == 'R'):
            message += '0'
        if (photons[n] == 'V') and (detectors[n] == 'R'):
            message += '1'
        if (photons[n] == 'E') and (detectors[n] == 'D'):
            message += '0'
        if (photons[n] == 'F') and (detectors[n] == 'D'):
            message += '1'
        if (photons[n] == 'H') and (detectors[n] == 'D'):
            message += '1'
        if (photons[n] == 'V') and (detectors[n] == 'D'):
            message += '0'
        if (photons[n] == 'E') and (detectors[n] == 'R'):
            message += '1'
        if (photons[n] == 'F') and (detectors[n] == 'R'):
            message += '0'
    return message


def create_key(m1, m2):
    key = ""
    for n in range(len(m1)):
        if m1[n] == m2[n]:
            key += m1[n]
    return key


# get ALice info
print("H - horizontal, V - vertical, E - diagonal 1, F - diagonal 2")
alice_photons = input("Alice enter your photons as a string:   ")
print("R - horizontal/vertical, D - diagonal1/diagonal2")
alice_detectors = input("Alice enter your detectors as a string: ")
alice_translation = translation(alice_photons, alice_detectors)
print("Alice translation is:                  ", alice_translation)

# get Bob info
print("R - horizontal/vertical, D - diagonal1/diagonal2")
bob_detectors = input("Bob enter your detectors as a string:   ")
bob_translation = translation(alice_photons, bob_detectors)
print("Bob translations is:                   ", translation(alice_photons, bob_detectors))

# make key
ourkey = create_key(alice_translation, bob_translation)
print("Key is :                               ", ourkey)