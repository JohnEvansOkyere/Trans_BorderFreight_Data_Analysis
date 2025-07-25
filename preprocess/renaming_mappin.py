import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Paths
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../worked_data'))
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../notebooks/worked_data'))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define all mapping dictionaries
# Define all mapping dictionaries
MAPPINGS = {
    'mode_map': {
        '1': 'Vessel',
        '3': 'Air',
        '4': 'Mail (U.S. Postal Service)',
        '5': 'Truck',
        '6': 'Rail',
        '7': 'Pipeline',
        '8': 'Other',
        '9': 'Foreign Trade Zones (FTZs)'
    },
    
    'us_state_map': {
        'AL': 'Alabama', 'AK': 'Alaska', 'AS': 'American Samoa', 'AZ': 'Arizona',
        'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut',
        'DE': 'Delaware', 'DC': 'District of Columbia', 'FL': 'Florida', 'GA': 'Georgia',
        'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana',
        'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana',
        'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan',
        'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana',
        'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
        'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota',
        'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',
        'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee',
        'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia',
        'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming',
        'DU': 'Unknown',
        # Handle common null representations
        'nan': 'Unknown',
        'None': 'Unknown',
        'NULL': 'Unknown',
        '': 'Unknown',
        ' ': 'Unknown'
    },
    
    'country_map': {
        '1220': 'Canada',
        '2010': 'Mexico'
    },
    
    'canada_prov_map': {
        'XA': 'Alberta', 'XC': 'British Columbia', 'XM': 'Manitoba', 'XB': 'New Brunswick',
        'XW': 'Newfoundland', 'XT': 'Northwest Territories', 'XN': 'Nova Scotia',
        'XO': 'Ontario', 'XP': 'Prince Edward Island', 'XQ': 'Quebec',
        'XS': 'Saskatchewan', 'XV': 'Nunavut', 'XY': 'Yukon Territory', 'OT': 'Province Unknown',

          # Handle common null representations
        'nan': 'Unknown',
        'None': 'Unknown',
        'NULL': 'Unknown',
        '': 'Unknown',
        ' ': 'Unknown'
    },
    
    'container_code_map': {
        'X': 'Containerized',
        '0': 'Non-Containerized',
        '1': 'Not Specified'
    },
    
    'df_map': {
        '1': 'Domestic',
        '2': 'Foreign',

          # Handle common null representations
        'nan': 'Unknown',
        'None': 'Unknown',
        'NULL': 'Unknown',
        '': 'Unknown',
        ' ': 'Unknown'
    },
    
    'mex_state_map': {
        'AG': 'Aguascalientes', 'BC': 'Baja California', 'BN': 'Baja California Norte',
        'BS': 'Baja California Sur', 'CH': 'Chihuahua', 'CL': 'Colima',
        'CM': 'Campeche', 'CO': 'Coahuila', 'CS': 'Chiapas', 'DF': 'Distrito Federal',
        'DG': 'Durango', 'GR': 'Guerrero', 'GT': 'Guanajuato', 'HG': 'Hidalgo',
        'JA': 'Jalisco', 'MI': 'Michoacán', 'MO': 'Morelos', 'MX': 'Estado de Mexico',
        'NA': 'Nayarit', 'NL': 'Nuevo Leon', 'OA': 'Oaxaca', 'PU': 'Puebla',
        'QR': 'Quintana Roo', 'QT': 'Queretaro', 'SI': 'Sinaloa', 'SL': 'San Luis Potosi',
        'SO': 'Sonora', 'TB': 'Tabasco', 'TL': 'Tlaxcala', 'TM': 'Tamaulipas',
        'VE': 'Veracruz', 'YU': 'Yucatan', 'ZA': 'Zacatecas', 'OT': 'State Unknown',

          # Handle common null representations
        'nan': 'Unknown',
        'None': 'Unknown',
        'NULL': 'Unknown',
        '': 'Unknown',
        ' ': 'Unknown'
    },
    
    'month_map': {
        '1': 'January', '2': 'February', '3': 'March', '4': 'April',
        '5': 'May', '6': 'June', '7': 'July', '8': 'August',
        '9': 'September', '10': 'October', '11': 'November', '12': 'December'
    },
    
    'trade_type_map': {
        '1': 'Export',
        '2': 'Import'
    },

    'commodity_map' : {
        '01': 'Live Animals', '02': 'Meat', '03': 'Fish & Aquatic Life', '04': 'Dairy & Animal Products', '05': 'Other Animal Products',
        '06': 'Live Plants & Flowers', '07': 'Vegetables & Roots', '08': 'Fruits & Nuts', '09': 'Coffee, Tea & Spices', '10': 'Cereals',
        '11': 'Milling Products', '12': 'Seeds & Medicinal Plants', '13': 'Gums & Resins', '14': 'Other Veg Products', '15': 'Fats & Oils',
        '16': 'Meat & Seafood Prep', '17': 'Sugars & Confectionery', '18': 'Cocoa Products', '19': 'Bakery Products', '20': 'Fruit & Veg Prep',
        '21': 'Misc Edibles', '22': 'Beverages & Spirits', '23': 'Animal Feed & Waste', '24': 'Tobacco', '25': 'Salt, Stone, Cement',
        '26': 'Ores & Ash', '27': 'Mineral Fuels & Oils', '28': 'Inorganic Chemicals', '29': 'Organic Chemicals', '30': 'Pharmaceuticals',
        '31': 'Fertilizers', '32': 'Dyes & Pigments', '33': 'Perfumes & Cosmetics', '34': 'Soaps & Cleaning', '35': 'Glues & Enzymes',
        '36': 'Explosives & Matches', '37': 'Photographic Goods', '38': 'Misc Chemicals', '39': 'Plastics', '40': 'Rubber Products',
        '41': 'Raw Hides & Leather', '42': 'Leather Articles', '43': 'Furs & Products', '44': 'Wood & Woodwork', '45': 'Cork Products',
        '46': 'Straw & Basketware', '47': 'Pulp & Waste Paper', '48': 'Paper & Articles', '49': 'Books & Printed Goods', '50': 'Silk',
        '51': 'Wool & Animal Hair', '52': 'Cotton', '53': 'Veg Textiles & Yarn', '54': 'Man-made Filaments', '55': 'Man-made Fibers',
        '56': 'Yarns, Ropes & Cords', '57': 'Carpets', '58': 'Lace & Embroidery', '59': 'Coated Textiles', '60': 'Knitted Fabrics',
        '61': 'Knit Apparel', '62': 'Non-knit Apparel', '63': 'Other Textile Articles', '64': 'Footwear', '65': 'Headgear',
        '66': 'Umbrellas & Canes', '67': 'Feathers & Hair Goods', '68': 'Stone, Cement Goods', '69': 'Ceramics', '70': 'Glassware',
        '71': 'Jewelry & Precious Metal', '72': 'Iron & Steel', '73': 'Iron/Steel Products', '74': 'Copper Products', '75': 'Nickel Products',
        '76': 'Aluminum Products', '77': 'Reserved', '78': 'Lead Products', '79': 'Zinc Products', '80': 'Tin Products',
        '81': 'Other Base Metals', '82': 'Tools & Cutlery', '83': 'Misc Base Metal Goods', '84': 'Machinery & Boilers', '85': 'Electrical Equipment',
        '86': 'Railway Equipment', '87': 'Vehicles & Parts', '88': 'Aircraft & Parts', '89': 'Ships & Boats', '90': 'Precision Instruments',
        '91': 'Clocks & Watches', '92': 'Musical Instruments', '93': 'Arms & Ammunition', '94': 'Furniture & Fixtures', '95': 'Toys & Sports Gear',
        '96': 'Misc Manufactured Goods', '97': 'Art & Antiques', '98': 'Special Provisions', '99': 'Temporary Imports',


          # Handle common null representations
        'nan': 'Unknown',
        'None': 'Unknown',
        'NULL': 'Unknown',
        '': 'Unknown',
        ' ': 'Unknown'
    },
    
    # Note: Port district mapping is incomplete - you'll need to add the full mapping
    'port_district_map': {
        "0101": "PORTLAND, ME", "0102": "BANGOR, ME", "0103": "EASTPORT, ME", "0104": "JACKMAN, ME", "0105": "VANCEBORO, ME",
        "0106": "HOULTON, ME", "0107": "FORT FAIRFIELD, ME", "0108": "VAN BUREN, ME", "0109": "MADAWASKA, ME", "0110": "FORT KENT, ME",
        "0111": "BATH, ME", "0112": "BAR HARBOR, ME", "0115": "CALAIS, ME", "0118": "LIMESTONE, ME", "0121": "ROCKLAND, ME",
        "0122": "JONESPORT, ME", "0127": "BRIDGEWATER, ME", "0131": "PORTSMOUTH, NH", "0132": "BELFAST, ME", "0152": "SEARSPORT, ME",
        "0181": "LEBANON AIRPORT", "0182": "MANCHESTER AIRPORT, NH", "0201": "ST. ALBANS, VT", "0203": "RICHFORD, VT", "0206": "BEECHER FALLS, VT",
        "0207": "BURLINGTON, VT", "0209": "DERBY LINE, VT", "0211": "NORTON, VT", "0212": "HIGHGATE SPRINGS/ALBURG", "0401": "BOSTON, MA",
        "0402": "SPRINGFIELD, MA", "0403": "WORCESTER, MA", "0404": "GLOUCESTER, MA", "0405": "NEW BEDFORD, MA", "0406": "PLYMOUTH, MA",
        "0407": "FALL RIVER, MA", "0408": "SALEM, MA", "0409": "PROVINCETOWN, MA", "0410": "BRIDGEPORT, CONNECTICUT", "0411": "HARTFORD, CONNECTICUT",
        "0412": "NEW HAVEN, CONNECTICUT", "0413": "NEW LONDON, CONNECTICUT", "0416": "LAWRENCE, MA", "0417": "LOGAN AIRPORT, MA", "0501": "NEWPORT, RI",
        "0502": "PROVIDENCE, RI", "0503": "MELLVILLE, RI", "0701": "OGDENSBURG, NY", "0704": "MASSENA, NY", "0706": "CAPE VINCENT, NY",
        "0708": "ALEXANDRIA BAY, NY", "0712": "CHAMPLAIN-ROUSES POINT, NY", "0714": "CLAYTON, NY", "0715": "TROUT RIVER, NY", "0901": "BUFFALO-NIAGARA FALLS, NY",
        "0903": "ROCHESTER, NY", "0904": "OSWEGO, NY", "0905": "SODUS POINT, NY", "0906": "SYRACUSE, NY", "0907": "UTICA, NY", "0971": "TNT SKYPAK",
        "0972": "SWIFT SURE COURIER SERVICE", "0981": "BINGHAMTON REGIONAL AIRPORT, NY", "1001": "NEW YORK, NY", "1002": "ALBANY, NY", "1003": "NEWARK, NJ",
        "1012": "JOHN F. KENNEDY AIRPORT, NY", "1101": "PHILADELPHIA, PA", "1102": "CHESTER, PA", "1103": "WILMINGTON, DE", "1104": "PITTSBURGH, PA",
        "1105": "PAULSBORO, NJ", "1106": "WILKES-BARRE/SCRANTON, PA", "1107": "CAMDEN, NJ", "1108": "PHILADELPHIA INTERNATIONAL AIRPORT, PA",
        "1109": "HARRISBURG, PA", "1113": "GLOUCESTER CITY, NJ", "1119": "ALLENTOWN, PA (LEHIGH VALLEY INTL AIRPORT)", "1181": "ALLENTOWN-BETHLEHEM, PA (EASTON AIRPORT)",
        "1182": "ATLANTIC CITY REGIONAL AIRPORT, NJ", "1183": "TRENTON/MERCER COUNTY AIRPORT, NJ", "1195": "UPS, PHILADELPHIA, PA",
        "1301": "ANNAPOLIS, MD", "1302": "CAMBRIDGE, MD", "1303": "BALTIMORE, MD", "1304": "CRISFIELD, MD", "1305": "BWI AIRPORT",
        "1401": "NORFOLK, VA", "1402": "NEWPORT NEWS, VA", "1404": "RICHMOND-PETERSBURG, VA", "1408": "HOPEWELL, VA", "1409": "CHARLESTON, WV",
        "1410": "FRONT ROYAL, VA", "1412": "NEW RIVER VALLEY, VA", "1501": "WILMINGTON, NC", "1502": "WINSTON-SALEM, NC", "1503": "DURHAM, NC",
        "1506": "REIDSVILLE, NC", "1511": "BEAUFORT-MOREHEAD CTY, NC", "1512": "CHARLOTTE, NC", "1601": "CHARLESTON, SC", "1602": "GEORGETOWN, SC",
        "1603": "GREENVILLE-SPARTANBURG, SC", "1604": "COLUMBIA, SC", "1681": "MYRTLE BEACH INTERNATIONAL AIRPORT, SC", "1701": "BRUNSWICK, GA",
        "1703": "SAVANNAH, GA", "1704": "ATLANTA, GA", "1801": "TAMPA, FL", "1803": "JACKSONVILLE, FL", "1805": "FERNANDINA BEACH, FL",
        "1807": "BOCA GRANDE, FL", "1808": "ORLANDO, FL", "1809": "ORLANDO-SANFORD AIRPORT, FL", "1814": "ST. PETERSBURG, FL", "1816": "PORT CANAVERAL, FL",
        "1818": "PANAMA CITY, FL", "1819": "PENSACOLA, FL", "1821": "PORT MANATEE, FL", "1822": "FORT MYERS AIRPORT, FL", "1883": "SARASOTA BRADENTON AIRPORT, FL",
        "1884": "DAYTONA BEACH INT'L AIRPORT, FL", "1885": "MELBOURNE REGIONAL AIRPORT, FL", "1886": "OCALA REGIONAL AIRPORT, FL", "1887": "LEESBURG REGIONAL AIRPORT, FL",
        "1901": "MOBILE, AL", "1902": "GULFPORT, MS", "1903": "PASCAGOULA, MS", "1904": "BIRMINGHAM, AL", "1910": "HUNTSVILLE, AL",
        "2001": "MORGAN CITY, LA", "2002": "NEW ORLEANS, LA", "2003": "LITTLE ROCK, AR", "2004": "BATON ROUGE, LA", "2005": "PORT SULPHUR, LA",
        "2006": "MEMPHIS, TN", "2007": "NASHVILLE, TN", "2008": "CHATTANOOGA, TN", "2009": "DESTREHAN, LA", "2010": "GRAMERCY, LA",
        "2011": "GREENVILLE, MS", "2012": "AVONDALE, LA", "2013": "ST. ROSE, LA", "2014": "GOOD HOPE, LA", "2015": "VICKSBURG, MS",
        "2016": "KNOXVILLE, TN", "2017": "LAKE CHARLES, LA", "2018": "SHREVEPORT/BOSSIER CITY", "2082": "TRI CITY USER FEE AIRPORT, TN",
        "2083": "ARKANSAS AEROPLEX, AR", "2095": "FEDERAL EXPRESS, MEMPHIS, TN", "2101": "PORT ARTHUR, TX", "2102": "SABINE, TX", "2103": "ORANGE, TX",
        "2104": "BEAUMONT, TX", "2301": "BROWNSVILLE, TX", "2302": "DEL RIO, TX", "2303": "EAGLE PASS, TX", "2304": "LAREDO, TX",
        "2305": "HIDALGO, PHARR, TX", "2307": "RIO GRANDE CITY, TX", "2309": "PROGRESO, TX", "2310": "ROMA, TX", "2381": "EDINBURG USER FEE AIRPORT",
        "2402": "EL PASO, TX", "2403": "PRESIDIO, TX", "2404": "FABENS, TX", "2406": "COLUMBUS, NM", "2407": "ALBUQUERQUE, NM",
        "2408": "SANTA TERESA, NM", "2481": "SANTA TERESA AIRPORT", "2501": "SAN DIEGO, CA", "2502": "ANDRADE, CA", "2503": "CALEXICO, CA",
        "2504": "SAN YSIDRO, CA", "2505": "TECATE, CA", "2506": "OTAY MESA, CA", "2507": "CALEXICO-EAST, CA", "2601": "DOUGLAS, AZ",
        "2602": "LUKEVILLE, AZ", "2603": "NACO, AZ", "2604": "NOGALES, AZ", "2605": "PHOENIX, AZ", "2606": "SASABE, AZ", "2608": "SAN LUIS, AZ",
        "2609": "TUCSON, AZ", "2704": "LOS ANGELES, CA", "2707": "PORT SAN LUIS HARBOR, CA", "2709": "LONG BEACH, CA", "2711": "EL SEGUNDO, CA",
        "2712": "VENTURA, CA", "2713": "PORT HUENEME, CA", "2715": "CAPITAN, CA", "2719": "MORRO BAY, CA", "2720": "LOS ANGELES INTERNATIONAL AIRPORT",
        "2721": "ONTARIO INTERNATIONAL AIRPORT", "2722": "LAS VEGAS, NV", "2770": "DHL, LOS ANGELES, CA", "2772": "GATEWAY FREIGHT SERVICES INC",
        "2773": "AIR CARGO HANDLING SERVICES", "2774": "VIRGIN ATLANTIC CARGO", "2775": "TNT EXPRESS, LAX, CA", "2776": "IBC PACIFIC",
        "2781": "PALM SPRINGS USER FEE, LAX, CA", "2782": "SAN BERNARDINO INTERNATIONAL AIRPORT", "2791": "LOS ANGELES, CA", "2795": "UPS - ONTARIO, CA",
        "2801": "SAN FRANCISCO INTERNATIONAL AIRPORT", "2802": "EUREKA, CA", "2803": "FRESNO, CA", "2805": "MONTEREY, CA", "2809": "SAN FRANCISCO, CA",
        "2810": "STOCKTON, CA", "2811": "OAKLAND, CA", "2812": "RICHMOND, CA", "2813": "ALAMEDA, CA", "2815": "CROCKETT, CA",
        "2816": "SACRAMENTO, CA", "2820": "MARTINEZ, CA", "2821": "REDWOOD CITY, CA", "2827": "SELBY, CA", "2828": "SAN JOAQUIN RIVER, CA",
        "2829": "SAN PABLO BAY, CA", "2830": "CARQUINEZ STRAIT, CA", "2831": "SUISUN BAY, CA", "2833": "RENO, NV", "2834": "SAN JOSE INTERNATIONAL AIRPORT",
        "2835": "SACRAMENTO INTERNATIONAL AIRPORT, CA", "2870": "DHL WORLDWIDE EXPRESS", "2871": "AIR CARGO HANDLING SERVICES", "2872": "TNT SKYPAK",
        "2873": "IBC PACIFIC, CA", "2881": "SACRAMENTO INTERNATIONAL AIRPORT", "2895": "FEDERAL EXPRESS, OAKLAND, CA", "2901": "ASTORIA, OR",
        "2902": "NEWPORT, OR", "2903": "COOS BAY, OR", "2904": "COLUMBIA SNAKE RIVER", "2905": "LONGVIEW, WA", "2907": "BOISE, ID",
        "2908": "VANCOUVER, WA", "2909": "KALAMA, WA", "2910": "PORTLAND INTERNATIONAL AIRPORT", "3001": "SEATTLE, WA", "3002": "TACOMA, WA",
        "3003": "ABERDEEN, WA", "3004": "BLAINE, WA", "3005": "BELLINGHAM, WA", "3006": "EVERETT, WA", "3007": "PORT ANGELES, WA",
        "3008": "PORT TOWNSEND, WA", "3009": "SUMAS, WA", "3010": "ANACORTES, WA", "3011": "NIGHTHAWK, WA", "3012": "DANVILLE, WA",
        "3013": "FERRY, WA", "3014": "FRIDAY HARBOR, WA", "3015": "BOUNDARY, WA", "3016": "LAURIER, WA", "3017": "POINT ROBERTS, WA",
        "3018": "KENMORE AIR HARBOR, WA", "3019": "OROVILLE, WA", "3020": "FRONTIER, WA", "3022": "SPOKANE, WA", "3023": "LYNDEN, WA",
        "3025": "METALINE FALLS, WA", "3026": "OLYMPIA, WA", "3027": "NEAH BAY, WA", "3029": "SEATTLE-TACOMA INTERNATIONAL AIRPORT",
        "3071": "UPS", "3072": "AVION BROKERS @ SEATAC", "3073": "DHL WORLDWIDE EXPRESS", "3074": "AIRBORNE EXPRESS @ SEATAC",
        "3081": "YAKIMA AIR TERMINAL", "3082": "GRANT COUNTY AIRPORT", "3095": "UPS COURIER HUB", "3101": "JUNEAU, AK", "3102": "KETCHIKAN, AK",
        "3103": "SKAGWAY, AK", "3104": "ALCAN, AK", "3105": "WRANGELL, AK", "3106": "DALTON CACHE, AK", "3107": "VALDEZ, AK",
        "3111": "FAIRBANKS, AK", "3112": "PETERSBURG, AK", "3115": "SITKA, AK", "3124": "PELICAN, AK", "3126": "ANCHORAGE, AK",
        "3127": "KODIAK, AK", "3181": "ST PAUL AIRPORT", "3195": "FEDERAL EXPRESS, ANCHORAGE, AK", "3201": "HONOLULU, HI", "3202": "HILO, HI",
        "3203": "KAHULUI, HI", "3204": "NAWILIWILI-PORT ALLEN, HI", "3205": "HONOLULU INTERNATIONAL AIRPORT", "3206": "KONA, HI",
        "3295": "HONOLULU AIRPORT", "3301": "RAYMOND, MT", "3302": "EASTPORT, ID", "3303": "SALT LAKE CITY, UT", "3304": "GREAT FALLS, MT",
        "3305": "BUTTE, MT", "3306": "TURNER, MT", "3307": "DENVER, CO", "3308": "PORTHILL, ID", "3309": "SCOBEY, MT", "3310": "SWEETGRASS, MT",
        "3312": "WHITETAIL, MT", "3316": "PIEGAN, MT", "3317": "OPHEIM, MT", "3318": "ROOSVILLE, MT", "3319": "MORGAN, MT",
        "3321": "WHITLASH, MT", "3322": "DEL BONITA, MT", "3323": "WILDHORSE, MT", "3324": "KALISPELL AIRPORT", "3325": "WILLOW CREEK, HAVRE, MT",
        "3382": "NATRONA COUNTY INTERNATIONAL AIRPORT", "3384": "ARAPAHOE COUNTY PUBLIC AIRPORT, CO", "3385": "EAGLE COUNTY REGIONAL AIRPORT, CO",
        "3401": "PEMBINA, ND", "3403": "PORTAL, ND", "3404": "NECHE, ND", "3405": "ST JOHN, ND", "3406": "NORTHGATE, ND",
        "3407": "WALHALLA, ND", "3408": "HANNAH, ND", "3409": "SARLES, ND", "3410": "AMBROSE, ND", "3411": "FARGO, ND",
        "3413": "ANTLER, ND", "3414": "SHERWOOD, ND", "3415": "HANSBORO, ND", "3416": "MAIDA, ND", "3417": "FORTUNA, ND",
        "3419": "WESTHOPE, ND", "3420": "NOONAN, ND", "3421": "CARBURY, ND", "3422": "DUNSEITH, ND", "3423": "WARROAD, MN",
        "3424": "BAUDETTE, MN", "3425": "PINECREEK, MN", "3426": "ROSEAU, MN", "3427": "GRAND FORKS, ND", "3429": "CRANE LAKE, MN",
        "3430": "LANCASTER, MN", "3433": "WILLISTON AIRPORT, ND", "3434": "MINOT AIRPORT, ND", "3501": "MINNEAPOLIS-ST. PAUL, MN",
        "3502": "SIOUX FALLS, SD", "3510": "DULUTH, MN - SUPERIOR, WI", "3511": "ASHLAND, WI", "3512": "OMAHA, NE", "3513": "DES MOINES, IA",
        "3581": "USER FEE AIRPORT", "3604": "INTERNATIONAL FALLS, MN", "3613": "GRAND PORTAGE, MN", "3614": "SILVER BAY, MN",
        "3701": "MILWAUKEE, WI", "3702": "MARINETTE, WI", "3703": "GREEN BAY, WI", "3706": "MANITOWOC, WI", "3707": "SHEBOYGAN, WI",
        "3708": "RACINE, WI", "3801": "DETROIT, MI", "3802": "PORT HURON, MI", "3803": "SAULT STE. MARIE, MI", "3804": "SAGINAW/BAY CITY, MI",
        "3805": "BATTLE CREEK, MI", "3806": "GRAND RAPIDS, MI", "3807": "DETROIT METROPOLITAN AIRPORT, MI", "3808": "ESCANABA, MI",
        "3809": "MARQUETTE, MI", "3814": "ALGONAC, MI", "3815": "MUSKEGON, MI", "3816": "GRAND HAVEN, MI", "3818": "ROGERS CITY, MI",
        "3819": "DETOUR, MI", "3820": "MACKINAC ISLE, MI", "3842": "PRESQUE ISLE, MI", "3843": "ALPENA, MI", "3844": "FERRYSBURG, MI",
        "3881": "OAKLAND/PONTIAC AIRPORT", "3882": "WILLOW RUN AIRPORT", "3901": "CHICAGO, IL", "3902": "PEORIA, IL", "3905": "GARY, IN",
        "3908": "DAVENPORT-ROCK ISLAND", "3909": "GREATER ROCKFORD AIRPORT", "3981": "WAUKEGAN AIRPORT", "3983": "PAL-WAUKEE MUNICIPAL AIRPORT",
        "3984": "DUPAGE AIRPORT, IL", "3985": "DECATUR USER FEE AIRPORT", "3991": "NIPPON COURIER HUB", "4101": "CLEVELAND, OH",
        "4102": "CINCINNATI, OH", "4103": "COLUMBUS, OH", "4104": "DAYTON, OH", "4105": "TOLEDO, OH", "4106": "ERIE, PA",
        "4110": "INDIANAPOLIS, IN", "4112": "AKRON, OH", "4115": "LOUISVILLE, KY", "4116": "OWENSBORO, KY", "4117": "HURON, OH",
        "4121": "LORAIN, OH", "4122": "ASHTABULA/CONNEAUT, OH", "4181": "AIRBORNE AIR PARK", "4183": "FORT WAYNE AIRPORT",
        "4184": "BLUE GRASS AIRPORT", "4185": "HULMAN REGIONAL AIRPORT", "4192": "BURLINGTON AIR EXPRESS", "4194": "DHL EXPRESS, WILMINGTON, OHIO",
        "4195": "EMERY COURIER", "4196": "UPS COURIER", "4198": "FEDERAL EXPRESS INDIANAPOLIS, IN", "4501": "KANSAS CITY, MO",
        "4502": "ST JOSEPH, MO", "4503": "ST LOUIS, MO", "4504": "WICHITA, KS", "4505": "SPRINGFIELD, MO", "4506": "SPIRIT OF ST. LOUIS",
        "4601": "NEWARK, NJ", "4602": "PERTH AMBOY, NJ", "4670": "UPS", "4671": "FEDEX ECCF", "4681": "MORRISTOWN AIRPORT, NJ",
        "4701": "JOHN F KENNEDY AIRPORT, NY", "4770": "FEDERAL EXPRESS CORP.", "4771": "NYACC", "4772": "DHL AIRWAYS", "4773": "EMERY WORLDWIDE",
        "4774": "AIR FRANCE (MACH PLUS)", "4775": "DWORKIN/COSELL COURIER", "4776": "SWISSAIR (SKYRACER)", "4777": "ALITALIA (ALIEXPRESS)",
        "4778": "TNT SKYPAK", "4901": "AGUADILLA, PR", "4904": "FAJARDO, PR", "4906": "HUMACAO, PR", "4907": "MAYAGUEZ, PR",
        "4908": "PONCE, PR", "4909": "SAN JUAN, PR", "4911": "JOBOS, PR", "4912": "GUAYANILLA, PR", "4913": "INTERNATIONAL AIRPORT, PR",
        "5101": "CHARLOTTE AMALIE, VI", "5102": "CRUZ BAY, VI", "5103": "CORAL BAY, VI", "5104": "CHRISTIANSTED, VI", "5105": "FREDERIKSTED, VI",
        "5201": "MIAMI, FL", "5202": "KEY WEST, FL", "5203": "PORT EVERGLADES, FL", "5204": "WEST PALM BEACH, FL", "5205": "FORT PIERCE, FL",
        "5206": "MIAMI INTERNATIONAL AIRPORT", "5210": "FT. LAUDERDALE-HOLLYWOOD INTERNATIONAL", "5270": "INT. COURIER ASS.",
        "5271": "DHL WORLDWIDE EXPRESS", "5272": "MIA/CFS EXP CONSIG FACILITY", "5273": "UPS MIAMI AIRPORT", "5295": "UPS COURIER HUB, MIAMI, FL",
        "5297": "FEDERAL EXPRESS COURIER HUB MIAMI, FL", "5298": "IBC COURIER HUB", "5301": "HOUSTON, TX", "5306": "TEXAS CITY, TX",
        "5309": "HOUSTON INTERCONTINENTAL", "5310": "GALVESTON, TX", "5311": "FREEPORT, TX", "5312": "CORPUS CHRISTI, TX",
        "5313": "PORT LAVACA, TX", "5381": "SUGAR LAND REGIONAL AIRPORT, TX", "5401": "WASHINGTON, DC", "5402": "ALEXANDRIA, VA",
        "5501": "DALLAS/FT. WORTH, TX", "5502": "AMARILLO, TX", "5503": "LUBBOCK, TX", "5504": "OKLAHOMA CITY, OK", "5505": "TULSA, OK",
        "5506": "AUSTIN, TX", "5507": "SAN ANTONIO, TX", "5582": "MIDLAND INTERNATIONAL AIRPORT", "5583": "FORT WORTH ALLIANCE AIRPORT",
        "5584": "ADDISON AIRPORT", "01XX": "PORTLAND, ME", "02XX": "ST. ALBANS, VT", "04XX": "BOSTON, MA", "05XX": "PROVIDENCE, RI",
        "07XX": "OGDENSBURG, NY", "09XX": "BUFFALO, NY", "10XX": "NEW YORK CITY, NY", "11XX": "PHILADELPHIA, PA", "13XX": "BALTIMORE, MD",
        "14XX": "NORFOLK, VA", "15XX": "CHARLOTTE, NC", "16XX": "CHARLESTON, SC", "17XX": "SAVANNAH, GA", "18XX": "TAMPA, FL",
        "19XX": "MOBILE, AL", "20XX": "NEW ORLEANS, LA", "21XX": "PORT ARTHUR, TX", "23XX": "LAREDO, TX", "24XX": "EL PASO, TX",
        "25XX": "SAN DIEGO, CA", "26XX": "NOGALES, AZ", "27XX": "LOS ANGELES, CA", "28XX": "SAN FRANCISCO, CA", "29XX": "COLUMBIA-SNAKE, OR",
        "30XX": "SEATTLE, WA", "31XX": "ANCHORAGE, AK", "32XX": "UPS COURIER HUB / HONOLULU, HI", "33XX": "GREAT FALLS, MT",
        "34XX": "PEMBINA, ND", "35XX": "MINNEAPOLIS, MN", "36XX": "DULUTH, MN", "37XX": "MILWAUKEE, WI", "38XX": "DETROIT, MI",
        "39XX": "CHICAGO, IL", "41XX": "CLEVELAND, OH", "45XX": "ST. LOUIS, MO", "46XX": "NEWARK, NJ", "47XX": "JAMAICA, NY",
        "49XX": "SAN JUAN, PR", "51XX": "VIRGIN ISLANDS OF THE UNITED STATES", "52XX": "MIAMI, FL", "53XX": "HOUSTON-GALVESTON, TX",
        "54XX": "WASHINGTON, DC", "55XX": "DALLAS/FT. WORTH, TX"
    }
}

