import java.sql.*;
import java.util.Scanner;

public class testConnection {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/studydatabase",
                    "root",
                    "yosef@6607???"
            );
            if (conn != null) {
                System.out.println("Connection successful");
                Scanner scanner = new Scanner(System.in);
                System.out.print("Enter table name: ");
                String tableName = scanner.nextLine();
                System.out.print("Enter column name: ");
                String columnName = scanner.nextLine();
                String query = "SELECT " + columnName + " FROM " + tableName;
                Statement stmt = conn.createStatement();
                ResultSet rs = stmt.executeQuery(query);
                while (rs.next()) {
                    System.out.println(rs.getString(columnName));
                }
                scanner.close();
                rs.close();
                stmt.close();
                conn.close();
            }
        } catch (ClassNotFoundException | SQLException e) {
            System.out.println("Connection error: " + e.getMessage());
        }
    }
}
