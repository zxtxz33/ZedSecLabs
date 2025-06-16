def run_rustscan():
    target = input("Enter target IP or domain: ")
    print("\n[+] Running RustScan on", target)
    import os
    os.system(f"rustscan -a {target} -r 1-65535 -- -sV -sC")
