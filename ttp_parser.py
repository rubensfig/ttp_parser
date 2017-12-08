import json
import anytree as at
from flow_tables import FlowTables

def get_table_per_name(table_list, name):
    for item in table_list:
        if name in item.name:
            return item

def get_table_number(tn, name):
    try:
        for item in tn:
            if name in item['name']:
                return item['number']
    except TypeError:
        return ''

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
                #print(temp['instruction'])
                ft.append(FlowTables(item['name'], get_table_number(table_numbers, item['name']), temp))
        return ft

def get_group_entries(filename):
    with open(filename) as f:
        js = json.load(f)
        ge = []
        for item in js['group_entry_types']:   
            #print('FT name', item['name'], '| FM type', item['group_type'])
            for ac_set in item['bucket_types']:
                print('NAME', ac_set['name'])
                print(ac_set)
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
            print(item)
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
#ge = get_group_entries('ttp_input')
# print(ft[0].fl_md_tp['instruction'])
# with open('ttp_input') as b:
    # js = json.load(b)
    # table_numbers = list(js['table_map'])
    # table_no =  get_table_number(table_numbers, ft[0].name)
    # print(table_no,  ft[0].get_next_tables())
# for f in ft:
    # temp = f.get_next_tables()
    # with open('ttp_input') as b:
        # js = json.load(b)
        # table_numbers = list(js['table_map'])
        # table_no =  get_table_number(table_numbers, temp)
    # print(f.name, f.table_no, '=>', temp, table_no)
#pol_acl = get_table_per_name(ft, 'Policy ACL')
#pol_acl.print_structures_per_table()

# flow_tables = at.Node(ft[0]) #PARENT => INGRESS TABLES
#print_flow_tables('ttp_input')
print_entry_types('ttp_input')
