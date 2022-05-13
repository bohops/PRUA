import sys

def usage():
    echo = "==============================\n"
    echo+= "PASSWORD RE-USE AUDITOR (PRUA)\n"
    echo+= "==============================\n\n"
    echo+= "Purpose\n"
    echo+= "-------\n"
    echo+= "[*] A utility for discovering password (hash) re-use across one-to-many NTLM hashdumps\n\n"
    echo+= "Use Cases\n"
    echo+= "---------\n"
    echo+= "[*] Auditing: Monitor security|password policies across machines, AD domains, and logical security boundaries\n"
    echo+= "[*] Penetration Testing: Discover eligible accounts for testing and exploiting trust relationships\n\n"
    echo+= "Requirements\n"
    echo+= "------------\n"
    echo+= "[*] PRUA is designed to process CORESECURITY Impacket secretsdump.py hashdump output\n"
    echo+= "[*] Secretsdump Example: python secretsdump.py domain/administrator@localdc.domain.int -outputfile\n"
    echo+= "[*] Record Hash Format: <SAMACCOUNTNAME>:<RID>:<LM HASH>:<NTLM HASH>:::\n"
    echo+= "[*] Record Hash Example: acmeadmin:500:aad3b435b51404eeaad3b435b51404ee:7e442618b06285c490c28c5c49b092fe:::\n\n"
    echo+= "Usage\n"
    echo+= "-----\n"
    echo+= "[*] python3 " + sys.argv[0] + " [hashdump 1] [hashdump 2] [hashdump n]\n\n"
    print(echo)

def import_hashfiles():
    try:
        #file_data = []
        data_set = {}
        ntlm_set = {}
        files = sys.argv[1:]
        for file in files:
            with open(file) as f:
                records = f.readlines()
            records = [record.strip() for record in records]
            file_data = []
            for record in records:
                data = record.split(':')
                data.append(file)
                file_data.append(data)
                ntlm_set[data[3]] = []
            data_set[file] = file_data
        return ntlm_set, data_set
    except(Exception, e):
        print( "[-] " + str(e))

def compare_hashes(ntlm_set, data_set):
    for key, data in data_set.items():
        for record in data_set.get(key):
            ntlm_set.get(record[3]).append(record)
    return ntlm_set

def output_results(ntlm_set):
    echo = "\n"
    echo+= "=================\n"
    echo+= "[*] PRUA Results:\n"
    echo+= "================="
    print(echo)
    for key, data in ntlm_set.items():
        if len(data) > 1:
            print( "\n[+] ------------------------------------------------------------------------------------\n")
            for field in data:
                print(field[0] + ":" + field[1] + ":" + field[2] + ":" + field[3] + ":::  (" + field[7] + ")")

def main():
    if len(sys.argv) > 1:
        ntlm_set, data_set  = import_hashfiles()
        ntlm_set = compare_hashes(ntlm_set, data_set)
        output_results(ntlm_set)
    else:
        usage()

if __name__ == "__main__":
    main()
