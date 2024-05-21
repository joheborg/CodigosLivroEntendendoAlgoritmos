estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])
estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca","az"])
estacao_final = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estacao_final.add(melhor_estacao)
    estados_abranger -= estados_cobertos

print(estacao_final)