# Column rename mappings
COLUMN_RENAMES = {
    'dot1': {
        'TRDTYPE': 'Trade_Type',
        'USASTATE': 'US_State',
        'DEPE': 'Port_District',
        'DISAGMOT': 'Mode_of_Transport',
        'MEXSTATE': 'Mexico_State',
        'CANPROV': 'Canada_Province',
        'COUNTRY': 'Country',
        'VALUE': 'Trade_Value',
        'SHIPWT': 'Weight',
        'FREIGHT_CHARGES': 'Freight_Charges',
        'DF': 'Direction_Flag',
        'CONTCODE': 'Container_Code',
        'MONTH': 'Month',
        'YEAR': 'Year',
        'SOURCE_FILE': 'Source_File'
    },
    
    'dot2': {
        'TRDTYPE': 'Trade_Type',
        'USASTATE': 'US_State',
        'DEPE': 'Port_District',
        'DISAGMOT': 'Mode_of_Transport',
        'MEXSTATE': 'Mexico_State',
        'CANPROV': 'Canada_Province',
        'COUNTRY': 'Country',
        'VALUE': 'Trade_Value',
        'SHIPWT': 'Weight',
        'FREIGHT_CHARGES': 'Freight_Charges',
        'DF': 'Direction_Flag',
        'CONTCODE': 'Container_Code',
        'MONTH': 'Month',
        'YEAR': 'Year',
        'SOURCE_FILE': 'Source_File',
        'COMMODITY2': 'Commodity_Code'
    },
    
    'dot3': {
        'TRDTYPE': 'Trade_Type',
        'DEPE': 'Port_District',
        'COMMODITY2': 'Commodity_Code',
        'DISAGMOT': 'Mode_of_Transport',
        'COUNTRY': 'Country',
        'VALUE': 'Trade_Value',
        'SHIPWT': 'Weight',
        'FREIGHT_CHARGES': 'Freight_Charges',
        'DF': 'Direction_Flag',
        'CONTCODE': 'Container_Code',
        'MONTH': 'Month',
        'YEAR': 'Year',
        'SOURCE_FILE': 'Source_File'
    }
}



