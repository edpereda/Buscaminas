/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Map;
import java.util.Properties;
import java.util.TreeMap;
import java.util.logging.Level;
import java.util.logging.Logger;
/**
 *
 * @author eliot
 */
public class Score {

    public String putNewScore(int segundos, int minutos, int hora, String nombre) 
    {
        String result="";
        String newKey = hora+":"+minutos+":"+segundos;
        try {
            //File file = new File("data.bin");
            File file = new java.io.File("data.bin");
             Map<String, String> ldapContent = new TreeMap<>();
            Properties properties = new Properties();
            if (!file.exists()) {
                 file.createNewFile();
            }
            else 
            {
                 properties.load(new FileInputStream(file));

                for (String key : properties.stringPropertyNames()) {
                    ldapContent.put(key, properties.get(key).toString());
                }
            }
            

            //Actualizar
            ldapContent.put(newKey, nombre);
            
            //Escribir
            properties = new Properties();
            
            int n = 1;
            for (Map.Entry<String,String> entry : ldapContent.entrySet()) {
                result+=n+"   :    "+entry.getValue()+"  :  "+entry.getKey()+"\n";
                properties.put(entry.getKey(), entry.getValue());
            }

            properties.store(new FileOutputStream("data.bin"), null);
            
            
        } catch (FileNotFoundException ex) {
            Logger.getLogger(Score.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(Score.class.getName()).log(Level.SEVERE, null, ex);
        }
        return result;
    }
    /**
     * @param args the command line arguments
     */
    /*public static void main(String[] args) {
        Score s = new Score();
       System.out.println( s.putNewScore(0, 3, 1, "Carlos"));
        // TODO code application logic here
    }*/
    
}

