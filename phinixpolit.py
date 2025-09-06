#!/usr/bin/env python3
import socket
import subprocess
import argparse
import logging
from colorama import Fore, Style, init
from datetime import datetime
import whois
import os

# Init
init(autoreset=True)
logging.basicConfig(filename="phinixpolit.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# ─── Banner ────────────────────────────────────────────────────────────────
def banner():
    print(Fore.MAGENTA + Style.BRIGHT + r"""
██████╗ ██╗  ██╗██╗███╗   ██╗██╗██╗  ██╗██████╗  ██████╗ ██╗     ██╗████████╗
██╔══██╗██║  ██║██║████╗  ██║██║╚██╗██╔╝██╔══██╗██╔═══██╗██║     ██║╚══██╔══╝
██████╔╝███████║██║██╔██╗ ██║██║ ╚███╔╝ ██████╔╝██║   ██║██║     ██║   ██║   
██╔═══╝ ██╔══██║██║██║╚██╗██║██║ ██╔██╗ ██╔═══╝ ██║   ██║██║     ██║   ██║   
██║     ██║  ██║██║██║ ╚████║██║██╔╝ ██╗██║     ╚██████╔╝███████╗██║   ██║   
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚═╝   ╚═╝   
                """ + Fore.CYAN + ">>> CRAZY CYBER TOOL LOADING <<<\n")

# ─── Save Reports ───────────────────────────────────────────────────────────
def save_report(report, scan_type, combined=False):
    if combined:
        return f"\n{'='*40}\n[ {scan_type} REPORT ]\n{'='*40}\n{report}\n"
    else:
        filename = f"report_{scan_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(report)
        print(Fore.GREEN + f"[+] {scan_type} report saved as {filename}")
        return None

# ─── Port Scanner ───────────────────────────────────────────────────────────
def port_scan(target, combined=False):
    print(Fore.YELLOW + f"[*] Scanning ports on {target}...\n")
    report = f"Port Scan Report for {target}\n\n"
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(Fore.GREEN + f"[OPEN] {port}/tcp ({service})")
                report += f"[OPEN] {port}/tcp ({service})\n"
            sock.close()
        return save_report(report, "PortScan", combined)
    except Exception as e:
        print(Fore.RED + f"[!] Port scan failed: {e}")
        logging.error(f"Port scan failed: {e}")
        return ""

# ─── Vulnerability Scan ─────────────────────────────────────────────────────
def vulnerability_scan(target, combined=False):
    print(Fore.YELLOW + "[*] Running Vulnerability Scan...\n")
    try:
        process = subprocess.Popen(["nmap", "--script", "vuln", target],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   text=True)
        output, _ = process.communicate()
        print(Fore.CYAN + output)
        return save_report(output, "VulnerabilityScan", combined)
    except Exception as e:
        print(Fore.RED + f"[!] Vulnerability scan failed: {e}")
        logging.error(f"Vulnerability scan failed: {e}")
        return ""

# ─── Web Scan (Nikto) ──────────────────────────────────────────────────────
def web_scan(target, combined=False):
    print(Fore.YELLOW + "[*] Running Web Scan...\n")
    try:
        process = subprocess.Popen(["nikto", "-h", target],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   text=True)
        output, _ = process.communicate()
        print(Fore.CYAN + output)
        return save_report(output, "WebScan", combined)
    except Exception as e:
        print(Fore.RED + "[!] Nikto failed")
        logging.error(f"Nikto scan failed: {e}")
        return ""

# ─── SSL Scan ───────────────────────────────────────────────────────────────
def ssl_scan(target, combined=False):
    print(Fore.YELLOW + "[*] Running SSL Scan...\n")
    try:
        process = subprocess.Popen(["sslscan", target],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   text=True)
        output, _ = process.communicate()
        print(Fore.CYAN + output)
        return save_report(output, "SSLScan", combined)
    except Exception as e:
        print(Fore.RED + f"[!] SSL scan failed: {e}")
        logging.error(f"SSL scan failed: {e}")
        return ""

# ─── Footprinting ──────────────────────────────────────────────────────────
def footprinting(domain, combined=False):
    print(Fore.YELLOW + "[*] Running Footprinting...\n")
    try:
        info = whois.whois(domain)
        report = str(info)
        print(Fore.CYAN + report)
        return save_report(report, "Footprinting", combined)
    except Exception as e:
        print(Fore.RED + f"[!] Footprinting failed: {e}")
        logging.error(f"Footprinting failed: {e}")
        return ""

# ─── Reconnaissance ────────────────────────────────────────────────────────
def reconnaissance(target, combined=False):
    print(Fore.YELLOW + "[*] Running Reconnaissance...\n")
    try:
        cmd = ["ping", "-c", "4", target] if os.name != "nt" else ["ping", "-n", "4", target]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        output, _ = process.communicate()
        print(Fore.CYAN + output)
        return save_report(output, "Reconnaissance", combined)
    except Exception as e:
        print(Fore.RED + f"[!] Reconnaissance failed: {e}")
        logging.error(f"Reconnaissance failed: {e}")
        return ""

# ─── Enumeration ───────────────────────────────────────────────────────────
def enumeration(target, combined=False):
    print(Fore.YELLOW + "[*] Running Enumeration...\n")
    try:
        process = subprocess.Popen(["nmap", "-A", target],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   text=True)
        output, _ = process.communicate()
        print(Fore.CYAN + output)
        return save_report(output, "Enumeration", combined)
    except Exception as e:
        print(Fore.RED + f"[!] Enumeration failed: {e}")
        logging.error(f"Enumeration failed: {e}")
        return ""

# ─── Main ───────────────────────────────────────────────────────────────────
def main():
    banner()

    parser = argparse.ArgumentParser(description="PhinixPolit - Cybersecurity Multi-Tool", add_help=True)
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-p", "--portscan", action="store_true", help="Run port scan")
    parser.add_argument("-v", "--vulnscan", action="store_true", help="Run vulnerability scan")
    parser.add_argument("-w", "--webscan", action="store_true", help="Run web scan with Nikto")
    parser.add_argument("-s", "--sslscan", action="store_true", help="Run SSL scan")
    parser.add_argument("-f", "--footprinting", action="store_true", help="Run footprinting (WHOIS)")
    parser.add_argument("-r", "--recon", action="store_true", help="Run reconnaissance (ping/traceroute)")
    parser.add_argument("-e", "--enum", action="store_true", help="Run enumeration (Nmap -A)")
    parser.add_argument("-a", "--all", action="store_true", help="Run all scans and save in ONE report")
    args = parser.parse_args()

    if args.all:
        combined_report = ""
        combined_report += port_scan(args.target, combined=True) or ""
        combined_report += vulnerability_scan(args.target, combined=True) or ""
        combined_report += web_scan(args.target, combined=True) or ""
        combined_report += ssl_scan(args.target, combined=True) or ""
        combined_report += footprinting(args.target, combined=True) or ""
        combined_report += reconnaissance(args.target, combined=True) or ""
        combined_report += enumeration(args.target, combined=True) or ""

        filename = f"PhinixPolit_FULLREPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(combined_report)
        print(Fore.GREEN + f"[+] Full report saved as {filename}")

    else:
        if args.portscan:
            port_scan(args.target)
        if args.vulnscan:
            vulnerability_scan(args.target)
        if args.webscan:
            web_scan(args.target)
        if args.sslscan:
            ssl_scan(args.target)
        if args.footprinting:
            footprinting(args.target)
        if args.recon:
            reconnaissance(args.target)
        if args.enum:
            enumeration(args.target)

if __name__ == "__main__":
    main()

