# 🕵️ One-File Recon Snapshot

Minimal Python automation tool for quick reconnaissance snapshots.  
Performs basic IP resolution, HTTP/HTTPS status checking, and logs results into JSON & log files.  
Lightweight, single-file, and perfect for cybersecurity learners.

---

## ⚙️ Features
- IP address resolution (`socket`)
- HTTP/HTTPS request and status code retrieval (`requests`)
- JSON result output
- Simple retry mechanism
- Basic logging support
- CLI argument support (`argparse`)

---

## 🚀 Usage
### Install dependencies
```bash
pip install requests
```

## Run the script
python recon_snapshot.py

or specify parameters:
python recon_snapshot.py -t target.txt -o results.json

Results are saved in:
results.json
recon.log

## 📁 Example Output
{
  "IP": "93.184.216.34",
  "Status Code": 200
}

## 🧠 Notes
For educational and legal purposes only.
Do not use on unauthorized targets.
Ideal for those starting in ethical hacking and red team automation.
