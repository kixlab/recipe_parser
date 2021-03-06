import pickle

ingredient_dictionary = {
'cake': {'pound':None},
'juice': {'cane':None, 'orange':2, 'lemon':2, 'lime':2, 'watermelon':2, 'cherry':2, 'apple':2},
'batter': {'cake':None, 'pancake':None},
'bok': {'isolated':None, 'choy': None, 'choi':None},
'baba': {'isolated':None, 'ghanous':None},
'bagna': {'isolated':None, 'cauda':None},
'foie': {'isolated':None, 'gras':None},
'ammonium': {'isolated':None, 'bicarbonate':2},
'bark': {'almond': None, 'peppermint':None },
'bread': {'potato':None, 'crumbs':1, 'pumpernickel':1, 'sourdough':1, 'rye':1, 'ciabatta':1, 'white':None, 'french':None, 'wheat':None, 'bread':None},
'butter': {'apple': None, 'almond': None, 'clarified': None, 'macadamia': None, 'peanut':1, 'chip':None, 'chips':None},
'bacon': {'canadian': None, 'grease':1},
'cheese': {'provolone':1, 'havarti':1, 'goat':None, 'brie':1, 'boursin': 1, 'cheddar': 1, 'asiago': 1, 'beer': None, 'brick': None, 'buxton': None, 'blue': None, 'basket': None, 'banon': None, 'chesire': None, 'cottage': 2, 'cream': 2, 'derby': None, 'dovedale': None, 'farmer': None, 'feta': 1, 'fontina': 1, 'grating': None, 'hard': None, 'hispanic': None, 'jack': None, 'lancashire': None, 'mimolette': None, 'babybel': None, 'parmesan': 1, 'filata': None, 'processed': None, 'ricotta': 1, 'romano': None, 'provel': None, 'rope': None, 'semi-hard': None, 'shropshire':None, 'soft':None, 'spanish':None, 'specialty':None, 'swiss':1, 'washed-rind':None, 'wensleydale':None},
'cherry': {'amarena': None, 'maraschino':None },
'cabbage': {'chinese':None},
'beef': {'corned':None, 'salted':None, 'jerky':1},
'creme' : {'brulee': None, 'cassis': None, 'cacao': None, 'fraiche': 2, 'menthe':2},
'cacao' : {'nib':1, 'powder':None},
'date': {'chinese':None},
'duck': {'bombay': None, 'muscovy':None},
'flour': {'corn': None, 'gram': None, 'white': None, 'milled': None, 'wheat': None, 'grain': None, 'rice':None, 'pastry':None},
'fry': {'isolated':None, 'french':None},
'bouquet': {'isolated':None, 'garni':None},
'ginger': {'crystallized': None, 'beer': 1, 'ale':1, 'snap':None},
'berry': {'goji':None},
'cracker': {'graham':None}, 
'groat': {'buckwheat':None},
'chile': {'habanero': None, 'ancho':None},
'hash': {'isolated':None, 'brown':None},
'cream': {'heavy': None, 'ice': 2, 'light': None, 'coconut': None, 'sour': 2, 'tartar': 2, 'wheat':2},
'ham': {'hock': 2},
'espresso': {'instant':None},
'artichoke': {'jerusalem': None, 'hearts':None},
'kale': {'black': None, 'baby':None},
'kern': {'green':None},
'essence': {'kewra': None, 'khus': None, 'rose':None},
'kiwi': {'baby':None},
'leaf' : {'bay': None, 'curry':None, 'thyme':None},
'crema': {'leche':None},
'dried': {'leeks': None, 'apricots':None},
'bean': {'fava': None, 'green': None, 'kidney': None, 'long': None, 'cannellini': None, 'black': None, 'fermented': None, 'jelly': None, 'azuki': None, 'adzuki': None, 'cranberry': None, 'navy': None, 'lima': None, 'moth': None, 'mung': None, 'northern': None, 'great': None, 'pea': None, 'pink': None, 'pinto': None, 'soy': None, 'thread': None, 'vanilla': None, 'white':None},
'beans': {'fava': None, 'green': None, 'kidney': None, 'long': None, 'cannellini': None, 'black': None, 'fermented': None, 'jelly': None, 'azuki': None, 'adzuki': None, 'cranberry': None, 'navy': None, 'lima': None, 'moth': None, 'mung': None, 'northern': None, 'great': None, 'pea': None, 'pink': None, 'pinto': None, 'soy': None, 'thread': None, 'vanilla': None, 'white':None},
'lemon': {'grass': None, 'juice': None, 'balm': None, 'preserved':None, 'zest':1},
'lime': {'kaffir': None, 'pickling':None},
'liqueur': {'alize': None, 'amarula': None, 'cream': None, 'coffee':None},
'liver': {'chicken': None, 'pork': None, 'goose':None},
'mahi': {'mahi':None},
'beurre': {'blanc': None, 'manie':None},
'marrows': {'baby': None, 'vegetable': None, 'bone':None},
'marrow': {'baby': None, 'vegetable': None, 'bone':None},
'monosodium': {'glutamate':None},
'grand': {'marnier':None},
'gran': {'marnier':None},
'masa': {'harina':None},
'matzo': {'meal':None},
'melon': {'honeydew': None, 'bitter': None, 'pie': None, 'musk':None},
'milk': {'whole':None, '1%':None, '2%':None, 'low-fat':None, 'evaporated': None, 'condensed': None, 'coconut': None, 'soy': None, 'almond': None, 'rice':None},
'muffin': {'english':None},
'mui': {'hing':None},
'mustard': {'english':None},
'mushroom': {'cremini': None, 'portabella':None},
'mushrooms' : {'cremini': None, 'portabella':None},
'grape': {'leaves': None, 'muscadine':None},
'nut': {'brazil': None, 'cashew': None, 'ginkgo': None, 'macadamia': None, 'pine':None},
'nuts': {'brazil': None, 'cashew': None, 'ginkgo': None, 'macadamia': None, 'pine':None},
'oil': {'canola': None, 'argan': None, 'coconut': None, 'citrus': None, 'olive': None, 'palm':None, 'vegetable':None, 'peanut':None, 'corn':None},
'onion': {'green': None, 'vidalia': None, 'red': None, 'yellow': None, 'white':None},
'orange': {'mandarin': None, 'tangerine': None, 'seville':None, 'zest':1},
'oven': {'dutch':None},
'bel': {'paese':None},
'palm': {'hearts': None, 'sugar':None},
'egg' : {'white':1, 'yolk':1},
'pan': {'bundt':None},
'panna': {'cotta':None},
'cocoa' : {'powder':None, 'nibs':1},
'paste': {'anchovy': None, 'almond':None},
'pea': {'black-eyed': None, 'snap': None, 'snow': None, 'split':None},
'peel': {'lemon': None, 'orange': None, 'lime':None},
'pepper': {'ancho': None, 'cayenne': None, 'chile': None, 'chipotle': None, 'aleppo': None, 'peppadew': None, 'birdseye': None, 'sweet': None, 'chili':None, 'lemon':None},
'dough': {'phyllo':None, 'cookie':None},
'pico': {'gallo': None},
'pig': {'cheek': None, 'feet': None, 'knuckle': None, 'tongue':None},
'molasses': {'pomegranate': None, 'black': None},
'potato': {'chips': None, 'flakes': None, 'sweet':None},
'powder': {'onion':None, 'baking': None, 'cocoa': None, 'curry': None, 'garlic': None, 'amchoor': None, 'dhania-jeera': None, 'chili': None, 'file': None, 'meringue': None, 'red': None, 'mustard': None, 'five-spice':None},
'pudding': {'indian': None, 'mix': None, 'rice': None, 'tapioca': None, 'vanilla':None, 'chocolate':None},
'pastry': {'puff': None},
'broccoli': {'raab': None},
'red': {'cabbage': None, 'bean': None, 'pepper': None, 'leicester': None},
'rice': {'arborio': None, 'basmati': None, 'paper': None, 'brown': None, 'black': None, 'red': None, 'vermicelli': None, 'wild': None, 'wine': None},
'roll': {'jelly': None, 'cottage': None},
'lettuce': {'romaine': None, 'bibb':None, 'iceberg':None},
'recado': {'isolated':None, 'rojo': None},
'sauce': {'sriracha':1, 'horseradish':1, 'spaghetti':None, 'red':None, 'white':None, 'chili': None, 'fish': None, 'hoisin': 1, 'oyster': None, 'apple': None, 'alfredo': 1, 'marinara':1, 'bean': None, 'hot': None, 'soy': None, 'barbecue': 1, 'pie': None, 'tabasco': 1, 'tartar': 1, 'worcestershire': 1, 'cranberry':None},
'sausage': {'chaurice': None, 'andouille': 1, 'creole': None, 'breakfast':None},
'sea': {'cucumber': None, 'bream':None},
'seasoning': {'poultry': None, 'smoke': None},
'seed': {'fennel': None, 'mustard': None, 'caraway': None, 'celery': None, 'poppy': None, 'annatto': None, 'nigella': None, 'flax': None, 'pumpkin': None, 'sunflower': None, 'sesame': None, 'sunflower': None},
'chocolate': {'semi-sweet': None, 'semisweet': None, 'bittersweet':None, 'bitter-sweet':None, 'dark': None, 'milk': None, 'white': None, 'chips': 1, 'chip':None, 'unsweetened': None},
'jamon': {'serrano': None},
'bamboo': {'shoot': None, 'preserved':None},
'extract': {'vanilla':1, 'peppermint':1, 'almond':1},
'smoked': {'salmon': 1, 'turkey':1},
'snapper': {'red': None},
'soda': {'water':None, 'baking': None, 'crackers': 1},
'sodium': {'isolated':None, 'citrate': None},
'crab': {'soft-shell': None},
'spice': {'apple': None, 'pie': None, 'pumpkin': None, 'mixed': None, 'kabsa': None},
'sprouts': {'bean': None, 'brussel': None, 'alfalfa': None},
'squash': {'acorn': None, 'butternut': None},
'irish': {'mist': None, 'coffee': None, 'cream': 1},
'starch': {'potato': None, 'gelatinized': None},
'egg': {'substitute': None, 'hundred-year': None, 'preserved':None},
'sugar': {'powdered': None, 'brown': None, 'invert': None, 'raw': None, 'date': None, 'icing': None, 'muscovado': None, 'barley': None, 'turbinado': None, 'vanilla':None, 'confectioners':None, 'bakers':None},
'sweetener': {'artificial': None},
'syrup': {'corn': None, 'maple': None, 'golden': None, 'ginger': None, 'orgean': None, 'simple':None},
'tomato': {'cherry':None, 'green':None, 'plum': None, 'juice': None, 'sauce': None, 'paste': None, 'rotel': None, 'puree':None},
'kielbasa': {'turkey': None, 'pork': None, 'beef': None},
'vinegar': {'balsamic': None, 'rice': None, 'cider': None, 'malt': None, 'wine':None},
'seaweed': {'wakame':None},
'water': {'isolated':None, 'orange': 2, 'flower': 2, 'chestnut': 2, 'rose': 2, 'kewra': 2, 'tonic': 2, 'acidulated':2},
'radish': {'watermelon':None},
'whip': {'miracle': None, 'cool':None },
'cooking': {'spray':1},
'wine': {'ice': None, 'cooking': None, 'white': None, 'red': None, 'zinfandel':None},
'skin': {'wonton':None},
'wrap': {'plastic': None, 'wonton': None, 'moo': None, 'mooshu': None, 'mu': None, 'lumpia':None},
'wrapper': {'plastic': 1, 'wonton': None, 'moo': None, 'mooshu': None, 'mu': None, 'lumpia':None},
'xantham': {'isolated':None, 'gum':None},
'shortening': {'vegetable':None},
'wheat': {'isolated':None, 'berries': None, 'bulgur': None, 'germ':None},
}

pickle.dump(ingredient_dictionary, open( "save_compound_ingredients.p", "wb" ) )
