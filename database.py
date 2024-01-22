import sqlite3
conn = sqlite3.connect("C:\\Users\\Judy Abusteit\\MixSafe\\reactions.db")
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product1 TEXT,
        product2 TEXT,
        reaction TEXT
    )
''')

reactions= [

    ('Ammonium hydroxide', 'Sulfuric acid', 'Ammonium sulfate'),
    ('Ammonium hydroxide', 'Acetic acid', 'Ammonium acetate'),
    ('Ammonium hydroxide', 'Formic acid', 'Ammonium formate'),
    ('Ammonium hydroxide', 'Copper sulfate', 'Ammonium copper'),
    ('Ammonium hydroxide', 'Iron sulfate', 'Ammonium iron'),
    ('Ammonium hydroxide', 'Chloroform', 'Ammonium chloroformate'),
    ('Ammonium hydroxide', 'Ethanol', 'Ammonium ethanoate'),
    ('Ammonium hydroxide', 'Isopropyl alcohol', 'Ammonium isopropanoate'),
    ('Ammonium hydroxide', 'Methanol', 'Ammonium methanoate'),
    ('Ammonium hydroxide', 'Benzalkonium chloride', 'Ammonium benzalkonium'),
    ('Ammonium hydroxide', 'Sodium dichloroisocyanurate', 'Ammonium dichloroisocyanurate'),
    ('Ammonium hydroxide', 'Sodium percarbonate', 'Ammonium percarbonate'),
    ('Ammonium hydroxide', 'Alcohol ethoxylates', 'Ammonium ethoxylate'),
    ('Ammonium hydroxide', 'Sodium lauryl sulfate', 'Ammonium lauryl sulfate'),
    ('Ammonium hydroxide', 'Cocamidopropyl betaine', 'Ammonium cocamidopropyl betaine'),
    ('Ammonium hydroxide', 'Sodium gluconate', 'Ammonium gluconate'),
    ('Ammonium hydroxide', 'Trisodium phosphate', 'Ammonium phosphate'),
    ('Ammonium hydroxide', 'Sodium borate', 'Ammonium borate'),
    ('Ammonium hydroxide', 'Aluminum sulfate', 'Ammonium aluminum sulfate'),
    ('Ammonium hydroxide', 'Sodium chlorite', 'Ammonium chlorite'),
    ('Ammonium hydroxide', 'Potassium hydroxide', 'Potassium ammonium'),
    ('Ammonium hydroxide', 'Sodium thiosulfate', 'Ammonium thiosulfate'),
    ('Ammonium hydroxide', 'Sodium metabisulfite', 'Ammonium bisulfite'),
    ('Ammonium hydroxide', 'Calcium chloride', 'Ammonium chloride'),
    ('Ammonium hydroxide', 'Sodium chloride', 'Ammonium chloride'),
    ('Ammonium hydroxide', 'Copper chloride', 'Ammonium copper'),
    ('Ammonium hydroxide', 'Iron chloride', 'Ammonium iron'),
    ('Ammonium hydroxide', 'Boric acid', 'Ammonium borate'),
    ('Ammonium hydroxide', 'Glycerin', 'Ammonium glycerate'),
    ('Ammonium hydroxide', 'Sodium bicarbonate', 'Ammonium bicarbonate'),
    ('Ammonium hydroxide', 'Potassium permanganate', 'Ammonium permanganate'),
    ('Ammonium hydroxide', 'Citric acid', 'Ammonium citrate'),
    ('Ammonium hydroxide', 'Lactic acid', 'Ammonium lactate'),

    ('Sodium hypochlorite', 'Ammonia', 'Chloramine'),
    ('Sodium hypochlorite', 'Sulfuric acid', 'Chlorine gas and Sulfuric acid mist'),
    ('Sodium hypochlorite', 'Acetic acid', 'Chlorine gas and Acetic acid vapors'),
    ('Sodium hypochlorite', 'Hydrochloric acid', 'Chlorine gas and Hypochlorous acid'),
    ('Sodium hypochlorite', 'Formic acid', 'Carbon monoxide'),
    ('Sodium hypochlorite', 'Copper sulfate', 'Copper hydroxide'),
    ('Sodium hypochlorite', 'Iron sulfate', 'Iron hydroxide'),
    ('Sodium hypochlorite', 'Chloroform', 'Chloroform'),
    ('Sodium hypochlorite', 'Ethanol', 'Acetaldehyde'),
    ('Sodium hypochlorite', 'Isopropyl alcohol', 'Acetone'),
    ('Sodium hypochlorite', 'Methanol', 'Formaldehyde'),
    ('Sodium hypochlorite', 'Sodium dichloroisocyanurate', 'Cyanuric acid'),
    ('Sodium hypochlorite', 'Alcohol ethoxylates', 'Aldehydes'),
    ('Sodium hypochlorite', 'Sodium lauryl sulfate', 'Sulfur compounds'),
    ('Sodium hypochlorite', 'Cocamidopropyl betaine', 'Sulfur compounds'),
    ('Sodium hypochlorite', 'Sodium gluconate', 'Sodium compounds'),
    ('Sodium hypochlorite', 'Trisodium phosphate', 'Sodium compounds'),
    ('Sodium hypochlorite', 'Sodium borate', 'Boron compounds'),
    ('Sodium hypochlorite', 'Sodium silicate', 'Sodium compounds'),
    ('Sodium hypochlorite', 'Sodium chlorite', 'Chlorine dioxide'),
    ('Sodium hypochlorite', 'Ammonium chloride', 'Ammonium hydroxide'),
    ('Sodium hypochlorite', 'Phosphoric acid', 'Phosphorus compounds'),
    ('Sodium hypochlorite', 'Calcium chloride', 'Calcium compounds'),
    ('Sodium hypochlorite', 'Copper chloride', 'Copper compounds'),
    ('Sodium hypochlorite', 'Iron chloride', 'Iron compounds'),
    ('Sodium hypochlorite', 'Benzene sulfonic acid', 'Benzene compounds'),
    ('Sodium hypochlorite', 'Polyethylene glycol', 'Polyethylene compounds'),
    ('Sodium hypochlorite', 'Sodium acetate', 'Acetic acid'),
    ('Sodium hypochlorite', 'Sodium perborate', 'Sodium compounds'),
    ('Sodium hypochlorite', 'Hydrogen peroxide', 'Oxygen and Chlorine gas'),
    ('Sodium hypochlorite', 'Potassium permanganate', 'Chlorine gas and Potassium hydroxide'),
    ('Sodium hypochlorite', 'Sodium carbonate', 'Chlorine gas and Sodium carbonate dust'),
    ('Sodium hypochlorite', 'Citric acid', 'Chlorine gas and Citric acid vapors'),
    ('Sodium hypochlorite', 'Lactic acid', 'Chlorine gas and Lactic acid vapors'),
    ('Sodium hypochlorite', 'Boric acid', 'Chlorine gas and Boric acid vapors'),
    ('Sodium hypochlorite', 'Glycerin', 'Chlorine gas and Glycerol vapors'),
    ('Sodium hypochlorite', 'Sodium bicarbonate', 'Chlorine gas and Sodium carbonate dust'),
    ('Sodium hypochlorite', 'Chloroform', 'Chloroform and Chlorine gas'),
    ('Sodium hypochlorite', 'Sodium sulfate', 'Chlorine gas and Sodium sulfate dust'),
    ('Sodium hypochlorite', 'Aluminum sulfate', 'Chlorine gas and Aluminum compounds'),
    ('Sodium hypochlorite', 'Ammonium hydroxide', 'Ammonium hydroxide vapors'),
    ('Sodium hypochlorite', 'Phosphorus compounds', 'Phosphorus vapors'),
    ('Sodium hypochlorite', 'Calcium compounds', 'Calcium vapors'),
    ('Sodium hypochlorite', 'Copper compounds', 'Copper vapors'),
    ('Sodium hypochlorite', 'Iron compounds', 'Iron vapors'),
    ('Sodium hypochlorite', 'Boron trioxide', 'Boron trioxide vapors'),
    ('Sodium hypochlorite', 'Glycerin', 'Glycerin vapors'),
    ('Sodium hypochlorite', 'Carbon monoxide', 'Carbon monoxide gas'),
    ('Sodium hypochlorite', 'Sulfur dioxide', 'Sulfur dioxide gas'),
    ('Sodium hypochlorite', 'Potassium compounds', 'Potassium oxide'),
    ('Sodium hypochlorite', 'Phosphorus compounds', 'Phosphorus pentoxide'),
    ('Sodium hypochlorite', 'Calcium compounds', 'Calcium peroxide'),
    ('Sodium hypochlorite', 'Iron compounds', 'Iron oxide'),
    ('Sodium hypochlorite', 'Polyethylene compounds', 'Polyethylene oxide'),
    ('Sodium hypochlorite', 'Acetic acid', 'Acetic acid vapors'),
    ('Sodium hypochlorite', 'Sodium compounds', 'Sodium oxide'),
    ('Sodium hypochlorite', 'Chlorine dioxide', 'Chlorine dioxide gas')

    ('Hydrogen peroxide', 'Ammonia', 'Ammonium hydroxide'),
    ('Hydrogen peroxide', 'Chlorine bleach', 'Chlorine gas'),
    ('Hydrogen peroxide', 'Sulfuric acid', 'Peroxymonosulfuric acid'),
    ('Hydrogen peroxide', 'Acetic acid', 'Peracetic acid'),
    ('Hydrogen peroxide', 'Potassium permanganate', 'Ozone'),
    ('Hydrogen peroxide', 'Sodium hypochlorite', 'Chlorine gas'),
    ('Hydrogen peroxide', 'Hydrochloric acid', 'Chlorine gas'),
    ('Hydrogen peroxide', 'Formic acid', 'Carbon monoxide'),
    ('Hydrogen peroxide', 'Sodium carbonate', 'Carbon dioxide'),
    ('Hydrogen peroxide', 'Copper sulfate', 'Sulfur dioxide'),
    ('Hydrogen peroxide', 'Iron sulfate', 'Sulfur dioxide'),
    ('Hydrogen peroxide', 'Sodium chloride', 'Chlorine gas'),
    ('Hydrogen peroxide', 'Citric acid', 'Carbon dioxide'),
    ('Hydrogen peroxide', 'Lactic acid', 'Carbon dioxide'),
    ('Hydrogen peroxide', 'Boric acid', 'Boron trioxide'),
    ('Hydrogen peroxide', 'Glycerin', 'Carbon dioxide'),
    ('Hydrogen peroxide', 'Sodium bicarbonate', 'Carbon dioxide'),
    ('Hydrogen peroxide', 'Chloroform', 'Phosgene'),
    ('Hydrogen peroxide', 'Sodium sulfate', 'Sulfur dioxide'),
    ('Hydrogen peroxide', 'Ethanol', 'Acetaldehyde'),
    ('Hydrogen peroxide', 'Isopropyl alcohol', 'Acetone'),
    ('Hydrogen peroxide', 'Methanol', 'Formaldehyde'),
    ('Hydrogen peroxide', 'Benzalkonium chloride', 'Ammonium compounds'),
    ('Hydrogen peroxide', 'Sodium dichloroisocyanurate', 'Chlorine gas'),
    ('Hydrogen peroxide', 'Sodium percarbonate', 'Carbon dioxide'),
    ('Hydrogen peroxide', 'Alcohol ethoxylates', 'Aldehydes'),
    ('Hydrogen peroxide', 'Sodium lauryl sulfate', 'Sulfur compounds'),
    ('Hydrogen peroxide', 'Cocamidopropyl betaine', 'Sulfur compounds')
    
    ('Ammonia', 'Chlorine', 'Chloramine'),
    ('Ammonia', 'Bleach', 'Chloramine gas'),
    ('Ammonia', 'Sodium hypochlorite', 'Chloramine gas'),
    ('Ammonia', 'Hydrogen peroxide', 'Hydroxylamine'),
    ('Ammonia', 'Sulfuric acid', 'Ammonium sulfate'),
    ('Ammonia', 'Nitric acid', 'Ammonium nitrate'),
    ('Ammonia', 'Acetic acid', 'Ammonium acetate'),
    ('Ammonia', 'Phosphoric acid', 'Ammonium phosphate'),
    ('Ammonia', 'Sodium hydroxide', 'Ammonium hydroxide'),
    ('Ammonia', 'Calcium chloride', 'Ammonium chloride'),
    ('Ammonia', 'Sodium carbonate', 'Ammonium carbonate'),
    ('Ammonia', 'Copper sulfate', 'Ammonium copper'),
    ('Ammonia', 'Iron sulfate', 'Ammonium iron'),
    ('Ammonia', 'Hydrochloric acid', 'Ammonium chloride'),
    ('Ammonia', 'Potassium hydroxide', 'Potassium ammonium'),
    ('Ammonia', 'Sodium chloride', 'Ammonium chloride'),
    ('Ammonia', 'Sodium thiosulfate', 'Ammonium thiosulfate'),
    ('Ammonia', 'Sodium metabisulfite', 'Ammonium bisulfite'),
    ('Ammonia', 'Citric acid', 'Ammonium citrate'),
    ('Ammonia', 'Lactic acid', 'Ammonium lactate'),
    ('Ammonia', 'Boric acid', 'Ammonium borate'),
    ('Ammonia', 'Glycerin', 'Ammonium glycerate'),
    ('Ammonia', 'Sodium bicarbonate', 'Ammonium bicarbonate'),
    ('Ammonia', 'Potassium permanganate', 'Ammonium permanganate'),
    ('Ammonia', 'Chloroform', 'Ammonium chloroformate'),
    ('Ammonia', 'Sodium sulfate', 'Ammonium sulfate'),
    ('Ammonia', 'Ethanol', 'Ammonium ethanoate'),
    ('Ammonia', 'Isopropyl alcohol', 'Ammonium isopropanoate'),
    ('Ammonia', 'Methanol', 'Ammonium methanoate'),
    ('Ammonia', 'Benzalkonium chloride', 'Ammonium benzalkonium'),
    ('Ammonia', 'Sodium dichloroisocyanurate', 'Ammonium dichloroisocyanurate'),
    ('Ammonia', 'Sodium percarbonate', 'Ammonium percarbonate'),
    ('Ammonia', 'Alcohol ethoxylates', 'Ammonium ethoxylate'),
    ('Ammonia', 'Sodium lauryl sulfate', 'Ammonium lauryl sulfate'),
    ('Ammonia', 'Cocamidopropyl betaine', 'Ammonium cocamidopropyl betaine'),
    ('Ammonia', 'Sodium gluconate', 'Ammonium gluconate'),
    ('Ammonia', 'Trisodium phosphate', 'Ammonium phosphate'),
    ('Ammonia', 'Sodium borate', 'Ammonium borate'),
    ('Ammonia', 'Sodium silicate', 'Ammonium silicate'),
    ('Ammonia', 'Aluminum sulfate', 'Ammonium aluminum sulfate'),
    ('Ammonia', 'Sodium chlorite', 'Ammonium chlorite'),
    ('Ammonia', 'Hydrogen peroxide', 'Ammonium peroxide'),
    ('Ammonia', 'Sodium hypochlorite', 'Ammonium hypochlorite')

    ('Isopropyl alcohol', 'Ammonia', 'Isopropylamine'),
    ('Isopropyl alcohol', 'Sodium hypochlorite', 'Isopropyl hypochlorite'),
    ('Isopropyl alcohol', 'Sulfuric acid', 'Isopropyl sulfate'),
    ('Isopropyl alcohol', 'Hydrogen chloride', 'Isopropyl chloride'),
    ('Isopropyl alcohol', 'Calcium chloride', 'Isopropyl chloride'),
    ('Isopropyl alcohol', 'Boric acid', 'Isopropyl borate'),
    ('Isopropyl alcohol', 'Phosphoric acid', 'Isopropyl phosphate'),
    ('Isopropyl alcohol', 'Sodium hydroxide', 'Isopropyl sodium'),
    ('Isopropyl alcohol', 'Potassium hydroxide', 'Isopropyl potassium'),
    ('Isopropyl alcohol', 'Citric acid', 'Isopropyl citrate'),
    ('Isopropyl alcohol', 'Lactic acid', 'Isopropyl lactate'),
    ('Isopropyl alcohol', 'Hydrogen peroxide', 'Isopropyl peroxide'),
    ('Isopropyl alcohol', 'Sodium bicarbonate', 'Isopropyl carbonate'),
    ('Isopropyl alcohol', 'Sodium carbonate', 'Isopropyl carbonate'),
    ('Isopropyl alcohol', 'Copper sulfate', 'Isopropyl copper'),
    ('Isopropyl alcohol', 'Sodium laureth sulfate', 'Isopropyl sulfate'),
    ('Isopropyl alcohol', 'Potassium sorbate', 'Isopropyl sorbate'),
    ('Isopropyl alcohol', 'Glycerin', 'Isopropyl glycerate'),
    ('Isopropyl alcohol', 'Sodium metabisulfite', 'Isopropyl sulfite'),
    ('Isopropyl alcohol', 'Ammonium hydroxide', 'Isopropyl ammonium'),
    ('Isopropyl alcohol', 'Chlorine dioxide', 'Isopropyl chlorite'),
    ('Isopropyl alcohol', 'Hydrogen cyanide', 'Isopropyl cyanide'),
    ('Isopropyl alcohol', 'Sulfur dioxide', 'Isopropyl sulfite'),
    ('Isopropyl alcohol', 'Phosphorus trichloride', 'Isopropyl phosphite'),
    ('Isopropyl alcohol', 'Magnesium sulfate', 'Isopropyl magnesium'),
    ('Isopropyl alcohol', 'Magnesium sulfate', 'Isopropyl magnesium'),
    ('Isopropyl alcohol', 'Thionyl chloride', 'Isopropyl chloride'),
    ('Isopropyl alcohol', 'Mercury chloride', 'Isopropyl mercury'),
    ('Isopropyl alcohol', 'Aluminum chloride', 'Isopropyl chloride'),
    ('Isopropyl alcohol', 'Chromium trioxide', 'Isopropyl chromate'),
    ('Isopropyl alcohol', 'Potassium permanganate', 'Isopropyl permanganate'),
    ('Isopropyl alcohol', 'Chloroform', 'Isopropyl chloroformate'),
    ('Isopropyl alcohol', 'Sodium thiosulfate', 'Isopropyl thiosulfate'),
    ('Isopropyl alcohol', 'Acetic acid', 'Isopropyl acetate'),
    ('Isopropyl alcohol', 'Ammonium chloride', 'Isopropyl ammonium')

    ('Ethyl alcohol', 'Ammonia', 'Ethylamine'),
    ('Ethyl alcohol', 'Sodium hypochlorite', 'Ethyl hypochlorite'),
    ('Ethyl alcohol', 'Sulfuric acid', 'Ethyl sulfate'),
    ('Ethyl alcohol', 'Hydrogen chloride', 'Ethyl chloride'),
    ('Ethyl alcohol', 'Calcium chloride', 'Ethyl calcium'),
    ('Ethyl alcohol', 'Boric acid', 'Ethyl borate'),
    ('Ethyl alcohol', 'Phosphoric acid', 'Ethyl phosphate'),
    ('Ethyl alcohol', 'Sodium hydroxide', 'Sodium ethoxide'),
    ('Ethyl alcohol', 'Potassium hydroxide', 'Potassium ethoxide'),
    ('Ethyl alcohol', 'Citric acid', 'Ethyl citrate'),
    ('Ethyl alcohol', 'Lactic acid', 'Ethyl lactate'),
    ('Ethyl alcohol', 'Hydrogen peroxide', 'Ethyl peroxide'),
    ('Ethyl alcohol', 'Sodium bicarbonate', 'Ethyl carbonate'),
    ('Ethyl alcohol', 'Sodium carbonate', 'Ethyl carbonate'),
    ('Ethyl alcohol', 'Copper sulfate', 'Ethyl copper'),
    ('Ethyl alcohol', 'Sodium laureth sulfate', 'Ethyl sulfate'),
    ('Ethyl alcohol', 'Potassium sorbate', 'Ethyl sorbate'),
    ('Ethyl alcohol', 'Glycerin', 'Ethyl glycerate'),
    ('Ethyl alcohol', 'Sodium metabisulfite', 'Ethyl sulfite'),
    ('Ethyl alcohol', 'Ammonium hydroxide', 'Ethyl ammonium'),
    ('Ethyl alcohol', 'Chlorine dioxide', 'Chloroethyl alcohol'),
    ('Ethyl alcohol', 'Sodium chlorite', 'Ethyl chlorite'),
    ('Ethyl alcohol', 'Hydrogen cyanide', 'Ethyl cyanide'),
    ('Ethyl alcohol', 'Sulfur dioxide', 'Ethyl sulfite'),
    ('Ethyl alcohol', 'Potassium hydroxide', 'Potassium ethoxide'),
    ('Ethyl alcohol', 'Phosphorus trichloride', 'Ethyl phosphite'),
    ('Ethyl alcohol', 'Sodium hydroxide', 'Sodium ethoxide'),
    ('Ethyl alcohol', 'Magnesium sulfate', 'Ethyl magnesium'),
    ('Ethyl alcohol', 'Thionyl chloride', 'Ethyl chloride'),
    ('Ethyl alcohol', 'Mercury chloride', 'Ethyl mercury'),
    ('Ethyl alcohol', 'Aluminum chloride', 'Ethyl chloride'),
    ('Ethyl alcohol', 'Chromium trioxide', 'Ethyl chromate'),
    ('Ethyl alcohol', 'Potassium permanganate', 'Ethyl permanganate'),
    ('Ethyl alcohol', 'Chloroform', 'Ethyl chloroformate'),
    ('Ethyl alcohol', 'Sodium thiosulfate', 'Ethyl thiosulfate'),
    ('Ethyl alcohol', 'Acetic acid', 'Ethyl acetate'),
    ('Ethyl alcohol', 'Ammonium chloride', 'Ethyl ammonium')

    ('Citric Acid', 'Sodium Hypochlorite (Bleach)', 'Chlorine Gas'),
    ('Citric Acid', 'Ammonia', 'Ammonium Citrate'),
    ('Citric Acid', 'Sulfuric Acid', 'Hydrogen Gas'),
    ('Citric Acid', 'Sodium Hydroxide', 'Sodium Citrate'),
    ('Citric Acid', 'Hydrogen Peroxide', 'Carbon Dioxide Gas'),
    ('Citric Acid', 'Potassium Permanganate', 'Manganese Dioxide'),
    ('Citric Acid', 'Chlorine', 'Chlorine Dioxide'),
    ('Citric Acid', 'Phosphoric Acid', 'Hydrogen Gas'),
    ('Citric Acid', 'Sodium Bicarbonate (Baking Soda)', 'Sodium Citrate'),
    ('Citric Acid', 'Acetic Acid (Vinegar)', 'Acetic Citric Acid'),
    ('Citric Acid', 'Ethanol', 'Ethyl Citrate'),
    ('Citric Acid', 'Chlorine Bleach (Sodium Hypochlorite)', 'Chlorine Gas'),
    ('Citric Acid', 'Hydrochloric Acid', 'Hydrogen Gas'),
    ('Citric Acid', 'Ammonium Hydroxide', 'Ammonium Citrate'),
    ('Citric Acid', 'Sodium Carbonate (Washing Soda)', 'Sodium Citrate'),
    ('Citric Acid', 'Calcium Hydroxide (Lime)', 'Calcium Citrate'),
    ('Citric Acid', 'Sodium Chloride (Salt)', 'Sodium Citrate'),
    ('Citric Acid', 'Potassium Hydroxide', 'Potassium Citrate'),
    ('Citric Acid', 'Chlorine Gas', 'Chlorine Dioxide'),
    ('Citric Acid', 'Chloramine', 'Chloramine Citrate'),
    ('Citric Acid', 'Chloroform', 'Chloroform Gas'),
    ('Citric Acid', 'Sodium Nitrite', 'Nitrous Acid'),
    ('Citric Acid', 'Sodium Sulfite', 'Sulfur Dioxide'),
    ('Citric Acid', 'Sodium Bisulfite', 'Sulfur Dioxide'),
    ('Citric Acid', 'Sodium Thiosulfate', 'Hydrogen Sulfide Gas'),
    ('Citric Acid', 'Potassium Nitrate', 'Nitrogen Dioxide Gas'),
    ('Citric Acid', 'Potassium Sulfate', 'Potassium Bisulfate'),
    ('Citric Acid', 'Calcium Chloride', 'Calcium Citrate'),
    ('Citric Acid', 'Sodium Metabisulfite', 'Sulfur Dioxide'),
    ('Citric Acid', 'Sodium Hexametaphosphate', 'Sodium Citrate'),
    ('Citric Acid', 'Aluminum Sulfate', 'Aluminum Citrate'),
    ('Citric Acid', 'Sodium Dichloroisocyanurate', 'Chlorine Gas'),
    ('Citric Acid', 'Sodium Hydrosulfite', 'Sulfur Dioxide'),
    ('Citric Acid', 'Sodium Nitrate', 'Nitrous Acid'),
    ('Citric Acid', 'Sodium Borate (Borax)', 'Sodium Citrate'),
    ('Citric Acid', 'Potassium Chloride', 'Potassium Citrate'),
    ('Citric Acid', 'Calcium Carbonate', 'Calcium Citrate'),
    ('Citric Acid', 'Sodium Permanganate', 'Manganese Dioxide'),
    ('Citric Acid', 'Sodium Nitrate', 'Nitric Acid'),
    ('Citric Acid', 'Sodium Silicate', 'Silicic Acid'),
    ('Citric Acid', 'Sodium Tetraborate (Borax)', 'Sodium Citrate'),
    ('Citric Acid', 'Sodium Fluoride', 'Hydrogen Fluoride Gas'),
    ('Citric Acid', 'Potassium Nitrite', 'Potassium Nitrate'),
    ('Citric Acid', 'Calcium Nitrate', 'Calcium Nitrate'),
    ('Citric Acid', 'Sodium Molybdate', 'Molybdic Acid'),
    ('Citric Acid', 'Sodium Hypophosphite', 'Phosphorous Acid'),
    ('Citric Acid', 'Sodium Polyphosphate', 'Sodium Citrate'),
    ('Citric Acid', 'Sodium Fluoride', 'Hydrofluoric Acid'),
    ('Citric Acid', 'Sodium Hexametaphosphate', 'Sodium Citrate')

    ('Sodium Hypochlorite', 'Ammonia', 'Chloramine Gas'),
    ('Sodium Hypochlorite', 'Acetic Acid', 'Chlorine Gas'),
    ('Sodium Hypochlorite', 'Isopropyl Alcohol', 'Chloroform'),
    ('Hydrogen Peroxide', 'Acetic Acid', 'Peracetic Acid'),
    ('Ammonia', 'Acetic Acid', 'Ammonium Acetate'),
    ('Acetic Acid', 'Sodium Bicarbonate', 'Carbon Dioxide Gas'),
    ('Sodium Hypochlorite', 'Sulfuric Acid', 'Chlorine Gas'),
    ('Ammonia', 'Isopropyl Alcohol', 'Acetamide'),
    ('Ammonia', 'Acetone', 'Acetonitrile'),
    ('Acetic Acid', 'Hydrogen Peroxide', 'Peracetic Acid'),
    ('Sodium Hypochlorite', 'Acetone', 'Trichloroethylene')
    ('a','b','test')
 ]

cur.executemany('''INSERT INTO products (product1, product2, reaction) VALUES (?, ?, ?)''', reactions)

conn.commit()
cur.close()
conn.close()

# Sodium Hypochlorite
# Ammonia
# Isopropyl Alcohol
# Hydrogen Peroxide
# Acetic Acid
# Citric Acid
# Sodium Bicarbonate
# Ethanol
# Sodium Hydroxide
# Sodium Lauryl Sulfate
# Sodium Laureth Sulfate
# Benzalkonium Chloride
# Triclosan
# Phosphoric Acid
# Butyl Cellosolve
# Propylene Glycol
# Formaldehyde
# Ethylene Glycol
# Lactic Acid
# Potassium Hydroxide
# Sodium Carbonate
# Sodium Chloride
# Potassium Sorbate
# Potassium Carbonate
# Sodium Metasilicate
# Sodium Percarbonate
# Sodium Silicate
# Tetrasodium EDTA
# Chlorine Dioxide
# Trisodium Phosphate
# Boric Acid
# Methyl Ethyl Ketone
# Peracetic Acid
# Acetone
# Glycerin
# Sulfuric Acid
# Dimethyl Sulfoxide
# Acetonitrile
# Calcium Carbonate
# Isopropylamine
# Isopropyl Chloride
# Isopropyl Borate
# Isopropyl Phosphate
# Isopropyl Sodium
# Isopropyl Potassium
# Isopropyl Citrate
# Isopropyl Lactate
# Isopropyl Acetate
# Isopropyl Chloroformate
# Isopropyl Sulfite
# Isopropyl Ammonium
# Isopropyl Chlorite
# Isopropyl Cyanide
# Isopropyl Magnesium
# Isopropyl Chromate
# Isopropyl Permanganate
# Isopropyl Thiosulfate
# Ethylamine
# Ethyl Hypochlorite
# Ethyl Sulfate
# Ethyl Chloride
# Ethyl Calcium
# Ethyl Borate
# Ethyl Phosphate
# Sodium Ethoxide
# Potassium Ethoxide
# Ethyl Citrate
# Ethyl Lactate
# Ethyl Peroxide
# Ethyl Carbonate
# Ethyl Copper
# Ethyl Sorbate
# Ethyl Glycerate
# Ethyl Sulfite
# Ethyl Ammonium
# Ethyl Chlorite
# Ethyl Cyanide
# Ethyl Magnesium
# Ethyl Chromate
# Ethyl Permanganate
# Ethyl Thiosulfate
# Ethyl Acetate
# Ethyl Mercury
# Ethyl Borate
# Ethyl Phosphate
# Ethyl Calcium
# Ethyl Chloride
# Ethyl Borate
# Ethyl Glycerate
# Ethyl Carbonate
# Ethyl Phosphate
# Ethyl Chloride
# Ethyl Mercury
# Ethyl Chloride
# Ethyl Borate
# Ethyl Glycerate
# Ethyl Carbonate
# Ethyl Phosphate
# Ethyl Chromate
# Ethyl Thiosulfate