# Mapping relationships: original_column -> mapping_dict_name
COLUMN_MAPPINGS = {
    'TRDTYPE': 'trade_type_map',
    'USASTATE': 'us_state_map',
    'DEPE': 'port_district_map',
    'DISAGMOT': 'mode_map',
    'MEXSTATE': 'mex_state_map',
    'CANPROV': 'canada_prov_map',
    'COUNTRY': 'country_map',
    'DF': 'df_map',
    'CONTCODE': 'container_code_map',
    'MONTH': 'month_map',
    'COMMODITY2': 'commodity_map'
}

def safe_map_values(series, mapping_dict, unknown_value="Unknown"):
    """Safely map values, handling various data types and missing values."""
    if series.empty:
        return series
    
    # Convert to string for mapping, handle NaN values
    mapped_series = series.astype(str).map(mapping_dict)
    
    # Fill unmapped values with original values first
    mapped_series = mapped_series.fillna(series.astype(str))
    
    # Replace 'nan' strings (from NaN conversion) with unknown_value
    mapped_series = mapped_series.replace('nan', unknown_value)
    
    # Also handle common null representations
    null_representations = ['None', 'NULL', 'null', '', ' ', 'NaN', 'N/A']
    for null_rep in null_representations:
        mapped_series = mapped_series.replace(null_rep, unknown_value)
    
    return mapped_series

