import json
import anytree as at
from flow_tables import FlowTables

def get_table_number(tn, name):
    for item in tn:
        if name in item['name']:
            return item['number']

def get_flow_tables(filename):
    with open(filename) as f:
        js = json.load(f)
        table_numbers = list(js['table_map'])
        ft = []
        for item in js['flow_tables']:   
            for fl_md_tp in item['flow_mod_types']:
                temp = {}
                temp['fl_md_name'] = fl_md_tp['name']
                temp['match_set']  = fl_md_tp['match_set']
                temp['instruction']  = fl_md_tp['instruction_set']
            ft.append(FlowTables(item['name'], get_table_number(table_numbers, item['name']), temp))
        return ft

def print_flow_tables(filename):
    with open(filename) as f:
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

def print_entry_types(filename):
    with open(filename) as f:
        js = json.load(f)
        for item in js['group_entry_types']:   
            print('FT name', item['name'], '| FM type', item['group_type'])
            for ac_set in item['bucket_types']:
                print('NAME', ac_set['name'])
                for s in ac_set['action_set']:
                    try:
                        if s['action'] == 'OUTPUT':
                            print('PORT', s['port'])
                        if s['action'] == 'SET_FIELD':
                            print('PORT', s['field'], '| VALUE', s['value'])
                    except KeyError:
                        print('no output/field')
                        continue
            print('\n')

ft = get_flow_tables('ttp_input')
for f in ft:
    print(f.name, '=>', f.get_next_tables())
flow_tables = at.Node(ft[0]) #PARENT => INGRESS TABLES
#print_flow_tables('ttp_input')
#print_entry_types('ttp_input')
