def trigo(preco, i, nc, nv):
    pd=[]
    while len(pd)!=i and len(pd)>=0:
        pd.append(preco)
        preco = preco+1
        
    for z in pd:
        totalcomprado=preco*nc*i
        totalvendido=preco*nv*i
        total = totalvendido-totalcomprado
    print("O Total de lucro foi de: R$",total)

preco=int(input("Digite o preço do primeiro dia: "))
i=int(input("Digite a quantidade de dias: "))
nc=int(input("Digite quanto você deseja comprar por dia: "))
nv=int(input("Digite quanto você deseja vender por dia: "))
trigo(preco, i, nc, nv)
