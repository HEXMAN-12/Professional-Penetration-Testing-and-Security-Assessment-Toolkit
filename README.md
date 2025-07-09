# 🔒 Professional Penetration Testing & Security Assessment Toolkit

<div align="center">
  <img src="https://img.shields.io/badge/Security-Penetration%20Testing-red?style=for-the-badge&logo=security&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-green?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
</div>

<div align="center">
  <h3>Advanced Penetration Testing Suite</h3>
  <p>A comprehensive web-based dashboard for password testing & network attacks</p>
</div>



## 🎯 Overview

This Toolkit is a unified web interface that integrates multiple penetration testing tools and security assessment utilities. Built with Flask and Python, it provides an intuitive dashboard for conducting various security tests including password cracking, hash analysis, vulnerability scanning, and network reconnaissance.

## ✨ Key Features

### 🔐 Password & Hash Analysis

- **Hash Identification** - Automatically identify hash types (MD5, SHA1, SHA256, etc.)
- **Password Cracking** - John the Ripper and Hashcat integration
- **File Password Recovery** - Crack passwords for PDF, Office, ZIP, and RAR files
- **Custom Wordlist Generation** - CeWL integration for targeted wordlist creation

### 🌐 Network Security Testing

- **Service Authentication** - Medusa brute force testing
- **WiFi Security** - WPA/WPA2 password recovery with Aircrack-ng
- **WordPress Security** - Comprehensive WPScan integration
- **Vulnerability Assessment** - Metasploit framework integration

### 🛡️ Security Analysis Tools

- **Password Strength Testing** - Cracklib integration for password policy validation
- **File Type Detection** - Automatic file type identification
- **Comprehensive Logging** - Detailed activity logging for audit trails

## 🖥️ User Interface

<div align="center">
    <img src="documentation/demo videos/User-Interface.png" alt="User Interface Screenshot" width="100%"/>
    <p><em>Intuitive web-based dashboard with comprehensive security testing capabilities</em></p>
</div>

## 📦 Installation & Setup

### Prerequisites

- Python 3.11 or higher
- Linux environment (Ubuntu/Debian recommended)
- Administrative privileges for system tool installation

### Quick Start

1. **Clone the Repository**

   ```bash
   git clone https://github.com/HEXMAN-12/Professional-Penetration-Testing-and-Security-Assessment-Toolkit.git
   cd Professional-Penetration-Testing-and-Security-Assessment-Toolkit
   ```

2. **Set up Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install System Tools** (Ubuntu/Debian)

   ```bash
   sudo apt-get update
   sudo apt-get install hashcat john medusa aircrack-ng wpscan cewl
   sudo apt-get install wordlists  # Common wordlists including rockyou.txt
   ```

5. **Create Required Directories**

   ```bash
   mkdir -p uploads
   ```

6. **Run the Application**

   ```bash
   python app.py
   ```

7. **Access the Dashboard**
   - Open your browser and navigate to: `http://localhost:5000`

## 🚀 Usage Examples

### 🔍 Hash Identification & Password Cracking

The dashboard provides comprehensive hash analysis and password cracking capabilities using industry-standard tools.

<video src="https://github.com/user-attachments/assets/d744e633-8107-497d-b322-74eb394b4fb1" 
       autoplay 
       muted 
       loop 
       playsinline 
       controls 
       >
Your browser does not support the video tag.
</video>

**Hash Detection & Analysis:**

- Automatic identification of 50+ hash types (MD5, SHA1, SHA256, SHA512, NTLM, bcrypt, etc.)
- Real-time hash format validation and analysis
- Support for both single hashes and batch processing

**Password Cracking Capabilities:**

- **John the Ripper Integration** - Extensive format support with customizable rules and incremental attacks
- **Hashcat Integration** - GPU-accelerated cracking with CUDA and OpenCL support
- **Multiple Attack Modes** - Dictionary, brute force, rule-based, hybrid, and mask attacks
- **Performance Optimization** - Automatic hardware detection and multi-threading support

---

### 🗂️ File Password Recovery

Automated password recovery for various file formats using optimized cracking techniques.


<video src="https://github.com/user-attachments/assets/7741c3d9-1fba-4843-a5da-f8e7e793e822" 
       autoplay 
       muted 
       loop 
       playsinline 
       controls 
       >
