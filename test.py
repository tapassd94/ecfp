#oidx is index of the connecting atom
#b.bondtype is 1 for sing bond 2 for double bond
#b.index is index of the bond among all bonds of the molecule


from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw

m = Chem.MolFromSmiles('CCCC(=O)N')
# tmp=AllChem.Compute2DCoords(m)
# Draw.MolToFile(m,'cdk2_mol1.o.png')    


print(m.GetNumBonds())
print(m.GetNumAtoms())
for a in m.GetAtoms():
  for b in a.GetBonds():
    print(b.GetBeginAtom(), b.GetBeginAtomIdx(), b.GetBondType(), b.GetEndAtom(), b.GetEndAtomIdx(), b.GetIdx())
    
ecfp(m, radius=2)
