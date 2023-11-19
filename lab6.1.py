total_party_a=0
total_party_b=0
total_party_c=0
country_total_party_a=0
country_total_party_b=0
country_total_party_c=0
for i in range(1,3):
    quota=int(input("milletcekili kontenjanı:"))
    print(f"Partilerin {i}. şehirindeki oyunu yazınız. ")
    party_a=int(input("oyu:"))
    party_b=int(input("oyu:"))
    party_c=int(input("oyu:"))
    while quota>0:
        if party_a>party_b and party_a>party_c:
            quota-=1
            total_party_a+=1
            party_a/=2
        elif party_b>party_a and party_b>party_c:
            quota-=1
            total_party_b+=1
            party_b/=2
        elif party_c>party_b and party_c>party_a:
            quota-=1
            total_party_c+=1
            party_c/=2

    country_total_party_a+=total_party_a
    country_total_party_b+=total_party_b
    country_total_party_c+=total_party_c
print(country_total_party_a)
print(country_total_party_b)
print(country_total_party_c)
print(country_total_party_a+country_total_party_b+country_total_party_c)
    