def apply_mappings(df, dataset_name):
    """Apply all relevant mappings to a dataframe."""
    logger.info(f"Applying mappings to {dataset_name}")
    
    # Get the rename mapping for this dataset
    rename_mapping = COLUMN_RENAMES.get(dataset_name, {})
    
    # Rename columns first
    df_mapped = df.rename(columns=rename_mapping)
    
    # Apply value mappings to original columns (before renaming)
    for orig_col, mapping_name in COLUMN_MAPPINGS.items():
        if orig_col in df.columns:
            mapping_dict = MAPPINGS[mapping_name]
            new_col = rename_mapping.get(orig_col, orig_col)
            
            try:
                df_mapped[new_col] = safe_map_values(df[orig_col], mapping_dict)
                logger.debug(f"Mapped {orig_col} -> {new_col} using {mapping_name}")
            except Exception as e:
                logger.warning(f"Failed to map {orig_col}: {e}")
                # Keep original values if mapping fails
                df_mapped[new_col] = df[orig_col]
    
    # Final cleanup: replace any remaining null values with "Unknown"
    # This is especially useful for categorical columns
    categorical_columns = ['Trade_Type', 'US_State', 'Port_District', 'Mode_of_Transport',
                          'Mexico_State', 'Canada_Province', 'Country', 'Direction_Flag',
                          'Container_Code', 'Month', 'Commodity_Code']
    
    for col in categorical_columns:
        if col in df_mapped.columns:
            df_mapped[col] = df_mapped[col].fillna('Unknown')
    
    return df_mapped

