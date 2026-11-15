#!/usr/bin/env python3
"""Reporte semiautomatizado de trazabilidad Req-CU-Clase-Prueba.
Uso: python tools/reporte_trazabilidad.py artefactos/matriz_RF.csv artefactos/matriz_RNF.csv [salida.md]
Valida el formato de los IDs y calcula la cobertura mínima por requisito."""
import csv, re, sys
PAT={'RF':r'^RF-\d{2}$','RNF':r'^RNF-\d{2}$','CU':r'^CU-\d{2}$','HU':r'^HU-\d{2}$',
     'SEC':r'^SEC-\d{2}(/\d{2})?$','CP':r'^CP-\d{2}(\.\d)?$','CPRNF':r'^CP-RNF\d{2}$','CLASE':r'^[A-Z][A-Za-z]+$'}
def partes(s): return [x.strip() for x in re.split(r'[;,]',s) if x.strip() and x.strip()!='—']
def leer(p): return list(csv.DictReader(open(p,encoding='utf-8-sig')))
def main():
    rf=leer(sys.argv[1]); rnf=leer(sys.argv[2]); out=[]
    err=[]
    cols={'CU':'CU','HU':'HU','Clases':'CLASE','Secuencia':'SEC','Prueba':'CP'}
    cov={k:0 for k in cols}
    for r in rf:
        if not re.match(PAT['RF'],r['RF']): err.append(f"ID de requisito inválido: {r['RF']}")
        for c,t in cols.items():
            v=partes(r[c])
            if v: cov[c]+=1
            for x in v:
                x=re.sub(r'\s*\(.*?\)','',x).strip()
                if x and not re.match(PAT[t],x): err.append(f"{r['RF']}: ID inválido en {c}: {x}")
    n=len(rf)
    out.append(f"# Reporte de trazabilidad Req-CU-Clase-Prueba\n\n## Requisitos funcionales ({n})\n")
    out.append("| Vínculo | Con vínculo | Cobertura |\n|---|---|---|")
    for c in cols: out.append(f"| {c} | {cov[c]} de {n} | {100*cov[c]//n}% |")
    completos=[r['RF'] for r in rf if all(partes(r[c]) for c in cols)]
    out.append(f"\nRF con la cadena completa (CU, HU, clase, secuencia y prueba): **{len(completos)} de {n}**.")
    rp=[r['RNF'] for r in rnf if any(x.startswith('CP-RNF') for x in partes(r['Prueba']))]
    for r in rnf:
        for x in partes(r['Prueba']):
            if x.startswith('CP-RNF') and not re.match(PAT['CPRNF'],x): err.append(f"{r['RNF']}: ID de prueba inválido: {x}")
    sinp=[r['RNF'] for r in rnf if r['RNF'] not in rp]
    out.append(f"\n## Requisitos no funcionales ({len(rnf)})\n\nRNF con prueba propia (CP-RNFnn): **{len(rp)} de {len(rnf)}**.")
    if sinp: out.append("RNF sin prueba propia: "+", ".join(sinp)+".")
    out.append("\n## Validación de IDs\n"+("Sin errores de formato." if not err else "\n".join("- "+e for e in err)))
    txt="\n".join(out)+"\n"
    if len(sys.argv)>3: open(sys.argv[3],'w',encoding='utf-8').write(txt)
    print(txt)
main()
