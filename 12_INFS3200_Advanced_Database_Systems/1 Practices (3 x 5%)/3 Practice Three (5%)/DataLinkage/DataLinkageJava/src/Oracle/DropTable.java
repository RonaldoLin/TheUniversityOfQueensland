package Oracle;

public class DropTable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DBConnection.OpenConnection();
		String update = "DROP TABLE RESTAURANT";
		DBConnection.ExecuteUpdate(update);
		DBConnection.CloseConnection();
	}

}
