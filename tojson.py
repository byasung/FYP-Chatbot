import json
x = {
	"lib_info": {
		"Main Library": {
			"address": "Main Library, University of Hong Kong, Pokfulam, Hong Kong",
			"email": "libis@hku.hk",
			"phone": "(852) 3917-2203",
			"fax": "(852) 2559-5045",
			"services": "1",
			"direction": "MTR to HKU Station, walk via University Street and turn left on the split road",
			"opening_hours": [{
					"date": "weekdays",
					"open_time": "9:00 am",
					"close_time": "9:00 pm"
				},
				{
					"date": "saturday",
					"open_time": "9:00 am",
					"close_time": "6:00 pm"
				}, {
					"date": "sunday",
					"open_time": "10:00 am",
					"close_time": "6:00 pm"
				}
			]
		},
		"Dental Library": {
			"address": "5th Floor and 6th Floor, Prince Philip Dental Hospital, 34 Hospital Road, Sai Ying Pun, Hong Kong",
			"email": "denlib@hku.hk",
			"phone": "(852) 2859-0402",
			"services": "",
			"direction": "https: //lib.hku.hk/images/denlib/HKU-Dental%20Lib%20Map.jpg",
			"opening_hours": [{
					"date": "weekdays",
					"open_time": "8:30 am",
					"close_time": "10:00 pm"
				},
				{
					"date": "saturday",
					"open_time": "9:00 am",
					"close_time": "6:00 pm"
				}, {
					"date": "sunday",
					"open_time": '1',
					"close_time": '1'
				}
			]
		},
		"Fung Ping Shan Library": {
			"address": "4th - 6th floors, Main Library, University of Hong Kong, Pokfulam, Hong Kong",
			"email": "fpslib@hku.hk",
			"phone": "(852) 3917-2203",
			"fax": "(852) 2858-9420",
			"services": "1",
			"direction": "1",
			"opening_hours": [{
					"date": "weekdays",
					"open_time": "9:00 am",
					"close_time": "9:00 pm"
				},
				{
					"date": "saturday",
					"open_time": "9:00 am",
					"close_time": "6:00 pm"
				}, {
					"date": "sunday",
					"open_time": "10:00 am",
					"close_time": "6:00 pm"
				}
			]
		},
		"Lui Che Woo Law Library": {
			"address": "1-2/F, Cheng Yu Tung Tower, The University of Hong Kong, Pokfulam Road, Hong Kong ",
			"email": "lawlib@hku.hk",
			"phone": "(852) 3917-2914",
			"fax": "(852) 2548-0143",
			"services": "1",
			"direction": "1",
			"opening_hours": [{
					"date": "weekdays",
					"open_time": "9:00 am",
					"close_time": "10:00 pm"
				},
				{
					"date": "saturday",
					"open_time": "9:00 am",
					"close_time": "7:00 pm"
				}, {
					"date": "sunday",
					"open_time": "12:00 noon",
					"close_time": "4:00 pm"
				}
			]
		},
		"Music Library": {
			"address": "11/F, Run Run Shaw Tower, Centennial Campus, University of Hong Kong, Pokfulam Road, Hong Kong ",
			"email": "muslib@hku.hk",
			"phone": "(852) 3917-2218",
			"fax": "(852) 2549-9653",
			"services": "1",
			"direction": "1",
			"opening_hours": [{
					"date": "weekdays",
					"open_time": "9:00 am",
					"close_time": "8:00 pm"
				},
				{
					"date": "saturday",
					"open_time": "12:00 nn",
					"close_time": "5:00 pm"
				}, {
					"date": "sunday",
					"open_time": '1',
					"close_time": '1'
				}
			]
		},
		"Tin Ka Ping Education Library": {
			"address": "8/F, Meng Wah Complex, University of Hong Kong, Pokfulam, Hong Kong ",
			"email": "edulib@hku.hk",
			"phone": "(852) 3917-2205",
			"fax": "1",
			"services": "1",
			"direction": "1",
			"opening_hours": [{
					"date": "weekdays",
					"open_time": "9:00 am",
					"close_time": "9:00 pm"
				},
				{
					"date": "saturday",
					"open_time": "9:00 am",
					"close_time": "6:00 pm"
				}, {
					"date": "sunday",
					"open_time": '1',
					"close_time": '1'
				}
			]
		},
		"Yu Chun Keung Medical Library": {
			"address": "LG1, William MW Mong Block, 21 Sassoon Road, University of Hong Kong, Pokfulam, Hong Kong ",
			"email": "medlib@hku.hk",
			"phone": "(852) 3917-9215",
			"fax": "(852) 2855-9343",
			"services": "24-hour Study Room",
			"direction": "https://www.med.hku.hk/f/page/37/2559/transportationmap.pdf",
			"opening_hours": [{
					"date": "weekdays",
					"open_time": "8:15 am",
					"close_time": "11:00 pm"
				},
				{
					"date": "saturday",
					"open_time": "8:30 am",
					"close_time": "7:00 pm"
				}, {
					"date": "sunday",
					"open_time": "10:00 am",
					"close_time": "5:00 pm"
				}
			]
		}
	}
}

with open('data.txt','w') as outfile:
  json.dump(x,outfile)
