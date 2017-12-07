import json

def get_table_number(tn, name):
    for item in tn:
        if name in item['name']:
            return item['number']

with open('ttp_input') as f:
    js = json.load(f)
    table_numbers = list(js['table_map'])
    for item in js['flow_tables']:   

        print('FT name', item['name'], '| Tb nbmr', get_table_number(table_numbers, item['name']))

        for fl_md_tp in item['flow_mod_types']:
            print('Flow mod name:', fl_md_tp['name'])

            for field in fl_md_tp['match_set']:
                print('MATCH FIELD', field['field'],'MATCH TYPE',field['match_type'])

            for instruction in fl_md_tp['instruction_set']:
                try:
                    if instruction['instruction'] == 'GOTO_TABLE':
                        print('TABLE', instruction['table'])
                except KeyError:
                    print('no_next_table')
                    continue
        print('\n')

