patches= {
    0xbc860: b'\x48\xC7\xC0\x01\x00\x00\x00\xC3',
    0xe918a: b'\x90'*11
}

c=bytearray(open("prismlauncher.exe","rb").read())

for offset, replacement in patches.items():
    c[offset:offset+len(replacement)]=replacement


open("prismlauncher_patched.exe", "wb").write(c)
