import os
import re
import subprocess
def main():
    target_ip = "localhost"
    output= get_target_OS(get_target_ttl(target_ip))
    print(output)

def get_target_OS(TTL):
    ttl = int(TTL)
    if ttl >= 0 and ttl <= 64:
        return "User device OS: Linux (ttl -> 64)"
    elif ttl >= 65 and ttl <= 128:
        return "User device OS: Windows (ttl -> 128)"

def get_target_ttl(ip):
    try:
        ping_process = subprocess.Popen(["ping", "-c", "1", ip ], stdout=subprocess.PIPE)
        grep_process = subprocess.Popen(["grep","ttl"],stdin=ping_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ping_process.stdout.close()
        output, error = grep_process.communicate()
        result = output.decode("utf-8").split()[6].split('=')[1]
        return result
    except subprocess.CalledProcessError:
        print("Ping failed.")



if __name__ == "__main__":
    main()