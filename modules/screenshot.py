def run_gowitness():
    target = input("Enter URL or file with URLs: ")
    print("\n[+] Capturing screenshot(s) of", target)
    import os
    os.system(f"gowitness single --url {target} -d screenshots")
