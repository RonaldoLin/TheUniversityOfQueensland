package Data;

import java.util.*;

public class Similarity {
	
	public static double CalcuJaccard(String str1, String str2, int q) {
		HashSet<String> str1Tokens = Tokenize(str1, q); 
		HashSet<String> str2Tokens = Tokenize(str2, q); 

        HashSet<String> allTokens = new HashSet<String>(); 
        allTokens.addAll(str1Tokens);
        allTokens.addAll(str2Tokens);
 
        return (double) ((str1Tokens.size() + str2Tokens.size()) - allTokens.size()) / (double) (allTokens.size()); 
	}
	
	private static HashSet<String> Tokenize(String str, int q) {
		HashSet<String> tokens = new HashSet<String>();
		if (q == 0) {
			String[] temp = str.split(" ");
			for (int i = 0; i < temp.length; i++)
				tokens.add(temp[i]);
		} else {
			for (int i = 0; i < str.length() - q + 1; i++)
				tokens.add(str.substring(i, i + q));
		}
		return tokens;
	}
	
	public static double CalcuEDSim(String str1, String str2) {
		if (str1.equals(str2))
			return 1;
		
		int ed = CalcuED(str1, str2);
		return (1 - (double) ed / Math.max(str1.length(), str2.length()));
	}
	
	private static int CalcuED(String str1, String str2) {
		int ed = 0;
		
		/*
		 * Please implement the calculation of edit distance between two strings
		 * Dynamic programming should be used
		 */
		
		return ed;
	}
}
