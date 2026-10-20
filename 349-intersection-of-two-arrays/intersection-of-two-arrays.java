class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        int ar[]=new int[1001];

        ArrayList<Integer> al=new ArrayList<>();

        int n1=nums1.length;
        int n2=nums2.length;

        for(int i=0;i<n1;i++){
            ar[nums1[i]]++;
        }

        for(int i=0;i<n2;i++){
            if(ar[nums2[i]]!=0){
                al.add(nums2[i]);
                ar[nums2[i]]=0;
            }
        }

        int ans[]=new int[al.size()];
        
        for(int i=0;i<al.size();i++){
            ans[i]=al.get(i);
        }
        return ans;
    }
}