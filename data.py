data = '''115.124.42.90 1080    SOCKS4  Anonymous   India   Unknown
43.225.163.209 4153 SOCKS4  Anonymous   India   Unknown
202.168.146.116 1080    SOCKS4  Anonymous   India   Unknown
165.22.220.151 36362    SOCKS4  Anonymous   India   Unknown
45.249.79.105 3629  SOCKS4  Anonymous   India   Unknown
103.59.203.145 4145 SOCKS4  Anonymous   India   Unknown
103.66.233.153 4145 SOCKS4  Anonymous   India   Unknown
103.211.8.181 52616 SOCKS4  Anonymous   India   Unknown
150.129.171.123 6667    SOCKS4  Anonymous   India   Unknown
103.60.138.65 4153  SOCKS4  Anonymous   India   Unknown
103.60.137.17 4153  SOCKS4  Anonymous   India   Unknown
103.84.178.193 4153 SOCKS4  Anonymous   India   Unknown
111.91.231.65 4153  SOCKS4  Anonymous   India   Unknown
1.186.60.25 4153    SOCKS4  Anonymous   India   Unknown
114.69.243.93 4145  SOCKS4  Anonymous   India   Unknown
103.240.33.193 8291 SOCKS4  Anonymous   India   Unknown
117.202.20.66 1088  SOCKS4  Anonymous   India   Unknown
103.59.203.149 4145 SOCKS4  Anonymous   India   Unknown
115.124.45.1 1080   SOCKS4  Anonymous   India   Unknown
103.84.178.2 4153   SOCKS4  Anonymous   India   Unknown'''

for i in data.split("\n"):
    ip = i.split(" ")
    print("'"+ip[0]+":"+ip[1]+"',")
