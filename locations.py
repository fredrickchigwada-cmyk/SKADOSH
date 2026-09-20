from dataclasses import dataclass
import math


@dataclass
class Location:
    location_id: str
    name: str
    location_type: str
    map_name: str
    x: float
    y: float
    description: str = ""
    interactive: bool = True
    unlocked: bool = True

    def distance_to(self, x, y):
        return math.hypot(
            self.x - x,
            self.y - y
        )


class LocationManager:

    def __init__(self):
        self.locations = []

    def add(self, location):
        self.locations.append(location)

    def by_type(self, location_type):
        return [
            location
            for location in self.locations
            if location.location_type == location_type
        ]

    def by_map(self, map_name):
        return [
            location
            for location in self.locations
            if location.map_name == map_name
        ]

    def nearby(self, x, y, radius=250):
        return sorted(
            [
                location
                for location in self.locations
                if location.distance_to(x, y) <= radius
            ],
            key=lambda location:
                location.distance_to(x, y)
        )

    def nearest(self, x, y, location_type=None):
        locations = self.locations

        if location_type:
            locations = self.by_type(
                location_type
            )

        if not locations:
            return None

        return min(
            locations,
            key=lambda location:
                location.distance_to(x, y)
        )

    def count(self):
        return len(self.locations)


# =========================================================
# LOCATION DATABASE
# =========================================================

