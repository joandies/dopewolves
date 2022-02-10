from PIL import Image
import json
import random
import threading
from itertools import repeat


"""
Watch out on the syntax and make sure to add a new trait all over the script if you add one. Same goes for removing a trait.
"""
rarities = {
    "Backgrounds": [{'Trait': 'Pink', 'Quantity': 5, 'Rarity': 0.05}, {'Trait': 'Blue', 'Quantity': 5, 'Rarity': 0.05}, {'Trait': 'Orange', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Gradient Red', 'Quantity': 5, 'Rarity': 0.05}, {'Trait': 'Gradient Blue', 'Quantity': 5, 'Rarity': 0.05}, {'Trait': 'Gradient Green', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Gradient Orange', 'Quantity': 5, 'Rarity': 0.05}, {'Trait': 'Graffiti Wall', 'Quantity': 5, 'Rarity': 0.05}, {'Trait': 'Jungle', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Pink Wolf', 'Quantity': 5, 'Rarity': 0.05}, {'Trait': 'Blue Wolf', 'Quantity': 5, 'Rarity': 0.05}, {'Trait': 'Yellow Wolf', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Orange Wolf', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Green Wolf', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Gradient Pink', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Gradient Yellow', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Gradient Gray', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Graffiti Negative', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Night', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Oasis', 'Quantity': 5, 'Rarity': 0.05}],

    "Skins": [{'Trait': 'Regular', 'Quantity': 9, 'Rarity': 0.09}, {'Trait': 'Albino', 'Quantity': 9, 'Rarity': 0.09}, {'Trait': 'Silver Cyborg', 'Quantity': 9, 'Rarity': 0.09},
    {'Trait': 'Golden Cyborg', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'Dirty', 'Quantity': 8, 'Rarity': 0.08},{'Trait': 'Gold', 'Quantity': 8, 'Rarity': 0.08},
    {'Trait': 'Rainbow', 'Quantity': 8, 'Rarity': 0.08},{'Trait': 'Silver', 'Quantity': 8, 'Rarity': 0.08},{'Trait': 'Ruby', 'Quantity': 8, 'Rarity': 0.08},
    {'Trait': 'Sapphire', 'Quantity': 8, 'Rarity': 0.08},{'Trait': 'Emerald', 'Quantity': 8, 'Rarity': 0.08},{'Trait': 'Pink', 'Quantity': 8, 'Rarity': 0.08}],

    "Tops": [{'Trait': 'White', 'Quantity': 6, 'Rarity': 0.06}, {'Trait': 'Red', 'Quantity': 6, 'Rarity': 0.06},{'Trait': 'Gray', 'Quantity': 6, 'Rarity': 0.06},
    {'Trait': 'Hype', 'Quantity': 6, 'Rarity': 0.06},{'Trait': 'Black Suit', 'Quantity': 6, 'Rarity': 0.06},{'Trait': 'Metal Suit', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Red Suit', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Gold Suit', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Black', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Basketball Yellow', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Basketball Blue', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'None', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Sleeveless Black', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Sleeveless Pink', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Leather Jacket', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Mummy', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Turtleneck Black', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Turtleneck Beige', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Turtleneck White', 'Quantity': 5, 'Rarity': 0.05}],

    "Chains": [{'Trait': 'Silver', 'Quantity': 10, 'Rarity': 0.1}, {'Trait': 'Gold', 'Quantity': 9, 'Rarity': 0.09}, {'Trait': 'BTC', 'Quantity': 9, 'Rarity': 0.09},
    {'Trait': 'Hawai', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'None', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'Gold Wolf', 'Quantity': 9, 'Rarity': 0.09},
    {'Trait': 'Silver Wolf', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'Dog Collar', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'Rose', 'Quantity': 9, 'Rarity': 0.09},
    {'Trait': 'Chain', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'YingYang', 'Quantity': 9, 'Rarity': 0.09}],

    "Mouths": [{'Trait': 'Normal', 'Quantity': 7, 'Rarity': 0.07}, {'Trait': 'Gold', 'Quantity': 7, 'Rarity': 0.07},{'Trait': 'Bone', 'Quantity': 7, 'Rarity': 0.07},
    {'Trait': 'Juice', 'Quantity': 7, 'Rarity': 0.07},{'Trait': 'Bloody', 'Quantity': 6, 'Rarity': 0.06},{'Trait': 'Mad', 'Quantity': 6, 'Rarity': 0.06},
    {'Trait': 'Rainbow Tongue', 'Quantity': 6, 'Rarity': 0.06},{'Trait': 'Pacifier', 'Quantity': 6, 'Rarity': 0.06},{'Trait': 'Tongue', 'Quantity': 6, 'Rarity': 0.06},
    {'Trait': 'Mask Black', 'Quantity': 6, 'Rarity': 0.06},{'Trait': 'Mask Blue', 'Quantity': 6, 'Rarity': 0.06},{'Trait': 'Mask White', 'Quantity': 6, 'Rarity': 0.06},
    {'Trait': 'Gum Pink', 'Quantity': 6, 'Rarity': 0.06},{'Trait': 'Gum Green', 'Quantity': 6, 'Rarity': 0.06},{'Trait': 'Animal', 'Quantity': 6, 'Rarity': 0.06},
    {'Trait': 'Sad', 'Quantity': 6, 'Rarity': 0.06}],

    "Eyes": [{'Trait': 'Regular', 'Quantity': 5, 'Rarity': 0.05}, {'Trait': 'Damaged', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Regular Left', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Scared', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Tired', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Dollar', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Glasses', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Laser', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Patch', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Wink', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Blue Cyclope', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Green Cyclope', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Red Cyclope', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Dead', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Stoned', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Kawaii', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Monocle', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Star', 'Quantity': 5, 'Rarity': 0.05},
    {'Trait': 'Mask', 'Quantity': 5, 'Rarity': 0.05},{'Trait': 'Alert', 'Quantity': 5, 'Rarity': 0.05}],

    "Over Heads": [{'Trait': 'Cap', 'Quantity': 8, 'Rarity': 0.08}, {'Trait': 'Halo', 'Quantity': 8, 'Rarity': 0.08},{'Trait': 'Sim', 'Quantity': 7, 'Rarity': 0.07},
    {'Trait': 'None', 'Quantity': 7, 'Rarity': 0.07},{'Trait': 'Beanie', 'Quantity': 7, 'Rarity': 0.07},{'Trait': 'Cheff', 'Quantity': 7, 'Rarity': 0.07},
    {'Trait': 'Bandana Black', 'Quantity': 7, 'Rarity': 0.07},{'Trait': 'Hardhat', 'Quantity': 7, 'Rarity': 0.07},{'Trait': 'Bandana Red', 'Quantity': 7, 'Rarity': 0.07},
    {'Trait': 'Bandana Blue', 'Quantity': 7, 'Rarity': 0.07},{'Trait': 'Bandana Wolf', 'Quantity': 7, 'Rarity': 0.07},{'Trait': 'Head Pilot', 'Quantity': 7, 'Rarity': 0.07},
    {'Trait': 'Bowler Hat', 'Quantity': 7, 'Rarity': 0.07},{'Trait': 'Crown', 'Quantity': 7, 'Rarity': 0.07}],
    # New:
    "Ears": [{'Trait': 'Bandage', 'Quantity': 10, 'Rarity': 0.1}, {'Trait': 'Airpod', 'Quantity': 9, 'Rarity': 0.09}, {'Trait': 'None', 'Quantity': 9, 'Rarity': 0.09},
    {'Trait': 'Diamond', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'Full Gold', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'Full Silver', 'Quantity': 9, 'Rarity': 0.09},
    {'Trait': 'Gold Piercing', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'Silver Piercing', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'Gold Cross', 'Quantity': 9, 'Rarity': 0.09},
    {'Trait': 'Silver Cross', 'Quantity': 9, 'Rarity': 0.09},{'Trait': 'Dollar', 'Quantity': 9, 'Rarity': 0.09}],
    
    "Noses": [{'Trait': 'Silver', 'Quantity': 20, 'Rarity': 0.2}, {'Trait': 'Gold', 'Quantity': 20, 'Rarity': 0.2},{'Trait': 'Moustache', 'Quantity': 20, 'Rarity': 0.2},
    {'Trait': 'Bone', 'Quantity': 20, 'Rarity': 0.2},{'Trait': 'None', 'Quantity': 20, 'Rarity': 0.2}]
}

whole = [] # for duplicate check

"""
Creates random shuffled lists of each trait category with all its traits and their desired quantity.
"""
backgroundsList = []
for x in rarities['Backgrounds']:
    backgroundsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(backgroundsList)
skinsList = []
for x in rarities['Skins']:
    skinsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(skinsList)
topsList = []
for x in rarities['Tops']:
    topsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(topsList)
chainsList = []
for x in rarities['Chains']:
    chainsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(chainsList)
mouthsList = []
for x in rarities['Mouths']:
    mouthsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(mouthsList)
eyesList = []
for x in rarities['Eyes']:
    eyesList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(eyesList)
overheadsList = []
for x in rarities['Over Heads']:
    overheadsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(overheadsList)
# New:
earsList = []
for x in rarities['Ears']:
    earsList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(earsList)
nosesList = []
for x in rarities['Noses']:
    nosesList.extend(repeat(x['Trait'], x['Quantity']))
random.shuffle(nosesList)
path = 'D:\DopeWolves\images/' # standard path to the images directory

"""
Please keep the same format which is having Eyes_ for example at least before the actual trait name. Don't forget .png or .jpg or whatever at the end.
"""
bgs = ['00_BG_Pink.png', '01_BG_Blue.png', '02_BG_Orange.png','03_BG_Gradient Red.png','04_BG_Gradient Blue.png','05_BG_Gradient Green.png','06_BG_Gradient Orange.png',
'07_BG_Graffiti Wall.png','08_BG_Jungle.png','09_BG_Pink Wolf.png','10_BG_Blue Wolf.png','11_BG_Yellow Wolf.png','12_BG_Orange Wolf.png','13_BG_Green Wolf.png',
'14_BG_Gradient Pink.png','15_BG_Gradient Yellow.png','16_BG_Gradient Gray.png','17_BG_Graffiti Negative.png','18_BG_Night.png','19_BG_Oasis.png']
skins = ['00_Skin_Regular.png', '01_Skin_Albino.png','02_Skin_Silver Cyborg.png','03_Skin_Golden Cyborg.png','04_Skin_Dirty.png','05_Skin_Gold.png','06_Skin_Rainbow.png',
'07_Skin_Silver.png','08_Skin_Ruby.png','09_Skin_Sapphire.png','10_Skin_Emerald.png','11_Skin_Pink.png']
tops = ['00_Top_White.png', '01_Top_Red.png','02_Top_Gray.png','03_Top_Hype.png','04_Top_Black Suit.png','05_Top_Metal Suit.png','06_Top_Red Suit.png','07_Top_Gold Suit.png',
'08_Top_Black.png','09_Top_Basketball Yellow.png','10_Top_Basketball Blue.png','11_Top_None.png','12_Top_Sleeveless Black.png','13_Top_Sleeveless Pink.png',
'14_Top_Leather Jacket.png','15_Top_Mummy.png','16_Top_Turtleneck Black.png','17_Top_Turtleneck Beige.png','18_Top_Turtleneck White.png']
chains = ['00_Chain_Silver.png', '01_Chain_Gold.png','02_Chain_Rose.png','03_Chain_BTC.png','04_Chain_Hawai.png','05_Chain_None.png','06_Chain_Gold Wolf.png','07_Chain_Silver Wolf.png','08_Chain_Dog Collar.png',
'09_Chain_Chain.png','10_Chain_YingYang.png']
mouths = ['00_Mouth_Normal.png', '01_Mouth_Gold.png','02_Mouth_Bone.png','03_Mouth_Juice.png','04_Mouth_Bloody.png','05_Mouth_Mad.png','06_Mouth_Rainbow Tongue.png',
'07_Mouth_Pacifier.png','08_Mouth_Tongue.png','09_Mouth_Mask Black.png','10_Mouth_Mask Blue.png','11_Mouth_Mask White.png','12_Mouth_Gum Pink.png','13_Mouth_Gum Green.png',
'14_Mouth_Animal.png','15_Mouth_Sad.png']
eyez = ['00_Eyes_Regular.png', '01_Eyes_Damaged.png','02_Eyes_Regular Left.png','03_Eyes_Scared.png','04_Eyes_Tired.png','05_Eyes_Dollar.png','06_Eyes_Glasses.png','07_Eyes_Laser.png',
'08_Eyes_Patch.png','09_Eyes_Wink.png','10_Eyes_Blue Cyclope.png','11_Eyes_Green Cyclope.png','12_Eyes_Red Cyclope.png','13_Eyes_Dead.png','14_Eyes_Stoned.png',
'15_Eyes_Kawaii.png','16_Eyes_Monocle.png','17_Eyes_Star.png','18_Eyes_Mask.png','19_Eyes_Alert.png']
overheads = ['00_Head_Cap.png', '01_Head_Halo.png','02_Head_Sim.png','03_Head_None.png','04_Head_Beanie.png','05_Head_Cheff.png','06_Head_Bandana Black.png','07_Head_Hardhat.png',
'08_Head_Bandana Red.png','09_Head_Bandana Blue.png','10_Head_Bandana Wolf.png','11_Head_Pilot.png','12_Head_Bowler Hat.png','13_Head_Crown.png']
# New:
ears = ['00_Ear_Bandage.png','01_Ear_Airpod.png','02_Ear_None.png','03_Ear_Diamond.png','04_Ear_Full Gold.png','05_Ear_Full Silver.png','06_Ear_Gold Piercing.png','07_Ear_Silver Piercing.png',
'08_Ear_Gold Cross.png','09_Ear_Silver Cross.png','10_Ear_Dollar.png']
noses = ['00_Nose_Silver.png','01_Nose_Gold.png','02_Nose_Moustache.png','03_Nose_Bone.png','04_Nose_None.png']

total=100 # size of collection

def gen():
    count = 0
    while count != total: # size of collection, so script stops
        traits = []
        traits_names = []

        """
        Just some checks to avoid issues coming up in the big lists of traits.
        """
        for x in backgroundsList:
            if len(x) < 2:
                backgroundsList.remove(x)
        for x in skinsList:
            if len(x) < 2:
                skinsList.remove(x)
        for x in topsList:
            if len(x) < 2:
                topsList.remove(x)
        for x in chainsList:
            if len(x) < 2:
                chainsList.remove(x)
        for x in mouthsList:
            if len(x) < 2:
                mouthsList.remove(x)
        for x in eyesList:
            if len(x) < 2:
                eyesList.remove(x)
        for x in overheadsList:
            if len(x) < 2:
                overheadsList.remove(x)
        # New:
        for x in earsList:
            if len(x) < 2:
                earsList.remove(x)
        for x in nosesList:
            if len(x) < 2:
                nosesList.remove(x)
                
        """
        Collecting of the randomly chosen traits.
        """
        bgcheck = random.choice(backgroundsList)
        backgroundsList.remove(bgcheck)
        for x in bgs:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == bgcheck:
                bg = x
                break

        skincheck = random.choice(skinsList)
        skinsList.remove(skincheck)
        for x in skins:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == skincheck:
                skin = x
                break

        topcheck = random.choice(topsList)
        topsList.remove(topcheck)
        for x in tops:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == topcheck:
                top = x
                break

        chaincheck = random.choice(chainsList)
        chainsList.remove(chaincheck)
        for x in chains:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == chaincheck:
                chain = x
                break

        mouthcheck = random.choice(mouthsList)
        mouthsList.remove(mouthcheck)
        for x in mouths:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == mouthcheck:
                mouth = x
                break

        eyescheck = random.choice(eyesList)
        eyesList.remove(eyescheck)
        for x in eyez:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == eyescheck:
                eyes = x
                break

        overheadcheck = random.choice(overheadsList)
        overheadsList.remove(overheadcheck)
        for x in overheads:
            #print(f'x: {x}, ohc: {overheadcheck}')
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == overheadcheck:
                overhead = x
                break
        # New:
        earscheck = random.choice(earsList)
        earsList.remove(earscheck)
        for x in ears:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == earscheck:
                ear = x
                break
        
        nosescheck = random.choice(nosesList)
        nosesList.remove(nosescheck)
        for x in noses:
            if x.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] == nosescheck:
                nose = x
                break
        
                
        """
        Exceptions for traits that don't fit with everything.
        """       
        # if armor == '01_Armor_Example1.png':
        #     eyes = '00_Eyes_None.png'
        # if overhead == '07_Overhead_Example_2.png':
        #     eyes = '00_Eyes_None.png'
        #     mouth = '00_Mouth_None.png'

        traits.extend((bg, skin, top, chain, mouth, nose, eyes, overhead, ear)) # putting all traits for this NFT in a list (make sure to choose your order of layering by this list from left to right)

        for trait in traits:
            trait = trait.split('.png')[0].replace('_', ' ').replace(' ', '_', 2).split('_')[2] # getting the exact trait names from the file name
            traits_names.append(trait)
            
        if traits not in whole: # duplicate check

            whole.append(traits)

            for trait in traits:
                if 'BG' in trait:
                    #print(trait)
                    nft = Image.open(path+trait).convert('RGBA') # important for background
                else:
                    #print(trait)
                    trait = Image.open(path+trait).convert('RGBA')
                    nft = Image.alpha_composite(nft, trait) # layer process of each trait
            
            """
            This is the most dangerous part. Please triple check your metadata because 95% of all errors when uploading to a Candy Machine are caused by wrong metadata.
            Please remove the comments from it if you are done with setup xd.
            """
            metadata = {
                "name":f"Wolf #{count+1}","symbol":"", # +1 because metadata files need to start with 0 but your NFT obviously has the number 1
                "description":"8888 Dope Wolves are here, ready for the HUNT", # description of your project
                "seller_fee_basis_points":500,"image":f"{count}.png","external_url":"/https://dopewolves.com//", # 500 stands for 5% royalties on marketplaces and external_url is your project's website
                "attributes":[
                    {"trait_type":"Background","value":traits_names[0]}, # number in the brackets is the index number of the trait in the list where you decided the layer order
                    {"trait_type":"Skin","value":traits_names[1]},
                    {"trait_type":"Top","value":traits_names[2]},
                    {"trait_type":"Chain","value":traits_names[3]},
                    {"trait_type":"Mouth","value":traits_names[4]},
                    {"trait_type":"Nose","value":traits_names[5]},
                    {"trait_type":"Eyes","value":traits_names[6]},
                    {"trait_type":"Over Head","value":traits_names[7]},
                    {"trait_type":"Ear","value":traits_names[8]}],
                    "collection":{"name":"Wolf","family":"Dope Wolves"},
                    "properties":{"files":[{"uri":f"{count}.png","type":"image/png"}],
                    "category":"image","maxSupply":1,"creators":[{"address":"FALTA PONER WALLET","share":33}, {"address":"FALTA PONER WALLET","share":33}, {"address":"FALTA PONER WALLET","share":34}]} # 100 means 100% of the royalties' proceeds and you can add more to split it
            }

            nft.save(f'DWresults/{count}.png',"PNG") # saving of the generated NFT

            metadata = json.dumps(metadata)
            metadataFile = open(f"DWresults/{count}.json", "w")
            metadataFile.write(metadata) # saving of the metadata of this generated NFT
            metadataFile.close()

            count += 1

        else: # add traits to the list when a duplicate is found
            backgroundsList.append(traits_names[0])
            skinsList.append(traits_names[1])
            topsList.append(traits_names[2])
            chainsList.append(traits_names[3])
            mouthsList.append(traits_names[4])
            eyesList.append(traits_names[5])
            overheadsList.append(traits_names[6])
            earsList.append(traits_names[6])
            nosesList.append(traits_names[6])
            #invisibleList.append(virtue)

    else:
        print('Successfully Generated All NFTs!')

threading.Thread(target=gen, args=()).start() # thread to start the gen, feel free to add more function and threads to speed up the generation process
