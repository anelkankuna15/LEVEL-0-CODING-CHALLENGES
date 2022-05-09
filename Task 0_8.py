def convertor(m):
        return m//60,m%60

h,m=convertor(120)
print(f"{h}:{m}")