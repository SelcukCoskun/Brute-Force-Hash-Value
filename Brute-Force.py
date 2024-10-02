import hashlib


hash_value=input("Enter the hash value =")

dosya=open("C:\\Users\\User\\Desktop\\pasword.txt","r")#Create a file of frequently used passwords in plain text.

while True:
    for text in dosya:
        text=text.strip()
        text_utf=text.encode('utf-8')

        hash1=hashlib.md5(text_utf)
        hash_md_5=hash1.hexdigest()

        hash2=hashlib.sha1(text_utf)
        hash_sha_1=hash2.hexdigest()

        hash=hashlib.sha256(text_utf)
        hash_sha_256=hash.hexdigest()

        hash3=hashlib.sha512(text_utf)
        hash_sha_512=hash3.hexdigest()
        
        if hash_md_5==hash_value:
            print(f"Encrypted with md-5. Unencrypted text={text}")
            break
    
        elif hash_sha_1==hash_value:
            print(f"Encrypted with sha-1. Unencrypted text={text}")
            break

        elif hash_sha_256==hash_value:
            print(f"Encrypted with Sha-256. Unencrypted text={text}")
            break

        elif hash_sha_512==hash_value:
            print(f"Encrypted with Sha-512. Unencrypted text={text}")
            break
    break

dosya.close()
