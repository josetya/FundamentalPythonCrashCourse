"""
memahami dictionary

"""

data_server_gojek = {
    'tanggal' : '2020-30-10',
    'list_driver' : [
        {'nama': 'eka', 'jarak': 40},
        {'nama' : 'dwi', 'jarak' : 20},
        {'nama' : 'tri', 'jarak' : 100}
    ]
}
print(f"jarak driver #2 : {data_server_gojek['list_driver'][1]['jarak']} km")