def save_enriched_data(df_original, df_mapped, output_path, dataset_name):
    """Save enriched data with both original and mapped columns."""
    logger.info(f"Saving enriched data to {output_path}")
    
    # Start with original data
    enriched_df = df_original.copy()
    
    # Ensure column names are consistent
    enriched_df.columns = [c.strip().upper() for c in enriched_df.columns]
    
    # Add mapped columns with _MAPPED suffix
    rename_mapping = COLUMN_RENAMES.get(dataset_name, {})
    
    for orig_col, new_col in rename_mapping.items():
        if orig_col in enriched_df.columns and new_col in df_mapped.columns:
            enriched_df[f"{new_col}_MAPPED"] = df_mapped[new_col]
    
    enriched_df.to_csv(output_path, index=False)
    logger.info(f"Saved enriched data with {len(enriched_df.columns)} columns")

# Load data (following your original approach)
print('Loading data...')
dot1 = pd.read_csv(os.path.join(DATA_DIR, 'dot1_all.csv'))
dot2 = pd.read_csv(os.path.join(DATA_DIR, 'dot2_all.csv'))
dot3 = pd.read_csv(os.path.join(DATA_DIR, 'dot3_all.csv'))

# Process each dataset
logger.info('Processing dot1...')
dot1_mapped = apply_mappings(dot1, 'dot1')

