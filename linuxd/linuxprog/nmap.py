import subprocess;

nmap_command = ['nmap', '-p', '20-1040', 'localhost'];

arpscan_command = ['arp-scan', '-A', 'FORWAR', 'localhost', 'DROP']; 

arpscan_ln = ['arp-scan', '--localnet'];

resultado = subprocess.run(nmap_command, capture_output=True, text=True);
resultado2 = subprocess.run(arpscan_command, capture_output=True, text=True); 
resultado3 = subprocess.run(arpscan_ln, capture_output=True, text=True);

print(resultado.stderr);
print(resultado.stdout);

print(resultado2.stderr)
print(resultado2.stdout); 

print(resultado3.stderr);
print(resultado3.stdout);