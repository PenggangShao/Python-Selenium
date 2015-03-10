import sys
sys.path.append(r"C:\Users\shaopenggang\Desktop\selenium\test_case")
from sutie import *
def caselist():
    alltestnames = [
    'aem_asset.Asset',
    'aem_login.Login',
    'aem_site.Site',
    'aem_classic.Classic']
    print "success read case list "
    return alltestnames