logger.info('Processing dot2...')
dot2_mapped = apply_mappings(dot2, 'dot2')

logger.info('Processing dot3...')
dot3_mapped = apply_mappings(dot3, 'dot3')

# Save cleaned files (mapped columns only)
dot1_mapped.to_csv(os.path.join(OUTPUT_DIR, 'dot1_all_cleaned.csv'), index=False)
dot2_mapped.to_csv(os.path.join(OUTPUT_DIR, 'dot2_all_cleaned.csv'), index=False)
dot3_mapped.to_csv(os.path.join(OUTPUT_DIR, 'dot3_all_cleaned.csv'), index=False)

# Save enriched files with all original and mapped columns
save_enriched_data(dot1, dot1_mapped, os.path.join(OUTPUT_DIR, 'dot1_all_enriched.csv'), 'dot1')
save_enriched_data(dot2, dot2_mapped, os.path.join(OUTPUT_DIR, 'dot2_all_enriched.csv'), 'dot2')
save_enriched_data(dot3, dot3_mapped, os.path.join(OUTPUT_DIR, 'dot3_all_enriched.csv'), 'dot3')

print('Saved enriched files with all original and mapped columns to notebooks/worked_data/.')
print('Renamed and saved cleaned files to notebooks/worked_data/.')

# Main execution (following your original script style)
if __name__ == "__main__":
    # Load data (following your original approach)
    print('Loading data...')
    dot1 = pd.read_csv(os.path.join(DATA_DIR, 'dot1_all.csv'))
    dot2 = pd.read_csv(os.path.join(DATA_DIR, 'dot2_all.csv'))
    dot3 = pd.read_csv(os.path.join(DATA_DIR, 'dot3_all.csv'))

    # Process each dataset
    logger.info('Processing dot1...')
    dot1_mapped = apply_mappings(dot1, 'dot1')

    logger.info('Processing dot2...')
    dot2_mapped = apply_mappings(dot2, 'dot2')

    logger.info('Processing dot3...')
    dot3_mapped = apply_mappings(dot3, 'dot3')

    # Save cleaned files (mapped columns only)
    dot1_mapped.to_csv(os.path.join(OUTPUT_DIR, 'dot1_all_cleaned.csv'), index=False)
    dot2_mapped.to_csv(os.path.join(OUTPUT_DIR, 'dot2_all_cleaned.csv'), index=False)
    dot3_mapped.to_csv(os.path.join(OUTPUT_DIR, 'dot3_all_cleaned.csv'), index=False)

    # Save enriched files with all original and mapped columns
    save_enriched_data(dot1, dot1_mapped, os.path.join(OUTPUT_DIR, 'dot1_all_enriched.csv'), 'dot1')
    save_enriched_data(dot2, dot2_mapped, os.path.join(OUTPUT_DIR, 'dot2_all_enriched.csv'), 'dot2')
    save_enriched_data(dot3, dot3_mapped, os.path.join(OUTPUT_DIR, 'dot3_all_enriched.csv'), 'dot3')

    print('Saved enriched files with all original and mapped columns to notebooks/worked_data/.')
    print('Renamed and saved cleaned files to notebooks/worked_data/.')