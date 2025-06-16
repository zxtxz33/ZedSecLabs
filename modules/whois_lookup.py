def run_whois():
    domain = input("Enter domain or IP: ")
    print("\n[+] Running whois lookup on", domain)
    import os
    os.system(f"whois {domain}")
