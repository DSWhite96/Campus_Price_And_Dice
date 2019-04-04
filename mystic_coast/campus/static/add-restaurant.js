var app = new Vue({
    el:'#app',
    data:{
		message: 'testing',
		restaurantName: "",
		restaurantLocation: "",
		itemPrice: 0,
		itemName: "",
		itemList: new Array(),
		showFirstTab: true,
		showSecondTab: false
    },
	methods:{
		addItem : function () {
			let name = this.itemName;
			let price = this.itemPrice;
			this.itemList.push();
		},
		removeItem : function (index) {
			this.itemList.splice(index, 1);
		},
		gotoFirst : function () {
			if (!this.showFirstTab)
			{
				this.showFirstTab = true;
				this.showSecondTab = false;
			}
		},
		gotoSecond : function () {
			if (!this.showSecondTab)
			{
				this.showSecondTab = true;
				this.showFirstTab = false;
			}
		},
		addRestaurantAction : function () {
			
		}
	}

//add_restaurant_action


});
