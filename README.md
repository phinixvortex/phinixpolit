# PhinixPolit

PhinixPolit is a command-line cybersecurity multi-tool (Python) that provides:
- Port scanning (basic socket scanner)
- Vulnerability scanning (wraps `nmap --script vuln`)
- Web scanning (wraps `nikto`)
- SSL scanning (wraps `sslscan`)
- Footprinting (WHOIS)
- Reconnaissance (ping)
- Enumeration (wraps `nmap -A`)

## Requirements
- Python 3.8+
- External tools (for full functionality): `nmap`, `nikto`, `sslscan`
- Python packages: `colorama`, `python-whois` (package name may be `whois`)
- Run with appropriate permissions and **only** against systems you own or have permission to test.

## Usage
```bash
python3 phinixpolit.py example.com --portscan
python3 phinixpolit.py 1.2.3.4 -a   # run all scans (requires installed external tools)
```

## Responsible Use
This tool can be used for legitimate security testing and learning. Do **not** use it to scan or attack systems without explicit authorization. The author and contributors are not responsible for misuse.

## License
MIT
