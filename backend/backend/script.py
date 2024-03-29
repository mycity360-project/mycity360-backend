categories = [
    "Cars",
    "Bikes",
    "Farm Land",
    "Properties",
    "Mobiles",
    "Jobs",
    "Electronics",
    "Automobile",
    "Old Household",
    "Fashion",
    "Donations",
    "Pets",
    "Matrimony",
]

sub_categories = {
    "Cars": [],
    "Bikes": [
        "Motorcycle",
        "Scooters",
        "Spare parts",
        "Bicycle",
        "Other Bikes",
    ],
    "Farm Land": [],
    "Properties": [
        "For Rent: House & Apartment",
        "For Sale: House & Apartment",
        "Lands & Plots",
        "For Rent: Shops & offices",
        "For Sale: Shops & Offices",
        "PG & Guest Houses",
    ],
    "Mobiles": ["Mobile Phones", "Accessories", "Tablets"],
    "Jobs": ["Teacher", "Cook", "IT Engineer", "Other Jobs"],
    "Electronics": [
        "TV",
        "Computer & Laptop",
        "Camera",
        "Refrigerator",
        "Washing Machine",
        "Air Conditioner",
        "Printer",
        "Other Electronics",
    ],
    "Automobile": [
        "Tractor",
        "Jeep",
        "Commercial Vehicle",
        "Other Automobile",
    ],
    "Old Household": [
        "Sofa",
        "Dining",
        "Bed",
        "Wardrobe",
        "Home Decor",
        "Books",
        "Gym & Sports Equipment",
        "Other Household",
    ],
    "Fashion": ["Men", "Women", "Kids"],
    "Donations": [],
    "Pets": [
        "Cow",
        "Buffallo",
        "Horse",
        "Dog",
        "Cat",
        "Pet Food & Accessories",
        "Other Pets",
    ],
    "Matrimony": ["Boy", "Girl"],
}

from backend.models.category import Category

for j, i in enumerate(categories):
    Category.objects.create(name=i, sequence=j, phone="9315538805")

for k, v in sub_categories.items():
    try:
        cat = Category.objects.get(name=k)
        for j, i in enumerate(v):
            Category.objects.create(
                name=i, sequence=j, phone="9315538805", category_id=cat.id
            )
    except:
        print(k)


