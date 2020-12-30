'''
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
'''

kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother', 'mother': 'ibu'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])
print(kamus_ind_eng['mother'])

print('\n Data ini dikirimkan oleh server gojek untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-12-30',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 30},
        {'nama': 'Tri', 'jarak': 100},
        {'nama': 'Catur', 'jarak': 1000}
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"\nDriver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"\nDriver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"\nDriver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
