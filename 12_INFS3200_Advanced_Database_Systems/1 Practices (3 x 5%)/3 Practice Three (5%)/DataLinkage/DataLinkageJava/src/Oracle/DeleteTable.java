package Oracle;

public class DeleteTable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DBConnection.OpenConnection();
		String update = "DELETE FROM RESTAURANT";
		DBConnection.ExecuteUpdate(update);
		DBConnection.CloseConnection();
	}

}