Your browser does not support the video tag.
</video>




**Supported File Formats:**

- **PDF Documents** - Advanced password recovery using pikepdf library
- **Microsoft Office** - Word, Excel, PowerPoint files (all versions supported)
- **ZIP Archives** - Standard and encrypted ZIP file password recovery
- **RAR Archives** - WinRAR and other RAR format files

**File Cracking Capabilities**

- **Automatic File Detection** - Intelligent file type identification and format analysis
- **Optimized Libraries** - Uses specialized tools for each file type (pikepdf, msoffcrypto-tool)
- **Custom Wordlists** - Upload personal dictionaries or use built-in rockyou.txt
- **Progress Monitoring** - Real-time status updates and detailed recovery logging
- **Batch Processing** - Support for multiple files with queue management

---

### 🌐 Network Service Authentication Testing

Professional-grade network authentication testing using Medusa and other specialized tools.

<video src="https://github.com/user-attachments/assets/331ac682-3231-434b-a76f-00d8a90b7faf" 
       autoplay 
       muted 
       loop 
       playsinline 
       controls 
       >
Your browser does not support the video tag.
</video>


**Supported Network Services:**

- **SSH (Secure Shell)** - Remote server authentication testing
- **FTP (File Transfer Protocol)** - File server credential validation
- **HTTP/HTTPS** - Web application login form testing
- **Telnet** - Legacy system authentication analysis
- **MySQL/PostgreSQL** - Database server credential testing
- **SNMP** - Network device community string testing

**Advanced Configuration:**

- **Parallel Processing** - Configurable threading for multiple simultaneous attacks
- **Timeout Management** - Custom timeout settings for different service types
- **Service Detection** - Automatic protocol detection and optimization
- **Credential Management** - Targeted username and password list uploads
- **Detailed Reporting** - Comprehensive logging of authentication attempts and results

---

### 📝 Custom Wordlist Generation

Generate targeted wordlists using CeWL (Custom Word List Generator) for enhanced attack precision.

<video src="https://github.com/user-attachments/assets/942adae2-0d64-4c6d-b2da-51419f231723" 
       autoplay 
       muted 
       loop 
       playsinline 
       controls 
       >
Your browser does not support the video tag.
</video>

**Website Analysis Capabilities:**

- **Intelligent Crawling** - Automated website traversal with configurable depth levels
- **Keyword Extraction** - Context-specific word harvesting from web content
- **Email Discovery** - Automatic email address extraction from web pages
- **Content Filtering** - Minimum word length and character type filtering

**Advanced Options:**

- **Depth Control** - Configurable crawling depth for comprehensive coverage
- **Alphanumeric Support** - Include numbers and special characters in wordlists
- **Custom Parameters** - Advanced configuration for specialized target environments
- **Export Formats** - Multiple output formats for integration with other tools
- **Integration Ready** - Direct compatibility with dashboard password cracking tools

---

### 🛡️ Additional Security Testing Features

**WordPress Security Scanning** - Comprehensive vulnerability detection using WPScan with user enumeration, plugin analysis, and theme security assessment capabilities.

**WiFi Security Testing** - WPA/WPA2 password recovery with Aircrack-ng integration, capture file analysis, and dictionary-based wireless network security assessment.

**Password Strength Validation** - Cracklib integration for password policy testing with real-time strength analysis, security recommendations, and compliance checking against industry standards.

## 🛠️ Tool Integration

### Supported Tools

| Tool                | Purpose                            | Integration Status  |
| ------------------- | ---------------------------------- | ------------------- |
| **Hashcat**         | GPU-accelerated password cracking  | ✅ Full Integration |
| **John the Ripper** | Password cracking                  | ✅ Full Integration |
| **Medusa**          | Network authentication brute force | ✅ Full Integration |
| **Aircrack-ng**     | WiFi security testing              | ✅ Full Integration |
| **WPScan**          | WordPress vulnerability scanner    | ✅ Full Integration |
| **CeWL**            | Custom wordlist generator          | ✅ Full Integration |
| **Cracklib**        | Password strength testing          | ✅ Full Integration |
| **HashID**          | Hash type identification           | ✅ Full Integration |
| **Metasploit**      | Exploitation framework             | 🔄 In Development   |

### File Cracking Support

