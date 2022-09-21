"""
Aula 114 - Subprocess - Executando programas e comandos externos
"""
import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4'],
    capture_output=True,
    text=True
)

saida = proc.stdout
# print(proc.stderr)
# print(proc.stdout)
# print(proc.returncode)
# print(proc.args)
saida = proc.stdout
# saida = saida.replace('icmp_seq', 'LUIZOTAVIO')
print(saida)
