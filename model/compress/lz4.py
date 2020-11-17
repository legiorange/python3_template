import lz4tools


def lz4composs(source_dir):
    lz4tools.compressTarDefault(source_dir)
    testTar = lz4tools.openTar(source_dir+'.tar.lz4')
    testTar.list()
