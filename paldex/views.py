# views.py
from django.conf import settings
from django.shortcuts import render

# from .models import PalModel

def home_view(request):
    return render(request, 'home.html')

# def pals_view(request): -----DB Verison, wasn't working so i want to try something new
#     pal_data = PalModel.objects.all()
#     return render(request, 'pals.html', {'pal_data': pal_data})
def get_pals_data():
    pals_data = [{'Name': 'Lamball', 'Image': './images/1.png', 'Type': 'Neutral', 'Skill': 'Fluffy Shield', 'Work': 'Farming L1, Handiwork L1, Transporting L1', 'Drops': 'Lamball Mutton, Wool', 'Price': '1000'}, {'Name': 'Cattiva', 'Image': './images/2.png', 'Type': 'Neutral', 'Skill': 'Cat Helper', 'Work': 'Gathering L1, Handiwork L1, Mining L1, Transporting L1', 'Drops': 'Red Berries', 'Price': '1000'}, {'Name': 'Chikipi', 'Image': './images/3_y8vAEc3.png', 'Type': 'Neutral', 'Skill': 'Egg Layer', 'Work': 'Farming L1, Gathering L1', 'Drops': 'Chikipi Poultry, Egg', 'Price': '1000'}, {'Name': 'Lifmunk', 'Image': './images/4.png', 'Type': 'Grass', 'Skill': 'Lifmunk Recoil', 'Work': 'Gathering L1, Handiwork L1, Lumbering L1, Medicine L1, Planting L1', 'Drops': 'Berry Seeds, Low Grade Medical Supplies', 'Price': '1010'}, {'Name': 'Foxparks', 'Image': './images/5.png', 'Type': 'Fire', 'Skill': 'Huggy Fire', 'Work': 'Kindling L1', 'Drops': 'Flame Organ, Leather', 'Price': '1040'}, {'Name': 'Fuack', 'Image': './images/6.png', 'Type': 'Water', 'Skill': 'Surfing Slam', 'Work': 'Handiwork L1, Transporting L1, Watering L1', 'Drops': 'Leather, Pal Fluids', 'Price': '1120'}, {'Name': 'Sparkit', 'Image': './images/7.png', 'Type': 'Electric', 'Skill': 'Static Electricity', 'Work': 'Electricity L1, Handiwork L1, Transporting L1', 'Drops': 'Electric Organ', 'Price': '1030'}, {'Name': 'Tanzee', 'Image': './images/8.png', 'Type': 'Grass', 'Skill': 'Cheery Rifle', 'Work': 'Gathering L1, Handiwork L1, Lumbering L1, Planting L1, Transporting L1', 'Drops': 'Mushroom', 'Price': '1280'}, {'Name': 'Rooby', 'Image': './images/9.png', 'Type': 'Fire', 'Skill': 'Tiny Spark', 'Work': 'Kindling L1', 'Drops': 'Flame Organ, Leather', 'Price': '2950'}, {'Name': 'Pengullet', 'Image': './images/10.png', 'Type': 'Ice, Water', 'Skill': 'Pengullet Cannon', 'Work': 'Cooling L1, Handiwork L1, Transporting L1, Watering L1', 'Drops': 'Ice Organ, Pal Fluids', 'Price': '1080'}, {'Name': 'Penking', 'Image': './images/11_E7e8OsI.webp', 'Type': 'Ice, Water', 'Skill': 'Brave Sailor', 'Work': 'Cooling L2, Handiwork L2, Mining L2, Transporting L2, Watering L2', 'Drops': 'Ice Organ, Penking Plume', 'Price': '5410'}, {'Name': 'Jolthog', 'Image': './images/12.webp', 'Type': 'Electric', 'Skill': 'Jolt Bomb', 'Work': 'Electricity L1', 'Drops': 'Electric Organ', 'Price': '1060'}, {'Name': 'Gumoss', 'Image': './images/13.webp', 'Type': 'Grass, Ground', 'Skill': 'Logging Assistance', 'Work': 'Planting L1', 'Drops': 'Berry Seeds, Gumoss Leaf', 'Price': '1310'}, {'Name': 'Vixy', 'Image': './images/14.webp', 'Type': 'Neutral', 'Skill': 'Dig Here', 'Work': 'Farming L1, Gathering L1', 'Drops': 'Bone, Leather', 'Price': '1000'}, {'Name': 'Hoocrates', 'Image': './images/15.webp', 'Type': 'Dark', 'Skill': 'Dark Knowledge', 'Work': 'Gathering L1', 'Drops': 'Fiber, High Grade Technical Manual', 'Price': '1050'}, {'Name': 'Teafant', 'Image': './images/16.webp', 'Type': 'Water', 'Skill': 'Soothing Shower', 'Work': 'Watering L1', 'Drops': 'Pal Fluids', 'Price': '1000'}, {'Name': 'Depresso', 'Image': './images/17.webp', 'Type': 'Dark', 'Skill': 'Caffeine Inoculation', 'Work': 'Handiwork L1, Mining L1, Transporting L1', 'Drops': 'Venom Gland', 'Price': '1050'}, {'Name': 'Cremis', 'Image': './images/18.webp', 'Type': 'Neutral', 'Skill': 'Fluffy Wool', 'Work': 'Farming L1, Gathering L1', 'Drops': 'Wool', 'Price': '1420'}, {'Name': 'Daedream', 'Image': './images/19.webp', 'Type': 'Dark', 'Skill': 'Dream Chaser', 'Work': 'Gathering L1, Handiwork L1, Transporting L1', 'Drops': 'Small Pal Soul, Venom Gland', 'Price': '1330'}, {'Name': 'Rushoar', 'Image': './images/20.webp', 'Type': 'Ground', 'Skill': 'Hard Head', 'Work': 'Mining L1', 'Drops': 'Bone, Leather, Rushoar Pork', 'Price': '1680'}, {'Name': 'Nox', 'Image': './images/21.webp', 'Type': 'Dark', 'Skill': 'Kuudere', 'Work': 'Gathering L1', 'Drops': 'Leather, Small Pal Soul', 'Price': '1480'}, {'Name': 'Fuddler', 'Image': './images/22.webp', 'Type': 'Ground', 'Skill': 'Ore Detector', 'Work': 'Handiwork L1, Mining L1, Transporting L1', 'Drops': 'Leather', 'Price': '1360'}, {'Name': 'Killamari', 'Image': './images/23.webp', 'Type': 'Dark', 'Skill': 'Fried Squid', 'Work': 'Gathering L1, Transporting L2', 'Drops': 'Venom Gland', 'Price': '1200'}, {'Name': 'Mau', 'Image': './images/24.webp', 'Type': 'Dark', 'Skill': 'Gold Digger', 'Work': 'Farming L1', 'Drops': 'Gold Coin', 'Price': '1000'}, {'Name': 'Celaray', 'Image': './images/25.webp', 'Type': 'Water', 'Skill': 'Zephyr Glider', 'Work': 'Transporting L1, Watering L1', 'Drops': 'Pal Fluids', 'Price': '2860'}, {'Name': 'Direhowl', 'Image': './images/26.webp', 'Type': 'Neutral', 'Skill': 'Direhowl Rider', 'Work': 'Gathering L1', 'Drops': 'Gold Coin, Leather, Ruby', 'Price': '1920'}, {'Name': 'Tocotoco', 'Image': './images/27.webp', 'Type': 'Neutral', 'Skill': 'Eggbomb Launcher', 'Work': 'Gathering L1', 'Drops': 'Gunpowder, Tocotoco Feather', 'Price': '1090'}, {'Name': 'Flopie', 'Image': './images/28.webp', 'Type': 'Grass', 'Skill': 'Helper Bunny', 'Work': 'Gathering L1, Handiwork L1, Medicine L1, Planting L1, Transporting L1', 'Drops': 'Low Grade Medical Supplies, Wheat Seeds', 'Price': '1220'}, {'Name': 'Mozzarina', 'Image': './images/29.webp', 'Type': 'Neutral', 'Skill': 'Milk Maker', 'Work': 'Farming L1', 'Drops': 'Milk, Mozzarina Meat', 'Price': '2620'}, {'Name': 'Bristla', 'Image': './images/30.webp', 'Type': 'Grass', 'Skill': 'Princess Gaze', 'Work': 'Handiwork L1, Gathering L1, Medicine L2, Planting L1, Transporting L1', 'Drops': 'Lettuce Seeds, Wheat Seeds', 'Price': '1140'}, {'Name': 'Gobfin', 'Image': './images/31.webp', 'Type': 'Water', 'Skill': 'Angry Shark', 'Work': 'Handiwork L1, Transporting L1, Watering L2', 'Drops': 'Pal Fluids', 'Price': '1840'}, {'Name': 'Hangyu', 'Image': './images/32.webp', 'Type': 'Ground', 'Skill': 'Flying Trapeze', 'Work': 'Gathering L1, Handiwork L1, Transporting L2', 'Drops': 'Fiber', 'Price': '1020'}, {'Name': 'Mossanda', 'Image': './images/33.webp', 'Type': 'Grass', 'Skill': 'Grenadier Panda', 'Work': 'Handiwork L2, Lumbering L2, Planting L2, Transporting L3', 'Drops': 'Leather, Mushroom, Tomato Seeds', 'Price': '6200'}, {'Name': 'Woolipop', 'Image': './images/34.webp', 'Type': 'Neutral', 'Skill': 'Candy Pop', 'Work': 'Farming L1', 'Drops': 'Cotton Candy, High Quality Pal Oil', 'Price': '1450'}, {'Name': 'Caprity', 'Image': './images/35.webp', 'Type': 'Grass', 'Skill': 'Berry Picker', 'Work': 'Farming L1, Planting L2', 'Drops': 'Caprity Meat, Horn, Red Berries', 'Price': '2510'}, {'Name': 'Melpaca', 'Image': './images/36.webp', 'Type': 'Neutral', 'Skill': 'Pacapaca Wool', 'Work': 'Farming L1', 'Drops': 'Leather, Wool', 'Price': '2740'}, {'Name': 'Eikthyrdeer', 'Image': './images/37.webp', 'Type': 'Neutral', 'Skill': 'Guardian of the Forest', 'Work': 'Lumbering L2', 'Drops': 'Eikthyrdeer Venison, Horn, Leather', 'Price': '2620'}, {'Name': 'Nitewing', 'Image': './images/38.webp', 'Type': 'Neutral', 'Skill': 'Travel Companion', 'Work': 'Gathering L2', 'Drops': 'Leather', 'Price': '6300'}, {'Name': 'Ribbuny', 'Image': './images/39.webp', 'Type': 'Neutral', 'Skill': 'Skilled Fingers', 'Work': 'Gathering L1, Handiwork L1, Transporting L1', 'Drops': 'Beautiful Flower, Leather', 'Price': '1160'}, {'Name': 'Incineram', 'Image': './images/40.webp', 'Type': 'Dark, Fire', 'Skill': 'Flameclaw Hunter', 'Work': 'Handiwork L2, Kindling L1, Mining L1, Transporting L2', 'Drops': 'Horn, Leather', 'Price': '4780'}, {'Name': 'Cinnamoth', 'Image': './images/41.webp', 'Type': 'Grass', 'Skill': 'Mysterious Scales', 'Work': 'Medicine L1, Planting L2', 'Drops': 'Honey, Lettuce Seeds, Wheat Seeds', 'Price': '5700'}, {'Name': 'Arsox', 'Image': './images/42.webp', 'Type': 'Fire', 'Skill': 'Warm Body', 'Work': 'Kindling L2, Lumbering L1', 'Drops': 'Horn, Flame Organ', 'Price': '3520'}, {'Name': 'Dumud', 'Image': './images/43.webp', 'Type': 'Ground', 'Skill': 'Soil Improver', 'Work': 'Mining L2, Transporting L1, Watering L1', 'Drops': 'Raw Dumud, High Quality Pal Oil', 'Price': '4690'}, {'Name': 'Cawgnito', 'Image': './images/44.webp', 'Type': 'Dark', 'Skill': 'Telepeck', 'Work': 'Lumbering L1', 'Drops': 'Bone, Venom Gland, Small Pal Soul', 'Price': '1840'}, {'Name': 'Leezpunk', 'Image': './images/45.webp', 'Type': 'Dark', 'Skill': 'Sixth Sense', 'Work': 'Gathering L1, Handiwork L1, Transporting L1', 'Drops': 'Copper Key, Silver Key', 'Price': '1720'}, {'Name': 'Loupmoon', 'Image': './images/46.webp', 'Type': 'Dark', 'Skill': 'Claws Glistening in the Dark', 'Work': 'Handiwork L2', 'Drops': 'Bone', 'Price': '2400'}, {'Name': 'Galeclaw', 'Image': './images/47.webp', 'Type': 'Neutral', 'Skill': 'Galeclaw Rider', 'Work': 'Gathering L2', 'Drops': 'Galeclaw Poultry, Leather', 'Price': '2010'}, {'Name': 'Robinquill', 'Image': './images/48.webp', 'Type': 'Grass', 'Skill': 'Hawk Eye', 'Work': 'Gathering L2, Handiwork L2, Lumbering L1, Medicine L1, Planting L1, Transporting L2', 'Drops': 'Wheat Seeds, Arrow', 'Price': '2050'}, {'Name': 'Gorirat', 'Image': './images/49.webp', 'Type': 'Neutral', 'Skill': 'Full-power Gorilla Mode', 'Work': 'Handiwork L1, Lumbering L2, Transporting L3', 'Drops': 'Leather, Bone', 'Price': '2010'}, {'Name': 'Beegarde', 'Image': './images/50.webp', 'Type': 'Grass', 'Skill': 'Worker Bee', 'Work': 'Farming L1, Gathering L1, Handiwork L1, Lumbering L1, Medicine L1, Planting L1, Transporting L2', 'Drops': 'Honey', 'Price': '1880'}, {'Name': 'Elizabee', 'Image': './images/51.webp', 'Type': 'Grass', 'Skill': 'Queen Bee Command', 'Work': 'Gathering L2, Handiwork L2, Lumbering L1, Medicine L2, Planting L2', 'Drops': 'Honey, Elizabee’s Staff', 'Price': '6830'}, {'Name': 'Grintale', 'Image': './images/52.webp', 'Type': 'Neutral', 'Skill': 'Plump Body', 'Work': 'Gathering L2', 'Drops': 'High Quality Pal Oil', 'Price': '5510'}, {'Name': 'Swee', 'Image': './images/53.webp', 'Type': 'Ice', 'Skill': 'Fluffy', 'Work': 'Cooling L1, Gathering L1', 'Drops': 'Wool', 'Price': '1180'}, {'Name': 'Sweepa', 'Image': './images/54.webp', 'Type': 'Ice', 'Skill': 'King of Fluff', 'Work': 'Cooling L2, Gathering L2', 'Drops': 'Wool', 'Price': '6400'}, {'Name': 'Chillet', 'Image': './images/55.webp', 'Type': 'Dragon, Ice', 'Skill': 'Wriggling Weasel', 'Work': 'Cooling L1, Gathering L1', 'Drops': 'Leather', 'Price': '3450'}, {'Name': 'Univolt', 'Image': './images/56.webp', 'Type': 'Electric', 'Skill': 'Swift Deity', 'Work': 'Electricity L1, Lumbering L1', 'Drops': 'Leather, Electric Organ, Horn', 'Price': '4280'}, {'Name': 'Foxcicle', 'Image': './images/57.webp', 'Type': 'Ice', 'Skill': 'Aurora Guide', 'Work': '-', 'Drops': 'Ice Organ, Leather', 'Price': '3730'}, {'Name': 'Pyrin', 'Image': './images/58.webp', 'Type': 'Fire', 'Skill': 'Red Hare', 'Work': 'Kindling L2, Lumbering L1', 'Drops': 'Flame Organ, Leather', 'Price': '6720'}, {'Name': 'Reindrix', 'Image': './images/59.webp', 'Type': 'Ice', 'Skill': 'Cool Body', 'Work': 'Cooling L2, Lumbering L2', 'Drops': 'Reindrix Venison, Leather, Horn, ice Organ', 'Price': '2800'}, {'Name': 'Rayhound', 'Image': './images/60.webp', 'Type': 'Electric', 'Skill': 'Jumping Force', 'Work': 'Generating Electricity L2', 'Drops': 'Electric Organ', 'Price': '3880'}, {'Name': 'Kitsun', 'Image': './images/61.webp', 'Type': 'Fire', 'Skill': 'Clear Mind', 'Work': '-', 'Drops': 'Flame Organ, Leather', 'Price': '3170'}, {'Name': 'Dazzi', 'Image': './images/62.webp', 'Type': 'Electric', 'Skill': 'Lady of Lightning', 'Work': 'Electricity L1, Handiwork L1, Transporting L1', 'Drops': 'Electric Organ', 'Price': '1390'}, {'Name': 'Lunaris', 'Image': './images/63.webp', 'Type': 'Neutral', 'Skill': 'Antigravity', 'Work': 'Gathering L1, Handiwork L3, Transporting L1', 'Drops': 'Paldium Fragment', 'Price': '1760'}, {'Name': 'Dinossom', 'Image': './images/64.webp', 'Type': 'Dragon, Grass', 'Skill': 'Fragrant Dragon', 'Work': 'Lumbering L2, Planting L2', 'Drops': 'Wheat Seeds', 'Price': '3240'}, {'Name': 'Surfent', 'Image': './images/65.webp', 'Type': 'Water', 'Skill': 'Swiss Swimmer', 'Work': 'Watering L2', 'Drops': 'Pal Fluids', 'Price': '5050'}, {'Name': 'Maraith', 'Image': './images/66.webp', 'Type': 'Dark', 'Skill': 'Messenger of Death', 'Work': 'Gathering L2, Mining L1', 'Drops': 'Bone, Small Pal Soul', 'Price': '1570'}, {'Name': 'Digtoise', 'Image': './images/67.webp', 'Type': 'Ground', 'Skill': 'Drill Crusher', 'Work': 'Mining L3', 'Drops': 'Ore, High Quality Pal Oil', 'Price': '2980'}, {'Name': 'Tombat', 'Image': './images/68.webp', 'Type': 'Dark', 'Skill': 'Ultrasonic Sensor', 'Work': 'Gathering L2, Mining L2, Transporting L2', 'Drops': 'Leather, Small pal Soul', 'Price': '3810'}, {'Name': 'Lovander', 'Image': './images/69.webp', 'Type': 'Neutral', 'Skill': 'Heart Drain', 'Work': 'Handiwork L2, Medicine L2, Mining L1, Transporting L2', 'Drops': 'Mushroom, Cake, Suspicious Juice, Strange Juice', 'Price': '2450'}, {'Name': 'Flambelle', 'Image': './images/70.webp', 'Type': 'Fire', 'Skill': 'Magma Tears', 'Work': 'Farming L1, Handiwork L1, Kindling L1, Transporting L1', 'Drops': 'Flame Organ, High Quality Pal Oil', 'Price': '2500'}, {'Name': 'Vanwyrm', 'Image': './images/71.webp', 'Type': 'Dark, Fire', 'Skill': 'Aerial Maurader', 'Work': 'Kindling L1, Transporting L3', 'Drops': 'Bone, Ruby, Gold Coin', 'Price': '4360'}, {'Name': 'Bushi', 'Image': './images/72.webp', 'Type': 'Fire', 'Skill': 'Brandish Blade', 'Work': 'Gathering L1, Handiwork L1, Kindling L2, Lumbering L3, Transporting L2', 'Drops': 'Bone, Ingot', 'Price': '4520'}, {'Name': 'Beakon', 'Image': './images/73.webp', 'Type': 'Electric', 'Skill': 'Thunderous', 'Work': 'Electricity L2, Gathering L1, Transporting L3', 'Drops': 'Electric Organ', 'Price': '7490'}, {'Name': 'Ragnahawk', 'Image': './images/74.webp', 'Type': 'Fire', 'Skill': 'Flame Wing', 'Work': 'Kindling L3, Transporting L3', 'Drops': 'Flame Organ', 'Price': '6720'}, {'Name': 'Katress', 'Image': './images/75.webp', 'Type': 'Dark', 'Skill': 'Grimoire Collector', 'Work': 'Handiwork L2, Medicine L2, Transporting L2', 'Drops': 'Leather, Katress Hair, High Grade Technical Manual', 'Price': '4120'}, {'Name': 'Wixen', 'Image': './images/76.webp', 'Type': 'Fire', 'Skill': 'Lord Fox', 'Work': 'Handiwork L3, Kindling L2, Transporting L2', 'Drops': 'Flame Organ, High Grade Technical Manual', 'Price': '1540'}, {'Name': 'Verdash', 'Image': './images/77.webp', 'Type': 'Grass', 'Skill': 'Grassland Speedster', 'Work': 'Gathering L3, Handiwork L3, Lumbering L2, Planting L2, Transporting L2', 'Drops': 'Leather, Bone', 'Price': '2200'}, {'Name': 'Vaelet', 'Image': './images/78.webp', 'Type': 'Grass', 'Skill': 'Purification of Gaia', 'Work': 'Gathering L2, Handiwork L2, Medicine L3, Planting L2, Transporting L1', 'Drops': 'Low Grade Medical Supplies, Tomato Seeds', 'Price': '1960'}, {'Name': 'Sibelyx', 'Image': './images/79.webp', 'Type': 'Ice', 'Skill': 'Silk Maker', 'Work': 'Cooling L2, Farming L1, Medicine L2', 'Drops': 'High Quality Cloth, Ice Organ', 'Price': '5900'}, {'Name': 'Elphidran', 'Image': './images/80.webp', 'Type': 'Dragon', 'Skill': 'Amicable Holy Dragon', 'Work': 'Lumbering L2', 'Drops': 'High Quality Pal Oil', 'Price': '5230'}, {'Name': 'Kelpsea', 'Image': './images/81.webp', 'Type': 'Water', 'Skill': 'Aqua Spout', 'Work': 'Watering L1', 'Drops': 'Raw Kelpsea, Pal Fluids', 'Price': '1260'}, {'Name': 'Azurobe', 'Image': './images/82.webp', 'Type': 'Dragon, Water', 'Skill': 'Waterwing Dance', 'Work': 'Watering L3', 'Drops': 'Cloth', 'Price': '5600'}, {'Name': 'Cryolinx', 'Image': './images/83.webp', 'Type': 'Ice', 'Skill': 'Dragon Hunter', 'Work': 'Cooling L3, Handiwork L1, Lumbering L2', 'Drops': 'Ice Organ', 'Price': '8440'}, {'Name': 'Blazehowl', 'Image': './images/84.webp', 'Type': 'Dark, Fire', 'Skill': 'HellFire Lion', 'Work': 'Kindling L3, Lumbering L2', 'Drops': 'Flame Organ', 'Price': '4040'}, {'Name': 'Relaxaurus', 'Image': './images/85.webp', 'Type': 'Dragon, Water', 'Skill': 'Hungry Missile', 'Work': 'Transporting L1, Watering L2', 'Drops': 'High Quality Pal Oil, Ruby', 'Price': '10240'}, {'Name': 'Broncherry', 'Image': './images/86.webp', 'Type': 'Grass', 'Skill': 'Overaffectionate', 'Work': 'Planting L3', 'Drops': 'Broncherry Meat, Tomato Seeds', 'Price': '2920'}, {'Name': 'Petallia', 'Image': './images/87.webp', 'Type': 'Grass', 'Skill': 'Blessing of the Flower Spirit', 'Work': 'Gathering l2, Handiwork L2, Medicine L2, Planting L3, Transporting L1', 'Drops': 'Beautiful Flower', 'Price': '3590'}, {'Name': 'Reptyro', 'Image': './images/88.webp', 'Type': 'Fire, Ground', 'Skill': 'Ore-Loving Beast', 'Work': 'Kindling L3, Mining L3', 'Drops': 'Flame Organ', 'Price': '6940'}, {'Name': 'Kingpaca', 'Image': './images/89.webp', 'Type': 'Neutral', 'Skill': 'King of Muscles', 'Work': 'Gathering L1', 'Drops': 'Wool', 'Price': '5800'}, {'Name': 'Mammorest', 'Image': './images/90.webp', 'Type': 'Grass', 'Skill': 'Gaia Crusher', 'Work': 'Lumbering L2, Mining L2, Planting L2', 'Drops': 'High Quality Pal Oil, Leather, Mammorest Meat', 'Price': '9450'}, {'Name': 'Wumpo', 'Image': './images/91.webp', 'Type': 'Ice', 'Skill': 'Guardian of the Snowy Mountain', 'Work': 'Cooling L2, Handiwork L2, Lumbering L3, Transporting L4', 'Drops': 'Ice Organ, Beautiful Flower', 'Price': '5900'}, {'Name': 'Warsect', 'Image': './images/92.webp', 'Type': 'Grass, Ground', 'Skill': 'Hard Armor', 'Work': 'Handiwork L1, Lumbering L3, Planting L1, Transporting L3', 'Drops': 'Honey', 'Price': '6830'}, {'Name': 'Fenglope', 'Image': './images/93.webp', 'Type': 'Neutral', 'Skill': 'Wind and Clouds', 'Work': 'Lumbering L2', 'Drops': 'Leather, Horn', 'Price': '2250'}, {'Name': 'Felbat', 'Image': './images/94.webp', 'Type': 'Dark', 'Skill': 'Life Steal', 'Work': 'Medicine L3', 'Drops': 'Cloth, Small Pal Soul', 'Price': '2100'}, {'Name': 'Quivern', 'Image': './images/95.webp', 'Type': 'Dragon', 'Skill': "Sky Dragon's Affection", 'Work': 'Gathering L2, Handiwork L1, Mining L2, Transporting L3', 'Drops': 'High Quality Pal Oil', 'Price': '6830'}, {'Name': 'Blazamut', 'Image': './images/96.webp', 'Type': 'Fire', 'Skill': 'Magma Kaiser', 'Work': 'Kindling L3, Mining L4', 'Drops': 'Coal, Flame Organ', 'Price': '10520'}, {'Name': 'Helzephyr', 'Image': './images/97.webp', 'Type': 'Dark', 'Skill': 'Wings of Death', 'Work': 'Transporting L3', 'Drops': 'Venom Gland, Medium Pal Soul', 'Price': '7840'}, {'Name': 'Astegon', 'Image': './images/98.webp', 'Type': 'Dark, Dragon', 'Skill': 'Black Ankylosaur', 'Work': 'Handiwork L1, Mining L4', 'Drops': 'Pal Metal Ingot, Pure Quartz', 'Price': '8200'}, {'Name': 'Menasting', 'Image': './images/99.webp', 'Type': 'Dark, Ground', 'Skill': 'Steel Scorpion', 'Work': 'Lumbering L2, Mining L3', 'Drops': 'Coal, Venom Gland', 'Price': '7050'}, {'Name': 'Anubis', 'Image': './images/100.webp', 'Type': 'Ground', 'Skill': 'Guardian of the Desert', 'Work': 'Handiwork L4, Mining L3, Transporting L2', 'Drops': 'Bone, Large Pal Soul, Innovative Technical Manual', 'Price': '4960'}, {'Name': 'Jormuntide', 'Image': './images/101.webp', 'Type': 'Dragon, Water', 'Skill': 'Stormbringer Sea Dragon', 'Work': 'Watering L4', 'Drops': 'Pal Fluids', 'Price': '9320'}, {'Name': 'Suzaku', 'Image': './images/102.webp', 'Type': 'Fire', 'Skill': 'Wings of Fire', 'Work': 'Kindling L3', 'Drops': 'Flame Organ', 'Price': '9840'}, {'Name': 'Grizzbolt', 'Image': './images/103.webp', 'Type': 'Electric', 'Skill': 'Yellow Tank', 'Work': 'Electricity L3, Handiwork L2, Lumbering L2, Transporting L3', 'Drops': 'Electric Organ, Leather', 'Price': '7720'}, {'Name': 'Lyleen', 'Image': './images/104.webp', 'Type': 'Grass', 'Skill': 'Harvest Goddess', 'Work': 'Gathering L2, Handiwork L3, Medicine L3, Planting L4', 'Drops': '-', 'Price': '7160'}, {'Name': 'Faleris', 'Image': './images/105.webp', 'Type': 'Fire', 'Skill': 'Scorching Predator', 'Work': 'Kindling L3, Transporting L3', 'Drops': 'Flame Organ', 'Price': '6720'}, {'Name': 'Orserk', 'Image': './images/106_Fnse9rl.webp', 'Type': 'Dragon, Electric', 'Skill': 'Ferocious Thunder Dragon', 'Work': 'Electricity L4, Handiwork L2, Transporting L3', 'Drops': 'Electric Organ', 'Price': '8320'}, {'Name': 'Shadowbeak', 'Image': './images/107.webp', 'Type': 'Dark', 'Skill': 'Modified DNA', 'Work': 'Gathering L1', 'Drops': 'Pal Metal Ingot, Carbon Fiber, Innovative Technical Manual', 'Price': '9060'}, {'Name': 'Paladius', 'Image': './images/108.webp', 'Type': 'Neutral', 'Skill': 'Holy Knight Of The Firmament', 'Work': 'Lumbering L2, Mining L2', 'Drops': 'Pal Metal Ingot', 'Price': '8810'}, {'Name': 'Necromus', 'Image': './images/109.webp', 'Type': 'Dark', 'Skill': 'Dark Knight of the Abyss', 'Work': 'Lumbering L2, Mining L2', 'Drops': 'Pal Metal Ingot, Large Pal Soul', 'Price': '8930'}, {'Name': 'Frostallion', 'Image': './images/110.webp', 'Type': 'Ice', 'Skill': 'Ice Steed', 'Work': 'Cooling L4', 'Drops': 'Ice Organ, Diamond', 'Price': '8440'}, {'Name': 'Jetragon', 'Image': './images/111.webp', 'Type': 'Dragon', 'Skill': 'Aerial Missile', 'Work': 'Gathering L3', 'Drops': 'Pure Quartz, Polymer, Carbon Fiber, Diamond', 'Price': '8680'}, {'Name': 'Boltmane', 'Image': '', 'Type': 'Electric', 'Skill': '-', 'Work': '-', 'Drops': 'Flame Organ', 'Price': '4200'}, {'Name': 'Dragostrophe', 'Image': '', 'Type': 'Dark, Dragon', 'Skill': '-', 'Work': '-', 'Drops': 'Bone', 'Price': '8440'}]
    return pals_data

