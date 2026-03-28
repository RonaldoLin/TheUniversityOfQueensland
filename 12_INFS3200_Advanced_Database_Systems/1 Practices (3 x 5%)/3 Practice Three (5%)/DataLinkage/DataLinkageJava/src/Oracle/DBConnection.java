package Oracle;

import java.sql.*;
import java.util.*;

import Data.Restaurant;

public class DBConnection {

	private static String driver = "oracle.jdbc.driver.OracleDriver";
	private static String url = "jdbc:oracle:thin:@localhost:1521:orcl";
	private static String username = "S1234567";
	private static String password = "w";
	private static Connection con = null;
	private static Statement stmt = null;

	public static void OpenConnection() {
		try {
			// load the driver class
			Class.forName(driver);

			// create the connection object
			con = DriverManager.getConnection(url, username, password);
			
			// create the statement object
			stmt = con.createStatement();

		} catch (Exception e) {
			System.out.println(e);
		}

	}
	
	public static void ExecuteUpdate(String update) {
		try {
			// execute update
			stmt.executeUpdate(update);

		} catch (Exception e) {
			System.out.println(e);
		}
	}
	
	public static Restaurant[] ExecuteQuery(String query) {
		List<Restaurant> restaurantList = new ArrayList<Restaurant>();
		try {
			// execute query
			ResultSet rs = stmt.executeQuery(query);
			while (rs.next()) {
				int id = rs.getInt(1);
				String name = rs.getString(2);
				String address = rs.getString(3);
				String city = rs.getString(4);
				Restaurant restaurant = new Restaurant(id, name, address, city);
				restaurantList.add(restaurant);
			}

		} catch (Exception e) {
			System.out.println(e);
		}
		
		Restaurant[] restaurants = new Restaurant[restaurantList.size()];
		Iterator<Restaurant> it = restaurantList.iterator();
		for (int i = 0; i < restaurantList.size(); i++)
			restaurants[i] = it.next();
		return restaurants;
	}

	public static void CloseConnection() {
		try {
			// close the connection object
			con.close();
			
		} catch (Exception e) {
			System.out.println(e);
		}
	}
}