| File Type  | Library          | Status       |
| ---------- | ---------------- | ------------ |
| **PDF**    | pikepdf          | ✅ Supported |
| **Office** | msoffcrypto-tool | ✅ Supported |
| **ZIP**    | zipfile          | ✅ Supported |
| **RAR**    | rarfile          | ✅ Supported |

## 📁 Project Structure

```
pentest-project/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── setup                 # Installation instructions
├── templates/
│   └── index.html        # Main dashboard interface
├── uploads/              # File upload directory
├── demo files/           # Sample files for testing
│   ├── passwords.txt     # Sample password list
│   ├── sample.txt        # Sample hash file
│   └── test.*           # Test files (PDF, Office, ZIP, RAR)
└── documentation/        # Project documentation
    ├── Demo Video.mp4    # Demo video
    ├── Project Report.pdf # Detailed project report
    └── Project Presentation.pptx # Project presentation
```

## 🔧 Configuration

### File Upload Settings

- **Maximum file size**: 32MB
- **Upload directory**: `uploads/`
- **Supported file types**: PDF, Office documents, ZIP, RAR

### Default Wordlist

- **Default path**: `/usr/share/wordlists/rockyou.txt`
- **Custom wordlists**: Can be uploaded via the interface

### Logging

- **Log file**: `security_tool.log`
- **Log level**: INFO
- **Format**: Timestamp, Level, Message

## 📖 Comprehensive Documentation

### Project Report

This project includes a **comprehensive Project Report** (`Project Report.pdf`) that provides detailed documentation about all the penetration testing tools integrated into this dashboard. The report covers:

- **Detailed Tool Analysis** - In-depth examination of John the Ripper, Hydra, Hashcat, Medusa, CeWL, WPScan, and Metasploit
- **Practical Test Cases** - Step-by-step testing procedures for various file formats and network services
- **Real-world Applications** - Password cracking techniques for PDF, Office documents, ZIP/RAR archives
- **Security Assessment Methods** - WordPress vulnerability scanning, SSH/FTP brute forcing, custom wordlist generation
- **Technical Implementation** - Command-line examples and parameter configurations
- **Results & Analysis** - Detailed output analysis and security recommendations

## 🐛 Known Issues & Limitations

- **Metasploit integration**: Currently commented out, requires additional setup
- **Windows compatibility**: Running on Windows may require WSL or Linux environment
- **Resource intensive**: Password cracking can be CPU/GPU intensive
- **File size limits**: 32MB upload limit for security reasons

## 🤝 Contributing

We welcome contributions to improve this penetration testing toolkit! Here's how you can help:

### How to Contribute

1. **Fork the repository**

```bash
git fork https://github.com/HEXMAN-12/Professional-Penetration-Testing-&-Security-Assessment-Toolkit.git
```

2. **Create a feature branch**

```bash
git checkout -b feature/amazing-feature
```

3. **Commit your changes**

```bash
git commit -m 'Add amazing feature'
```

4. **Push to the branch**

```bash
git push origin feature/amazing-feature
```

5. **Open a Pull Request**

## 🫂 Contributors

- **Sabih Uddin Qureshi** - [@HEXMAN-12](https://github.com/HEXMAN-12) - Lead Developer
- **Mehreen Umer Khan** - [@H4ckWizHer](https://github.com/H4ckWizHer) - Co-Developer

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/HEXMAN-12/Professional-Penetration-Testing-and-Security-Assessment-Toolkit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/HEXMAN-12/Professional-Penetration-Testing-and-Security-Assessment-Toolkit/discussions)
- **Detailed Tool Guide**: Check the `documentation/` folder for detailed guides
- **Documentation**: Refer to `Project Report.pdf` for comprehensive tool documentation and testing procedures

## 🏆 Acknowledgments

- **Flask Framework** - Web application framework
- **Security Tool Developers** - Hashcat, John the Ripper, Medusa, Aircrack-ng, WPScan, CeWL
- **Python Community** - Various libraries and tools
- **Security Community** - Inspiration and best practices

---

<div align="center">
  <p><strong>⚠️ Use Responsibly | Educational Purpose Only | Get Permission First ⚠️</strong></p>
  <p>Made with ❤️ by Sabih Qureshi & Mehreen Khan</p>
</div>
