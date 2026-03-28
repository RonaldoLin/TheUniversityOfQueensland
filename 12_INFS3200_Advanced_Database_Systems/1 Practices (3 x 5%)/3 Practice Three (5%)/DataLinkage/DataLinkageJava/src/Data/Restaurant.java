package Data;

public class Restaurant {

	private int id;
	private String name;
	private String address;
	private String city;
	
	public Restaurant (int id, String name, String address, String city) {
		this.id = id;
		this.name = name;
		this.address = address;
		this.city = city;
	}

	public int GetID() {
		return id;
	}

	public void SetID(int id) {
		this.id = id;
	}

	public String GetName() {
		return name;
	}

	public void SetName(String name) {
		this.name = name;
	}

	public String GetAddress() {
		return address;
	}

	public void SetAddress(String address) {
		this.address = address;
	}

	public String GetCity() {
		return city;
	}

	public void SetCity(String city) {
		this.city = city;
	}
}
