package Oracle;

import java.io.*;

public class InsertTable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DBConnection.OpenConnection();

		try {
			File file = new File("data\\restaurant.csv");
			if (!file.exists())
				System.out.println("No file");
			BufferedReader reader = new BufferedReader(new FileReader(file));
			String line = null, insert = null;
			String[] tokens = null;
			while ((line = reader.readLine()) != null) {
				line = line.replaceAll("'", " ");
				tokens = line.split(",");
				insert = "INSERT INTO RESTAURANT VALUES (" + tokens[0] + ", '" + tokens[1] + "', '" + tokens[2] + "', '"
						+ tokens[3] + "')";
				DBConnection.ExecuteUpdate(insert);
			}
			reader.close();

		} catch (Exception e) {
			e.printStackTrace();
		}

		DBConnection.CloseConnection();
	}

}
