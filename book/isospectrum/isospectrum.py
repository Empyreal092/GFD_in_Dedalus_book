import numpy as np

def isospectrum(psi_mag):

    if psi_mag.ndim == 1:
        N = psi_mag.size
        psi_spec = (psi_mag[0::2]+psi_mag[1::2])/2
        psi_spec[0] += psi_mag[0]/2
    
    elif psi_mag.ndim == 2:
    # Input of k, l is not neede for isotropic discretizated fields
        if type(k) is bool:
            N = psi_mag.shape[0]
            k_mat, l_mat = np.meshgrid(range(N), range(N))
            spec_k_ary = np.arange(0,int(N/2)) # the K array where the spectrum will be indexed by
        else:
            k=k.ravel(); l=l.ravel()
            k_min = np.min([k[-1],l[-1]])
            k_mat, l_mat = np.meshgrid(k, l)
            dk = k[2]-k[1]; dl = l[2]-l[1]; dkmax = np.max([dk,dl])
            spec_k_ary = np.arange(0,k_min,dkmax)
        #####  
        psi_spec = np.zeros(spec_k_ary.size)
        for i in range(spec_k_ary.size):
            # make the mask for each K
            mask = np.sqrt(k_mat**2+l_mat**2) < spec_k_ary[i]
            mask *= np.sqrt(k_mat**2+l_mat**2) >= spec_k_ary[i-1]
            mask = mask*1/4; mask[0,:] *= 2; mask[:,0] *= 2;

            psi_spec[i] = (mask*psi_mag.T).sum()

    return psi_spec