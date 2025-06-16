#!/bin/bash

# ZedSec Blackpulse Installer & Deployer

echo -e "\n[+] Initializing ZedSec Blackpulse environment..."

# Python venv
if [ ! -d "venv" ]; then
    python3 -m venv venv || exit 1
fi
source venv/bin/activate
pip install --upgrade pip
pip install rich

# Create tool directory
mkdir -p tools

# Tool installs
declare -A tools=(
  [rustscan]="github RustScan/RustScan"
  [subfinder]="github projectdiscovery/subfinder"
  [whois]="apt"
  [nmap]="apt"
  [gowitness]="github sensepost/gowitness"
  [whatweb]="github urbanadventurer/WhatWeb"
)

for tool in "${!tools[@]}"; do
  if ! command -v $tool &> /dev/null; then
    src="${tools[$tool]}"
    if [[ "$src" == apt ]]; then
      sudo apt update && sudo apt install -y $tool
    else
      repo="${src#github }"
      name=$(basename "$repo")
      dest="tools/$name"
      git clone --depth 1 https://github.com/$repo.git "$dest"
      cd "$dest" || continue
      go mod init $name; go mod tidy
      go build . && sudo cp $name /usr/local/bin/ || echo "[-] $name failed to build."
      cd - >/dev/null
    fi
  fi
  echo "[+] $tool ready."
done

echo "\n✅ Done. Launch via:\nsource venv/bin/activate && python Blackpulse.py --menu"