questions_car = [
    {
        "question": "Brand",
        "category": "Cars",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Brand",
        "placeholder": "Select the brand",
        "is_required": True,
        "answer_limit": 0,
        "values": [
            "Maruti Suzuki",
            "Hyundai",
            "Mahindra",
            "Tata",
            "Honda",
            "Toyota",
            "Renault",
            "Ford",
            "Volkswagen",
            "Nissan",
            "Skoda",
            "MG",
            "Kia",
            "Fiat",
            "Mercedes-Benz",
            "BMW",
            "Audi",
            "Volvo",
            "Land Rover",
            "Jaguar",
            "Jeep",
            "Mitsubishi",
            "Porsche",
            "Mini",
            "Datsun",
            "Isuzu",
            "Force Motors",
            "Lamborghini",
            "Bentley",
            "Rolls-Royce",
            "Jaguar",
            "Maserati",
        ],
    },
    {
        "question": "Year of Purchase",
        "category": "Cars",
        "sequence": 2,
        "field_type": "Number",
        "label": "Year",
        "placeholder": "Enter the year of Purchase",
        "is_required": True,
        "answer_limit": 4,
        "values": [],
    },
    {
        "question": "Fuel Type",
        "category": "Cars",
        "sequence": 3,
        "field_type": "Dropdown",
        "label": "Fuel",
        "placeholder": "Select the Fuel used",
        "is_required": True,
        "answer_limit": 0,
        "values": [
            "Petrol",
            "Diesel",
            "Electric",
            "Hybrid",
            "LPG",
            "CNG",
            "Biofuel",
            "Hydrogen",
        ],
    },
    {
        "question": "Transmission Type",
        "category": "Cars",
        "sequence": 4,
        "field_type": "Dropdown",
        "label": "Transmission",
        "placeholder": "Select the Transmission",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Manual", "Automatic", "Semi-Automatic"],
    },
    {
        "question": "KM driven",
        "category": "Cars",
        "sequence": 5,
        "field_type": "Number",
        "label": "KM driven",
        "placeholder": "Enter KM driven",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
    {
        "question": "No. of Owners",
        "category": "Cars",
        "sequence": 6,
        "field_type": "Dropdown",
        "label": "No. of Owners",
        "placeholder": "Select No. of Owners",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1st", "2nd", "3rd", "4th", "4+"],
    },
]
questions_farm_land = [
    {
        "question": "Type",
        "category": "Farm Land",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Type",
        "placeholder": "Select the type",
        "is_required": True,
        "answer_limit": 0,
        "values": ["For Rent", "For Sale"],
    },
    {
        "question": "Listed by",
        "category": "Farm Land",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Listed by",
        "placeholder": "Select Listed by",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Builder", "Dealer", "Owner"],
    },
    {
        "question": "Plot Area",
        "category": "Farm Land",
        "sequence": 3,
        "field_type": "Number",
        "label": "Plot Area",
        "placeholder": "Enter Plot Area",
        "is_required": True,
        "answer_limit": 6,
        "values": [],
    },
    {
        "question": "Facing",
        "category": "Farm Land",
        "sequence": 4,
        "field_type": "Text",
        "label": "Facing",
        "placeholder": "Enter Facing",
        "is_required": False,
        "answer_limit": 6,
        "values": [],
    },
]
questions_land_plots = [
    {
        "question": "Type",
        "category": "Lands & Plots",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Type",
        "placeholder": "Select the type",
        "is_required": True,
        "answer_limit": 0,
        "values": ["For Rent", "For Sale"],
    },
    {
        "question": "Listed by",
        "category": "Lands & Plots",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Listed by",
        "placeholder": "Select Listed by",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Builder", "Dealer", "Owner"],
    },
    {
        "question": "Plot Area",
        "category": "Lands & Plots",
        "sequence": 3,
        "field_type": "Number",
        "label": "Plot Area",
        "placeholder": "Enter Plot Area",
        "is_required": True,
        "answer_limit": 6,
        "values": [],
    },
    {
        "question": "Facing",
        "category": "Lands & Plots",
        "sequence": 4,
        "field_type": "Text",
        "label": "Facing",
        "placeholder": "Enter Facing",
        "is_required": False,
        "answer_limit": 6,
        "values": [],
    },
]
questions_motorcycle = [
    {
        "question": "Brand",
        "category": "Motorcycle",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Brand",
        "placeholder": "Select the Brand",
        "is_required": True,
        "answer_limit": 0,
        "values": [
            "Hero MotoCorp",
            "Bajaj",
            "TVS",
            "Honda",
            "Yamaha",
            "Royal Enfield",
            "Suzuki",
            "KTM",
            "Mahindra",
            "Harley-Davidson",
            "Triumph",
            "Kawasaki",
            "Ducati",
            "BMW Motorrad",
            "Benelli",
            "Jawa",
            "Husqvarna",
            "UM",
            "Techo Electra",
            "Revolt Motors",
            "Okinawa",
            "Ather Energy",
            "Evolet",
            "Kabira Mobility",
        ],
    },
    {
        "question": "Year",
        "category": "Motorcycle",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Year",
        "placeholder": "Enter the Year",
        "is_required": True,
        "answer_limit": 4,
        "values": [],
    },
    {
        "question": "KM driven",
        "category": "Motorcycle",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "KM driven",
        "placeholder": "Enter KM driven",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
]
questions_scooter = [
    {
        "question": "Brand",
        "category": "Scooters",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Brand",
        "placeholder": "Select the Brand",
        "is_required": True,
        "answer_limit": 0,
        "values": [
            "Hero MotoCorp",
            "Bajaj",
            "TVS",
            "Honda",
            "Yamaha",
            "Royal Enfield",
            "Suzuki",
            "KTM",
            "Mahindra",
            "Harley-Davidson",
            "Triumph",
            "Kawasaki",
            "Ducati",
            "BMW Motorrad",
            "Benelli",
            "Jawa",
            "Husqvarna",
            "UM",
            "Techo Electra",
            "Revolt Motors",
            "Okinawa",
            "Ather Energy",
            "Evolet",
            "Kabira Mobility",
        ],
    },
    {
        "question": "Year",
        "category": "Scooters",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Year",
        "placeholder": "Enter the Year",
        "is_required": True,
        "answer_limit": 4,
        "values": [],
    },
    {
        "question": "KM driven",
        "category": "Scooters",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "KM driven",
        "placeholder": "Enter KM driven",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
]
question_cycle = [
    {
        "question": "Brand",
        "category": "Bicycle",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Brand",
        "placeholder": "Select the Brand",
        "is_required": True,
        "answer_limit": 0,
        "values": [
            "Hero Cycles",
            "Atlas Cycles",
            "Firefox",
            "Avon Cycles",
            "BSA",
            "Hercules",
            "Btwin",
            "Montra",
            "Schnell",
            "Rockrider",
            "Schnell",
            "Mach City",
            "Roadeo",
            "Stryder",
            "Kross",
            "La Sovereign",
            "Mongoose",
            "Frog",
            "Kross",
        ],
    }
]
question_house = [
    {
        "question": "Type",
        "category": "For Rent: House & Apartment",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Type",
        "placeholder": "Select the Type",
        "is_required": True,
        "answer_limit": 0,
        "values": [
            "Apartments",
            "Builder Floors",
            "Farm Houses",
            "Houses & Villas",
        ],
    },
    {
        "question": "Bedrooms",
        "category": "For Rent: House & Apartment",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Bedrooms",
        "placeholder": "Select the Bedrooms Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "4", "4+"],
    },
    {
        "question": "Bathrooms",
        "category": "For Rent: House & Apartment",
        "sequence": 3,
        "field_type": "Dropdown",
        "label": "Bathrooms",
        "placeholder": "Select the Bathrooms Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "4", "4+"],
    },
    {
        "question": "Furnishing",
        "category": "For Rent: House & Apartment",
        "sequence": 4,
        "field_type": "Dropdown",
        "label": "Furnishing",
        "placeholder": "Select the Furnishing",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Furnished", "Semi-Furnished", "Unfurnished"],
    },
    {
        "question": "Construction Status",
        "category": "For Rent: House & Apartment",
        "sequence": 5,
        "field_type": "Dropdown",
        "label": "Construction Status",
        "placeholder": "Select the Construction Status",
        "is_required": True,
        "answer_limit": 0,
        "values": ["New Launch", "Ready to Move", "Under Construction"],
    },
    {
        "question": "Listed by",
        "category": "For Rent: House & Apartment",
        "sequence": 6,
        "field_type": "Dropdown",
        "label": "Listed by",
        "placeholder": "Select the Listed by",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Builder", "Dealer", "Owner"],
    },
    {
        "question": "Super Builtup area",
        "category": "For Rent: House & Apartment",
        "sequence": 7,
        "field_type": "Text",
        "label": "Super Builtup area",
        "placeholder": "Enter the Super Builtup area",
        "is_required": True,
        "answer_limit": 40,
        "values": [],
    },
    {
        "question": "Carpet Area",
        "category": "For Rent: House & Apartment",
        "sequence": 8,
        "field_type": "Text",
        "label": "Carpet Area",
        "placeholder": "Enter the Carpet Area",
        "is_required": True,
        "answer_limit": 40,
        "values": [],
    },
    {
        "question": "Bachelors Allowed",
        "category": "For Rent: House & Apartment",
        "sequence": 9,
        "field_type": "Toggle",
        "label": "Bachelors Allowed",
        "placeholder": "Select the Bachelors Allowed",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Yes", "No"],
    },
    {
        "question": "Maintenance (Monthly)",
        "category": "For Rent: House & Apartment",
        "sequence": 10,
        "field_type": "Number",
        "label": "Maintenance (Monthly)",
        "placeholder": "Enter the Maintenance (Monthly) in Rs.",
        "is_required": False,
        "answer_limit": 10,
        "values": [],
    },
    {
        "question": "Total Floors",
        "category": "For Rent: House & Apartment",
        "sequence": 11,
        "field_type": "Number",
        "label": "Total Floors",
        "placeholder": "Enter the Total Floors",
        "is_required": False,
        "answer_limit": 2,
        "values": [],
    },
    {
        "question": "Floor No",
        "category": "For Rent: House & Apartment",
        "sequence": 12,
        "field_type": "Number",
        "label": "Floor No",
        "placeholder": "Enter the Floor No",
        "is_required": False,
        "answer_limit": 2,
        "values": [],
    },
    {
        "question": "Car Parking",
        "category": "For Rent: House & Apartment",
        "sequence": 13,
        "field_type": "Dropdown",
        "label": "Car Parking",
        "placeholder": "Select the Car Parking Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "3+"],
    },
    {
        "question": "Type",
        "category": "For Sale: House & Apartment",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Type",
        "placeholder": "Select the Type",
        "is_required": True,
        "answer_limit": 0,
        "values": [
            "Apartments",
            "Builder Floors",
            "Farm Houses",
            "Houses & Villas",
        ],
    },
    {
        "question": "Bedrooms",
        "category": "For Sale: House & Apartment",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Bedrooms",
        "placeholder": "Select the Bedrooms Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "4", "4+"],
    },
    {
        "question": "Bathrooms",
        "category": "For Sale: House & Apartment",
        "sequence": 3,
        "field_type": "Dropdown",
        "label": "Bathrooms",
        "placeholder": "Select the Bathrooms Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "4", "4+"],
    },
    {
        "question": "Furnishing",
        "category": "For Sale: House & Apartment",
        "sequence": 4,
        "field_type": "Dropdown",
        "label": "Furnishing",
        "placeholder": "Select the Furnishing",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Furnished", "Semi-Furnished", "Unfurnished"],
    },
    {
        "question": "Construction Status",
        "category": "For Sale: House & Apartment",
        "sequence": 5,
        "field_type": "Dropdown",
        "label": "Construction Status",
        "placeholder": "Select the Construction Status",
        "is_required": True,
        "answer_limit": 0,
        "values": ["New Launch", "Ready to Move", "Under Construction"],
    },
    {
        "question": "Listed by",
        "category": "For Sale: House & Apartment",
        "sequence": 6,
        "field_type": "Dropdown",
        "label": "Listed by",
        "placeholder": "Select the Listed by",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Builder", "Dealer", "Owner"],
    },
    {
        "question": "Super Builtup area",
        "category": "For Sale: House & Apartment",
        "sequence": 7,
        "field_type": "Text",
        "label": "Super Builtup area",
        "placeholder": "Enter the Super Builtup area",
        "is_required": True,
        "answer_limit": 40,
        "values": [],
    },
    {
        "question": "Carpet Area",
        "category": "For Sale: House & Apartment",
        "sequence": 8,
        "field_type": "Text",
        "label": "Carpet Area",
        "placeholder": "Enter the Carpet Area",
        "is_required": True,
        "answer_limit": 40,
        "values": [],
    },
    {
        "question": "Maintenance (Monthly)",
        "category": "For Sale: House & Apartment",
        "sequence": 9,
        "field_type": "Number",
        "label": "Maintenance (Monthly)",
        "placeholder": "Enter the Maintenance (Monthly) in Rs.",
        "is_required": False,
        "answer_limit": 10,
        "values": [],
    },
    {
        "question": "Total Floors",
        "category": "For Sale: House & Apartment",
        "sequence": 10,
        "field_type": "Number",
        "label": "Total Floors",
        "placeholder": "Enter the Total Floors",
        "is_required": False,
        "answer_limit": 2,
        "values": [],
    },
    {
        "question": "Floor No",
        "category": "For Sale: House & Apartment",
        "sequence": 11,
        "field_type": "Number",
        "label": "Floor No",
        "placeholder": "Enter the Floor No",
        "is_required": False,
        "answer_limit": 2,
        "values": [],
    },
    {
        "question": "Car Parking",
        "category": "For Sale: House & Apartment",
        "sequence": 12,
        "field_type": "Dropdown",
        "label": "Car Parking",
        "placeholder": "Select the Car Parking Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "3+"],
    },
]
question_office = [
    {
        "question": "Furnishing",
        "category": "For Rent: Shops & offices",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Furnishing",
        "placeholder": "Select the Furnishing",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Furnished", "Semi-Furnished", "Unfurnished"],
    },
    {
        "question": "Listed by",
        "category": "For Rent: Shops & offices",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Listed by",
        "placeholder": "Select the Listed by",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Builder", "Dealer", "Owner"],
    },
    {
        "question": "Washrooms",
        "category": "For Rent: Shops & offices",
        "sequence": 3,
        "field_type": "Dropdown",
        "label": "Washrooms",
        "placeholder": "Select the Washrooms Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "4", "4+"],
    },
    {
        "question": "Super Builtup area",
        "category": "For Rent: Shops & offices",
        "sequence": 4,
        "field_type": "Text",
        "label": "Super Builtup area",
        "placeholder": "Enter the Super Builtup area",
        "is_required": True,
        "answer_limit": 40,
        "values": [],
    },
    {
        "question": "Carpet Area",
        "category": "For Rent: Shops & offices",
        "sequence": 5,
        "field_type": "Text",
        "label": "Carpet Area",
        "placeholder": "Enter the Carpet Area",
        "is_required": True,
        "answer_limit": 40,
        "values": [],
    },
    {
        "question": "Maintenance (Monthly)",
        "category": "For Rent: Shops & offices",
        "sequence": 6,
        "field_type": "Number",
        "label": "Maintenance (Monthly)",
        "placeholder": "Enter the Maintenance (Monthly) in Rs.",
        "is_required": False,
        "answer_limit": 12,
        "values": [],
    },
    {
        "question": "Car Parking",
        "category": "For Rent: Shops & offices",
        "sequence": 7,
        "field_type": "Dropdown",
        "label": "Car Parking",
        "placeholder": "Select the Car Parking Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "3+"],
    },
    {
        "question": "Furnishing",
        "category": "For Sale: Shops & Offices",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Furnishing",
        "placeholder": "Select the Furnishing",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Furnished", "Semi-Furnished", "Unfurnished"],
    },
    {
        "question": "Construction Status",
        "category": "For Sale: Shops & Offices",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Construction Status",
        "placeholder": "Select the Construction Status",
        "is_required": True,
        "answer_limit": 0,
        "values": ["New Launch", "Ready to Move", "Under Construction"],
    },
    {
        "question": "Listed by",
        "category": "For Sale: Shops & Offices",
        "sequence": 3,
        "field_type": "Dropdown",
        "label": "Listed by",
        "placeholder": "Select the Listed by",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Builder", "Dealer", "Owner"],
    },
    {
        "question": "Washrooms",
        "category": "For Sale: Shops & Offices",
        "sequence": 4,
        "field_type": "Dropdown",
        "label": "Washrooms",
        "placeholder": "Select the Washrooms Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "4", "4+"],
    },
    {
        "question": "Super Builtup area",
        "category": "For Sale: Shops & Offices",
        "sequence": 5,
        "field_type": "Text",
        "label": "Super Builtup area",
        "placeholder": "Enter the Super Builtup area",
        "is_required": True,
        "answer_limit": 40,
        "values": [],
    },
    {
        "question": "Carpet Area",
        "category": "For Sale: Shops & Offices",
        "sequence": 6,
        "field_type": "Text",
        "label": "Carpet Area",
        "placeholder": "Enter the Carpet Area",
        "is_required": True,
        "answer_limit": 40,
        "values": [],
    },
    {
        "question": "Maintenance (Monthly)",
        "category": "For Sale: Shops & Offices",
        "sequence": 7,
        "field_type": "Number",
        "label": "Maintenance (Monthly)",
        "placeholder": "Enter the Maintenance (Monthly) in Rs.",
        "is_required": False,
        "answer_limit": 12,
        "values": [],
    },
    {
        "question": "Car Parking",
        "category": "For Sale: Shops & Offices",
        "sequence": 8,
        "field_type": "Dropdown",
        "label": "Car Parking",
        "placeholder": "Select the Car Parking Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "3+"],
    },
]
question_pg = [
    {
        "question": "Subtype",
        "category": "PG & Guest Houses",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Subtype",
        "placeholder": "Select the Subtype",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Guest Houses", "PG", "Roommate"],
    },
    {
        "question": "Furnishing",
        "category": "PG & Guest Houses",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Furnishing",
        "placeholder": "Select the Furnishing",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Furnished", "Semi-Furnished", "Unfurnished"],
    },
    {
        "question": "Listed by",
        "category": "PG & Guest Houses",
        "sequence": 3,
        "field_type": "Dropdown",
        "label": "Listed by",
        "placeholder": "Select the Listed by",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Builder", "Dealer", "Owner"],
    },
    {
        "question": "Car Parking",
        "category": "PG & Guest Houses",
        "sequence": 4,
        "field_type": "Dropdown",
        "label": "Car Parking",
        "placeholder": "Select the Car Parking Count",
        "is_required": True,
        "answer_limit": 0,
        "values": ["1", "2", "3", "3+"],
    },
    {
        "question": "Meals Included",
        "category": "PG & Guest Houses",
        "sequence": 5,
        "field_type": "Toggle",
        "label": "Meals Included",
        "placeholder": "Select the Meals Included",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Yes", "No"],
    },
]
question_mobile = [
    {
        "question": "Brand",
        "category": "Mobile Phones",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Brand",
        "placeholder": "Select the Brand",
        "is_required": True,
        "answer_limit": 0,
        "values": [
            "Apple",
            "Samsung",
            "Huawei",
            "Xiaomi",
            "Oppo",
            "Vivo",
            "OnePlus",
            "Motorola",
            "LG",
            "Sony",
            "Nokia",
            "Google",
            "HTC",
            "Lenovo",
            "Asus",
            "BlackBerry",
            "Meizu",
            "ZTE",
            "Alcatel",
            "Honor",
            "Realme",
            "TCL",
            "Micromax",
            "Panasonic",
            "Sharp",
            "Coolpad",
            "Gionee",
            "LeEco",
            "Infinix",
            "Tecno",
            "Itel",
            "Lava",
            "Karbonn",
            "Intex",
            "Micromax",
            "Meitu",
            "Umidigi",
            "BLU",
            "Razer",
            "Doogee",
        ],
    },
    {
        "question": "Model",
        "category": "Mobile Phones",
        "sequence": 2,
        "field_type": "Text",
        "label": "Model",
        "placeholder": "Enter the Model",
        "is_required": True,
        "answer_limit": 25,
        "values": [
            "Apple",
            "Samsung",
            "Huawei",
            "Xiaomi",
            "Oppo",
            "Vivo",
            "OnePlus",
            "Motorola",
            "LG",
            "Sony",
            "Nokia",
            "Google",
            "HTC",
            "Lenovo",
            "Asus",
            "BlackBerry",
            "Meizu",
            "ZTE",
            "Alcatel",
            "Honor",
            "Realme",
            "TCL",
            "Micromax",
            "Panasonic",
            "Sharp",
            "Coolpad",
            "Gionee",
            "LeEco",
            "Infinix",
            "Tecno",
            "Itel",
            "Lava",
            "Karbonn",
            "Intex",
            "Micromax",
            "Meitu",
            "Umidigi",
            "BLU",
            "Razer",
            "Doogee",
        ],
    },
    {
        "question": "Type",
        "category": "Accessories",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Type",
        "placeholder": "Select the Type",
        "is_required": True,
        "answer_limit": 25,
        "values": ["Mobile", "Tablets"],
    },
    {
        "question": "Type",
        "category": "Tablets",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Type",
        "placeholder": "Select the Type",
        "is_required": True,
        "answer_limit": 25,
        "values": ["iPads", "Samsung", "Other Tablets"],
    },
]
question_jobs = [
    {
        "question": "Salary period",
        "category": "Teacher",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Salary period",
        "placeholder": "Select the Salary period",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Hourly", "Monthly", "Weekly", "Yearly"],
    },
    {
        "question": "Position type",
        "category": "Teacher",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Position type",
        "placeholder": "Select the Position type",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Contract", "Full-time", "Part-time", "Temporary"],
    },
    {
        "question": "Salary from",
        "category": "Teacher",
        "sequence": 3,
        "field_type": "Number",
        "label": "Salary from",
        "placeholder": "Enter the Salary",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
    {
        "question": "Salary to",
        "category": "Teacher",
        "sequence": 4,
        "field_type": "Number",
        "label": "Salary to",
        "placeholder": "Enter the Salary",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
    {
        "question": "Salary period",
        "category": "Cook",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Salary period",
        "placeholder": "Select the Salary period",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Hourly", "Monthly", "Weekly", "Yearly"],
    },
    {
        "question": "Position type",
        "category": "Cook",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Position type",
        "placeholder": "Select the Position type",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Contract", "Full-time", "Part-time", "Temporary"],
    },
    {
        "question": "Salary from",
        "category": "Cook",
        "sequence": 3,
        "field_type": "Number",
        "label": "Salary from",
        "placeholder": "Enter the Salary",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
    {
        "question": "Salary to",
        "category": "Cook",
        "sequence": 4,
        "field_type": "Number",
        "label": "Salary to",
        "placeholder": "Enter the Salary",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
    {
        "question": "Salary period",
        "category": "IT Engineer",
        "sequence": 1,
        "field_type": "Dropdown",
        "label": "Salary period",
        "placeholder": "Select the Salary period",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Hourly", "Monthly", "Weekly", "Yearly"],
    },
    {
        "question": "Position type",
        "category": "IT Engineer",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Position type",
        "placeholder": "Select the Position type",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Contract", "Full-time", "Part-time", "Temporary"],
    },
    {
        "question": "Salary from",
        "category": "IT Engineer",
        "sequence": 3,
        "field_type": "Number",
        "label": "Salary from",
        "placeholder": "Enter the Salary",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
    {
        "question": "Salary to",
        "category": "IT Engineer",
        "sequence": 4,
        "field_type": "Number",
        "label": "Salary to",
        "placeholder": "Enter the Salary",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
    {
        "question": "Position Name",
        "category": "Other Jobs",
        "sequence": 1,
        "field_type": "Text",
        "label": "Salary period",
        "placeholder": "Enter Position Name",
        "is_required": True,
        "answer_limit": 120,
        "values": [],
    },
    {
        "question": "Salary period",
        "category": "Other Jobs",
        "sequence": 2,
        "field_type": "Dropdown",
        "label": "Salary period",
        "placeholder": "Select the Salary period",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Hourly", "Monthly", "Weekly", "Yearly"],
    },
    {
        "question": "Position type",
        "category": "Other Jobs",
        "sequence": 3,
        "field_type": "Dropdown",
        "label": "Position type",
        "placeholder": "Select the Position type",
        "is_required": True,
        "answer_limit": 0,
        "values": ["Contract", "Full-time", "Part-time", "Temporary"],
    },
    {
        "question": "Salary from",
        "category": "Other Jobs",
        "sequence": 4,
        "field_type": "Number",
        "label": "Salary from",
        "placeholder": "Enter the Salary",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
    {
        "question": "Salary to",
        "category": "Other Jobs",
        "sequence": 5,
        "field_type": "Number",
        "label": "Salary to",
        "placeholder": "Enter the Salary",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
]
question_vehicle = [
    {
        "question": "Year",
        "category": "Tractor",
        "sequence": 1,
        "field_type": "Number",
        "label": "Year",
        "placeholder": "Enter the Year",
        "is_required": True,
        "answer_limit": 4,
        "values": [],
    },
    {
        "question": "KM driven",
        "category": "Tractor",
        "sequence": 2,
        "field_type": "Number",
        "label": "KM driven",
        "placeholder": "Enter the KM driven",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
    {
        "question": "Year",
        "category": "Jeep",
        "sequence": 1,
        "field_type": "Number",
        "label": "Year",
        "placeholder": "Enter the Year",
        "is_required": True,
        "answer_limit": 4,
        "values": [],
    },
    {
        "question": "KM driven",
        "category": "Jeep",
        "sequence": 2,
        "field_type": "Number",
        "label": "KM driven",
        "placeholder": "Enter the KM driven",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
    {
        "question": "Type",
        "category": "Commercial Vehicle",
        "sequence": 1,
        "field_type": "Text",
        "label": "Year",
        "placeholder": "Enter the Type",
        "is_required": True,
        "answer_limit": 40,
        "values": [],
    },
    {
        "question": "Year",
        "category": "Commercial Vehicle",
        "sequence": 2,
        "field_type": "Number",
        "label": "Year",
        "placeholder": "Enter the Year",
        "is_required": True,
        "answer_limit": 4,
        "values": [],
    },
    {
        "question": "KM driven",
        "category": "Commercial Vehicle",
        "sequence": 3,
        "field_type": "Number",
        "label": "KM driven",
        "placeholder": "Enter the KM driven",
        "is_required": True,
        "answer_limit": 7,
        "values": [],
    },
]

final_questions = (
    questions_car
    + questions_farm_land
    + questions_land_plots
    + questions_motorcycle
    + questions_scooter
    + question_cycle
    + question_house
    + question_office
    + question_pg
    + question_mobile
    + question_jobs
    + question_vehicle
)
from backend.models.question import Question
from backend.models.category import Category

for q in final_questions:
    q["category_id"] = Category.objects.get(name=q.pop("category")).id
    Question.objects.create(**q)
