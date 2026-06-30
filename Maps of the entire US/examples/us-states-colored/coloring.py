#!/usr/bin/env python3
"""
Simple code to assign 5 colors (numbers 1-5) to US states (incl DC)
such that no two bordering states have the same color.
Uses greedy coloring.
"""

states = ["al","ak","az","ar","ca","co","ct","de","fl","ga","hi","id","il","in","ia","ks","ky","la","me","md","ma","mi","mn","ms","mo","mt","ne","nv","nh","nj","nm","ny","nc","nd","oh","ok","or","pa","ri","sc","sd","tn","tx","ut","vt","va","wa","wv","wi","wy","dc"]

adj = {
    "al": ["fl","ga","ms","tn"],
    "ak": [],
    "az": ["ca","nv","ut","nm","co"],
    "ar": ["mo","tn","ms","la","tx","ok"],
    "ca": ["or","nv","az"],
    "co": ["wy","ne","ks","ok","nm","az","ut"],
    "ct": ["ma","ri","ny"],
    "de": ["md","pa","nj"],
    "fl": ["al","ga"],
    "ga": ["al","fl","tn","nc","sc"],
    "hi": [],
    "id": ["wa","or","mt","wy","ut","nv"],
    "il": ["wi","ia","mo","ky","in"],
    "in": ["il","mi","oh","ky"],
    "ia": ["mn","sd","ne","mo","il","wi"],
    "ks": ["ne","co","ok","mo"],
    "ky": ["in","oh","wv","va","tn","mo","il"],
    "la": ["ar","ms","tx"],
    "me": ["nh"],
    "md": ["de","pa","wv","va","dc"],
    "ma": ["nh","vt","ny","ct","ri"],
    "mi": ["wi","in","oh"],
    "mn": ["nd","sd","ia","wi"],
    "ms": ["al","tn","ar","la"],
    "mo": ["ia","ne","ks","ok","ar","tn","ky","il"],
    "mt": ["id","wy","sd","nd"],
    "ne": ["sd","wy","co","ks","mo","ia"],
    "nv": ["id","ut","az","ca","or"],
    "nh": ["me","vt","ma"],
    "nj": ["ny","pa","de"],
    "nm": ["co","ok","tx","az"],
    "ny": ["vt","ma","ct","nj","pa"],
    "nc": ["va","tn","ga","sc"],
    "nd": ["mt","sd","mn"],
    "oh": ["mi","in","ky","wv","pa"],
    "ok": ["ks","co","nm","tx","ar","mo"],
    "or": ["wa","id","nv","ca"],
    "pa": ["ny","nj","de","md","wv","oh"],
    "ri": ["ct","ma"],
    "sc": ["nc","ga"],
    "sd": ["nd","mt","wy","ne","ia","mn"],
    "tn": ["ky","va","nc","ga","al","ms","ar","mo"],
    "tx": ["ok","nm","ar","la"],
    "ut": ["id","wy","co","nm","az","nv"],
    "vt": ["nh","ny","ma"],
    "va": ["md","wv","ky","tn","nc","dc"],
    "wa": ["id","or"],
    "wv": ["pa","md","va","ky","oh"],
    "wi": ["mn","ia","il","mi"],
    "wy": ["mt","id","ut","co","ne","sd"],
    "dc": ["md","va"]
}

# Greedy 5-coloring
color = {}
for state in states:
    used = set()
    for nei in adj.get(state, []):
        if nei in color:
            used.add(color[nei])
    for c in range(1, 6):
        if c not in used:
            color[state] = c
            break

if __name__ == "__main__":
    print("State coloring (1-5 colors, no adjacent same):")
    for s in sorted(color):
        print(f"  {s}: {color[s]}")
    print(f"\nColors used: {len(set(color.values()))}")
