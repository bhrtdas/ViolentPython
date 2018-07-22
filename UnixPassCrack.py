import crypt


def testpass(cryptpass):

    print 'cryptpass: ' + cryptpass
    print type(cryptpass)
    salt = cryptpass[0:2]
    print 'salt: ' + salt
    dictfile = open('dictionary.txt', 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        print 'word: ' + word
        cryptword = crypt.crypt(word, salt)
        print cryptword + ' == ' + cryptpass
        if cryptpass == cryptword:
            print '[+] Found Password: ' + word + '\n'
            return
    print "[-] Password Not Found. \n"
    return

def main():

    passfile = open('password.txt')
    for line in passfile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptpass = line.split(':')[1].strip(' ')
            print '[*] Cracking Password For: ' + user
            testpass(cryptpass)


if __name__ == '__main__':

    main()