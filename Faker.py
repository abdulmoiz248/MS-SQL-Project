import string
import pyodbc
from faker import Faker
import random

# Connection details
Driver = 'SQL Server'
server = 'DESKTOP-EQ55Q8H'
database = 'project'

# Connection string
connection = f"DRIVER={{{Driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

try:
    # Establishing connection
    conn = pyodbc.connect(connection)
    cursor = conn.cursor()

    fake = Faker('en_US')
    pakistan_cities = [
        "Abbottabad", "Ahmadpur East", "Ahmadpur Sial", "Akora Khattak", "Ali Pur", "Alipur Chatha", "Arifwala",
        "Attock",
        "Badin", "Baffa", "Bahawalnagar", "Bahawalpur", "Bajaur", "Bandhi", "Bannu", "Barikot", "Barkhan", "Basirpur",
        "Batkhela", "Battagram", "Bela", "Bhakkar", "Bhawana", "Bhera", "Bhimber", "Bhiria City", "Bhiria Road",
        "Bhopalwala", "Bhuawana", "Burewala", "Chachro", "Chagai", "Chak Azam Sahu", "Chak Jhumra", "Chak 33 NB",
        "Chak 4 Bahawalnagar", "Chak 46", "Chak 63", "Chak 89 NB", "Chakdara", "Chakwal", "Chaman", "Charsadda",
        "Chashma",
        "Chawinda", "Chichawatni", "Chilas", "Chiniot", "Chishtian", "Chitral", "Choha Khalsa", "Choha Sharif",
        "Chunian",
        "D.G. Khan", "Dadu", "Daharki", "Dalbandin", "Dandot", "Dargai", "Darya Khan", "Daska", "Daud Khel",
        "Daulatpur",
        "Daultala", "Dera Allah Yar", "Dera Bugti", "Dera Ghazi Khan", "Dera Ismail Khan", "Dera Murad Jamali",
        "Dhanot",
        "Dharki", "Dijkot", "Dina", "Dinga", "Diplo", "Dir", "Doaba", "Doliwala", "Duki", "Dullewala", "Dunai",
        "Dunyapur",
        "Eidgah", "Faisalabad", "Faqirwali", "Faruka", "Fateh Jang", "Fatehpur", "Fazalpur", "Fort Abbas",
        "Fort Sandeman",
        "Gaddani", "Gakhar Mandi", "Garh Maharaja", "Garhi Khairo", "Garhi Yasin", "Gharo", "Ghotki", "Gilgit", "Gojra",
        "Gojra", "Gujar Khan", "Gujranwala", "Gujrat", "Gulistan", "Gwadar", "Hadali", "Hafizabad", "Hala", "Hangu",
        "Harappa", "Haripur", "Harnai", "Haroonabad", "Hasilpur", "Hassan Abdal", "Hattar", "Haveli Lakha", "Havelian",
        "Hazro", "Hingorja", "Hujra Shah Muqeem", "Hyderabad", "Islamabad", "Islamkot", "Jacobabad", "Jahanian",
        "Jalalpur",
        "Jalalpur Jattan", "Jalalpur Pirwala", "Jamshoro", "Jampur", "Jamrud", "Jaranwala", "Jati", "Jatoi",
        "Jauharabad",
        "Jhang", "Jhawarian", "Jhelum", "Jhol", "Jhuddo", "Jiwani", "Johi", "Kabirwala", "Kacha Khooh", "Kahror Pakka",
        "Kakul", "Kalabagh", "Kalabagh", "Kalat", "Kalur Kot", "Kamalia", "Kamber Ali Khan", "Kamina", "Kamoke",
        "Kandhkot",
        "Kandiaro", "Karak", "Karor Lal Esan", "Karachi", "Kashmore", "Kasur", "Khairpur", "Khairpur Mir's",
        "Khan Bela",
        "Khan Garh", "Khanewal", "Khangarh", "Khanpur", "Khanpur Maher", "Kharan", "Kharian", "Khewra", "Khurrianwala",
        "Khushab", "Khuzdar", "Khyber", "Kohat", "Kohlu", "Kot Abdul Malik", "Kot Addu", "Kot Mithan", "Kot Mumin",
        "Kot Radha Kishan", "Kot Samaba", "Kot Sultan", "Kotli", "Kotli Loharan", "Kotri", "Kulachi", "Kundian",
        "Kunjah",
        "Kunri", "Lachi", "Lahore", "Lakki Marwat", "Lalamusa", "Larkana", "Layyah", "Liliani", "Lodhran", "Loralai",
        "Mach", "Mailsi", "Malakwal", "Mamoori", "Mananwala", "Mandi Bahauddin", "Mandi Faizabad", "Manga Mandi",
        "Mangla",
        "Mankera", "Mansehra", "Mardan", "Mastung", "Matiari", "Matli", "Mauping", "Mehar", "Mehrabpur", "Mian Channu",
        "Mianwali", "Mianwali Bangla", "Miani", "Miro Khan", "Mirpur", "Mirpur Khas", "Mirpur Mathelo", "Mithi",
        "Moenjo Daro",
        "Mong", "Moro", "Multan", "Muridke", "Murree", "Mustafabad", "Muzaffargarh", "Muzaffarabad", "Nabisar Road",
        "Nankana Sahib", "Narowal", "Naudero", "Naukot", "Nawabshah", "Nazimabad", "Nek Muhammad Wala", "New Mirpur",
        "Nowshera", "Nowshera Virkan", "Nurpur Noon", "Okara", "Ormara", "Pad Idan", "Paharpur", "Pakpattan", "Panjgur",
        "Pano Akil", "Parachinar", "Pasni", "Pattoki", "Peshawar", "Phalia", "Pind Dadan Khan", "Pindigheb",
        "Pir Mahal",
        "Pirmahal", "Pishin", "Qadirpur Ran", "Qazi Ahmad", "Quetta", "Rahim Yar Khan", "Raiwind", "Rajanpur",
        "Rajo Khanani",
        "Ranipur", "Rangoo", "Rangpur", "Ranipur Riyasat", "Rasulnagar", "Rawalakot", "Rawalpindi", "Renala Khurd",
        "Risalpur",
        "Rohri", "Rojhan", "Rustam", "Sadiqabad", "Sahiwal", "Sakrand", "Sambrial", "Samma Satta", "Samundri",
        "Sanghar",
        "Sangla Hill", "Sanjwal", "Sann", "Sarai Alamgir", "Sarai Naurang", "Sarai Saleh", "Sargodha", "Sehwan",
        "Setharja",
        "Shabqadar", "Shahdadkot", "Shahdadpur", "Shahpur", "Shahpur Chakar", "Shahpur Sadar", "Shakargarh",
        "Sheikhupura",
        "Shikarpur", "Shujaabad", "Sialkot", "Sibi", "Sillanwali", "Sita Road", "Sodhra", "Sohawa", "Sukkur", "Swabi",
        "Swat", "Takht Bhai", "Talagang", "Talhar", "Tando Adam", "Tando Allahyar", "Tando Jam", "Tando Muhammad Khan",
        "Tangwani", "Tank", "Taunsa", "Taxila", "Thatta", "Thul", "Timergara", "Toba Tek Singh", "Topi", "Turbat",
        "Ubaro", "Uch Sharif", "Umerkot", "Upper Dir", "Usta Mohammad", "Vehari", "Vihari", "Wah", "Warah", "Warburton",
        "Wazirabad", "Winder", "Yazman", "Zafarwal", "Zahir Pir", "Zhob", "Ziarat"
    ]
    men = [
        "Aamir", "Abbas", "Abdul", "Abdullah", "Abid", "Abrar", "Adam", "Adil", "Adnan", "Afzal",
        "Ahmad", "Ahmed", "Ahsan", "Ajmal", "Akbar", "Akhtar", "Alauddin", "Ali", "Amir", "Ammar",
        "Amjad", "Anas", "Anees", "Anwar", "Arif", "Arslan", "Asad", "Asghar", "Ashfaq", "Ashraf",
        "Asif", "Ata", "Atif", "Awais", "Ayan", "Azeem", "Azhar", "Aziz", "Babar", "Bashir",
        "Bilal", "Burhan", "Danish", "Dawood", "Ehsan", "Ejaz", "Emad", "Faheem", "Faisal", "Faraz",
        "Farhan", "Farrukh", "Fawad", "Feroz", "Furqan", "Ghaffar", "Ghalib", "Ghaus", "Ghulam", "Habib",
        "Haider", "Hamid", "Hamza", "Hanif", "Haroon", "Hashim", "Hasnain", "Hassan", "Hussain", "Ibrahim",
        "Idris", "Iftikhar", "Imad", "Imran", "Inam", "Iqbal", "Irshad", "Irtaza", "Ishtiaq", "Ishaq",
        "Ismail", "Jabbar", "Jafar", "Jamal", "Jawad", "Junaid", "Kabir", "Kaleem", "Kamran", "Kashif",
        "Kazim", "Khalid", "Khizar", "Khurshid", "Latif", "Luay", "Luqman", "Mansoor", "Masood", "Mateen",
        "Mehmood", "Miftah", "Mikael", "Mirza", "Moazzam", "Moeen", "Mohammad", "Mohammed", "Moin", "Momin",
        "Mubashir", "Mudasir", "Mufti", "Muhammad", "Mukhtar", "Munir", "Murtaza", "Mushtaq", "Mustafa", "Nabeel",
        "Nadeem", "Naeem", "Najeeb", "Najib", "Naseem", "Nasir", "Nawaz", "Nazar", "Nazim", "Nisar",
        "Noman", "Numan", "Nusrat", "Omar", "Osama", "Parvez", "Qadeer", "Qadir", "Qasim", "Rafi",
        "Rafiq", "Rahim", "Raheel", "Rameez", "Rashid", "Rauf", "Rayyan", "Rehan", "Riaz", "Rizwan",
        "Saad", "Saeed", "Safi", "Sajid", "Sajjad", "Salman", "Sami", "Saqib", "Sarfaraz", "Shabbir",
        "Shadab", "Shafi", "Shafqat", "Shahid", "Shakeel", "Shakil", "Shamim", "Shan", "Sharif", "Shehzad",
        "Sheraz", "Shibli", "Shoaib", "Sikandar", "Sohail", "Sultan", "Talha", "Tariq", "Tayyab", "Tufail",
        "Umair", "Umar", "Usama", "Usman", "Waqas", "Wasim", "Yahya", "Yasir", "Yousaf", "Yusuf",
        "Zafar", "Zahid", "Zain", "Zaheer", "Zakir", "Zubair", "Zulfiqar", "Abdulaziz", "Abdulbaqi", "Abdulbari",
        "Abdulfattah", "Abdulkadir", "Abdulkareem", "Abdullah", "Abdulmohsen", "Abdulrahman", "Abdulrahim",
        "Abdulrashid", "Abdurahman", "Abdussalam",
        "Abid", "Abu", "Adel", "Adham", "Adil", "Adnan", "Afif", "Ahmad", "Aiman", "Ajmal",
        "Akeem", "Alaa", "Ali", "Ameen", "Amjad", "Amro", "Anas", "Anees", "Aqeel", "Arafat",
        "Areeb", "Arfan", "Arif", "Arkan", "Arman", "Arshad", "Asad", "Ashfaq", "Ashraf", "Asif",
        "Aslam", "Ata", "Atif", "Ayman", "Ayyub", "Ayaz", "Azam", "Azeem", "Azfar", "Azhar",
        "Aziz", "Badar", "Baha", "Baqir", "Bashir", "Bilal", "Burhan", "Dawood", "Dhiya", "Dilawar",
        "Ehsan", "Elahi", "Elias", "Emad", "Emran", "Essa", "Eyman", "Fadi", "Fadil", "Fahad",
        "Fahim", "Faizan", "Fakhruddin", "Faraz", "Fareed", "Farhan", "Farrukh", "Fawad", "Fawzi", "Fayez",
        "Feroz", "Fuad", "Furqan", "Ghaith", "Ghazi", "Ghulam", "Habib", "Hafeez", "Hafiz", "Haider",
        "Hameed", "Hamid", "Hamza", "Hanif", "Harith", "Haroon", "Haseeb", "Hashim", "Hassan", "Hatem",
        "Hussain", "Hussam", "Ibrahim", "Idris", "Iftikhar", "Ihsan", "Ikram", "Imad", "Imran", "Irfan",
        "Irtaza", "Isam", "Ishtiaq", "Ismail", "Jabbar", "Jafar", "Jamal", "Jawad", "Jibril", "Junaid",
        "Kabeer", "Kamal", "Kamran", "Karam", "Kashif", "Khaled", "Khalid", "Khaleel", "Khayyam", "Khurram",
        "Latif", "Luqman", "Majeed", "Mansoor", "Marwan", "Masood", "Mateen", "Mehdi", "Mehmood", "Moin",
        "Moiz", "Mohammad", "Mohammed", "Momin", "Mudassar", "Mueen", "Mujahid", "Mukhtar", "Munir", "Murtaza",
        "Mustafa", "Nabeel", "Nadeem", "Naeem", "Najeeb", "Najib", "Naseem", "Nasir", "Nawaz", "Nazir",
        "Nisar", "Noman", "Numan", "Nusrat", "Omar", "Osama", "Parvez", "Qadir", "Qasim", "Qays",
        "Rafi", "Rafiq", "Raheel", "Rahim", "Raouf", "Rashid", "Rauf", "Rayyan", "Rehan", "Riaz",
        "Rizwan", "Saad", "Saeed", "Safi", "Sajid", "Sajjad", "Salman", "Sami", "Saqib", "Sarfaraz",
        "Shabbir", "Shadab", "Shafi", "Shafqat", "Shahid", "Shakeel", "Shakil", "Shamim", "Shan", "Sharif",
        "Shehzad", "Sheraz", "Shibli", "Shoaib", "Sikandar", "Sohail", "Sultan", "Talha", "Tariq", "Tayyab",
        "Tufail", "Umair", "Umar", "Usama", "Usman", "Waqas", "Wasim", "Yahya", "Yasir", "Yousaf",
        "Yusuf", "Zafar", "Zahid", "Zain", "Zaheer", "Zakir", "Zubair", "Zulfiqar"
    ]

    women = [
        "Aaliyah", "Aasma", "Abeer", "Abida", "Adeela", "Aeesha", "Afifa", "Afnan", "Afsana", "Ayesha",
        "Ahlam", "Aisha", "Aleena", "Aliya", "Amal", "Amara", "Ambreen", "Amina", "Aminah", "Amna",
        "Anam", "Anisa", "Anusha", "Arfa", "Arisha", "Arwa", "Asifa", "Asma", "Ayesha", "Aziza",
        "Badia", "Basma", "Batool", "Bibi", "Bilqis", "Bushra", "Dania", "Daniah", "Dilshad", "Duaa",
        "Durrah", "Emaan", "Eman", "Erum", "Esma", "Farah", "Fareeha", "Farida", "Fatema", "Fatemah",
        "Fatima", "Fatimah", "Fauzia", "Fawzia", "Fiza", "Fouzia", "Ghazala", "Gul", "Gulzar", "Habiba",
        "Hafsa", "Hafsah", "Haifa", "Haleema", "Hanan", "Hania", "Haniya", "Hanin", "Haseena", "Hawa",
        "Heba", "Hina", "Hira", "Huda", "Humaira", "Husna", "Ibtisam", "Iffat", "Ihsan", "Ikram",
        "Ilham", "Inaya", "Iqra", "Irsa", "Irum", "Isha", "Jameela", "Jamila", "Javeria", "Jihan",
        "Juwairiyah", "Khadija", "Khadijah", "Khalida", "Kiran", "Kulsoom", "Kulthum", "Laila", "Laiba", "Lina",
        "Lubna", "Luqma", "Maheen", "Mahira", "Mahnoor", "Maira", "Malaika", "Maliha", "Marwa", "Maryam",
        "Meher", "Mehreen", "Mina", "Mishal", "Mishkat", "Mona", "Mubeena", "Mumtaz", "Munira", "Munni",
        "Nabila", "Nadia", "Nadine", "Nafisa", "Naila", "Naima", "Najat", "Najma", "Nargis", "Nashwa",
        "Nasreen", "Nazia", "Nelofer", "Nida", "Nigar", "Nihal", "Nimra", "Noreen", "Nuha", "Nusrat",
        "Nuzhat", "Omaima", "Parveen", "Qamar", "Quratulain", "Rabia", "Rafia", "Rafiah", "Rafia", "Raja",
        "Ramla", "Rania", "Raniyah", "Rashida", "Razia", "Reema", "Rida", "Rimsha", "Rina", "Roma",
        "Rosa", "Rubab", "Rubeena", "Rubina", "Ruhina", "Rukhsana", "Ruqayyah", "Saadia", "Saba", "Sabeen",
        "Sabina", "Sabira", "Sabreen", "Sadaf", "Sadia", "Safa", "Safiya", "Sahar", "Sahira", "Saima",
        "Saira", "Sakina", "Salma", "Sameena", "Samia", "Samina", "Sana", "Sanam", "Sania", "Sara",
        "Sariyah", "Saba", "Shabana", "Shaista", "Shakira", "Shama", "Shamim", "Shanaz", "Shazia", "Sheema",
        "Shehla", "Shereen", "Shifa", "Shireen", "Shirin", "Sobia", "Sohaila", "Sonia", "Soraya", "Sumaiya",
        "Sumaya", "Sundus", "Suraiya", "Suriya", "Tabassum", "Tahira", "Taiba", "Tala", "Tamanna", "Tania",
        "Tasneem", "Uzma", "Wafa", "Wajiha", "Warda", "Wasila", "Yasmin", "Yasmine", "Yusra", "Zainab",
        "Zakia", "Zainab", "Zainab", "Zakia", "Zakiyah", "Zamzam", "Zara", "Zehra", "Zeinab", "Zohra",
        "Zoya", "Zubeida", "Zulekha", "Zunaira", "Aafreen", "Aala", "Aalya", "Aaminah", "Aatika", "Aatiya",
        "Aayat", "Abeer", "Adeeba", "Adeelah", "Adiba", "Adila", "Afifah", "Afra", "Afsar", "Afyah",
        "Ahana", "Ahmara", "Aida", "Ailah", "Aiman", "Aini", "Aira", "Akifah", "Aksa", "Alaya",
        "Aleemah", "Alina", "Alishba", "Almas", "Almaas", "Alvina", "Ambar", "Ameena", "Amirah", "Amra",
        "Amreen", "Ana", "Anan", "Anayah", "Andleeb", "Aniqa", "Anjum", "Ansha", "Anwaar", "Aqsa",
        "Arfa", "Arisha", "Arub", "Arwa", "Asbah", "Ashra", "Asiyah", "Atika", "Atiya", "Azhar",
        "Azizah", "Badriya", "Bahar", "Balqis", "Barkah", "Bashira", "Basimah", "Batool", "Benazir", "Bibiana",
        "Bishara", "Bisma", "Bushra", "Daisha", "Dalia", "Dania", "Daniah", "Danya", "Deeba", "Delara",
        "Dilara", "Durra", "Eesha", "Eilia", "Eliza", "Emira", "Emra", "Erum", "Eshaal", "Eshal",
        "Ezza", "Fadia", "Fadilah", "Faheema", "Faiqa", "Faiqah", "Faiza", "Faizah", "Falak", "Fara",
        "Fareena", "Farha", "Farhana", "Farida", "Fariha", "Fariya", "Fauzia", "Fawzia", "Ferhana", "Fiza",
        "Fouzia", "Gehan", "Ghadah", "Ghazala", "Ghazal", "Ghina", "Gul", "Gulalai", "Gulbano", "Habeeba",
        "Hafsa", "Hajrah", "Hajira", "Hala", "Haleema", "Hamida", "Hanaa", "Hanifa", "Hani", "Hania",
        "Haniyah", "Haniya", "Hannah", "Hasna", "Hawra"
    ]
    product_categories = [
    "Electronics", "Clothing", "Home & Kitchen", "Books", "Toys & Games",
    "Beauty & Personal Care", "Sports & Outdoors", "Automotive", "Health & Wellness",
    "Grocery & Gourmet Food", "Office Products", "Pet Supplies", "Tools & Home Improvement",
    "Musical Instruments", "Furniture", "Jewelry", "Shoes", "Watches",
    "Baby", "Outdoor Recreation", "Luggage & Travel", "Fitness & Exercise",
    "Home Decor", "Crafts & Hobbies", "Party Supplies"
    ]

    category_products = {
        "Electronics": [
            "Blender", "Microwave", "Refrigerator", "Washing Machine", "Vacuum Cleaner",
            "Television", "Computer", "Laptop", "Tablet", "Smartphone",
            "Speaker", "Headphones", "Camera", "Drone", "Projector",
            "Gaming Console", "Virtual Reality Headset", "Smartwatch", "Fitness Tracker",
            "Smart Home Hub", "Wireless Earbuds", "Portable Charger", "Gaming Mouse", "Keyboard"
        ],
        "Clothing": [
            "Shirt", "Pants", "Dress", "Skirt", "Jacket",
            "Sweater", "Shoes", "Boots", "Sandals", "Hat",
            "Underwear", "Socks", "Jewelry", "Scarf", "Sunglasses",
            "Swimwear", "Activewear", "Sleepwear", "Cosplay Costume",
            "Pajamas", "Leggings", "T-Shirt", "Dress Pants", "Formal Dress"
        ],
        "Home & Kitchen": [
            "Pots and Pans", "Dishes", "Flatware", "Utensils", "Cutlery Sets",
            "Coffee Maker", "Toaster", "Blender", "Food Processor", "Microwave",
            "Stove", "Oven", "Refrigerator", "Freezer", "Dishwasher",
            "Vacuum Cleaner", "Iron", "Ironing Board", "Trash Can", "Storage Containers",
            "Mixing Bowls", "Measuring Cups", "Knives", "Cutting Board", "Can Opener"
        ],
        "Books": [
            "The Lord of the Rings", "Jane Eyre", "Animal Farm", "Brave New World", "The Iliad",
            "Crime and Punishment", "Wuthering Heights", "Great Expectations", "The Divine Comedy",
            "A Tale of Two Cities",
            "Les Misérables", "The Brothers Karamazov", "Catch-22", "The Grapes of Wrath", "Slaughterhouse-Five",
            "The Adventures of Huckleberry Finn", "The Count of Monte Cristo", "Gone with the Wind", "Don Quixote",
            "The Scarlet Letter",
            "One Hundred Years of Solitude", "The Picture of Dorian Gray", "Dracula", "Madame Bovary", "Frankenstein",
            "The Metamorphosis", "Sense and Sensibility", "Anna Karenina", "A Clockwork Orange", "Heart of Darkness",
            "The Stranger", "Ulysses", "East of Eden", "A Farewell to Arms", "Rebecca",
            "Lord of the Flies", "The Shining", "The Road", "The Old Man and the Sea", "Lolita",
            "Beloved", "Middlemarch", "The Wind in the Willows", "The Call of the Wild", "Dune",
            "The Sun Also Rises", "Of Mice and Men", "The Name of the Rose", "The Secret Garden", "The Handmaid's Tale",
            "The Alchemist", "The Book Thief", "Life of Pi", "The Girl with the Dragon Tattoo", "Memoirs of a Geisha",
            "The Time Traveler's Wife", "The Help", "Water for Elephants", "The Hunger Games", "The Fault in Our Stars",
            "Twilight", "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets",
            "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire",
            "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince",
            "Harry Potter and the Deathly Hallows", "The Maze Runner", "Divergent",
            "The Giver", "Ender's Game", "Ready Player One", "The Chronicles of Narnia",
            "The Hitchhiker's Guide to the Galaxy",
            "The Martian", "A Game of Thrones", "American Gods", "The Road to Serfdom",
            "Sapiens: A Brief History of Humankind",
            "Educated", "Becoming", "Steve Jobs", "The Wright Brothers", "Unbroken",
            "Into the Wild", "Quiet: The Power of Introverts in a World That Can't Stop Talking",
            "Thinking, Fast and Slow", "Outliers: The Story of Success", "Grit: The Power of Passion and Perseverance"
        ],
        "Toys & Games": [
            "Action Figure", "Doll", "Board Game", "Card Game", "Puzzle",
            "Building Set", "Stuffed Animal", "Remote Control Car", "Art Set", "Musical Instrument (Toy)",
            "Sports Equipment (Toy)", "Dress-Up Clothes (Toy)", "Slime Kit", "Science Kit", "Legos",
            "Play Kitchen", "Play Tent", "Building Blocks", "Educational Toy", "Board Game (Classic)"
        ],
        "Beauty & Personal Care": [
            "Shampoo", "Conditioner", "Soap", "Lotion", "Body Wash",
            "Makeup", "Skincare", "Haircare", "Fragrance", "Shaving Supplies",
            "Nail Care", "Dental Care", "Bath Products", "Men's Grooming", "Cosmetics",
            "Makeup Brushes", "Hair Styling Tools", "Sunblock", "Deodorant", "Moisturizer"
        ],
        "Sports & Outdoors": [
            "Basketball", "Baseball", "Football", "Soccer Ball", "Tennis Racket",
            "Golf Club", "Bicycle", "Camping Tent", "Sleeping Bag", "Hiking Boots",
            "Fishing Rod", "Kayak", "Swimsuit", "Sunscreen", "Water Bottle",
            "Yoga Mat", "Fitness Tracker (watch)", "Sports Apparel", "Camping Stove", "Tent Lamp"
        ],
        "Automotive": [
            "Car Battery", "Engine Oil", "Tires", "Windshield Wipers", "Floor Mats",
            "Car Seat", "Headlights", "Tail Lights", "Car Wash Kit", "Jump Starter",
            "GPS Navigation", "Dash Cam", "Car Vacuum Cleaner", "Air Freshener", "Car Cover",
            "Windshield Washer Fluid", "Brake Pads", "Antifreeze", "Oil Filter", "Car Wax"
        ],
        "Health & Wellness": [
            "Vitamins", "Pain Relief Medication", "Allergy Medication", "Cold & Flu Medication", "First-Aid Kit",
            "Paper Towels", "Toilet Paper", "Trash Bags", "Cleaning Supplies", "Laundry Detergent",
            "Dish Soap", "Sponges", "Air Purifier", "Humidifier", "Thermometer"
        ],
        "Musical Instruments": [
            "Guitar", "Piano", "Violin", "Drums", "Flute",
            "Trumpet", "Saxophone", "Clarinet", "Keyboard", "Microphone",
            "Amplifier", "Speaker", "Music Stand", "Metronome", "Tuner"
        ],
        "Furniture": [
            "Sofa", "Bed", "Dining Table", "Coffee Table", "Desk",
            "Chair", "Wardrobe", "Bookshelf", "Cabinet", "Dresser",
            "Nightstand", "Futon", "TV Stand", "Ottoman", "Bean Bag Chair"
        ],
        "Jewelry": [
            "Necklace", "Earrings", "Bracelet", "Ring", "Pendant",
            "Anklet", "Brooch", "Charm", "Cufflinks", "Watch",
            "Body Jewelry", "Jewelry Box", "Jewelry Cleaner", "Jewelry Display", "Pearls"
        ],
        "Shoes": [
            "Sneakers", "Boots", "Sandals", "Heels", "Flats",
            "Loafers", "Oxfords", "Espadrilles", "Slippers", "Athletic Shoes",
            "Hiking Boots", "Dress Shoes", "Work Boots", "Platform Shoes", "Wedge Sandals"
        ],
        "Watches": [
            "Analog Watch", "Digital Watch", "Smartwatch", "Sports Watch", "Dress Watch",
            "Chronograph Watch", "Automatic Watch", "Mechanical Watch", "Skeleton Watch", "Pocket Watch",
            "Fitness Tracker (watch)", "Dive Watch", "Pilot Watch", "Field Watch", "Racing Watch"
        ],
        "Baby": [
            "Diapers", "Baby Wipes", "Baby Food", "Baby Bottles", "Pacifiers",
            "Baby Clothes", "Baby Shoes", "Baby Blankets", "Baby Carrier", "Baby Monitor",
            "Stroller", "Car Seat", "High Chair", "Baby Toys", "Baby Books"
        ],
        "Outdoor Recreation": [
            "Camping Tent", "Sleeping Bag", "Hiking Backpack", "Backpack", "Sleeping Pad",
            "Camp Stove", "Lantern", "Flashlight", "Camp Chair", "Cooler",
            "Hammock", "Outdoor Table", "Folding Chair", "Portable Grill", "Water Purifier"
        ],
        "Luggage & Travel": [
            "Suitcase", "Carry-On Bag", "Duffel Bag", "Backpack", "Weekender Bag",
            "Garment Bag", "Laptop Bag", "Tote Bag", "Travel Organizer", "Packing Cubes",
            "Travel Pillow", "Travel Adapter", "Luggage Scale", "Passport Holder", "Luggage Tag"
        ],
        "Fitness & Exercise": [
            "Dumbbells", "Kettlebell", "Resistance Bands", "Yoga Mat", "Exercise Ball",
            "Jump Rope", "Foam Roller", "Exercise Bike", "Treadmill", "Elliptical Machine",
            "Rowing Machine", "Weight Bench", "Pull-Up Bar", "Punching Bag", "Boxing Gloves"
        ],
        "Home Decor": [
            "Wall Art", "Picture Frame", "Vase", "Candle Holder", "Sculpture",
            "Mirrors", "Rug", "Throw Blanket", "Throw Pillow", "Curtains",
            "Clock", "Decorative Tray", "Decorative Bowls", "Artificial Plants", "Lamp"
        ],
        "Crafts & Hobbies": [
            "Painting Supplies", "Sketchbook", "Drawing Pencils", "Watercolor Paints", "Acrylic Paints",
            "Oil Paints", "Canvas", "Easel", "Sculpting Clay", "Pottery Wheel",
            "Knitting Needles", "Yarn", "Cross Stitch Kit", "Model Kit", "Jigsaw Puzzle"
        ],
        "Party Supplies": [
            "Balloons", "Party Hats", "Party Decorations", "Streamers", "Confetti",
            "Tableware", "Disposable Cups", "Plates", "Napkins", "Cutlery",
            "Tablecloth", "Party Favors", "Pinata", "Cake Toppers", "Party Games"
        ],
        "Grocery & Gourmet Food": [
            "Bread", "Milk", "Eggs", "Cheese", "Butter",
            "Fresh Fruits", "Fresh Vegetables", "Meat", "Poultry", "Seafood",
            "Cereal", "Snacks", "Beverages", "Canned Goods", "Condiments",
            "Pasta", "Rice", "Beans", "Baking Ingredients", "Frozen Foods"
        ],
        "Office Products": [
            "Pens", "Pencils", "Notebooks", "Binders", "File Folders",
            "Stapler", "Staples", "Scissors", "Tape", "Glue",
            "Desk Organizer", "Calendar", "Whiteboard", "Markers", "Highlighters",
            "Printer Paper", "Ink Cartridges", "Desk Chair", "Desk Lamp", "Shredder"
        ],
        "Pet Supplies": [
            "Dog Food", "Cat Food", "Dog Treats", "Cat Treats", "Dog Toy pack",
            "Cat Toys pack", "Pet Bed", "Pet Crate", "Leash", "Collar",
            "Pet Carrier", "Pet Brush", "Pet Shampoo", "Litter Box", "Fish Tank",
            "Bird Cage", "Hamster Wheel", "Rabbit Hutch", "Reptile Terrarium"
        ],
        "Tools & Home Improvement": [
            "Hammer", "Screwdriver Set", "Wrench Set", "Pliers", "Tape Measure",
            "Level", "Utility Knife", "Flashlight", "Toolbox", "Power Drill",
            "Circular Saw", "Sander", "Paintbrush Set", "Roller", "Drop Cloth",
            "Screws", "Nails", "Paint", "Caulk", "Wood Glue"
        ]
    }
    descriptions = [
        "Unleash the Power Of:",
        "Effortless Elegance:",
        "Innovation at Your Fingertips:",
        "Crafted for Performance:",
        "The Future is Here:",
        "Simplify Your Life:",
        "Experience the Difference:",
        "Built to Last:",
        "Your Gateway to:",
        "Level Up Your:",
        "Incredibly versatile ",
        "Luxuriously soft ",
        "Remarkably powerful ",
        "Seamlessly integrates with ",
        "Unbelievably comfortable ",
        "Ultra-portable and convenient ",
        "Stylish and functional ",
        "The perfect  ",
        "Elevate your everyday life with  ",
        "Discover the joy of  ",
        "Make a statement with ",
        "Take control of your ",
        "Live a more fulfilling life with ",
        "Memories made easy with ",
        "Get yours today!",
        "Upgrade your experience now with ",
        "Don't miss out, order now! :",
        "Limited time offer to get ",
        "Purchase here to learn more about :"
    ]

    towns = [
        "Johar Town", "Bahria Town", "DHA", "Ali Town", "Gulberg", "Model Town", "Iqbal Town",
        "Wapda Town", "Township", "Garden Town", "Faisal Town", "Shadman", "Sabzazar",
        "Samanabad", "Jubilee Town", "Valencia Town", "Pak Arab Housing Society",
        "Eden Gardens", "Jinnah Garden", "Margalla Town", "Green Town", "Chaklala Scheme",
        "Banigala", "Satellite Town", "Peshawar Town", "G-13", "G-14", "F-10", "F-11",
        "G-9", "G-8", "G-7", "G-6", "F-6", "F-7", "I-8", "I-9", "I-10", "I-11",
        "Khayaban-e-Amin", "Bahria Enclave", "Soan Gardens", "Naval Anchorage",
        "Gulistan-e-Jauhar", "Defence View", "Korangi Town", "Nazimabad", "North Nazimabad",
         "Buffer Zone", "Surjani Town", "Orangi Town", "Liaquatabad",
        "Gulshan-e-Iqbal", "Gulshan-e-Maymar", "Scheme 33", "Malir Town",
        "Shah Faisal Town", "Landhi Town", "Korangi Creek Cantonment", "Askari 1",
        "Askari 2", "Askari 3", "Askari 4", "Askari 5", "Askari 6", "Askari 7",
        "Askari 8", "Askari 9", "Askari 10", "Askari 11", "Gulshan-e-Ravi",
        "Gulshan-e-Hadeed", "Johar Abad", "Westridge", "Adiala Road", "Chakri Road",
        "Shalimar Town", "Saddar Town", "Cantt", "Garrison", "Blue Area", "Diplomatic Enclave",
        "Gulzar-e-Quaid", "Kuri Road", "Pindi Gheb", "Murree Brewery", "Ghouri Town",
        "PWD Colony", "Media Town", "Bhara Kahu", "Margalla Hills", "Fateh Jang",
        "H-8", "H-9", "H-10", "F-8", "F-5", "G-5", "G-10", "G-11", "G-12", "F-12",
        "E-11", "E-12", "D-12", "C-15", "C-16", "B-17", "A-18",
        "Rawat", "Rawal Town", "Faizabad", "New City", "Jinnah Town", "Gulberg Greens",
        "Lalazar", "Ayub Park", "Phase 8", "Phase 7", "Phase 6", "Phase 5",
        "Phase 4", "Phase 3", "Phase 2", "Phase 1"
    ]


    def total_products():
        total_products = 0
        for category, products in category_products.items():
            total_products += len(products)
        return total_products

    def insert_reg_user(name, email, password, phone_number,gender,country,city,postalcode,address):
        cursor.execute( "INSERT INTO registered_users(name, email, password,  phone_number,gender,country,city,postal_code,street_address) VALUES (  ?, ?, ?, ?,?,?,?,?,?)", (name, email, password,  phone_number,gender,country,city,postalcode,address))
        conn.commit()

    def insert_nonreg_user(cookie,name):
        cursor.execute("INSERT INTO non_registered_users(name,cookie) VALUES (?,?)", (name, cookie))
        conn.commit()

    def insert_prodcut_Category(name):
        cursor.execute( "INSERT INTO product_categories(category_name) VALUES (?)", (name))
        conn.commit()


    def insert_pre_booking(user_id, product_id,date):
        cursor.execute("exec prebookingpro  @user_id =?,  @product_id =?, @date=?",
                       ( user_id, product_id,date))
        conn.commit()

    def insert_retailers(retailer_name,phone ):
        cursor.execute(
            "INSERT INTO retailers (name, phone) VALUES (?, ?)",
            ( retailer_name,phone))
        conn.commit()


    def insert_customer_support_ticket( user_id, issue,status):
        cursor.execute("INSERT INTO customer_support_tickets ( user_id, issue,status) VALUES (?, ?, ?)",
                       ( user_id, issue,status))
        conn.commit()


    def insert_reviews(user_id, product_id, rating, review_text):
        cursor.execute("exec insertreviews  @product_id =?,@user_id =?, @rating =?,@review=?", (product_id,user_id, rating, review_text))
        conn.commit()


    def insert_products(name,catid,description,price,rating):
        cursor.execute("insert into products values (?,?,?,?,?)",name,catid,description,price,rating)
        conn.commit()

    def insert_coupon (discount,start,end,limit):
        cursor.execute("insert into coupons(discount_percent,start_date,end_date,limit) values (?,?,?,?)",discount,start,end,limit)
        conn.commit()

    def insert_shipping_method(method ,fees):
        cursor.execute("insert into shipping values (?,?)",method ,fees)
        conn.commit()

    def insert_rb_fill_inv(p_id,r_id,quantity,discount,date):
      cursor.execute("exec add_retailerbill_fill_inventory @product_id =?, @retailer_id =?, @quantity =?, @discount= ?,@date=?",p_id,r_id,quantity,discount,date)
      conn.commit()

    def insert_payment(orderid,date):
        cursor.execute("exec add_payments  @order_id =?,  @date=? ",orderid,date)
        conn.commit()

    def insert_cart(userid,cookie,total,date):
       if cookie=='null':
         cursor.execute("insert into cart(user_id ,total,date) values (?,?,?)",userid,total,date)
       elif userid=='null' :
         cursor.execute("insert into cart(cookie,total) values (?,?,?)", cookie, total,date)
         conn.commit()
       cursor.execute('select top 1 cart_id from cart order by cart_id desc ')
       id = cursor.fetchone()[0]

       for alt in range(1,random.randint(1,12)+1):
            insert_cart_items(id,random.randint(1, total_products()),random.randint(1,20))

    def insert_cart_items(cartid,productid,quantity):
        cursor.execute("exec add_cart_items @cart_id=?, @product_id=?,@quantity=?",cartid,productid,quantity)
        conn.commit()

    def insert_refunds(userid,productid,orderid,quantity,reason,date):
        cursor.execute("exec refunds    @user_id =?,    @product_id =?, @order_id =?,@quantity =?, @reason =?,	@date=?",userid,productid,orderid,quantity,reason,date)
        conn.commit()

    def pakistaninumbergen():
        mobile_code = random.choice(['300', '301', '302', '303', '304', '305', '306', '307', '308', '309',
                                     '311', '312', '313', '314', '315', '316', '317', '318', '319',
                                     '321', '322', '323', '324', '331', '332', '333', '334', '335',
                                     '336', '337', '338', '339'])
        country_code = '+92'
        number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        return f"{country_code} {mobile_code} {number}"

    def add_1000_users():
     i= 0
     while i<500:
      try:
       name=random.choice(men)
       father=random.choice(men)
       fullname=name+" "+father
       email=name+father+str(i)+"@gmail.com"
       insert_reg_user(fullname,email,fake.password(),pakistaninumbergen(),'M','Pakistan',random.choice(pakistan_cities),fake.postalcode(),str(random.randint(0, 1000)) +' '+ random.choice(string.ascii_uppercase)+ ' Block '+random.choice(towns))
       i=i+1
      except Exception as e:
          continue

     i=0
     while i<100:
      try:
       insert_nonreg_user(random.randint(0, 100000)+i, fake.name())
      except Exception as e:
          continue
      i=i+1
     i=0
     while i<500:
      try:
       name = random.choice(women)
       father = random.choice(men)
       fullname = name + " " + father
       email = name + father + str(i) + "@gmail.com"
       insert_reg_user(fullname, email, fake.password(),pakistaninumbergen(), 'F', 'Pakistan',random.choice(pakistan_cities), fake.postalcode(), str(random.randint(0, 1000)) + ' ' + random.choice(string.ascii_uppercase) + ' Block '+random.choice(towns))
       i = i + 1
      except Exception as e:
       continue

    def add_products_and_Cats():
     alt=1;
     for name in product_categories:
       insert_prodcut_Category(name)


       for products in category_products[name]:
           insert_products(products,alt,random.choice(descriptions)+products, random.randint(500 // 5, 10000 // 5) * 5,5)
       alt=alt+1

    def add_100_retailers():
     i=0
     while i<100:
      insert_retailers(random.choice(men)+ " "+random.choice(men),pakistaninumbergen())
      i=i+1


    def fill_inventory_for_1_year(year):
      for date in getdate(year):
       insert_rb_fill_inv(random.randint(1,total_products()),random.randint(1,100),random.randint(10,100),random.randint(5,15),date)

    def data_prebookings(year):
            cursor.execute('SELECT COUNT(*) FROM registered_users')
            count = cursor.fetchone()[0]
            for date in getdate(year):
                try:
                 insert_pre_booking(random.randint(1,count), random.randint(1,total_products()), date)
                except Exception as e:
                 continue


    def fill_100_coupons(year):
      for alt in range(1,101):
         try:
             date = random.choice(getdate(year))
             enddate = fixenddate(date)
             insert_coupon(random.randint(5, 15), date, enddate, random.randint(5, 50))
         except Exception as e:
             continue



    def fixenddate(date) :
        arr = date.split('-')
        arr[1] = int(arr[1]) + 1
        if(arr[1]==13):
            arr[0] = int(arr[0]) + 1
        if arr[1] not in (1, 3, 5, 7, 8, 10, 12) and arr[2]=='31':
            arr[2]=int(arr[2])-1
        return str(arr[0])+ '-' + str(arr[1]) + '-' + str(arr[2])

    def getdate(year):
        alldates=[]
        month = 1;
        while month <= 12:
            days = 0
            if month in (1, 3, 5, 7, 8, 10, 12):
                days = 31
            elif month == 2:
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    days = 29
                else:
                    days = 28
            else:
                days = 30
            for day in range(1, days + 1):
              alldates.append(str(year) + "-" + str(month) + "-" + str(day))
            month = month + 1
        return alldates

    def fillshipping():
        shipping_data = {
            "Standard Shipping": 100,
            "Express Shipping": 500,
            "Overnight Shipping": 250,
            "International Shipping": 750,
            "Same Day Delivery": 200
        }
        for method,fees in shipping_data.items():
         insert_shipping_method(method,fees)


    def fill_300_reviews():
        reviews = [
            "Excellent quality and service.",
            "Very satisfied with my purchase.",
            "Exceeded my expectations.",
            "Will definitely recommend to others.",
            "Great value for the price.",
            "Very happy with the prompt delivery.",
            "Good product, but could be improved.",
            "Not as good as I hoped, but still decent.",
            "Customer service was very helpful.",
            "Overall, a great experience.",
            "Would buy again.",
            "Product arrived on time and as described.",
            "Affordable and reliable.",
            "Met my needs perfectly.",
            "I had a fantastic experience.",
            "Very pleased with this purchase.",
            "Quick and easy transaction.",
            "The quality is top-notch.",
            "Solid performance.",
            "Just what I was looking for.",
            "Highly recommend!",
            "Very convenient and useful.",
            "Satisfactory performance.",
            "Works as expected.",
            "User-friendly and intuitive.",
            "Simply amazing!",
            "Will buy more in the future.",
            "A must-have for everyone.",
            "I'm impressed with the quality.",
            "Worth every penny.",
            "Great find!",
            "Well made and durable.",
            "Absolutely love it!",
            "Five stars.",
            "Good, but not great.",
            "Reasonable price for the quality.",
            "Customer support was excellent.",
            "Very versatile and handy.",
            "Made my life easier.",
            "Not bad, but could be better.",
            "Pleased with the purchase.",
            "Fantastic deal!",
            "Just okay.",
            "Reliable and efficient.",
            "One of the best purchases I've made.",
            "I'm quite satisfied.",
            "Served its purpose well.",
            "Very happy with the results.",
            "Outstanding performance.",
            "Quality exceeded my expectations.",
            "I will buy it again.",
            "Very practical.",
            "Just what I needed.",
            "No complaints here.",
            "Everything I wanted.",
            "Top quality!",
            "It's okay.",
            "Not impressed.",
            "Good value for money.",
            "Easy to use and setup.",
            "Quite pleased with it.",
            "Pretty good overall.",
            "Works like a charm.",
            "Very durable.",
            "Does the job.",
            "Highly efficient.",
            "Very effective.",
            "So far, so good.",
            "I'm a satisfied customer.",
            "Fantastic quality.",
            "Decent and reliable.",
            "Exceptional service.",
            "Smooth transaction.",
            "Very functional.",
            "No issues at all.",
            "As advertised.",
            "A worthwhile investment.",
            "Does what it's supposed to.",
            "Happy with my purchase.",
            "Excellent choice.",
            "The quality is decent.",
            "It does what it needs to.",
            "Great for everyday use.",
            "Works perfectly.",
            "Good enough for me.",
            "Totally satisfied.",
            "It's fine.",
            "Great quality for the price.",
            "Fits my needs.",
            "Not the best, but not the worst.",
            "Surpassed my expectations.",
            "Excellent!",
            "Very pleased.",
            "All good.",
            "Just perfect!",
            "Not bad at all.",
            "Very useful.",
            "Decent quality.",
            "Outstanding!",
            "Great experience.",
            "No problems so far.",
            "I'm happy with it.",
            "Very good value.",
            "It works.",
            "Satisfied overall.",
            "Can't complain.",
            "Pretty satisfied.",
            "Lives up to the hype.",
            "I'm quite happy with it.",
            "Great purchase.",
            "Works great.",
            "Just what I expected.",
            "All around great product.",
            "No regrets.",
            "Solid purchase.",
            "I'm content.",
            "Thumbs up.",
            "Above average.",
            "Impressed!",
            "Couldn't be happier.",
            "Love it!",
            "I like it a lot.",
            "Does its job well.",
            "Quite good.",
            "Very reliable.",
            "Superb!",
            "Very nice.",
            "Pretty decent.",
            "Good overall.",
            "Exceptional quality.",
            "I'm pleased.",
            "Wonderful!",
            "Does the trick.",
            "Good performance.",
            "Great buy.",
            "It's alright.",
            "Meets expectations.",
            "Reasonably good.",
            "Fulfills its purpose.",
            "Great!",
            "Solid quality.",
            "Very satisfied.",
            "Really good.",
            "Worth it!",
            "Nice product.",
            "Pleased overall.",
            "Good and reliable.",
            "It's useful.",
            "Sturdy and dependable.",
            "Very good quality.",
            "Totally worth it.",
            "Impressive!",
            "Quite reliable.",
            "Better than expected.",
            "Very decent.",
            "A good deal.",
            "Quite satisfactory.",
            "Very solid.",
            "All good here.",
            "Simply the best.",
            "Very happy.",
            "Can't go wrong with it.",
            "Love the quality.",
            "Dependable.",
            "No issues.",
            "Works as described.",
            "Nice and sturdy.",
            "Highly recommend it.",
            "Super useful.",
            "Well worth the price.",
            "Good experience.",
            "Fantastic!",
            "Completely satisfied.",
            "I'm enjoying it.",
            "Good for the price.",
            "I'm pleased with it.",
            "Well done.",
            "It met my expectations.",
            "Great for the price.",
            "Very happy with it.",
            "Impressed with the quality.",
            "Very handy.",
            "No disappointments.",
            "A great find.",
            "Definitely recommend.",
            "Happy with it.",
            "It's great.",
            "Works well.",
            "Quality is good.",
            "Good buy.",
            "Nice and reliable.",
            "Love the performance.",
            "Well worth it.",
            "Great investment.",
            "Pretty good.",
            "Very useful and practical.",
            "Fantastic product.",
            "Good quality.",
            "Works just fine.",
            "Very sturdy.",
            "Happy customer.",
            "Reliable quality.",
            "Excellent service.",
            "Totally happy with it.",
            "Great quality.",
            "Useful and practical.",
            "Top-notch!",
            "Outstanding product.",
            "Quality product.",
            "Very effective and efficient.",
            "It works great.",
            "Very happy indeed.",
            "Quality meets expectations.",
            "No complaints.",
            "Excellent value.",
            "Love this product.",
            "Very good product.",
            "No issues whatsoever.",
            "Good overall quality.",
            "Nice quality.",
            "Perfect quality.",
            "Highly pleased.",
            "Completely happy.",
            "Works as intended."]
        cursor.execute('SELECT COUNT(*) FROM registered_users')
        count = cursor.fetchone()[0]
        for alt in range(1,301):
            insert_reviews(random.randint(1,count),random.randint(1,total_products()),random.randint(1,5),random.choice(reviews))


    def fill_1year_cart(year):
        cursor.execute('SELECT COUNT(*) FROM registered_users')
        count = cursor.fetchone()[0]
        for date in getdate(year):
                insert_cart(random.randint(1, count), 'null', 0,date)
                insert_cart(random.randint(1, count), 'null', 0, date)
                try:
                 insert_cart('null',random.choice(1000,10000),0,date)
                except Exception as e:
                    continue


    def shift_cart_order(userid,shippingid,couponid,paymethod):
        cursor.execute("exec shift_to_order_from_cart @userid =?,@shippingid =?,@couponid =?,@paymentmethod=?",userid,shippingid,couponid,paymethod)
        conn.commit()

    def fill_500_orders():
      cursor.execute('SELECT user_id,cart_id FROM cart')
      carts=cursor.fetchall()
      cursor.execute('select coupon_id,limit from coupons')
      coupons = cursor.fetchall()
      methods=['Credit Card','Cash on delievery']
      for alt in range(1,501):
        cart=random.choice(carts)
        coupon=random.choice(coupons)
        shift_cart_order(cart[0],random.randint(1,5),coupon[0],random.choice(methods))

    def fill500payments():
        cursor.execute(' select  order_id, date, user_id   from orders')
        orders = cursor.fetchall()
        for alt in range(1,501):
         order=random.choice(orders)
         insert_payment(order[0],order[1])


    def fill_500_customer_issues():
        cursor.execute('SELECT COUNT(*) FROM registered_users')
        count = cursor.fetchone()[0]
        status=['Resolved','In Queue']
        category_issue = [
            "Login Issues", "Payment Problems", "Order Tracking", "Account Deactivation", "Bug Report",
            "Feature Request", "Performance Issues", "Security Concerns", "Order Cancellation", "Product Availability",
            "Installation Issues", "Upgrade Problems", "Notification Problems", "Data Sync Issues", "API Issues",
            "Password Reset", "Billing Errors", "Network Issues", "Crash Report", "Accessibility Issues",
            "Email Problems", "Session Timeout", "Website Freezing", "Data Privacy", "Resource Usage",
            "Unexpected Behavior", "Product Review Problems", "Localization Issues", "Customer Support", "Feedback",
            "Documentation Errors", "Slow Response Time", "Connectivity Issues", "Website Downtime", "Search Problems",
            "Integration Issues", "Database Errors", "Checkout Problems", "User Interface Glitch", "Service Outage",
            "Permission Issues", "Recovery Problems", "Functionality Missing", "Unexpected Logout", "Data Corruption",
            "Subscription Issues", "Push Notification Failure", "Account Lockout", "Form Submission Errors",
            "Screen Display Problems"
        ]
        actions = [
            "reported", "requested", "experienced", "encountered", "faced", "complained about",
            "raised a concern about", "highlighted", "pointed out", "mentioned"
        ]
        descriptions = [
            "frequent", "intermittent", "persistent", "sporadic", "rare", "constant", "recurring",
            "occasional", "critical", "severe", "minor", "major", "temporary", "long-term", "short-term"
        ]
        for alt in range(1,501):
         insert_customer_support_ticket(random.randint(1,count),random.choice(actions)+' '+random.choice(descriptions)+' '+random.choice(category_issue),random.choice(status))


    def fill_1year_refunds(year):
        cursor.execute('SELECT COUNT(*) FROM registered_users')
        count = cursor.fetchone()[0]
        cursor.execute('select order_id,user_id from orders')
        orders = cursor.fetchall()
        refund_reasons = [
            "Product not as described", "Received damaged product", "Incorrect item delivered", "Product not delivered",
            "Defective product", "Size doesn't match", "Product quality issues", "Item arrived late", "Changed mind",
            "Found a better price", "Product not needed anymore", "Product color doesn't match",
            "Missing parts/accessories",
            "Unauthorized purchase", "Item doesn't fit", "Allergic reaction", "Received extra item", "Wrong quantity",
            "Product not working", "Received counterfeit product", "Poor customer service experience",
            "Product expired",
            "Misleading advertising", "Item doesn't match website photo", "Incorrect product specifications",
            "Order arrived incomplete", "Received a used item", "Product warranty issues", "Overcharged for item",
            "Duplicate order", "Better product available", "Unwanted gift", "Subscription cancellation",
            "Product packaging damaged", "Product different from website description", "Shipping cost too high",
            "Billing error", "Didn't meet expectations", "Incorrect billing address", "Item not as pictured",
            "Promotional discount not applied", "Product malfunctioned", "Technical issue with the product",
            "Product not compatible", "Received wrong color", "Item not suitable for intended purpose",
            "Product recall", "Received wrong size", "Package delivered to wrong address", "Ordered by mistake",
            "Insufficient product details", "Delayed shipping", "Duplicate payment", "Item broke after short use",
            "Different product material", "Incorrect customization", "Missing installation instructions",
            "Received a substitute item", "Item out of stock", "Poor packaging", "Different item number",
            "Item not available", "Received product after event", "No longer needed", "Overstock",
            "Customer dissatisfaction",
            "Product safety concerns", "Inadequate performance", "Found a better alternative", "Delayed processing",
            "Item didn’t meet warranty", "Bad reviews post-purchase", "Found it cheaper elsewhere", "Delivery issues",
            "Item damaged in transit", "Received wrong model", "Received incorrect order",
            "Unhappy with product material",
            "Product delivered to neighbor", "Defective manufacturing", "Wrong product quantity", "Order mixed up",
            "Received duplicate item", "Wrong item customization", "Shipping address error", "Wrong item ordered",
            "Received previous season item", "Incorrect packaging", "Received wrong accessories",
            "Promo code didn’t work",
            "Received incorrect model", "Item perished", "Packaging issues", "Poor build quality", "Not as expected",
            "Price drop post-purchase", "Product looks different", "Wrong shipping method", "Received wrong version",
            "Issue with payment method", "Wrong product details", "Received different brand", "Defective electronics",
            "Item too large", "Item too small", "Gift not liked", "Didn’t fit description",
            "Product doesn’t match taste",
            "Product not genuine", "Received broken seal", "Delay in product return", "Order processing delay",
            "Bad packaging", "Wrong order fulfillment", "Product recall notice", "Received expired product",
            "Order discrepancy", "Technical error on website", "Issue with product setup", "Received damaged packaging",
            "Product out of warranty", "Misleading size chart", "Product design flaw", "Received wrong style",
            "Order incomplete", "Received less quantity", "Order not shipped", "Problem with refund process",
            "Wrong item weight", "Inadequate item details", "Product different color", "Item didn't match sample",
            "Product assembly issue", "Incorrect delivery info", "Item didn’t work", "Found better quality",
            "Delayed product availability", "Changed shipping address", "Incorrect refund amount",
            "Product didn’t work as expected",
            "Wrong delivery timeframe", "Order process failure", "Different item dimensions", "Item different finish",
            "Different item look", "Received wrong shipping label", "Item didn’t match order",
            "Product not shipped as promised",
            "Order not processed", "Misleading product photos", "Delivery window missed", "Item didn’t match reviews",
            "Incorrect product variant", "Order issue", "Late shipment", "Delayed payment processing",
            "Received different size",
            "Wrong product delivered", "Not satisfied with order", "Received wrong packaging", "Item not returnable",
            "Incorrect receipt", "Wrong product features", "Found product defect", "Item arrived after holiday",
            "Found incorrect item", "Unhappy with shipping service", "Wrong shipment date", "Item not liked",
            "Received incorrect parts", "Misleading product specs", "Received broken item", "Misleading product label",
            "Unhappy with product performance", "Incorrect product dimensions", "Didn’t receive order confirmation",
            "Received different item", "Received wrong invoice", "Order confirmation issue",
            "Item received in poor condition",
            "Incorrect item name", "Discrepancy in order details", "Product quality not as expected",
            "Wrong item ordered accidentally",
            "Received product late", "Unhappy with purchase", "Product defect", "Received different quantity",
            "Received wrong item details",
            "Unhappy with product quality", "Didn’t meet product description", "Wrong order received",
            "Product didn’t meet standards",
            "Received incorrect shipment", "Poor delivery service", "Misleading product info",
            "Unhappy with delivery speed",
            "Received product with wrong label", "Item received in damaged condition", "Received product after need",
            "Product found cheaper",
            "Wrong order quantity", "Product damaged", "Received wrong delivery info", "Product return issue",
            "Shipping error",
            "Unhappy with packaging", "Received defective product", "Product not as per website",
            "Order received incomplete",
            "Received damaged order", "Received different brand item", "Wrong order fulfillment details",
            "Product different than expected",
            "Order delivery error", "Received wrong product version", "Wrong order details",
            "Product damaged during shipping",
            "Received incorrect order details", "Received item past expected date", "Received wrong product details",
            "Incorrect billing",
            "Wrong order received", "Received incorrect product quantity", "Misleading product color",
            "Received expired item",
            "Shipping delay", "Received wrong order quantity", "Received damaged product",
            "Unhappy with product performance",
            "Received product with missing parts", "Incorrect product description", "Received defective item",
            "Product recall issue",
            "Received incorrect product specs", "Received item past return date", "Received wrong product dimensions",
            "Received different product",
            "Received different product variant", "Wrong product size", "Product damaged upon arrival",
            "Incorrect order details",
            "Received wrong shipping info", "Product damaged during transit", "Received wrong product material",
            "Item not as per website",
            "Wrong product specifications", "Received item with wrong label", "Received wrong product color",
            "Product not per description",
            "Received wrong size", "Product damaged during delivery", "Received incorrect product features",
            "Product didn’t match website",
            "Received wrong order details", "Received damaged product", "Product return issue",
            "Received incorrect item quantity",
            "Received incorrect order specs", "Incorrect product variant", "Wrong product delivered",
            "Received damaged product",
            "Received different product details", "Received wrong product variant", "Received wrong item label",
            "Product different than ordered",
            "Received wrong product name", "Received incorrect product version", "Product damaged in shipping",
            "Received different product brand",
            "Received damaged product", "Received incorrect order", "Received wrong product specs",
            "Received wrong order specs",
            "Received damaged product", "Product damaged in transit", "Received wrong order",
            "Incorrect product details",
            "Product return error", "Received incorrect product color", "Received different order",
            "Received different product version",
            "Product damaged upon receipt", "Incorrect product color", "Product different than described",
            "Received different order",
            "Received wrong product details", "Received incorrect item", "Product recall issue",
            "Received incorrect product description",
            "Product not as per website", "Received different product dimensions", "Received wrong product quantity",
            "Received incorrect product specs",
            "Received different order details", "Product not working", "Received different product color",
            "Received different product",
            "Product recall notice", "Received wrong item quantity", "Received incorrect product name",
            "Product recall issue",
            "Received different product specs", "Product different than expected", "Received incorrect product variant",
            "Received wrong order details",
            "Received wrong product material", "Received incorrect product specs", "Received wrong product variant",
            "Received incorrect product details",
            "Received wrong product name", "Received different product quantity", "Received incorrect product details",
            "Received wrong product specs",
            "Received damaged product", "Received incorrect product color", "Product different than ordered",
            "Received wrong product variant",
            "Received incorrect product quantity", "Received incorrect order details",
            "Received wrong product description", "Product recall notice",
            "Received wrong product variant", "Received different order details", "Received wrong product material",
            "Received different product specs",
            "Received wrong order specs", "Received wrong product details", "Received wrong product color",
            "Product different than described",
            "Received incorrect product quantity", "Received different product details",
            "Received incorrect product description", "Received incorrect product variant",
            "Received wrong product color", "Received incorrect product specs", "Received different product brand",
            "Received wrong product details",
            "Received incorrect order specs", "Received incorrect product details", "Received wrong product name",
            "Product damaged upon arrival",
            "Received wrong product variant", "Received different product quantity",
            "Received incorrect product details", "Received different product version",
            "Received wrong product description", "Received different product specs", "Received wrong product variant",
            "Product recall issue",
            "Received incorrect order details", "Received different product details", "Received wrong product specs",
            "Received wrong product quantity",
            "Received wrong product name", "Product recall notice", "Received different product color",
            "Received wrong product material",
            "Received wrong product specs", "Received different product quantity", "Product damaged in transit",
            "Received incorrect product variant",
            "Received incorrect product name", "Received wrong product details", "Received different product brand",
            "Received wrong product variant",
            "Received different product specs", "Received different product color",
            "Received incorrect product description", "Received wrong product quantity",
            "Received wrong product details", "Received different product brand", "Received incorrect product variant",
            "Product damaged upon arrival",
            "Received incorrect product color", "Received wrong product name", "Received different product quantity",
            "Product recall notice",
            "Received different product specs", "Received wrong product description",
            "Received incorrect product variant", "Received different product details",
            "Received wrong product specs", "Received different product color", "Product damaged during shipping",
            "Received incorrect product specs",
            "Received different product brand", "Received wrong product name", "Received wrong product details",
            "Received different product quantity",
            "Received incorrect product details", "Product damaged in transit", "Received different product color",
            "Received wrong product variant",
            "Received different product specs", "Product recall notice", "Received incorrect product variant",
            "Received different product details",
            "Received wrong product name", "Received different product quantity", "Received wrong product details",
            "Received incorrect product specs",
            "Received different product brand", "Received wrong product description",
            "Received incorrect product details", "Received different product color",
            "Received wrong product specs", "Received incorrect product variant", "Received different product quantity",
            "Product damaged upon receipt",
            "Received wrong product name", "Received incorrect product details", "Product damaged during transit",
            "Received different product specs",
            "Received wrong product variant", "Received different product details", "Received wrong product color",
            "Received different product quantity",
            "Received wrong product specs", "Received incorrect product variant", "Received different product color",
            "Received incorrect product details",
            "Product recall issue", "Received different product brand", "Received incorrect product specs",
            "Received wrong product name",
            "Received different product quantity", "Received different product specs", "Received wrong product variant",
            "Received different product details",
            "Received incorrect product description", "Received wrong product color",
            "Received incorrect product variant", "Received different product brand",
            "Received wrong product details", "Received different product quantity", "Received wrong product name",
            "Received incorrect product specs",
            "Received different product color", "Product damaged upon arrival", "Received wrong product variant",
            "Received incorrect product details",
            "Received different product specs", "Received incorrect product color", "Received different product brand",
            "Product recall notice",
            "Received incorrect product variant", "Received wrong product description", "Received wrong product name",
            "Received different product quantity",
            "Received different product details", "Received wrong product specs",
            "Received incorrect product description", "Received different product color",
            "Received incorrect product variant", "Received different product brand",
            "Received incorrect product details", "Received different product quantity",
            "Received wrong product name", "Received different product specs", "Received incorrect product color",
            "Received wrong product description",
            "Received different product details", "Received incorrect product variant",
            "Product damaged during transit", "Received wrong product quantity",
            "Received different product brand", "Received incorrect product details", "Received wrong product specs",
            "Received different product quantity",
            "Received wrong product variant", "Received different product details", "Received different product color",
            "Received incorrect product variant",
            "Received wrong product name", "Received different product specs", "Received different product brand",
            "Received different product quantity",
            "Received wrong product color", "Received incorrect product details", "Received wrong product variant",
            "Product damaged in transit",
            "Received different product details", "Received incorrect product specs",
            "Received different product color", "Received incorrect product variant",
            "Received wrong product name", "Received different product specs", "Received different product brand",
            "Received wrong product quantity",
            "Received different product details", "Received incorrect product variant", "Received wrong product specs",
            "Product damaged upon receipt",
            "Received different product quantity", "Received wrong product name", "Received incorrect product details",
            "Received different product specs",
            "Received different product color", "Received incorrect product variant",
            "Received different product brand", "Received wrong product quantity",
            "Received incorrect product description", "Received different product details",
            "Received different product specs", "Received incorrect product color",
            "Received different product brand", "Received wrong product name", "Received wrong product specs",
            "Received different product quantity",
            "Product damaged during shipping", "Received incorrect product variant", "Received different product specs",
            "Received different product details",
            "Received different product color", "Received incorrect product description",
            "Received wrong product quantity", "Received incorrect product details",
            "Received different product brand", "Received different product specs",
            "Received different product quantity", "Received wrong product variant",
            "Received incorrect product details", "Received different product color",
            "Received incorrect product variant", "Received different product specs",
            "Received wrong product name", "Received different product brand", "Received incorrect product details",
            "Received different product quantity",
            "Received wrong product specs", "Received different product details", "Received different product color",
            "Received incorrect product variant",
            "Received wrong product quantity", "Received different product specs", "Product damaged upon receipt",
            "Received different product brand",
            "Received incorrect product details", "Received different product color", "Received wrong product name",
            "Received different product details",
            "Received different product specs", "Received different product quantity",
            "Received incorrect product variant", "Product damaged in transit",
            "Received different product brand", "Received different product color",
            "Received incorrect product details", "Received wrong product specs",
            "Received different product quantity", "Received incorrect product variant",
            "Received different product specs", "Received wrong product name",
            "Received different product brand", "Received different product color",
            "Received different product details", "Received incorrect product variant",
            "Received wrong product quantity", "Received different product specs", "Received incorrect product details",
            "Received different product brand",
            "Received wrong product name", "Received different product quantity", "Received different product details",
            "Received different product specs",
            "Received incorrect product variant", "Received different product color",
            "Received different product brand", "Product damaged during transit",
            "Received different product specs", "Received different product details",
            "Received different product quantity", "Received incorrect product details",
            "Received wrong product name", "Received incorrect product variant", "Received different product color",
            "Received different product specs",
            "Received different product quantity", "Received different product brand",
            "Received different product details", "Received different product specs",
            "Received wrong product quantity", "Received incorrect product details", "Received different product color",
            "Received different product variant",
            "Received different product brand", "Received different product quantity",
            "Received different product specs", "Received different product details",
            "Received incorrect product variant", "Received different product color",
            "Received different product specs", "Received wrong product name",
            "Received incorrect product details", "Received different product brand",
            "Received different product quantity", "Received different product details",
            "Received different product specs", "Received incorrect product variant",
            "Received different product color", "Received different product brand",
            "Product damaged in transit", "Received different product quantity", "Received different product details",
            "Received different product specs",
            "Received incorrect product details", "Received different product brand",
            "Received different product color", "Received different product variant",
            "Received different product quantity", "Received different product specs",
            "Received different product details"]
        for alt in range(1,101):
         try:
          date=random.choice(getdate(year))
          order=random.choice(orders)
          insert_refunds(random.randint(1,count),random.randint(1,total_products()),order[0],1,random.choice(refund_reasons),date)
         except Exception as e:
             continue


    def start_for_1_year(year):
     add_1000_users()
     add_1000_users()
     print ('Added 2000 users')
     add_100_retailers()
     print('Added 100 retailers')
     data_prebookings(year)
     print('Pre Booking done for 1 year')
     fill_inventory_for_1_year(year)
     print('Inventory filled for 1 year')
     fill_100_coupons(year)
     print ('Coupons Added for 1 year')
     fill_300_reviews()
     fill_300_reviews()
     print('Added reviews for 1 year')
     fill_1year_cart(year)
     print('Added Cart for 1 year')
     fill_500_orders()
     print('Placed 1 year Orders')
     fill500payments()
     print('Payment of Orders')
     fill_500_customer_issues()
     print('1 year of issues')
     fill_1year_refunds(year)
     print('1 year Refunds')
     print('Added data for year=',year)


    #add_products_and_Cats()
    #fillshipping()
    start_for_1_year(2021)



    cursor.close()
    conn.close()

except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(f"Error connecting to the database: {sqlstate}")



