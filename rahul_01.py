# SET name rahul
# MSET name rahulsingh age 21 city Greater Noida      -    multiple values write
# GET name 
# MGET name age city                                  -    multiple values read
# DEL name 
# EXISTS name

# SET username rhx_21 NX                              -    NX means =  Only set if key does NOT already exist.

# SET user:101:name rahul
# SET user:101:age 21
# GET user:101:name

# APPEND    -   String ke end mein data add karna

# APPEND name Singh

# STRLEN    -   String ki length

# STRLEN name

# GETDEL    -   Value read karke key delete kar sakte ho

# GETDEL name

# GETEX     -   Ye value retrieve karne ke saath expiration set/update kar sakta hai

# GETEX user:101 EX 60


# OTP

# SET otp:user:111 123456
# EXPIRE otp:user:111 30
# TTL otp:user:111

# OTP 

# SETEX otp:user:111 30 123456    or    SET otp:user:111 123456 EX 30

# Handle Number

# SET counter 10
# INCR counter        -  11      (Real-world Example - Page Views)
# INCR counter        -  12
# INCRBY counter 6    -  18
# DECR counter        -  17
# DECRBY counter 10    - 7

# KEYS *   -  saari keys dikha dega but in production we use -  SCAN 0

# STRING 

# SET user:123 '{"id":123, "name":"rahulsingh", "age":21}'
# SET session:abc123 "user:123"
# MSET name rahulsingh age 21 city Greater Noida 
# MGET name age city

# LIST

# LPUSH notifications "Order Delivered"  -   LPUSH use for add items from left side
# RPUSH notifications "Give Feedback"    -   RPUSH use for add items from right side
# RPOP notifications                     -   ek-ek karke read karna
# LRANGE notifications 0 -1              -   List se data read karna ( 0 - first item, 1 - last item)

# SET  -  Set ka real-world use (Online users,User interests,Tags)

# SADD online_users 101  
# SADD online_users 102
# SADD online_users 103
# SMEMBERS online_users
# SISMEMBER online_users 102             -  User 102 online users ke Set mein hai.

# HASH   -  fields + values   (Ye database ke ek record jaisa feel hota hai. USE - Redis mein user ka cached data)

# HSET user:212 name "rahulSingh"
# HSET user:212 age 21
# HSET user:212 city "Greater Noida"
# HGET user:212 name                     -  Use for single field
# HMGET user:212 name age city           -  Use for multiple field
# HGETALL user:212                       -  Use for Entire Hash

# SORTED SET   -   Use in Gaming leaderboard, Ranking, Popular products, Trending content, Top users, Scores

# ZADD leaderboard 950 vaibhav
# ZADD leaderboard 850 sachin
# ZADD leaderboard 970 rahul
# ZRANGE leaderboard 0 -1 WITHSCORES

# STREAM   -  event/message stream