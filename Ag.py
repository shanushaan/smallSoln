import redis

# make the connection. 
conn = redis.StrictRedis(port="6391")

#1. Get the price for :200123
print conn.hgetall('booking:200123')['price_per_night']


#2. GEt the earliest checkin Date for 1042.
key = 'hotel_bookings:1042'
check_in_dates = []
for item in conn.lrange(key,0, conn.llen(key)):
    inner_key= "booking:"+str(item)
    check_in_dates.append(conn.hgetall(inner_key)['check_in_date'])

import time
check_in_dates.sort(key = lambda x:time.mktime(time.strptime(x, "%Y-%m-%d")))
print check_in_dates[0]



#3. get the highest five bookings.
top_5_bookings = conn.zrevrange('booking_prices',0,4,withscores=True)
print top_5_bookings

#4 . get total tax.
tax_hotel_ids = conn.smembers('hotels_charging_tax')
total_tax =0
total_booking_f_tax =0
for hotel in tax_hotel_ids:
    key = 'hotel_bookings:'+str(hotel)
    for item in conn.lrange(key,0, conn.llen(key)):
        booking_price = conn.zscore('booking_prices',item)
        total_booking_f_tax += booking_price

        #gettax and round it
        tax = (booking_price *7)/100
        tax = float ( "%.2f" %tax)
        total_tax += tax
print total_tax

