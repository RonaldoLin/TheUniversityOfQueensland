package Oracle;

public class CreateTable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DBConnection.OpenConnection();
		String create = "CREATE TABLE RESTAURANT("
				+ "ID NUMBER NOT NULL,"
				+ "NAME VARCHAR2(100 BYTE) NOT NULL,"
				+ "ADDRESS VARCHAR2(255 BYTE) NOT NULL,"
				+ "CITY VARCHAR2(50 BYTE) NOT NULL,"
				+ "CONSTRAINT RESTAURANT_PK PRIMARY KEY(ID) ENABLE)";
		DBConnection.ExecuteUpdate(create);
		DBConnection.CloseConnection();
	}

}
