from pyscf import gto, dft
from pyscf.geomopt.berny_solver import optimize
mol = gto.Mole()

mol.atom = '''
    C
    H 1 1.089
    H 1 1.089 2 109.4710
    H 1 1.089 2 109.4710 3 120
    H 1 1.089 2 109.4710 3 -120
'''

mol.basis = "6-31G*"
mol.build()

mf = dft.RKS(mol)
mf.xc = "B3LYP"
mf.conv_tol = 1e-12
mf.verbose = 4
mf.kernel()
geom = optimize(mf).tostring(format='zmat')
print(geom)


