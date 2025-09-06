🔥 PhinixPolit

**PhinixPolit** is a multifunctional cybersecurity tool written in Python.  
It combines **port scanning, enumeration, reconnaissance, footprinting, and vulnerability scanning** into one terminal-based toolkit.  

---

🚀 Features
- ✅ Colorful and interactive CLI interface (Matrix-style banner 🎉)  
- ✅ Port scanning (with Python sockets & Nmap integration)  
- ✅ WHOIS lookups for domains  
- ✅ HTTP/HTTPS reconnaissance (headers, status codes, scraping)  
- ✅ Vulnerability scanning (planned with Nmap & Nikto)  
- ✅ Logging of all activities for later review  

---

📦 Installation

1. Clone the repo
bash
git clone https://github.com/phinixvortex/phinixpolit.git
cd phinixpolit
````

2. (Optional) Create a virtual environment

bash
python3 -m venv venv
source venv/bin/activate      # Linux/macOS
.\venv\Scripts\activate       # Windows


3. Install dependencies

bash
pip install --upgrade pip
pip install -r requirements.txt


---

🛠️ Usage

Run the tool from your terminal:

bash
python phinixpolit.py -h


Example (scan a target):

bash
python phinixpolit.py -t example.com -p 80,443


---

📂 Project Structure


phinixpolit/
│
├── phinixpolit.py        # Main tool code
├── requirements.txt      # Python dependencies
├── setup.py              # For packaging (optional)
├── README.md             # Documentation
├── .gitignore            # Ignored files/folders
└── logs/                 # (planned) Scan logs and reports


---

🧑‍💻 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

📜 License

This project is licensed under the [MIT License](LICENSE).

---

✨ Roadmap / Future Features

* [ ] Nikto integration for web vulnerability scanning
* [ ] Directory/file brute forcing
* [ ] Automated report generation (HTML/PDF)
* [ ] Shodan API integration
* [ ] Improved multi-threaded scanning

