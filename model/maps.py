gender_map = {'Male': 0,
		  	  'Female': 1}

job_title_map = {'1st-line supervisors/managers construction & extraction workers': '6200',
			 '1st-line supervisors/managers farming, fishing, and forestry workers': '6005',
			 '1st-line supervisors/managers fire fighting & prevention workers': '3720',
			 '1st-line supervisors/managers food prep and serving workers': '4010',
			 '1st-line supervisors/managers housekeeping & janitorial workers': '4200',
			 '1st-line supervisors/managers landscape, lawn, grounds workers': '4210',
			 '1st-line supervisors/managers mechanics, installers, repairers': '7000',
			 '1st-line supervisors/managers of correctional officers': '3700',
			 '1st-line supervisors/managers of police and detectives': '3710',
			 '1st-line supervisors/managers of production & operating workers': '7700',
			 '1st-line supervisors/managers office & admin support workers': '5000',
			 'Accountants and auditors': '0800',
			 'Actors': '2700',
			 'Actuaries': '1200',
			 'Administrative services managers': '0100',
			 'Advertising and promotions managers': '0040',
			 'Advertising sales agents': '4800',
			 'Aerospace engineers': '1320',
			 'Agents and business managers of artists, performers, athletes': '0500',
			 'Agricultural and Biomedical engineers': '1340',
			 'Agricultural and food science technicians': '1900',
			 'Agricultural and food scientists': '1600',
			 'Agricultural inspectors': '6010',
			 'Air traffic controllers and airfield operations specialists': '9040',
			 'Aircraft mechanics and service technicians': '7140',
			 'Aircraft pilots and flight engineers': '9030',
			 'Aircraft structure, surfaces, rigging, and systems assemblers': '7710',
			 'Ambulance drivers, attendants, exc. emergency medical techs': '9110',
			 'Animal control workers': '3900',
			 'Animal trainers': '4340',
			 'Announcers': '2800',
			 'Appraisers and assessors of real estate': '0810',
			 'Architects, except naval': '1300',
			 'Archivists, curators, and museum technicians': '2400',
			 'Arme': '9840',
			 'Artists and related workers': '2600',
			 'Astronomers and physicists': '1700',
			 'Athletes, coaches, umpires, and related workers': '2720',
			 'Atmospheric and space scientists': '1710',
			 'Audiologists': '3140',
			 'Automotive body and related repairers': '7150',
			 'Automotive glass installers and repairers': '7160',
			 'Automotive service technicians and mechanics': '7200',
			 'Avionics technicians': '7030',
			 'Baggage porters, bellhops, and concierges': '4530',
			 'Bailiffs, correctional officers, and jailers': '3800',
			 'Bakers': '7800',
			 'Barbers': '4500',
			 'Bartenders': '4040',
			 'Bill and account collectors': '5100',
			 'Billing and posting clerks and machine operators': '5110',
			 'Biological scientists': '1610',
			 'Biological technicians': '1910',
			 'Boilermakers': '6210',
			 'Bookkeeping, accounting, and auditing clerks': '5120',
			 'Brickmasons, blockmasons, and stonemasons': '6220',
			 'Broadcast and sound engineering technicians and radio operators': '2900',
			 'Brokerage clerks': '5200',
			 'Budget analysts': '0820',
			 'Bus and truck mechanics and diesel engine specialists': '7210',
			 'Bus drivers': '9120',
			 'Business operations specialists, all other': '0740',
			 'Butchers and other meat, poultry, and fish processing workers': '7810',
			 'Cabinetmakers and bench carpenters': '8500',
			 'Cargo and freight agents': '5500',
			 'Carpenters': '6230',
			 'Carpet, floor, and tile installers and finishers': '6240',
			 'Cashiers': '4720',
			 'Cement masons, concrete finishers, and terrazzo workers': '6250',
			 'Cementing and gluing machine operators and tenders': '8850',
			 'Chefs and head cooks': '4000',
			 'Chemical engineers': '1350',
			 'Chemical processing machine setters, operators, and tenders': '8640',
			 'Chemical technicians': '1920',
			 'Chemists and materials scientists': '1720',
			 'Chief executives': '0010',
			 'Child care workers': '4600',
			 'Chiropractors': '3000',
			 'Civil engineers': '1360',
			 'Claims adjusters, appraisers, examiners, and investigators': '0540',
			 'Cleaners of vehicles and equipment': '9610',
			 'Cleaning, washing, metal pickling equipment operators, tenders': '8860',
			 'Clergy': '2040',
			 'Clinical laboratory technologists and technicians': '3300',
			 'Coin, vending, and amusement machine servicers and repairers': '7510',
			 'Combined food prep and serving workers, including fast food': '4050',
			 'Communications equipment operators, all other': '5030',
			 'Compensation and benefits manager': '0135',
			 'Compensation, benefits, and job analysis specialistst': '0640',
			 'Compliance officers': '0565',
			 'Computer and information reserach scientists': '1005',
			 'Computer and information systems managers': '0110',
			 'Computer control programmers and operators': '7900',
			 'Computer hardware engineers': '1400',
			 'Computer network architects': '1106',
			 'Computer occupation, all other': '1107',
			 'Computer operators': '5800',
			 'Computer programmers': '1010',
			 'Computer support specialists': '1050',
			 'Computer systems analysts': '1006',
			 'Computer, automated teller, and office machine repairers': '7010',
			 'Conservation scientists and foresters': '1640',
			 'Construction and building inspectors': '6660',
			 'Construction equipment operators, except Paving, surfacing, and tamping equip operators': '6320',
			 'Construction laborers': '6260',
			 'Construction managers': '0220',
			 'Control and valve installers and repairers': '7300',
			 'Cooks': '4020',
			 'Correspondence clerks and Order clerks': '5350',
			 'Cost estimators': '0600',
			 'Counselors': '2000',
			 'Counter and rental clerks': '4740',
			 'Counter attendants, cafeteria, food concession, and coffee shop': '4060',
			 'Couriers and messengers': '5510',
			 'Court, municipal, and license clerks': '5220',
			 'Crane and tower operators': '9510',
			 'Credit analysts': '0830',
			 'Credit authorizers, checkers, and clerks': '5230',
			 'Crossing guards': '3940',
			 'Crushing, grinding, polishing, mixing, and blending workers': '8650',
			 'Customer service representatives': '5240',
			 'Cutting workers': '8710',
			 'Cutting, punching, and press machine setters, operators, and tenders, metal, plastic': '7950',
			 'Dancers and choreographers': '2740',
			 'Data entry keyers': '5810',
			 'Database administrators': '1060',
			 'Dental assistants': '3640',
			 'Dental hygienists': '3310',
			 'Dentists': '3010',
			 'Derrick, rotary drill, service unit operators, oil, gas, mining': '6800',
			 'Designers': '2630',
			 'Detectives and criminal investigators': '3820',
			 'Diagnostic related technologists and technicians': '3320',
			 'Dietitians and nutritionists': '3030',
			 'Directors, religious activities and education': '2050',
			 'Dishwashers': '4140',
			 'Dispatchers': '5520',
			 'Door-to-door sales, news & street vendors, & related workers': '4950',
			 'Drafters': '1540',
			 'Dredge, excavating, and loading machine operators': '9520',
			 'Driver/sales workers and truck drivers': '9130',
			 'Drywall installers, ceiling tile installers, and tapers': '6330',
			 'Earth drillers, except oil and gas': '6820',
			 'Economists': '1800',
			 'Editors': '2830',
			 'Education administrators': '0230',
			 'Electric motor, power tool, and related repairers': '7040',
			 'Electrical and electronic engineers': '1410',
			 'Electrical and electronics repairers, industrial and utility': '7100',
			 'Electrical power-line installers and repairers': '7410',
			 'Electrical, electronics, and electromechanical assemblers': '7720',
			 'Electricians': '6355',
			 'Electronic equipment installers and repairers, motor vehicles': '7110',
			 'Electronic home entertainment equipment installers and repairers': '7120',
			 'Elementary and middle school teachers': '2310',
			 'Elevator installers and repairers': '6700',
			 'Eligibility interviewers, government programs': '5250',
			 'Emergency management directors': '0425',
			 'Emergency medical technicians and paramedics': '3400',
			 'Engine and other machine assemblers': '7730',
			 'Engineering managers': '0300',
			 'Engineering technicians, except drafters': '1550',
			 'Engineers, all other': '1530',
			 'Entertainers & performers, sports & related workers, all other': '2760',
			 'Environmental engineers': '1420',
			 'Environmental scientists and geoscientists': '1740',
			 'Etchers and engravers': '8910',
			 'Exercise Physiologists and Therapists, all other': '3245',
			 'Explosives workers, ordnance handling experts, and blasters': '6830',
			 'Extruding, drawing machine operators & tenders, metal, plastic': '7920',
			 'Extruding, forming, pressing, and compacting machine setters, operators, and tenders': '8720',
			 'Farm, ranch, and other agricultural managers': '0205',
			 'Fence erectors': '6710',
			 'File Clerks': '5260',
			 'Financial analysts': '0840',
			 'Financial clerks, all other': '5165',
			 'Financial examiners': '0900',
			 'Financial managers': '0120',
			 'Financial specialists, all other': '0950',
			 'Fire fighters': '3740',
			 'Fire inspectors': '3750',
			 'First-line supervisors/managers of gaming workers': '4300',
			 'First-line supervisors/managers of non-retail sales workers': '4710',
			 'First-line supervisors/managers of personal service workers': '4320',
			 'First-line supervisors/managers of retail sales workers': '4700',
			 'Fishers and related fishing workers': '6100',
			 'Flight Attendents': '9050',
			 'Food batchmakers': '7840',
			 'Food cooking machine operators and tenders': '7850',
			 'Food preparation and serving workers, all other including dining room and cafeteria attendants and bartender': '4130',
			 'Food preparation workers': '4030',
			 'Food processing workers, all other': '7855',
			 'Food servers, nonrestaurant': '4120',
			 'Food service managers': '0310',
			 'Food, tobacco roasting, baking, drying machine operators, tenders': '7830',
			 'Forest and conservation workers': '6120',
			 'Fundraisers': '0726',
			 'Funeral service workers': '4460',
			 'Furnace, kiln, oven, drier, and kettle operators and tenders': '8730',
			 'Furniture finishers': '8510',
			 'Gaming cage workers': '5130',
			 'Gaming managers': '0330',
			 'Gaming services workers': '4400',
			 'Gen and operations managers': '0020',
			 'Geological and petroleum technicians': '1930',
			 'Glaziers': '6360',
			 'Graders and sorters, agricultural products': '6040',
			 'Grinding, lapping, polishing, and buffing machine tool setters, operators, and tenders, metal & plastic': '8000',
			 'Grounds maintenance workers': '4250',
			 'Hairdressers, hairstylists, and cosmetologists': '4510',
			 'Hazardous materials removal workers': '6720',
			 'Health diagnosing and treating practitioners, all other': '3260',
			 'Health practitioner support technologists and technicians': '3420',
			 'Heating, air conditioning, refrigeration mechanics, installers': '7315',
			 'Heavy vehicle & mobile equipment service techs & mechanics': '7220',
			 'Helpers, construction trades': '6600',
			 'Helpers--installation, maintenance, and repair workers': '7610',
			 'Helpers--production workers': '8950',
			 'Highway maintenance workers': '6730',
			 'Hoist and winch operators, and conveyor operators and tenders': '9560',
			 'Home appliance repairers': '7320',
			 'Hosts and hostesses, restaurant, lounge, and coffee shop': '4150',
			 'Hotel, motel, and resort desk clerks': '5300',
			 'Human resources assistants, except payroll and timekeeping': '5360',
			 'Human resources managers': '0136',
			 'Human resources workers': '0630',
			 'Industrial and refractory machinery mechanics': '7330',
			 'Industrial engineers, including health and safety': '1430',
			 'Industrial production managers': '0140',
			 'Industrial truck and tractor operators': '9600',
			 'Information and record clerks, all other': '5420',
			 'Information security analysts': '1007',
			 'Inspectors, testers, sorters, samplers, and weighers': '8740',
			 'Insulation workers': '6400',
			 'Insurance claims and policy processing clerks': '5840',
			 'Insurance sales agents': '4810',
			 'Insurance underwriters': '0860',
			 'Interviewers, except eligibility and loan': '5310',
			 'Janitors and building cleaners': '4220',
			 'Jewelers and precious stone and metal workers': '8750',
			 'Judicial Law Clerks': '2105',
			 'Laborers and freight, stock, and material movers, hand': '9620',
			 'Lathe and turning machine tool setters, operators, and tenders, metal and plastic': '8010',
			 'Laundry and dry-cleaning workers': '8300',
			 'Lawyers, Judges, magistrates, and other judicial workers': '2100',
			 'Librarians': '2430',
			 'Library assistants, clerical': '5320',
			 'Library technicians': '2440',
			 'Licensed practical and licensed vocational nurses': '3500',
			 'Lifeguards and other recreational, and all other protective service workers': '3955',
			 'Loan counselors and officers': '0910',
			 'Loan interviewers and clerks': '5330',
			 'Locksmiths and safe repairers': '7540',
			 'Locomotive engineers and operators': '9200',
			 'Lodging managers': '0340',
			 'Logging workers': '6130',
			 'Logisticians': '0700',
			 'Machine feeders and offbearers': '9630',
			 'Machinists': '8030',
			 'Maids and housekeeping cleaners': '4230',
			 'Mail clerks and mail machine operators, except postal service': '5850',
			 'Maintenance and repair workers, general': '7340',
			 'Maintenance workers, machinery': '7350',
			 'Management analysts': '0710',
			 'Managers, all other': '0430',
			 'Manufactured building and mobile home installers': '7550',
			 'Marine engineers and naval architects': '1440',
			 'Market research analysts and marketing specialists': '0735',
			 'Marketing and sales managers': '0050',
			 'Massage therapists': '3630',
			 'Material moving workers, incl mine shuttle operators and tank car, truck, and ship loaders': '9750',
			 'Materials engineers': '1450',
			 'Mathematicians 15-2021, not': '1210',
			 'Mathematicians, Statisticians, and Misc mathematical science occ': '1240',
			 'Mechanical engineers': '1460',
			 'Medical Assistants': '3645',
			 'Medical Transcriptionists': '3646',
			 'Medical and health services managers': '0350',
			 'Medical records and health information technicians': '3510',
			 'Medical scientists and life scientists, all other': '1650',
			 'Medical, dental, and ophthalmic laboratory technicians': '8760',
			 'Meeting, convention, and event planners': '0725',
			 'Metal furnace and kiln operators and tenders': '8040',
			 'Metalworkers and plastic workers, all other': '8220',
			 'Meter readers, utilities': '5530',
			 'Millwrights': '7360',
			 'Mining & geological engineers, including mining safety engineers': '1500',
			 'Mining machine operators': '6840',
			 'Misc Textile, apparel, and furnishings workers, except upholsterers': '8460',
			 'Misc community and social service specialists, incl heal educators and comm health workers': '2025',
			 'Misc vehicle & mobile equipment mechanics, installers, repairers': '7260',
			 'Miscellaneous Woodworkers, incl model makers and pattern makers': '8550',
			 'Miscellaneous agricultural workers, incl animal breeders': '6050',
			 'Miscellaneous assemblers and fabricators': '7750',
			 'Miscellaneous construction and related workers,incl photovoltaic in': '6765',
			 'Miscellaneous entertainment attendants and related workers': '4430',
			 'Miscellaneous health technologists and technicians': '3535',
			 'Miscellaneous healthcare support occupations, incl medical equip preparers': '3655',
			 'Miscellaneous legal support workers': '2160',
			 'Miscellaneous life, physical, and social science technicians': '1965',
			 'Miscellaneous media and communication workers': '2860',
			 'Miscellaneous personal appearance workers': '4520',
			 'Miscellaneous plant and system operators': '8630',
			 'Miscellaneous social scientists, including survey researchers and sociologists': '1860',
			 'Models, demonstrators, and product promoters': '4900',
			 'Molders, molding machine operators, tenders, metal, plastic': '8100',
			 'Molders, shapers, and casters, except metal and plastic': '8920',
			 'Morticians, undertakers, and funeral directors': '4465',
			 'Motion picture projectionists': '4410',
			 'Motor vehicle operators, all other': '9150',
			 'Musicians, singers, and related workers': '2750',
			 'Natural sciences managers': '0360',
			 'Network and computer systems administrators': '1105',
			 'New accounts clerks': '5340',
			 'News analysts, reporters and correspondents': '2810',
			 'Nonfarm animal caretakers': '4350',
			 'Not reported, not codable [recoded to': '9990',
			 'Nuclear engineers': '1510',
			 'Nurse Anethstists': '3256',
			 'Nurse midwives and Nurse Practitioners': '3258',
			 'Nursing, psychiatric, and home health aides': '3600',
			 'Occupational therapist assistants and aides': '3610',
			 'Occupational therapists': '3150',
			 'Office and administrative support workers, including desktop pu': '5940',
			 'Office clerks, general': '5860',
			 'Office machine operators, except computer': '5900',
			 'Operations research analysts': '1220',
			 'Opticians, dispensing': '3520',
			 'Optometrists': '3040',
			 'Other education, training, and library workers': '2550',
			 'Other extraction workers, incl roof bolters and helpers': '6940',
			 'Other healthcare practitioners and technical occupations, including podiatrists': '3540',
			 'Other installation, maintenance, and repair workers, incl wind turbine service techs, commmercial drivers, and signal and train switch repairers': '7630',
			 'Other teachers and instructors': '2340',
			 'Other transportation workers, incl bridge and lock tenders': '9420',
			 'Packaging and filling machine operators and tenders': '8800',
			 'Packers and packagers, hand': '9640',
			 'Painters, construction and maintenance and paperhangers': '6420',
			 'Painting workers': '8810',
			 'Paper goods machine setters, operators, and tenders': '8930',
			 'Paralegals and legal assistants': '2145',
			 'Parking enforcement workers': '3840',
			 'Parking lot attendants': '9350',
			 'Parts salespersons': '4750',
			 'Paving, surfacing, and tamping equipment operators': '6300',
			 'Payroll and timekeeping clerks': '5140',
			 'Personal and home care aides': '4610',
			 'Personal care and service workers, all other': '4650',
			 'Personal financial advisors': '0850',
			 'Pest control workers': '4240',
			 'Petroleum engineers': '1520',
			 'Pharmacists': '3050',
			 'Pharmacy Aides': '3647',
			 'Phlebotomists': '3649',
			 'Photographers': '2910',
			 'Photographic process workers and processing machine operators': '8830',
			 'Physical scientists, all other': '1760',
			 'Physical therapist assistants and aides': '3620',
			 'Physical therapists': '3160',
			 'Physician assistants': '3110',
			 'Physicians and surgeons': '3060',
			 'Pipelayers, plumbers, pipefitters, and steamfitters': '6440',
			 'Plasterers and stucco masons': '6460',
			 'Plating and coating machine setters, operators, and tenders, metal and plastic': '8200',
			 'Police and sheriffs patrol officers': '3850',
			 'Postal serv mail sorters, processors, & proc machine operators': '5560',
			 'Postal service clerks': '5540',
			 'Postal service mail carriers': '5550',
			 'Postsecondary teachers': '2200',
			 'Power plant operators, distributors, and dispatchers': '8600',
			 'Precision instrument and equipment repairers': '7430',
			 'Prepress technicians and workers': '8250',
			 'Preschool and kindergarten teachers': '2300',
			 'Pressers, textile, garment, and related materials': '8310',
			 'Print binding and finishing workers': '8256',
			 'Printing press operators': '8255',
			 'Private detectives and investigators': '3910',
			 'Probation officers and correctional treatment specialists': '2015',
			 'Problem referral [recoded to ': '9970',
			 'Procurement clerks': '5150',
			 'Producers and directors': '2710',
			 'Production workers, incl semiconductor processors and cooling and freezing equipment operators': '8965',
			 'Production, planning, and expediting clerks': '5600',
			 'Proofreaders and copy markers': '5910',
			 'Property, real estate, and community association managers': '0410',
			 'Psychologists': '1820',
			 'Public relations managers': '0060',
			 'Public relations specialists': '2825',
			 'Pumping station operators': '9650',
			 'Purchasing agents and buyers, farm products': '0510',
			 'Purchasing agents, except wholesale, retail, and farm products': '0530',
			 'Purchasing managers': '0150',
			 'Radiation therapists': '3200',
			 'Radio and telecommunications equipment installers and repairers': '7020',
			 'Rail-track laying and maintenance equipment operators': '6740',
			 'Railroad brake, signal, switch opertors, conductors and yardmasters': '9240',
			 'Real estate brokers and sales agents': '4920',
			 'Receptionists and information clerks': '5400',
			 'Recreation and fitness workers': '4620',
			 'Recreational therapists': '3210',
			 'Refuse and recyclable material collectors': '9720',
			 'Registred Nurses': '3255',
			 'Reinforcing iron and rebar workers': '6500',
			 'Religious workers, all other': '2060',
			 'Reservation and transportation ticket agents and travel clerks': '5410',
			 'Residential advisors': '4640',
			 'Respiratory therapists': '3220',
			 'Retail salespersons': '4760',
			 'Riggers': '7560',
			 'Rolling machine setters, operators, tenders and forging maching setters, operators, and tenders, metal and plastic': '7940',
			 'Roofers': '6515',
			 'Roustabouts, oil and gas': '6920',
			 'Sailors and marine oilers and ship engineers': '9300',
			 'Sales and related workers, all other': '4965',
			 'Sales engineers': '4930',
			 'Sales representatives, services, all other': '4840',
			 'Sales representatives, wholesale and manufacturing': '4850',
			 'Sawing machine setters, operators, and tenders, wood': '8530',
			 'Secondary school teachers': '2320',
			 'Secretaries and administrative assistants': '5700',
			 'Securities, commodities, and financial services sales agents': '4820',
			 'Security and fire alarm systems installers': '7130',
			 'Security guards and gaming surveillance officers': '3930',
			 'Septic tank servicers and sewer pipe cleaners': '6750',
			 'Service station attendants': '9360',
			 'Sewing machine operators': '8320',
			 'Sheet metal workers': '6520',
			 'Ship and boat captains and operators': '9310',
			 'Shipping, receiving, and traffic clerks': '5610',
			 'Shoe and leather workers and repairers': '8330',
			 'Small engine mechanics': '7240',
			 'Social and community service managers': '0420',
			 'Social and human service assistants': '2016',
			 'Social workers': '2010',
			 'Software developers, applications, and systems software': '1020',
			 'Special education teachers': '2330',
			 'Speech-language pathologists': '3230',
			 'Stationary engineers and boiler operators': '8610',
			 'Statistical assistants': '5920',
			 'Statisticians 15-2041, not': '1230',
			 'Stock clerks and order fillers': '5620',
			 'Structural iron and steel workers': '6530',
			 'Structural metal fabricators and fitters': '7740',
			 'Subway, streetcar, and other rail transportation workers': '9260',
			 'Supervisors, protective service workers, all other': '3730',
			 'Supervisors, transportation and material moving workers': '9000',
			 'Surveying and mapping technicians': '1560',
			 'Surveyors, cartographers, and photogrammetrists': '1310',
			 'Switchboard operators, including answering service': '5010',
			 'Tailors, dressmakers, and sewers': '8350',
			 'Tax examiners, collectors, and revenue agents': '0930',
			 'Tax prepares': '0940',
			 'Taxi drivers and chauffeurs': '9140',
			 'Teacher assistants': '2540',
			 'Technical writers': '2840',
			 'Telecommunications line installers and repairers': '7420',
			 'Telemarketers': '4940',
			 'Telephone operators': '5020',
			 'Television, video, & motion picture camera operators & editors': '2920',
			 'Tellers': '5160',
			 'Textile cutting machine setters, operators, and tenders': '8400',
			 'Textile knitting & weaving machine setters, operators & tenders': '8410',
			 'Textile winding, twisting, drawing out machine setters, operators, tenders': '8420',
			 'Tire builders': '8940',
			 'Tool and die makers': '8130',
			 'Tool grinders, filers, and sharpeners': '8210',
			 'Tour and travel guides': '4540',
			 'Training and development managers': '0137',
			 'Training and development specialists': '0650',
			 'Transportation attendants, except flight attendants': '9415',
			 'Transportation inspectors': '9410',
			 'Transportation security screeners': '3945',
			 'Transportation, storage, and distribution managers': '0160',
			 'Travel agenets': '4830',
			 'Upholsterers': '8450',
			 'Urban and regional planners': '1840',
			 'Ushers, lobby attendants, and ticket takers': '4420',
			 'Veterinarians': '3250',
			 'Veterinary assistants and laboratory animal caretakers': '3648',
			 'Waiters and waitresses': '4110',
			 'Water and liquid waste treatment plant and system operators': '8620',
			 'Web developers': '1030',
			 'Weighers, measurers, checkers, and samplers, recordkeeping': '5630',
			 'Welding, soldering, and brazing workers': '8140',
			 'Wholesale and retail buyers, except farm products': '0520',
			 'Woodworking machine setters, operators, tenders, except sawing': '8540',
			 'Word processors and typists': '5820',
			 'Writers and authors': '2850'}

