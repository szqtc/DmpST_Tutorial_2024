## define a function for map visualization
def show_map(mcubefile, fitsidx=0, ibin=0, outfile=None):
    """
    mcubefile: the location of mdlcube.fits file
    fitsidx:   int, the index of the AllSource row in the mdlcube.fits file
    ibin:      int, the index of the energy bin to visualize
    outfile:   the output file name
    """
    from matplotlib import pyplot as plt
    from matplotlib import colors
    from DmpST import SkyMap
    # the binned model cube in each energy bin
    mcube = SkyMap.Ccube(mcubefile, hdu=fitsidx) # the index of AllSource is 5
    # make figure
    fig = plt.figure()#figsize=(6, 5))
    fig.add_subplot(111, projection=mcube.wcs)
    im = plt.imshow(mcube.data[:,:,ibin].T, origin='lower', norm=colors.PowerNorm(0.5))
    cb = plt.colorbar(im, label='photons/pixel')
    plt.xlabel('R.A.')
    plt.ylabel('Decl.')
    plt.title(mcubefile.split('/')[-1] + ' [%.1f - %.1f GeV]'%(mcube.emins[ibin]/1e3, mcube.emaxs[ibin]/1e3))
    if outfile is not None:
        plt.savefig(outfile)
    else:
        plt.show()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='a tool to convert fits map file to image file')
    parser.add_argument('mcubefile', type=str, help='the location of mdlcube.fits file')
    parser.add_argument('fitsidx', type=int, help='the index of row you want to show')
    parser.add_argument('outfile', type=str, help='the output image file name')
    parser.add_argument('-ibin', type=int, default=0, help='the index of the energy bin to visualize, default=0')
    args = parser.parse_args()
    show_map(args.mcubefile, args.fitsidx, args.ibin, args.outfile)