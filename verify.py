"""Exact original-coordinate adversarial checks for the GLN support-three proof.
Python 3 standard library only. No data download. No writes unless --output.
Finite checks supplement, and do not replace, the general proof.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
import argparse,json,sys

def plus(p,q,scale=F(1)):
    out=dict(p)
    for m,c in q.items():
        out[m]=out.get(m,F(0))+scale*c
        if not out[m]: del out[m]
    return out

def timesvar(p,i):
    out={}
    for m,c in p.items():
        mm=list(m);mm[i]+=1;out[tuple(mm)]=c
    return out

def scale(p,c):
    return {m:F(c)*v for m,v in p.items() if c*v}

def allowed(m,a,kind):
    if any(v>=a for v in m): return False
    if kind=="C": return m[0]<a-2
    return not(m[0]>=a-2 and m[1] and m[2])

def up(p,a,kind):
    out={}
    for m,c in p.items():
        for i in range(len(m)):
            mm=list(m);mm[i]+=1;mm=tuple(mm)
            if allowed(mm,a,kind): out[mm]=out.get(mm,F(0))+c
    return {m:c for m,c in out.items() if c}

def power(p,k,a,kind):
    for _ in range(k): p=up(p,a,kind)
    return p

def primitive(a,r):
    out={};c=F(1)
    for ell in range(r+1):
        out[(0,r-ell,ell)]=c
        if ell<r:
            c*=-F((r-ell)*(a-r+ell),(ell+1)*(a-1-ell))
    assert c==(-1)**r
    return out

def coupled(a,r,lam):
    p=primitive(a,r)
    t=plus(timesvar(p,1),timesvar(p,2))
    return plus(scale(timesvar(p,0),lam),t,-(a-3))

def primitive_checks():
    rows=[]
    for a in range(4,21):
        f=primitive(a,a-2) if a%2 else coupled(a,a-3,4)
        assert not power(f,a,a,"C")
        v=power(f,a,a,"A")
        u=(a-1,a-1,0);z=(a-1,0,a-1)
        delta=v.get(u,0)-v.get(z,0)
        expected=2*a if a%2 else 2*a*(a+1)
        assert delta==expected
        rows.append(dict(a=a,pair=1,power=a,delta=int(delta),expected=expected,
                         original_C_kernel=True,original_A_delta=True))
        f=primitive(a,a-1) if a%2==0 else coupled(a,a-2,2)
        k=a-2
        assert not power(f,k,a,"C")
        v=power(f,k,a,"A")
        u=(a-2,a-1,0);z=(a-2,0,a-1);p=(a-1,a-2,0);q=(a-1,0,a-2)
        delta=-k*v.get(u,0)+k*v.get(z,0)+v.get(p,0)-v.get(q,0)
        expected=-2*(a-2) if a%2==0 else -2*a*(a-3)
        assert delta==expected
        rows.append(dict(a=a,pair=2,power=k,delta=int(delta),expected=expected,
                         original_C_kernel=True,original_A_delta=True))
    return rows

def sparse_rank(columns,p=None):
    pivots={}
    for original in columns:
        v={i:(c%p if p else F(c)) for i,c in original.items() if c}
        if p: v={i:c for i,c in v.items() if c}
        while v:
            i=min(v);c=v[i]
            if i not in pivots:
                inv=pow(int(c),-1,p) if p else 1/c
                pivots[i]={j:(z*inv%p if p else z*inv) for j,z in v.items()}
                break
            for j,z in pivots[i].items():
                value=v.get(j,0)-c*z
                if p: value%=p
                if value: v[j]=value
                else: v.pop(j,None)
    return len(pivots)

def degree_basis(n,a):
    out={}
    for m in product(range(a),repeat=n):
        if allowed(m,a,"A"): out.setdefault(sum(m),[]).append(m)
    return out

def all_power_case(n,a):
    basis=degree_basis(n,a);soc=max(basis);ranks={}
    for i in range(soc+1):
        ranks[i,i]=len(basis.get(i,[]))
        for j in range(i+1,soc+1):
            rows=basis.get(j,[]);k=j-i;columns=[]
            for u in basis.get(i,[]):
                col={}
                for r,v in enumerate(rows):
                    d=tuple(v[t]-u[t] for t in range(n))
                    if min(d)>=0:
                        den=1
                        for z in d: den*=factorial(z)
                        col[r]=factorial(k)//den
                columns.append(col)
            rank=sparse_rank(columns)
            assert rank==min(len(basis[i]),len(rows)),(n,a,i,j,rank)
            ranks[i,j]=rank
    def R(i,j): return ranks.get((i,j),0)
    barcode=[]
    for b in range(soc+1):
        for e in range(b,soc+1):
            mult=R(b,e)-R(b-1,e)-R(b,e+1)+R(b-1,e+1)
            assert mult>=0
            if mult: barcode.append(dict(start=b,end=e,multiplicity=mult))
    center=3*a-5+(n-3)*(a-1)
    assert all(q["start"]+q["end"] in (center,center+1) for q in barcode)
    assert sum((q["end"]-q["start"]+1)*q["multiplicity"] for q in barcode)==sum(map(len,basis.values()))
    return dict(n=n,a=a,H=[len(basis[j]) for j in range(soc+1)],
                original_coordinate_maps=soc*(soc+1)//2,all_powers_maximal_rank=True,
                endpoint_sums=sorted({q["start"]+q["end"] for q in barcode}),barcode=barcode)

def run():
    return dict(primitive_certificates=primitive_checks(),
                all_power_original_coordinate_checks=[all_power_case(n,a) for n,a in [(3,4),(3,5),(3,6),(4,4),(4,5)]],
                universal_proof="See independent complete proof record; finite checks alone do not prove universal claims.",
                all_assertions_passed=True)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output")
    args=parser.parse_args()
    data=run()
    text=json.dumps(data,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(text,encoding="utf-8")
    else:
        if hasattr(sys.stdout,"reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
        print(text,end="")
