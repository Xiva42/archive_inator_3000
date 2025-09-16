import httplib2 as hlib

FORMAT = "utf-8"
str_data = "NULL"

h = hlib.Http(".cache")
(resp, data) = h.request("https://valorant.fandom.com/wiki/Status_Effect", "GET")

print("From Cache:", resp.fromcache)

print("\n respons:")
for d in resp:
    print("part of response: ",d ," -->> ", resp[d])

print("\nData length:", len(data))
print("first part of data", data[:70])

#str_data = data.decode(FORMAT)

val_buffs = str_data.find()



#################### This is using urllib instead of httplib2 to achive the same thing without using caches #######################

# from http.client import HTTPConnection
# HTTPConnection.debuglevel = 1

# from urllib.request import urlopen


# url = "https://www.imdb.com/title/tt1631867/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_edge%2520of%2520t"


# resp = urlopen(url).read()


# print(resp)

