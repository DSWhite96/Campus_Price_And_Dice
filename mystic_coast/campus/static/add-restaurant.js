import { hoursOfOperation } from './hours-of-operation.js';

var app = new Vue({
	delimiters: ['[[',']]'],
	el:'#app',
	data:{
			restaurantName: "",
			restaurantLocation: "",
			restaurantPhoneNumber: "",
			hoursOfOperation: hoursOfOperation,
			itemName: "",
			itemPrice: 0,
			itemList: new Array(),
			showFirstTab: true,
			showSecondTab: false
	},
	methods:{
		addItem: function () {
			let name = this.itemName;
			let price = this.itemPrice;

			let item = {
				name: name,
				price: price
			};

			this.itemList.push(item);
		},
		removeItem: function (index) {
			this.itemList.splice(index, 1);
		},
		goToFirst: function () {
			if (!this.showFirstTab)
			{
				this.showFirstTab = true;
				this.showSecondTab = false;
			}
		},
		goToSecond: function () {
			if (!this.showSecondTab)
			{
				this.showSecondTab = true;
				this.showFirstTab = false;
			}
		},
		packageData: function() {
			let packagedData = {
				restaurantName: this.restaurantName,
				restaurantLocation: this.restaurantLocation,
				restaurantPhoneNumber: this.restaurantPhoneNumber,
				hoursOfOperation: this.hoursOfOperation,
				itemList: this.itemList
			};

			return JSON.stringify(packagedData);
		},
		submitData: function() {

			let form = document.getElementById("restaurant_form");
			let xHttp = new XMLHttpRequest();

			xHttp.open('/campus/add_restaurant_action', true);

			let packagedData = this.packageData();

			/*xHttp.onreadystatechange = function() {
				if (xHttp.readyState == 4 && xHttp.status == 200) {

				}
			};*/

			xHttp.send(packagedData);
			//location.reload();
		}
	}
	
});
