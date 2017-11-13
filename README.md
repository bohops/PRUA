# PRUA

Description
===========
- PASSWORD RE-USE AUDITOR (PRUA) is a utility for discovering password (hash) re-use across one-to-many NTLM hashdumps

Use Case(s)
===========
- Auditing: Monitor security|password policies across machines, AD domains, and logical security boundaries
- Penetration Testing: Discover eligible accounts for testing and exploiting trust relationships


Requirements | Recommendations
==============================
- Python 2.x.x
- PRUA is designed to process CORESECURITY Impacket secretsdump.py hashdump output
- Secretsdump Example: python secretsdump.py domain/administrator@localdc.domain.int -outputfile
- Record Hash Format: [SAMACCOUNTNAME]:[RID]:[LM HASH]:[NTLM HASH]:::
- Record Hash Example: acmeadmin:500:aad3b435b51404eeaad3b435b51404ee:7e442618b06285c490c28c5c49b092fe:::


Tool Usage
==========
- python prua.py [hashdump 1] [hashdump 2] [hashdump n]
- e.g. python prua.py acme_domain.ntds
- e.g. python prua.py acme_domain.ntds widgets_domain.ntds gadgets_domain.ntds

Example Output
==============

====================================
[*] PASSWORD RE-USE AUDITOR Results:
====================================

[+] ------------------------------------------------------------------------------------

administrator:500:aad3b435b51404eeaad3b435b51404ee:7d44c618406285b490c28c5c59b092fe:::  (widgets_secrets.ntds)
acmeadmin:500:aad3b435b51404eeaad3b435b51404ee:7d44c618406285b490c28c5c59b092fe:::  (acme_secrets.ntds)

[+] ------------------------------------------------------------------------------------

xyz_svc:1121:aad3b435b51404eeaad3b435b51404ee:8c5e3e5dac2192457f36dd2609fa5a75:::  (widgets_secrets.ntds)
abc_svc:1122:aad3b435b51404eeaad3b435b51404ee:8c5e3e5dac2192457f36dd2609fa5a75:::  (widgets_secrets.ntds)
sqlmgr:1003:aad3b435b51404eeaad3b435b51404ee:8c5e3e5dac2192457f36dd2609fa5a75:::  (acme_secrets.ntds)


Tool Usage & Ethics
===================
This tool was designed to help security professionals perform ethical and legal vulnerability assessments and penetration tests.  Do not use for nefarious purposes.

