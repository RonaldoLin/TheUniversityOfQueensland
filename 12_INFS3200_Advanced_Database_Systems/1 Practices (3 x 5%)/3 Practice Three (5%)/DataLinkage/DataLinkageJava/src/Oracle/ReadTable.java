package Oracle;

import Data.Restaurant;

public class ReadTable {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DBConnection.OpenConnection();
		String query = "SELECT * FROM RESTAURANT";
		Restaurant[] restaurants = DBConnection.ExecuteQuery(query);
		DBConnection.CloseConnection();
		
		Restaurant restaurant = null;
		for (int i = 0; i < restaurants.length; i++) {
			restaurant = restaurants[i];
			System.out.println(restaurant.GetID() + "," + restaurant.GetName() + "," + restaurant.GetAddress() + ","
					+ restaurant.GetCity());
		}
		System.out.println(restaurants.length + " records in total.");
		
	}
	
}
