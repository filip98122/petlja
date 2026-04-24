ab,bc,cd,de=map(str,(input().strip()).split())
najmanji=""
najveci=""
if ab=="<":
    najmanji=najmanji+"a"
if ab==">":
    najveci=najveci+"a"


if ab=="<" and bc==">":
    najveci=najveci+"b"
if ab==">" and bc=="<":
    najmanji=najmanji+"b"


if bc=="<" and cd==">":
    najveci=najveci+"c"
if bc==">" and cd=="<":
    najmanji=najmanji+"c"
    

if cd=="<" and de==">":
    najveci=najveci+"d"
if cd==">" and de=="<":
    najmanji=najmanji+"d"

if de==">":
    najmanji=najmanji+"e"
if de=="<":
    najveci=najveci+"e"
print(najmanji)
print(najveci)