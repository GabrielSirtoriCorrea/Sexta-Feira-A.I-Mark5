/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.friday.GazeboIndustries.com.br;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

/**
 *
 * @author Gazebo
 */
public class DataBaseConnection {
    private String url = "jdbc:sqlite:E:\\Sexta-Feira(A.I.)-Mark 5\\CommandsSQL.db";
    //private String url = "jdbc:sqlite:C:\\Users\\Gazebo\\Documents\\Testesqlite.db";
    Connection connection;
    Statement statement;
    PreparedStatement preparedStatement;
    ResultSet resultSet;
    
    public DataBaseConnection(){
        try {
            
            this.connection = DriverManager.getConnection(this.url);
            this.statement = this.connection.createStatement();
            
            this.statement.execute("CREATE TABLE IF NOT EXISTS Projects(NameProject TEXT, ProjectPlatform TEXT, ProjectFiles TEXT)");
            this.statement.execute("CREATE TABLE IF NOT EXISTS Reminder(ReminderName TEXT, Time TEXT, Date TEXT)");
            this.statement.execute("CREATE TABLE IF NOT EXISTS HomeWorkManagement(HomeWorkType TEXT, Subject TEXT, HomeWork TEXT, Delivery TEXT, HomeWorkDescription TEXT)");

            
        } catch (SQLException ex) {
            Logger.getLogger(DataBaseConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
  
    public String [] getHeadProjects(){
            String response[] = {"Nome", "Plataforma", "Arquivos"};
            return response;
    }
    
    public Object [][] getProjects(){
        Object response[][] = new Object[40][3];
        String Project;
        String Platform;
        String Files;
                
        int contador = 0;
        
        try { 
            this.resultSet =  this.statement.executeQuery("SELECT * FROM Projects");
           
            while(this.resultSet.next()){
                Project = this.resultSet.getString("NameProject");
                Platform = this.resultSet.getString("ProjectPlatform");
                Files = this.resultSet.getString("ProjectFiles");
                
                response[contador][0] = Project;
                response[contador][1] = Platform;
                response[contador][2] = Files;
                
                contador++;
                System.out.println(Arrays.deepToString(response));
            }

        } catch (SQLException ex) {
            Logger.getLogger(DataBaseConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
        return response;
        
        
    }
    
    public String [] getHeadReminder(){
            String response[] = {"Nome", "Hora", "Data"};
            return response;
    }
    
    public Object [][] getReminder(){
        Object response[][] = new Object[40][3];
        String Name;
        String Time;
        String Date;
                
        int contador = 0;
        
        try { 
            this.resultSet =  this.statement.executeQuery("SELECT * FROM Reminder");
           
            while(this.resultSet.next()){
                Name = this.resultSet.getString("ReminderName");
                Time = this.resultSet.getString("Time");
                Date = this.resultSet.getString("Date");
                
                response[contador][0] = Name;
                response[contador][1] = Time;
                response[contador][2] = Date;
                
                contador++;
                System.out.println(Arrays.deepToString(response));
            }

        } catch (SQLException ex) {
            Logger.getLogger(DataBaseConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
        return response;
        
        
    }
    
    public String [] getHeadHomeWork(){
            String response[] = {"Tipo", "Matéria", "Tarefa", "Entrega", "Descrição"};
            return response;
    }
    
    public Object [][] getHomeWorks(){
        Object response[][] = new Object[40][5];
        String Type;
        String Subject;
        String HomeWork;
        String Delivery;
        String Description;
                
        int contador = 0;
        
        try { 
            this.resultSet =  this.statement.executeQuery("SELECT * FROM HomeWorkManagement");
           
            while(this.resultSet.next()){
                Type = this.resultSet.getString("HomeWorkType");
                Subject = this.resultSet.getString("Subject");
                HomeWork = this.resultSet.getString("HomeWork");
                Delivery= this.resultSet.getString("Delivery");
                Description = this.resultSet.getString("HomeWorkDescription");
                
                response[contador][0] = Type;
                response[contador][1] = Subject;
                response[contador][2] = HomeWork;
                response[contador][3] = Delivery;
                response[contador][4] = Description;
                
                contador++;
                System.out.println(Arrays.deepToString(response));
            }

        } catch (SQLException ex) {
            Logger.getLogger(DataBaseConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
        return response;
           
    }
    
    public String[] getInteration(){
        String response[] = new String[2];
        
        /*try{
            this.resultSet = this.statement.executeQuery("SELECT * FROM InterfaceInteraction");
            
            if(this.resultSet.next()){
                response[0] = this.resultSet.getString("ID");
                response[1] = this.resultSet.getString("Data");
            
                System.out.println(Arrays.toString(response));
              
            }
            
            this.preparedStatement = connection.prepareStatement("UPDATE InterfaceInteraction SET Data = ? WHERE ID = ?");
            this.preparedStatement.setString(1, "1024");
            this.preparedStatement.setString(2, "512");
            this.preparedStatement.executeUpdate();
            
        }catch(SQLException e){
             Logger.getLogger(DataBaseConnection.class.getName()).log(Level.SEVERE, null, e);
        }*/
        
        JSONObject jsonObject = new JSONObject();
        JSONParser parser = new JSONParser();
        FileWriter writeFile = null;
        
        try{
            jsonObject = (JSONObject) parser.parse(new FileReader( "E:\\Sexta-Feira(A.I.)-Mark 5\\InterfaceInteraction.json"));
            
            response[0] =jsonObject.get("ID").toString();
            response[1] = jsonObject.get("Data").toString();
            
        }catch(FileNotFoundException e){
                e.printStackTrace();
                
        } catch (IOException e) {
            e.printStackTrace();
            
        } catch (ParseException e) {
            e.printStackTrace();
        }     
    
        System.out.println(Arrays.toString(response));
        return response;
    }
    
}