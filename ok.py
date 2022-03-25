import os, platform

try:
   import requests

except:
   os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]
if bit == '64bit':
    from ZUBI import check
    check()
elif bit == '32bit':
    print('YOUR PHONE IS NOT SUPPORTED BRO')
