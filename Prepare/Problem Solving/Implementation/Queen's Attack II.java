import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public final class Solution{
    public static void main(String[] args){
        int arraySize, qRow, qCol;
        
         HashSet<List<Integer>> s = new HashSet<>();
         try (Scanner in = new Scanner(System.in)) {
        
        arraySize = in.nextInt();
        int numberObstacles = in.nextInt();
         qRow= in.nextInt();
         qCol= in.nextInt();
         while(numberObstacles-->0){
             int obsRow = in.nextInt();
             int obsCol = in.nextInt();
             s.add(Arrays.asList(obsRow, obsCol));
         }
         }
         
         int position[][] = new int[][]{{0,1}, {1,0}, {-1,0},{0,-1}, {1,1},{-1,1},{1,-1},{-1,-1}}; 
         long ans=0;
         for(int i=0; i<position.length;i++){
             int row = qRow+position[i][0];
             int col = qCol+position[i][1];
             while(!s.contains(Arrays.asList(row, col))){
                //  System.out.println(s.contains(Arrays.asList(row, col)));
                //  System.out.printf("using:(%d,%d)==> %d, %d\n", position[i][0], position[i][0], row, col);
                 if( row <1 || row > arraySize){
                     break;
                 }
                 if( col <1 || col > arraySize){
                     break;
                 }
                 ans+=1;
                 
                 
                 row+=position[i][0];
                 col+=position[i][1];
             }
             
         }
             System.out.println(ans);
        
        
        
    }
}
