import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashSet;

import org.fnlp.nlp.cn.CNFactory;


public class SentenceSegment {

	static String readFile(String fileName) throws IOException {
	    BufferedReader br = new BufferedReader(new FileReader(fileName));
	    try {
	        StringBuilder sb = new StringBuilder();
	        String line = br.readLine();

	        while (line != null) {
	            sb.append(line);
	            sb.append("\n");
	            line = br.readLine();
	        }
	        return sb.toString();
	    } finally {
	        br.close();
	    }
	}
	
	static void writeFile(String fileName, StringBuffer buf) throws IOException {
		BufferedWriter bw = new BufferedWriter(new FileWriter(fileName));
		bw.write(buf.toString());
		bw.close();
	}
	
	public static void main(String[] args) throws Exception {
		String inputstring = readFile(args[0]);
	    CNFactory factory = CNFactory.getInstance("models");
	    HashSet<String> biaodian = new HashSet<String>();
	    biaodian.add("，");
	    biaodian.add("。");
	    biaodian.add("！");
	    biaodian.add("？");
	    
	    String[] words = factory.seg(inputstring);
	    StringBuffer result = new StringBuffer();
	    for(int i=0; i<words.length; i++) {
	    	if (biaodian.contains(words[i])) result.append(words[i]+"\n");
	    	else result.append(words[i]+" ");
	    }
	    writeFile("output"+args[0], result);
	}
}
