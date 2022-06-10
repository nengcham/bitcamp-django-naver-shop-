from context.domains import Reader, File, Printer
import folium


class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.printer = Printer()
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.file.context = './data/'

    def save_police_pos(self):
        file = self.file
        file.fname = 'crime_in_seoul'
        crime = self.csv(file)
        station_names = []
        for name in crime['관서명']:
            station_names.append(f'서울{str(name[:-1])}경찰서')
        # print(f'station_names range: {len(station_names)}')  #서울시내 경찰서는 총 31개
        # for i, name in enumerate(station_names):
        #     print(f'name {i} = {name}')
        gmaps = self.gmaps()
        # a = gmaps.geocode('서울종암경찰서', language='ko')
        # print(a)
        '''
        [{'address_components': 
            [{'long_name': '３２９', 'short_name': '３２９', 'types': ['premise']}, 
            {'long_name': '백범로', 'short_name': '백범로', 'types': ['political', 'sublocality', 'sublocality_level_4']}, 
            {'long_name': '용산구', 'short_name': '용산구', 'types': ['political', 'sublocality', 'sublocality_level_1']}, 
            {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']}, 
            {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']}, 
            {'long_name': '140-111', 'short_name': '140-111', 'types': ['postal_code']}], 
            'formatted_address': '대한민국 서울특별시 용산구 백범로 329', 
            'geometry': {'location': 
                {'lat': 37.5387099, 'lng': 126.9659183}, 
                'location_type': 'ROOFTOP', 
                'viewport': {'northeast': {'lat': 37.5400588802915, 'lng': 126.9672672802915}, 
                'southwest': {'lat': 37.5373609197085, 'lng': 126.9645693197085}}}, 
                'partial_match': True, 'place_id': 'ChIJhbgEHxKifDURLOHanwAKdJI', 
                'plus_code': {'compound_code': 'GXQ8+F9 대한민국 서울특별시', 'global_code': '8Q98GXQ8+F9'}, 
                'types': ['establishment', 'point_of_interest', 'police']}]
        
        서울종암경찰서는 2021.12.20에 이전해 구글맵에 등록이 되어있지 않다. 
        '''
        station_addrs = []
        station_lats = []
        station_lngs = []
        print(station_names[21])
        for i, name in enumerate(station_names):
            if name != '서울종암경찰서':
                temp = gmaps.geocode(name, language='ko')
            else:
                temp = [{'address_components':
            [{'long_name': '３２', 'short_name': '３２', 'types': ['premise']},
            {'long_name': '화랑로7길', 'short_name': '화랑로7길', 'types': ['political', 'sublocality', 'sublocality_level_4']},
            {'long_name': '성북구', 'short_name': '성북구', 'types': ['political', 'sublocality', 'sublocality_level_1']},
            {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']},
            {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']},
            {'long_name': '140-111', 'short_name': '140-111', 'types': ['postal_code']}],
            'formatted_address': '대한민국 서울특별시 성북구 화랑로7길 32',
            'geometry': {'location':
                {'lat': 37.6038816, 'lng': 127.0400157},
                'location_type': 'ROOFTOP',
                'viewport': {'northeast': {'lat': 37.60388169879458, 'lng': 127.04001571848704},
                'southwest': {'lat': 37.60388169879458, 'lng': 127.04001571848704}}},
                'partial_match': True, 'place_id': 'ChIJhbgEHxKifDURLOHanwAKdJI',
                'plus_code': {'compound_code': 'GXQ8+F9 대한민국 서울특별시', 'global_code': '8Q98GXQ8+F9'},
                'types': ['establishment', 'point_of_interest', 'police']}]
            print(f'name {i} = {temp[0].get("formatted_address")}')


    def save_cctv_pos(self):
        file = self.file
        file.fname = 'cctv_in_seoul'
        cctv = self.csv(file)
        file.fname = 'pop_in_seoul'
        pop = self.xls(file=file, header=1, cols='B,D,G,J,N', skiprows=[2])
        print(pop)

    def save_police_norm(self):
        pass

    def folium_test(self):
        file = self.file
        file.fname = 'us-states.json'
        states = self.new_file(file)

        file.fname = 'us_unemployment'
        unemployment = self.csv(file)

        bins = list(unemployment["Unemployment"].quantile([0, 0.25, 0.5, 0.75, 1]))
        m = folium.Map(location=[39, -97], zoom_start=5)
        folium.Choropleth(
            geo_data=states, # dataframe 타입이 아닌 json
            name="choropleth",
            data=unemployment,
            columns=["State", "Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name="Unemployment Rate (%)",
            bins=bins,
            reset=True
        ).add_to(m)
        m.save("./save/folium_test.html")

    def draw_crime_map(self):
        file = self.file
        file.fname = 'geo_simple'
        print(self.json(file))


if __name__ == '__main__':
    s = Solution()
    # s.save_police_pos()
    # s.save_cctv_pos()
    # s.draw_crime_map()
    s.folium_test()

