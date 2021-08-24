from pyscf import gto, scf

for i in range(15, 81):
    geom = f'''
        C      1
        H      1 {i*.05}
        H      1 1.09367050435513 2 109.471486233994
        H      1 1.09367001056061 2 109.471202276655 3 120.000203073166
        H      1 1.09367001056062 2 109.47120227664 3 -120.000203073151
    '''
    mol = gto.M(atom = geom, basis = "CC-PVDZ")
    mol.build()
    mf = scf.RHF(mol)
    hf = mf.kernel()

