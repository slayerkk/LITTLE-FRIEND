
print('''
██╗░░░░░██╗████████╗████████╗██╗░░░░░███████╗  
██║░░░░░██║╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝  
██║░░░░░██║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░  
██║░░░░░██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░  
███████╗██║░░░██║░░░░░░██║░░░███████╗███████╗  
╚══════╝╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝  

███████╗██████╗░██╗███████╗███╗░░██╗██████╗░
██╔════╝██╔══██╗██║██╔════╝████╗░██║██╔══██╗
█████╗░░██████╔╝██║█████╗░░██╔██╗██║██║░░██║
██╔══╝░░██╔══██╗██║██╔══╝░░██║╚████║██║░░██║
██║░░░░░██║░░██║██║███████╗██║░╚███║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░''')
print('')
print('''▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒
▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒
▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒
▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌
▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒                       
▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

''')
print('''
█▀▀▄ █──█ ▄ 　 ░█▀▀▀█ ░█─── ─█▀▀█ ░█──░█ ░█▀▀▀ ░█▀▀█ 
█▀▀▄ █▄▄█ ─ 　 ─▀▀▀▄▄ ░█─── ░█▄▄█ ░█▄▄▄█ ░█▀▀▀ ░█▄▄▀ 
▀▀▀─ ▄▄▄█ ▀ 　 ░█▄▄▄█ ░█▄▄█ ░█─░█ ──░█── ░█▄▄▄ ░█─░█''')

escolha = -1

while escolha < 1 or escolha > 6:
    escolha = int(input("""O que você deseja fazer?
[ 1 ] = DoS (by: palahsu)
[ 2 ] = sqlmap
[ 3 ] = brutalforce
[ 4 ] = rapidscan
[ 5 ] = banir numero (whatsapp)
[ 6 ] = desbanir numero (whatsapp)
Sua escolha: """))
    print('')
    print('')
    print('')
    

if escolha == 1:
    exec(open('DoS.py', encoding="utf-8").read(), globals())

elif escolha == 2:
    exec(open('sqlmap.py', encoding="utf-8").read(), globals())

elif escolha == 3:
    exec(open('brute.py', encoding="utf-8").read(), globals())

elif escolha == 4:
    exec(open('rapidscan.py', encoding="utf-8").read(), globals())

if escolha == 5:
    exec(open('ban.py', encoding="utf-8").read(), globals())

if escolha == 6:
    exec(open('desban.py', encoding="utf-8").read(), globals())

else:
    print("Faça uma escolha valida")
    print('Inicie')