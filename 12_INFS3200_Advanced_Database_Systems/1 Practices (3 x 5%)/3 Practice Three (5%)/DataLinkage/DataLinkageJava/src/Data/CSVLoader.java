package Data;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class CSVLoader {
	
	public static Restaurant[] restaurantLoader(String filePath) {
		List<Restaurant> restaurantList = new ArrayList<Restaurant>();
		try {
			File file = new File(filePath);
			if (!file.exists())
				System.out.println("No file");
			BufferedReader reader = new BufferedReader(new FileReader(file));
			String line = null, insert = null;
			String[] tokens = null;
			
			while ((line = reader.readLine()) != null) {
				line = line.replaceAll("'", " ");
				tokens = line.split(",");
				Restaurant restaurant = new Restaurant(Integer.parseInt(tokens[0]), tokens[1], tokens[2], tokens[3]);
				restaurantList.add(restaurant);
			}
			reader.close();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		return restaurantList.toArray(new Restaurant[0]);
	}
}
