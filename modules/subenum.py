def run_subfinder():
    domain = input("Enter root domain: ")
    print("\n[+] Enumerating subdomains for", domain)
    import os
    os.system(f"subfinder -d {domain} -silent")
