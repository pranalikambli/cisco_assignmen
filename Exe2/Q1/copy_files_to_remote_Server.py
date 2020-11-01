import subprocess

p = subprocess.run(["scp", "Token_genrate.txt", "remote_upload"])
p = subprocess.run(["ftp", "Token_genrate.txt", "remote_upload"])
p = subprocess.run(["sftp", "Token_genrate.txt", "remote_upload"])

