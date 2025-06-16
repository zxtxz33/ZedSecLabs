from modules.banner import show_banner
from modules.portscan import run_rustscan
from modules.subenum import run_subfinder
from modules.whois_lookup import run_whois
from modules.techdetect import run_whatweb
from modules.screenshot import run_gowitness

def menu():
    show_banner()
    print("Select a module to run:\n")
    print("1. Port Scan (RustScan)")
    print("2. Subdomain Enumeration")
    print("3. WHOIS Lookup")
    print("4. Tech Detection")
    print("5. Capture Screenshots")
    print("0. Exit")

    choice = input("\n>> ")

    if choice == "1": run_rustscan()
    elif choice == "2": run_subfinder()
    elif choice == "3": run_whois()
    elif choice == "4": run_whatweb()
    elif choice == "5": run_gowitness()
    elif choice == "0": exit()
    else:
        print("Invalid selection.")
        menu()

if __name__ == "__main__":
    menu()
