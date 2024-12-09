package IntegrateDB;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;



public class PostgreSQLExample {


    static void PrintDB(Connection connect){
        String SSQL = "SELECT * FROM data";

        try(PreparedStatement preparedStatement = connect.prepareStatement(SSQL);
        ResultSet response = preparedStatement.executeQuery()){
            while(response.next()){
                System.out.println(response.getString("name")+" "+response.getString("password"));
            }

        }
        catch (Exception e) {
            System.err.println("Error in print: "+e);
        }


    }

    static void addToDB(String name, String password, Connection connect){
        String SSQL = "INSERT INTO data (name, password) VALUES (?, ?)";
        try(PreparedStatement preparedStatement = connect.prepareStatement(SSQL)){
            preparedStatement.setString(1, name);
            preparedStatement.setString(2, password);
            preparedStatement.executeUpdate();
            System.out.println("Update with sucess");

        }
        catch (Exception e) {
            System.err.println("Update error: "+e);
        }

    }

    public static void main(String[] args) {
        String URL = "jdbc:postgresql://localhost:5432/users";
        String USER = "postgres";
        String PASSWORD = "abc2109";

        try(Connection connect = DriverManager.getConnection(URL, USER, PASSWORD)) {
            System.out.println("Connect with sucess");

            addToDB("Luzia", "434", connect);
            PrintDB(connect);


            connect.close();
            
        }
        catch(Exception e){
            System.err.println("Error with connect: "+e);
            
        }



        

    }
}
