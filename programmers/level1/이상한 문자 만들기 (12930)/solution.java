package sad20;

class Solution {
    public String solution(String s) {
		int n;
        String []tokens = s.split(" ");
        String answer = "";
        for (int i=0;i<tokens.length;i++){
            n = tokens[i].length();
            if (n!=0){
	            for (int j=0;j<n;j++){
	                char tmp = tokens[i].charAt(j);
	                if (j%2==0){ //Â¦¼ö
	                	if (('a'<=tmp) && (tmp<='z'))
	                        tmp = (char)(tmp-32);
	                }
	                else{ //È¦¼ö
	                    if (('A'<=tmp) && (tmp<='Z'))
	                        tmp = (char)(tmp+32);
	                }
	                answer+=tmp;
	            }
	            if (i!=tokens.length-1)
	            	answer+=" ";
            }
            else
            	answer+=" ";
        }
        if (s.length()>answer.length()) {
        	for (int i=answer.length(); i<s.length();i++)
        		answer+=" ";
        }
        return answer;
    }
}