def pals_view(request):
    # Retrieve data from the database (if needed)
    # pal_data = PalModel.objects.all()
    pals_data = get_pals_data()
    for pal in pals_data:
        pal['Image'] = settings.MEDIA_URL + pal['Image']

    # Pass the data to the template context
    context = {'pal_data': pals_data}
    return render(request, 'pals.html', context)
    
def contact_view(request):
    return render(request, 'contact.html')

# def search_view(request): --------DB Version
#     query = request.GET.get('q')
#     pal_data = None
    
#     if query:
#         # Search for pals whose type matches the query
#         pal_data = PalModel.objects.filter(type__icontains=query.lower())
        
#         # If no results found, check if any pal has the query as one of its types
#         if not pal_data:
#             pal_data = PalModel.objects.filter(type__icontains=query.lower())
    
#     return render(request, 'search_results.html', {'query': query, 'pal_data': pal_data})

def search_view(request):
    query = request.GET.get('q')
    search_results = []
    
    if query:
        pals_data = get_pals_data()
        for pal in pals_data:
            pal_type = pal.get('Type', '').lower()
            if query.lower() in pal_type:
                # Preprocess image path if Image key exists in pal
                if 'Image' in pal:
                    pal['Image'] = settings.MEDIA_URL + pal['Image']
                search_results.append(pal)
    
    return render(request, 'search_results.html', {'query': query, 'search_results': search_results})



