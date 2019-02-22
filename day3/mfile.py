msrc = "fdsafj;kjlkfdsjaf"

mdst = {i  for i in msrc}

for i in mdst:
    if msrc.count(i) > 1:
        print(">1",i)
    else :
        print("==", i)

