import bnlearn as bn
df = bn.import_example()
model = bn.structure_learning.fit(df)
G = bn.plot(model)