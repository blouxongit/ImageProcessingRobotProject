import os

# fonction qui crée le fichier de description pour nos images négatives                


path1 = "images_neg_clean/"

for img in os.listdir(path1):
    line = path1 + img+'\n'
    with open('bg.txt','a') as f:
        f.write(line)

