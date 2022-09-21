# import re


class CalcIPv4:
    pass


if __name__ == '__main__':
    calc_ipv4 = CalcIPv4(ip='192.168.0.25', mascara='255.255.255.192')
    print(f'IP: {calc_ipv4.ip}')
    print(f'Mascara: {calc_ipv4.mascara}')
    print(f'Rede: {calc_ipv4.rede}')
    print(f'Broadcast: {calc_ipv4.broadcast}')
    print(f'Prefixo: {calc_ipv4.cidr}')
    print(f'Numero de IPs da rede: {calc_ipv4.numero_ips}')