LOCATIONS = [

    # -------------------------
    # SCHOOLS
    # -------------------------

    Location(
        "school_mwashita",
        "Mwashita Academy",
        "SCHOOL",
        "Harare",
        1200,
        1100,
        "Fictional SKADOSH school location."
    ),

    Location(
        "school_harare_heights",
        "Harare Heights Academy",
        "SCHOOL",
        "Harare",
        1800,
        1300
    ),

    Location(
        "school_bulawayo_elite",
        "Bulawayo Elite Academy",
        "SCHOOL",
        "Bulawayo",
        2200,
        1600
    ),

    Location(
        "school_eastern_highlands",
        "Eastern Highlands Academy",
        "SCHOOL",
        "Mutare",
        2600,
        2000
    ),

    Location(
        "school_midlands",
        "Midlands Elite Academy",
        "SCHOOL",
        "Gweru",
        3000,
        1700
    ),

    Location(
        "school_great_zimbabwe",
        "Great Zimbabwe Academy",
        "SCHOOL",
        "Masvingo",
        3500,
        2500
    ),

    Location(
        "school_hwange",
        "Hwange Academy",
        "SCHOOL",
        "Hwange",
        1500,
        3500
    ),

    Location(
        "school_victoria_falls",
        "Victoria Falls Academy",
        "SCHOOL",
        "Victoria Falls",
        3800,
        1200
    ),

    Location(
        "school_sports",
        "SKADOSH Sports Academy",
        "SCHOOL",
        "SKADOSH Arena",
        2500,
        1000
    ),

    Location(
        "school_tech",
        "SKADOSH Tech Institute",
        "SCHOOL",
        "Harare",
        2700,
        1200
    ),

    # -------------------------
    # SHOPS
    # -------------------------

    Location(
        "shop_clothing",
        "SKADOSH Clothing",
        "SHOP",
        "Harare",
        1600,
        1600
    ),

    Location(
        "shop_equipment",
        "SKADOSH Equipment",
        "SHOP",
        "Harare",
        1900,
        1700
    ),

    Location(
        "shop_electronics",
        "SKADOSH Electronics",
        "SHOP",
        "Bulawayo",
        2400,
        1800
    ),

    Location(
        "shop_food",
        "SKADOSH Food Market",
        "SHOP",
        "Harare",
        2100,
        1900
    ),

    # -------------------------
    # GARAGES
    # -------------------------

    Location(
        "garage_main",
        "SKADOSH Garage",
        "GARAGE",
        "Harare",
        2300,
        2300
    ),

    Location(
        "garage_bulawayo",
        "Bulawayo Garage",
        "GARAGE",
        "Bulawayo",
        2700,
        2400
    ),

    Location(
        "garage_hwange",
        "Hwange Garage",
        "GARAGE",
        "Hwange",
        1400,
        2800
    ),

    # -------------------------
    # RESTAURANTS
    # -------------------------

    Location(
        "restaurant_city",
        "SKADOSH Restaurant",
        "RESTAURANT",
        "Harare",
        1700,
        2200
    ),

    Location(
        "restaurant_falls",
        "Fallsview Restaurant",
        "RESTAURANT",
        "Victoria Falls",
        3900,
        1500
    ),

    Location(
        "restaurant_lake",
        "Kariba Lakeside Restaurant",
        "RESTAURANT",
        "Lake Kariba",
        3300,
        3200
    ),

    # -------------------------
    # HOSPITALS
    # -------------------------

    Location(
        "hospital_harare",
        "Harare Medical Centre",
        "HOSPITAL",
        "Harare",
        2800,
        2800
    ),

    Location(
        "hospital_bulawayo",
        "Bulawayo Medical Centre",
        "HOSPITAL",
        "Bulawayo",
        3200,
        2800
    ),

    # -------------------------
    # BUSINESSES
    # -------------------------

    Location(
        "business_garage",
        "SKADOSH Garage Business",
        "BUSINESS",
        "Harare",
        2350,
        2350
    ),

    Location(
        "business_restaurant",
        "SKADOSH Restaurant Business",
        "BUSINESS",
        "Harare",
        1750,
        2200
    ),

    Location(
        "business_clothing",
        "SKADOSH Clothing Business",
        "BUSINESS",
        "Harare",
        1650,
        1600
    ),

    Location(
        "business_dealership",
        "SKADOSH Motors",
        "BUSINESS",
        "Harare",
        2500,
        2200
    ),

    Location(
        "business_hotel",
        "SKADOSH Hotel",
        "BUSINESS",
        "Victoria Falls",
        4000,
        1700
    ),

    Location(
        "business_nightclub",
        "SKADOSH Nightclub",
        "BUSINESS",
        "Neon Bulawayo",
        3200,
        2100
    ),

    # -------------------------
    # PROPERTIES
    # -------------------------

    Location(
        "property_apartment",
        "SKADOSH City Apartment",
        "PROPERTY",
        "Harare",
        2600,
        2600
    ),

    Location(
        "property_luxury",
        "SKADOSH Luxury Estate",
        "PROPERTY",
        "Harare",
        3100,
        3000
    ),

    Location(
        "property_lakeside",
        "Kariba Lakeside Estate",
        "PROPERTY",
        "Lake Kariba",
        3600,
        3300
    ),

    # -------------------------
    # RACING
    # -------------------------

    Location(
        "race_harare",
        "Harare Street Circuit",
        "RACE",
        "Harare",
        3000,
        1800
    ),

    Location(
        "race_bulawayo",
        "Bulawayo Sprint Circuit",
        "RACE",
        "Bulawayo",
        3300,
        1900
    ),

    Location(
        "race_hwange",
        "Hwange Off-Road Circuit",
        "RACE",
        "Hwange",
        1800,
        3200
    ),

    Location(
        "race_arena",
        "SKADOSH Arena",
        "RACE",
        "SKADOSH Arena",
        2500,
        3500
    ),

    # -------------------------
    # VIP
    # -------------------------

    Location(
        "vip_city",
        "VIP City",
        "VIP",
        "Harare",
        3400,
        2500,
        "Fictional VIP district."
    ),

    Location(
        "vip_estate",
        "VIP Estate",
        "VIP",
        "Harare",
        3700,
        2800
    ),

    # -------------------------
    # LANDMARKS
    # -------------------------

    Location(
        "landmark_great_zimbabwe",
        "Great Zimbabwe Ruins",
        "LANDMARK",
        "Great Zimbabwe",
        3500,
        3500
    ),

    Location(
        "landmark_victoria_falls",
        "Victoria Falls",
        "LANDMARK",
        "Victoria Falls",
        4200,
        1000
    ),

    Location(
        "landmark_kariba",
        "Lake Kariba",
        "LANDMARK",
        "Lake Kariba",
        4000,
        3600
    ),

    Location(
        "landmark_matobo",
        "Matobo",
        "LANDMARK",
        "Matobo",
        1000,
        4000
    ),

    # -------------------------
    # SPECIAL
    # -------------------------

    Location(
        "mission_hub",
        "SKADOSH Mission Hub",
        "MISSION",
        "Harare",
        2500,
        2500
    ),

    Location(
        "airport",
        "SKADOSH International Airport",
        "AIRPORT",
        "Harare",
        4200,
        2200
    ),

    Location(
        "police",
        "SKADOSH Police Station",
        "POLICE",
        "Harare",
        2200,
        2800
    ),

    Location(
        "fire_station",
        "SKADOSH Fire Station",
        "FIRE",
        "Harare",
        2000,
        3000
    ),

    Location(
        "bus_station",
        "SKADOSH Bus Station",
        "TRANSPORT",
        "Harare",
        1800,
        2500
    ),

    Location(
        "fast_travel",
        "SKADOSH Fast Travel Hub",
        "FAST_TRAVEL",
        "Harare",
        2500,
        1500
    ),
]


def create_location_manager():
    manager = LocationManager()

    for location in LOCATIONS:
        manager.add(location)

    return manager
