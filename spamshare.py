import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))
