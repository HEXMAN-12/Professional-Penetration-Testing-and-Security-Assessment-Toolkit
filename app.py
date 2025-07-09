# Note from the creator:
# I know this code sucks but it's 3 a.m. and I'm tired. 
# The deadline is in 12 hours. I need to sleep.


from flask import Flask, render_template, request, jsonify
from hashid import HashID
import subprocess
import json
import os
import hashlib
from werkzeug.utils import secure_filename
import logging
import tempfile
import magic
import pikepdf
import msoffcrypto
import io
import zipfile
import tempfile
import rarfile
import subprocess


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB max file size

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Default path to rockyou.txt
DEFAULT_WORDLIST_PATH = '/usr/share/wordlists/rockyou.txt'

# Configure logging
logging.basicConfig(
    filename='security_tool.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def identify_hash(hash_string):
    """Identify hash type using Python HashID."""
    try:
        hashid = HashID()
        matches = hashid.identifyHash(hash_string)
        
        if not matches:
            return {'success': True, 'output': 'No matching hash types found.'}

        # Convert HashInfo objects to their string representation
        result = "Possible Hashes:\n" + "\n".join(str(match.name) for match in matches)
        return {'success': True, 'output': result}
    except Exception as e:
        return {'success': False, 'error': str(e)}


import time

def run_cewl(url):
    """Generate custom wordlist using CeWL"""
    try:
        cmd = ['cewl', url]  # Just pass the URL without additional parameters
        
        # Run the command
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Introduce a fixed delay to give time for the crawling to complete
        time.sleep(5)  # 5 seconds delay (you can adjust this as needed)

        # Get output and error after the delay
        stdout, stderr = process.communicate()

        # If there's an error, raise an exception to see what went wrong
        if stderr:
            raise Exception(stderr)

        # Return stdout which will contain the detailed output
        return stdout
    except Exception as e:
        return f"Error: {str(e)}"






def run_medusa(host, username, password_file, service):
    """Run Medusa brute force tool"""
    try:
        cmd = [
            'medusa',
            '-h', host,
            '-u', username,
            '-P', password_file,
            '-M', service
        ]
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        stdout, stderr = process.communicate()
        return {'success': True, 'output': stdout}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def run_aircrack(cap_file, wordlist):
    """Run Aircrack-ng"""
    try:
        cmd = [
            'aircrack-ng',
            '-w', wordlist,
            cap_file
        ]
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        stdout, stderr = process.communicate()
        return {'success': True, 'output': stdout}
    except Exception as e:
        return {'success': False, 'error': str(e)}



# Utility function to read wordlist with encoding fallback
def read_wordlist(wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            return [line.strip() for line in f]
    except Exception as e:
        raise Exception(f"Error reading wordlist: {str(e)}")

# PDF password cracking
def crack_pdf(pdf_file, wordlist):
    try:
        passwords = read_wordlist(wordlist)
        for password in passwords:
            try:
                with pikepdf.open(pdf_file, password=password) as pdf:
                    return {'success': True, 'password': password}
            except pikepdf.PasswordError:
                continue
        return {'success': False, 'error': 'Password not found'}
    except Exception as e:
        return {'success': False, 'error': str(e)}


# Office file password cracking
def crack_office(office_file, wordlist):
    try:
        file = msoffcrypto.OfficeFile(open(office_file, "rb"))
        passwords = read_wordlist(wordlist)
        for password in passwords:
            try:
                file.load_key(password=password)
                return {'success': True, 'password': password}
            except:
                continue
        return {'success': False, 'error': 'Password not found'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

# Zip file password cracking
def crack_zip(zip_file, wordlist):
    try:
        passwords = read_wordlist(wordlist)
        for password in passwords:
            try:
                with zipfile.ZipFile(zip_file) as zf:
                    zf.extractall(pwd=password.encode())
                    return {'success': True, 'password': password}
            except:
                continue
        return {'success': False, 'error': 'Password not found'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

# RAR file password cracking
def crack_rar(rar_file, wordlist):
    try:
        passwords = read_wordlist(wordlist)
        for password in passwords:
            try:
                with rarfile.RarFile(rar_file) as rf:
                    rf.extractall(pwd=password)
                    return {'success': True, 'password': password}
            except rarfile.BadRarFile:
                continue
        return {'success': False, 'error': 'Password not found'}
    except Exception as e:
        return {'success': False, 'error': str(e)}
    
    # def run_metasploit(target, ports, service_detect=False, vuln_scan=False):
    # try:
    #     cmd = ['msfconsole', '-q', '-x']
    #     commands = [
    #         f'db_nmap -p{ports} {target}',
    #         'services'
    #     ]
    #     if service_detect:
    #         commands.append('db_autopwn -p -t')
    #     if vuln_scan:
    #         commands.append('vulns')
    #     commands.append('exit')
        
    #     cmd.append(';'.join(commands))
    #     process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     stdout, stderr = process.communicate()
    #     return {'success': True, 'output': stdout.decode()}
    # except Exception as e:
    #     return {'success': False, 'error': str(e)}


def run_hashcat(hash_input, hash_type, attack_mode):
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write(hash_input.strip())
            hash_file = f.name

        wordlist_path = '/usr/share/wordlists/rockyou.txt'  # Adjust path if needed
        cmd = [
            'hashcat',
            '-m', hash_type,
            '-a', attack_mode,
            hash_file,
            wordlist_path,
            '--potfile-path', '/tmp/hashcat.potfile'  # Temporary potfile for clean runs
        ]

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            # Check results in the potfile
            show_cmd = ['hashcat', '--show', '-m', hash_type, hash_file, '--potfile-path', '/tmp/hashcat.potfile']
            show_process = subprocess.Popen(show_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            show_stdout, show_stderr = show_process.communicate()
            os.unlink(hash_file)  # Clean up hash file

            result = show_stdout.decode().strip()
            return {
                'success': True,
                'output': result if result else 'No passwords were cracked.'
            }
        else:
            os.unlink(hash_file)  # Clean up hash file
            return {'success': False, 'error': stderr.decode().strip()}
    except Exception as e:
        return {'success': False, 'error': str(e)}


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/api/metasploit', methods=['POST'])
# def api_metasploit():
#     target = request.form.get('target')
#     ports = request.form.get('ports')
#     service_detect = request.form.get('serviceDetect') == 'true'
#     vuln_scan = request.form.get('vulnScan') == 'true'
#     return jsonify(run_metasploit(target, ports, service_detect, vuln_scan))

@app.route('/api/hashcat', methods=['POST'])
def api_hashcat():
    hash_input = request.form.get('input', '').strip()
    hash_type = request.form.get('type', '0')  # Default to MD5
    attack_mode = request.form.get('mode', '0')  # Default to Wordlist

    if not hash_input:
        return jsonify({'success': False, 'error': 'Hash input is required.'})

    result = run_hashcat(hash_input, hash_type, attack_mode)
    return jsonify(result)


# Add similar routes for other tools...


@app.route('/api/identify_hash', methods=['POST'])
def api_identify_hash():
    hash_string = request.form.get('hash')
    if not hash_string:
        return jsonify({'error': 'No hash provided'}), 400
    result = identify_hash(hash_string)
    return jsonify(result)

@app.route('/api/cewl', methods=['POST'])
def api_cewl():
    url = request.form.get('url')
    if not url:
        return "Error: No URL provided", 400
    result = run_cewl(url)
    return result




# Additional routes for other tools...

@app.route('/api/john', methods=['POST'])
def api_john():
    hash_format = request.form.get('format')
    hash_input = request.form.get('input')
    use_rules = request.form.get('rules') == 'true'
    use_incremental = request.form.get('incremental') == 'true'
    
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write(hash_input)
            hash_file = f.name
            
        cmd = ['john', f'--format={hash_format}']
        if use_rules:
            cmd.append('--rules')
        if use_incremental:
            cmd.append('--incremental')
        cmd.append(hash_file)
        
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        os.unlink(hash_file)
        
        return jsonify({
            'success': True,
            'output': stdout.decode(),
            'error': stderr.decode()
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/wpscan', methods=['POST'])
def api_wpscan():
    url = request.form.get('url')
    enum_users = request.form.get('enumUsers') == 'true'
    enum_plugins = request.form.get('enumPlugins') == 'true'
    enum_themes = request.form.get('enumThemes') == 'true'
    check_vuln = request.form.get('vulnCheck') == 'true'
    aggressive = request.form.get('aggressive') == 'true'
    
    try:
        cmd = ['wpscan', '--url', url, '--format', 'json']
        if enum_users:
            cmd.extend(['--enumerate', 'u'])
        if enum_plugins:
            cmd.extend(['--enumerate', 'vp'])
        if enum_themes:
            cmd.extend(['--enumerate', 'vt'])
        if check_vuln:
            cmd.append('--detection-mode', 'aggressive' if aggressive else 'passive')
            
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        return jsonify({
            'success': True,
            'output': json.loads(stdout.decode()),
            'error': stderr.decode()
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/medusa', methods=['POST'])
def api_medusa():
    host = request.form.get('host')
    service = request.form.get('service')
    username = request.form.get('username')
    if 'passlist' not in request.files:
        return jsonify({'error': 'No password list provided'})
    
    passlist = request.files['passlist']
    if passlist.filename == '':
        return jsonify({'error': 'No file selected'})
    
    try:
        passlist_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(passlist.filename))
        passlist.save(passlist_path)
        
        result = run_medusa(host, username, passlist_path, service)
        os.remove(passlist_path)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/aircrack', methods=['POST'])
def api_aircrack():
    if 'capfile' not in request.files or 'wordlist' not in request.files:
        return jsonify({'error': 'Missing required files'})
        
    capfile = request.files['capfile']
    wordlist = request.files['wordlist']
    
    try:
        capfile_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(capfile.filename))
        wordlist_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(wordlist.filename))
        
        capfile.save(capfile_path)
        wordlist.save(wordlist_path)
        
        result = run_aircrack(capfile_path, wordlist_path)
        
        os.remove(capfile_path)
        os.remove(wordlist_path)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/cracklib', methods=['POST'])
def api_cracklib():
    passwords = request.form.get('passwords', '').splitlines()
    check_dict = request.form.get('checkDict') == 'true'
    check_common = request.form.get('checkCommon') == 'true'
    
    try:
        results = []
        for password in passwords:
            cmd = ['cracklib-check']
            process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate(input=password.encode())
            results.append({
                'password': password,
                'result': stdout.decode().strip()
            })
            
        return jsonify({
            'success': True,
            'results': results
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
 
 

@app.route('/api/crack-password', methods=['POST'])
def crack_password():
    file = request.files['file']
    wordlist = request.form.get('wordlist', DEFAULT_WORDLIST_PATH)
    
    # Save the uploaded file temporarily
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
    file.save(file_path)

    # Select the correct cracking function based on file type
    file_type = request.form.get('file_type')

    if file_type == 'pdf':
        result = crack_pdf(file_path, wordlist)
    elif file_type == 'office':
        result = crack_office(file_path, wordlist)
    elif file_type == 'zip':
        result = crack_zip(file_path, wordlist)
    elif file_type == 'rar':
        result = crack_rar(file_path, wordlist)
    else:
        result = {'success': False, 'error': 'Invalid file type'}

    # Clean up by deleting the uploaded file after processing
    os.remove(file_path)

    return jsonify(result)

@app.route('/api/crack_file', methods=['POST'])
def api_crack_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    wordlist = request.form.get('wordlist', DEFAULT_WORDLIST_PATH)

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Detect file type
    file_type = magic.from_file(filepath)

    if 'PDF' in file_type:
        result = crack_pdf(filepath, wordlist)
    elif 'Microsoft Office' in file_type:
        result = crack_office(filepath, wordlist)
    elif 'Zip archive' in file_type:
        result = crack_zip(filepath, wordlist)
    elif 'RAR archive' in file_type:
        result = crack_rar(filepath, wordlist)
    else:
        result = {'success': False, 'error': 'Unsupported file type'}

    # Clean up
    os.remove(filepath)

    return jsonify(result)


# Error handling (Enable for Production Environments)
# @app.errorhandler(500)
# def internal_error(e):
#     return jsonify({'success': False, 'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
    