city_name_map = {'Abilene, TX': '10180',
 				 'Akron, OH': '10420',
				 'Albany, GA': '10500',
				 'Albany-Schenectady-Troy, NY': '10580',
				 'Albuquerque, NM': '10740',
				 'Allentown-Bethlehem-Easton, PA-NJ': '10900',
				 'Altoona, PA': '11020',
				 'Amarillo, TX': '11100',
				 'Anderson, IN*': '11300',
				 'Anderson, SC*': '11340',
				 'Ann Arbor, MI': '11460',
				 'Anniston-Oxford-Jacksonville, AL': '11500',
				 'Appleton, WI': '11540',
				 'Asheville, NC': '11700',
				 'Athens-Clarke County, GA': '12020',
				 'Atlanta-Sandy Springs-Roswell, GA': '12060',
				 'Atlantic City-Hammonton, NJ': '12100',
				 'Auburn-Opelika, AL': '12220',
				 'Augusta-Richmond County, GA-SC': '12260',
				 'Austin-Round Rock, TX': '12420',
				 'Bakersfield, CA': '12540',
				 'Baltimore-Columbia-Towson, MD': '12580',
				 'Bangor, ME': '12620',
				 'Barnstable Town, MA': '70900',
				 'Barnstable, MA': '12700',
				 'Baton Rouge, LA': '12940',
				 'Battle Creek, MI': '12980',
				 'Beaumont-Port Arthur, TX': '13140',
				 'Bellingham, WA*': '13380',
				 'Bend-Redmond, OR': '13460',
				 'Billings, MT': '13740',
				 'Binghamton, NY': '13780',
				 'Birmingham-Hoover, AL': '13820',
				 'BlacksburgChristiansburg-Radford, VA': '13980',
				 'Bloomington, IL': '14010',
				 'Bloomington, IN': '14020',
				 'Bloomington-Normal, IL*': '14060',
				 'Boise City, ID': '14260',
				 'Boston-Cambridge-Newton, MA-NH': '14460',
				 'Boston-Cambridge-Quincy, MA-NH': '71650',
				 'Boulder, CO': '14500',
				 'Bowling Green, KY': '14540',
				 'Bremerton-Silverdale, WA*': '14740',
				 'Bridgeport-Stamford-Norwalk, CT': '14860',
				 'Brownsville-Harlingen, TX': '15180',
				 'Buffalo-Cheektowaga-Niagara Falls, NY': '15380',
				 'Burlington, NC': '15500',
				 'Burlington-South Burlington, VT': '15540',
				 'California-Lexington Park, MD': '15680',
				 'Canton-Massillon, OH': '15940',
				 'Cape Coral-Fort Myers, FL': '15980',
				 'Carbondale-Marion, IL': '16060',
				 'Cedar Rapids, IA': '16300',
				 'Chambersburg-Waynesboro, PA': '16540',
				 'Champaign-Urbana, IL': '16580',
				 'Charleston, WV': '16620',
				 'Charleston-North Charleston, SC': '16700',
				 'Charlotte-Concord-Gastonia, NC-SC': '16740',
				 'Charlottesville, VA': '16820',
				 'Chattanooga, TN-GA': '16860',
				 'Chicago-Naperville-Elgin, IL-IN-WI': '16980',
				 'Chico, CA': '17020',
				 'Cincinnati, OH-KY-IN': '17140',
				 'Clarksville, TN-KY': '17300',
				 'Cleveland, TN': '17420',
				 'Cleveland-Elyria, OH': '17460',
				 'Coeur dAlene, ID': '17660',
				 'College Station-Bryan, TX': '17780',
				 'Colorado Springs, CO': '17820',
				 'Columbia, MO': '17860',
				 'Columbia, SC': '17900',
				 'Columbus, GA-AL': '17980',
				 'Columbus, OH': '18140',
				 'Corpus Christi, TX': '18580',
				 'Dallas-Fort Worth-Arlington, TX': '19100',
				 'Danbury, CT': '72850',
				 'Daphne-Fairhope-Foley, AL': '19300',
				 'Davenport-Moline-Rock Island, IA-IL': '19340',
				 'Dayton, OH': '19380',
				 'Decatur, Al': '19460',
				 'Decatur, IL': '19500',
				 'Deltona-Daytona Beach-Ormond Beach, FL': '19660',
				 'Denver-Aurora-Lakewood, CO': '19740',
				 'Des Moines-West Des Moines, IA': '19780',
				 'Detroit-Warren-Dearborn, MI': '19820',
				 'Dover, DE': '20100',
				 'Duluth, MN-WI': '20260',
				 'Durham-Chapel Hill, NC': '20500',
				 'East Stroudsburg, PA': '20700',
				 'Eau Claire, WI': '20740',
				 'El Centro, CA': '20940',
				 'El Paso, TX': '21340',
				 'Elkhart-Goshen, IN': '21140',
				 'Erie, PA': '21500',
				 'Eugene, OR': '21660',
				 'Evansville, IN-KY': '21780',
				 'Fargo, ND-MN': '22020',
				 'Farmington, NM': '22140',
				 'Fayetteville, NC': '22180',
				 'Fayetteville-Springdale-Rogers, AR-MO': '22220',
				 'Flint, MI': '22420',
				 'Florence, SC': '22500',
				 'Florence-Muscle Shoals, AL': '22520',
				 'Fort Collins, CO': '22660',
				 'Fort Smith, AR-OK': '22900',
				 'Fort Walton Beach-Crestview-Destin, FL*': '23020',
				 'Fort Wayne, IN': '23060',
				 'Fresno, CA': '23420',
				 'Gainesville, FL': '23540',
				 'Gainesville, GA': '23580',
				 'Glen Falls, NY': '24020',
				 'Goldsboro, NC': '24140',
				 'Grand Rapids-Wyoming, MI': '24340',
				 'Greeley, CO': '24540',
				 'Green Bay, WI': '24580',
				 'Greensboro-High Point, NC': '24660',
				 'Greenville, NC': '24780',
				 'Greenville, SC': '24860',
				 'Gulfport-Biloxi, MS*': '25060',
				 'Hagerstown-Martinsburg, MD-WV': '25180',
				 'Hanford-Corcoran, CA': '25260',
				 'Harrisburg-Carlisle, PA': '25420',
				 'Harrisonburg, VA*': '25500',
				 'Hartford-West Hartford-East Hartford, CT': '73450',
				 'Hickory-Morganton-Lenoir, NC': '25860',
				 'Hilton Head Island-Bluffton-Beaufort, SC': '25940',
				 'Holland-Grand Haven, MI*': '26100',
				 'Honolulu, HI*': '26180',
				 'Houston-Baytown-Sugar Land, TX': '26420',
				 'Huntington-Ashland, WV-KY-OH': '26580',
				 'Huntsville, AL': '26620',
				 'Idaho Falls, ID': '26820',
				 'Indianapolis, IN': '26900',
				 'Iowa City, IA': '26980',
				 'Jackson, MI': '27100',
				 'Jackson, MS': '27140',
				 'Jacksonville, FL': '27260',
				 'Jacksonville, NC': '27340',
				 'Janesville-Beloit, WI': '27500',
				 'Johnson City, TN': '27740',
				 'Johnstown, PA': '27780',
				 'Joplin, MO*': '27900',
				 'Kahului-Wailuku-Lahaina, HI': '27980',
				 'Kalamazoo-Portage, MI': '28020',
				 'Kankakee-Bradley, IL*': '28100',
				 'Kansas City, MO-KS': '28140',
				 'Kennewick-Richland, WA': '28420',
				 'Killeen-Temple-Fort Hood, TX': '28660',
				 'Kingsport-Bristol, TN-VA': '28700',
				 'Kingston, NY*': '28740',
				 'Knoxville, TN': '28940',
				 'La Crosse, WI-MN*': '29100',
				 'Lafayette, LA': '29180',
				 'Lafayette-West Lafayette, IN': '29200',
				 'Lake Charles, LA': '29340',
				 'Lakeland-Winter Haven, FL': '29460',
				 'Lancaster, PA': '29540',
				 'Lansing-East Lansing, MI': '29620',
				 'Laredo, TX': '29700',
				 'Las Cruces, NM': '29740',
				 'Las Vegas-Paradise, NV': '29820',
				 'Lawrence, KS*': '29940',
				 'Lawton, OK*': '30020',
				 'Leominster-Fitchburg-Gardner, MA': '74500',
				 'Lewiston-Auburn, ME': '30340',
				 'Lexington-Fayette, KY': '30460',
				 'Little Rock-North Little Rock, AR': '30780',
				 'Longview, TX': '30980',
				 'Los Angeles-Long Beach-Anaheim, CA (Note the CBSA code change between 2003 and 2013)': '31080',
				 'Los Angeles-Long Beach-Santa Ana, CA*': '31100',
				 'Louisville, KY-IN': '31140',
				 'Lubbock, TX': '31180',
				 'Lynchburg, VA*': '31340',
				 'Macon, GA': '31420',
				 'Madera, CA*': '31460',
				 'Madison, WI': '31540',
				 'Manchester-Nashua, NH': '31700',
				 'McAllen-Edinburg-Mission, TX': '32580',
				 'Medford, OR': '32780',
				 'Memphis, TN-MS-AR': '32820',
				 'Merced, CA*': '32900',
				 'Miami-Fort Lauderdale-West Palm Beach, FL': '33100',
				 'Michigan City-La Porte, IN*': '33140',
				 'Midland, TX*': '33260',
				 'Milwaukee-Waukesha-West Allis, WI': '33340',
				 'Minneapolis-St Paul-Bloomington, MN-WI': '33460',
				 'Mobile, AL': '33660',
				 'Modesto, CA': '33700',
				 'Monroe, LA': '33740',
				 'Monroe, MI': '33780',
				 'Montgomery, AL': '33860',
				 'Morgantown, WV': '34060',
				 'Mount Vernon-Anacortes, WA': '34580',
				 'Muskegon-Norton Shores, MI': '34740',
				 'Myrtle Beach-Conway-North Myrtle Beach, SC-NC': '34820',
				 'Napa, CA*': '34900',
				 'Naples-Immokalee-Marco Island, FL': '34940',
				 'Nashville-Davidson-Murfreesboro, TN': '34980',
				 'New Haven, CT': '75700',
				 'New Haven-Milford, CT': '35300',
				 'New Orleans-Metairie, LA': '35380',
				 'New York-Newark- Jersey City, NY-NJ-PA (White Plains central city recoded to balance of metropolitan)': '35620',
				 'Niles-Benton Harbor, MI': '35660',
				 'North-Port-Sarasota-Bradenton, FL': '35840',
				 'Norwich-New London, CT': '35980',
				 'Norwich-New London, CT-RI': '76450',
				 'Ocala, FL': '36100',
				 'Ocean City, NJ*': '36140',
				 'Odessa, TX': '36220',
				 'Ogden-Clearfield, UT': '36260',
				 'Oklahoma City, OK': '36420',
				 'Olympia, WA*': '36500',
				 'Omaha-Council Bluffs, NE-IA': '36540',
				 'Orlando, FL': '36740',
				 'Oshkosh-Neenah, WI': '36780',
				 'Oxnard-Thousand Oaks-Ventura, CA': '37100',
				 'Palm Bay-Melbourne-Titusville, FL': '37340',
				 'Panama City, FL': '37460',
				 'Pensacola-Ferry Pass-Brent, FL': '37860',
				 'Peoria, IL': '37900',
				 'Philadelphia-Camden-Wilmington, PA-NJ-DE': '37980',
				 'Phoenix-Mesa-Scottsdale, AZ': '38060',
				 'Pine Bluff, AR': '38220',
				 'Pittsburgh, PA': '38300',
				 'Port St. Lucie-Fort Pierce, FL': '38940',
				 'Portland-South Portland, ME': '38860',
				 'Portland-Vancouver-Hillsboro, OR-WA': '38900',
				 'Poughkeepsie-Newburgh-Middletown, NY*': '39100',
				 'Prescott, AZ': '39140',
				 'Providence-Fall River-Warwick, RI-MA': '77200',
				 'Providence-Warwick, RI-MA': '39300',
				 'Provo-Orem, UT': '39340',
				 'Pueblo, CO*': '39380',
				 'Punta Gorda, FL*': '39460',
				 'Racine, WI': '39540',
				 'Raleigh, NC': '39580',
				 'Reading, PA': '39740',
				 'Redding, CA': '39820',
				 'Reno-Sparks, NV*': '39900',
				 'Richmond, VA': '40060',
				 'Riverside-San Bernardino-Ontario, CA': '40140',
				 'Roanoke, VA': '40220',
				 'Rochester, NY': '40380',
				 'Rochester-Dover, NH-ME': '77350',
				 'Rockford, IL': '40420',
				 'Sacramento--Arden-ArcadeRoseville, CA': '40900',
				 'Saginaw, MI': '40980',
				 'Salem, OR': '41420',
				 'Salinas, CA': '41500',
				 'Salisbury, MD': '41540',
				 'Salt Lake City, UT': '41620',
				 'San Antonio, TX': '41700',
				 'San Diego-Carlsbad-San Marcos, CA': '41740',
				 'San Francisco-Oakland-Fremont, CA': '41860',
				 'San Jose-Sunnyvale-Santa Clara, CA': '41940',
				 'San Luis Obispo-Paso Robles, CA': '42020',
				 'Santa Barbara-Santa Maria-Goleta, CA*': '42060',
				 'Santa Cruz-Watsonville, CA': '42100',
				 'Santa Fe, NM': '42140',
				 'Santa Rosa-Petaluma, CA': '42220',
				 'Sarasota-Bradenton-Venice, FL*': '42260',
				 'Savannah, GA': '42340',
				 'Scranton--Wilkes-Barre, PA': '42540',
				 'Seattle-Tacoma-Bellevue, WA': '42660',
				 'Sherman-Dennison, TX': '43300',
				 'Shreveport-Bossier City, LA': '43340',
				 'Sioux Falls, SD': '43620',
				 'South Bend-Mishawaka, IN-MI': '43780',
				 'Spartanburg, SC': '43900',
				 'Spokane-Spokane Valley, WA': '44060',
				 'Springfield, IL': '44100',
				 'Springfield, MA': '44140',
				 'Springfield, MA-CT': '78100',
				 'Springfield, MO': '44180',
				 'Springfield, OH*': '44220',
				 'St. Cloud, MN*': '41060',
				 'St. George, UT': '41100',
				 'St. Louis, MO-IL': '41180',
				 'Stockton, CA': '44700',
				 'Syracuse, NY': '45060',
				 'Tallahassee, FL': '45220',
				 'Tampa-St. Petersburg-Clearwater, FL': '45300',
				 'Terre Haute, IN': '45460',
				 'Toledo, OH': '45780',
				 'Topeka, KS': '45820',
				 'Trenton, NJ': '45940',
				 'Tucson, AZ': '46060',
				 'Tulsa, OK': '46140',
				 'Tuscaloosa, AL*': '46220',
				 'Tyler, TX': '46340',
				 'Urban Honolulu, HI': '46520',
				 'Utica-Rome, NY': '46540',
				 'Valdosta, GA*': '46660',
				 'Vallejo-Fairfield, CA': '46700',
				 'Vero Beach, FL': '46940',
				 'Victoria, TX*': '47020',
				 'Vineland-Bridgeton, NJ': '47220',
				 'Virginia Beach-Norfolk-Newport News, VA-NC': '47260',
				 'Visalia-Porterville, CA': '47300',
				 'Waco, TX': '47380',
				 'Warner Robins, GA': '47580',
				 'Washington-Arlington-Alexandria, DC-VA-MD-WV': '47900',
				 'Waterbury, CT': '78700',
				 'Waterloo-Cedar Falls, IA': '47940',
				 'Watertown-Fort Drum, NY': '48060',
				 'Wausau, WI': '48140',
				 'Wichita Falls, TX': '48660',
				 'Wichita, KS': '48620',
				 'Williamsport, PA': '48700',
				 'Winchester, VA-WV': '49020',
				 'Winston-Salem, NC': '49180',
				 'Worcester, MA-C': '79600',
				 'Worcester, MA-CT': '49340',
				 'Yakima, WA*': '49420',
				 'York-Hanover, PA': '49620',
				 'Youngstown-Warren-Boardman, OH-PA': '49660',
				 'Yuma, AZ': '49740'}