def binMultiply(bin1Str, bin2Str):
    dec1 = int(bin1Str, base=2)
    dec2 = int(bin2Str, base=2)
    ret = str(bin(dec1 * dec2)).replace('0b', '')
    print("binMultiply('%s', '%s')" % (bin1Str, bin2Str))
    print("    '%s' -> '%s'" % (bin1Str, dec1))
    print("    '%s' -> '%s'" % (bin2Str, dec2))
    print("    '%s' -> '%s'" % (dec1*dec2, ret))
    return ret

binMultiply('101', '10')
binMultiply('111', '101')
