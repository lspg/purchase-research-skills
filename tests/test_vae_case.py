#!/usr/bin/env python3
"""Integration assertions for the real VAE case study."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
D=R/"examples"/"vae-case-study"
products={x["id"]:x for x in json.loads((D/"products.json").read_text())}
session=json.loads((D/"session.json").read_text())
errors=[]
def expect(pid,req,value):
 got=products[pid].get("constraint_results",{}).get(req)
 if got!=value: errors.append(f"{pid} {req}: expected {value}, got {got}")
expect("decathlon-e-three-500","req-car-rack","FAIL")
for req in ("req-passenger","req-car-rack","req-france-sav","req-legal-vae"): expect("yuba-kombi-ep5",req,"PASS")
expect("garrett-miller-z-2026","req-passenger","UNRESOLVED")
expect("garrett-miller-z-2026","req-car-rack","UNRESOLVED")
expect("unikride-xtrail","req-passenger","UNRESOLVED")
expect("unikride-xtrail","req-car-rack","UNRESOLVED")
if session["stage"]!="WATCH":errors.append("session must be WATCH")
if not session["blocking_unknowns"]:errors.append("blocking_unknowns must not be empty")
if errors:
 print("\n".join("ERROR: "+e for e in errors));sys.exit(1)
print("VAE integration case OK")
