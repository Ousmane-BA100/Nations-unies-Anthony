from controller.___BrandsC import Brands

#br = Brands()

liste_brands = Brands.visualiserBrands()

print(liste_brands)

listeB = []

print("##################################")

for b in liste_brands:

    idb = b.getBrandId()

    nom = b.getBrandName()

    print(idb, nom)

    listeB.append((idb,nom)) # [], {}, (a,b)

print("**********************************")

print(listeB)
#%%
