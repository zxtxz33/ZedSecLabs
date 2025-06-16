# ZedSec Blackpulse

Blackpulse is a modular threat recon and adversary emulation platform by ZedSec Labs.

## Quick Install
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/zxtxz33/ZedSecLabs/main/Blackpulse_deploy.sh)"
```

## Manual Install
```bash
git clone https://github.com/zxtxz33/ZedSecLabs.git && \
cd ZedSecLabs && \
chmod +x Blackpulse_deploy.sh && \
./Blackpulse_deploy.sh
```

## Launch
```bash
source venv/bin/activate
python Blackpulse.py --menu
```
