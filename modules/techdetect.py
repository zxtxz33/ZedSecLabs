def run_whatweb():
    url = input("Enter target URL: ")
    print("\n[+] Detecting technologies used by", url)
    import os
    os.system(f"whatweb {url}")
