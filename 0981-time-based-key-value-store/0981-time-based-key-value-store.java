class TimeMap {
//to store key Value Pair, we will use Hash Map
//here for a single key we can have lots of value, so to store value we will use List 
//as the value will store value with time stamp so for Value we will use Pair class of Java
//Pair will hold <Value, TimeStamp>
HashMap<String, List<Pair<String, Integer>>> map;

    public TimeMap() {
        //We will initialize our map
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        //we will only set the key if it is not present in the map, for that we will use "putIfAbsent" method
        map.putIfAbsent(key, new ArrayList<>());
        //now we have to add the value in list
        //map.get will return the list for that particular key, in that list only we will add our value
        map.get(key).add(new Pair<String, Integer>(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        //we have to return the value in get method
        //So if the key is not present in the map means we can't find value, so we will return "", 
        //so we will store "" in our initial result
        String res = "";
        //we will do our all process if the map contains that key, else we will return empty string
        if(map.containsKey(key) == true){
            List<Pair<String, Integer>> temp = map.get(key);
            //now here we have to return the value with the timestamp which is near to the given timestamp
            /*
            example we have, map with foo, {<bar,1>, <bar2,2>}
    now if we call get(foo, 3), so 3 is not there in timestamp, so it should return bar2 whose timestamp is 2
             */
             //Since the time stamp is in increasing order we can apply Binary search on it
             int low = 0, high = temp.size()-1;
             while(low <= high){ //here <= is bcz if we want to include last timestamp also
             int mid = (low + high) / 2;
//here we will check if our current timesatamp <= timestamp or not, if yes we will search for more closer timestamp
                if(temp.get(mid).getValue() <= timestamp){
                    res = temp.get(mid).getKey();
                    //Now we will search for more closer timestamp
                    low = mid + 1;
                }
                else{ //we got a higher time stamp, so we will search for lesser timestamp
                    high = mid - 1;
                }
             }
        }
        return res;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */