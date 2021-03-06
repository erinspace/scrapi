'''
Harvester for the VCU Scholars Compass for the SHARE project

Example API call: http://scholarscompass.vcu.edu/do/oai/?verb=ListRecords&metadataPrefix=oai_dc
'''
from __future__ import unicode_literals

from scrapi.base import OAIHarvester


class Scholarscompass_vcuHarvester(OAIHarvester):
    short_name = 'scholarscompass_vcu'
    long_name = 'VCU Scholars Compass'
    url = 'http://scholarscompass.vcu.edu'

    base_url = 'http://scholarscompass.vcu.edu/do/oai/'
    property_list = ['date', 'source', 'format', 'identifier', 'type', 'setSpec']
    timezone_granularity = True
    approved_sets = [
        u'lhs',
        u'anat_pubs',
        u'anesth_pubs',
        u'arte_pubs',
        u'arth_pubs',
        u'bioc_pubs',
        u'biol_present',
        u'biol_pubs',
        u'biomarker_pubs',
        u'egrb_pubs',
        u'bios_pubs',
        u'britva',
        u'capstone',
        u'vcoa_case',
        u'biomarker',
        u'medsim',
        u'csbc',
        u'clse_pubs',
        u'chem_pubs',
        u'humsci',
        u'cei',
        u'cer',
        u'cenrinstitute',
        u'cenrinstitute_images',
        u'cer_resources',
        u'cmsc_pubs',
        u'conferences',
        u'anat',
        u'anesth',
        u'arte',
        u'arth',
        u'bioc',
        u'biol',
        u'egrb',
        u'bios',
        u'clse',
        u'chem',
        u'cmsc',
        u'econ',
        u'edlp',
        u'egre',
        u'emsa',
        u'engl',
        u'fmph',
        u'frsc',
        u'genp',
        u'grty',
        u'hadm',
        u'hcpr',
        u'hist',
        u'hgen',
        u'info',
        u'intmed',
        u'hems',
        u'kine',
        u'math',
        u'egmn',
        u'medc',
        u'micr',
        u'musc',
        u'neurology',
        u'neurosur',
        u'obgyn',
        u'occt',
        u'ophth',
        u'oralhealth',
        u'orsg',
        u'orthop',
        u'otolar',
        u'path',
        u'patc',
        u'pediatrics',
        u'peri',
        u'pceu',
        u'phtx',
        u'phar',
        u'phil',
        u'pmr',
        u'phty',
        u'phys',
        u'phis',
        u'pros',
        u'psych',
        u'psyc',
        u'radonc',
        u'radiology',
        u'sbhd',
        u'ssor',
        u'surgery',
        u'tedu',
        u'vcoa_editorial',
        u'community',
        u'community_resources',
        u'econ_pubs',
        u'edlp_pubs',
        u'egre_pubs',
        u'emsa_pubs',
        u'engl_pubs',
        u'fmph_present',
        u'fmph_pubs',
        u'frsc_pubs',
        u'fwap_pubs',
        u'genp_pubs',
        u'grty_pubs',
        u'rcdayposters',
        u'gradposters',
        u'gradschool',
        u'hadm_pubs',
        u'hcpr_pubs',
        u'hist_data',
        u'hist_pubs',
        u'medsim_pubs',
        u'hgen_pubs',
        u'info_pubs',
        u'inova',
        u'inova_pubs',
        u'ica',
        u'ica_pubs',
        u'intmed_pubs',
        u'jstae',
        u'hems_pubs',
        u'kine_pubs',
        u'wilder',
        u'wilder_pubs',
        u'lifesci',
        u'mcvq',
        u'mktg_pubs',
        u'massey',
        u'massey_pubs',
        u'math_pubs',
        u'egmn_pubs',
        u'medc_pubs',
        u'micr_pubs',
        u'neurology_pubs',
        u'neurosur_pubs',
        u'obgyn_pubs',
        u'occt_pubs',
        u'research',
        u'pharmacy_dean',
        u'arch001',
        u'ophth_pubs',
        u'oralhealth_pubs',
        u'orsg_pubs',
        u'orthop_pubs',
        u'otolar_pubs',
        u'partnershipinstitute',
        u'partnershipinstitute_images',
        u'path_pubs',
        u'patc_pubs',
        u'pediatrics_pubs',
        u'peri_pubs',
        u'pceu_pubs',
        u'phtx_pubs',
        u'phar_pubs',
        u'philipsinst',
        u'philipsinst_pubs',
        u'phil_pubs',
        u'pmr_pubs',
        u'phty_pubs',
        u'phys_pubs',
        u'phis_pubs',
        u'pros_pubs',
        u'psych_pubs',
        u'psyc_pubs',
        u'pharmacy_dean_pubs',
        u'radonc_pubs',
        u'radiology_pubs',
        u'rice',
        u'rice_symp',
        u'masc',
        u'masc_present',
        u'rpec_race',
        u'sahp',
        u'business',
        u'dentistry',
        u'education',
        u'engineering',
        u'medicine',
        u'nursing',
        u'nursing_pubs',
        u'pharmacy',
        u'socialwork',
        u'wrld',
        u'arts',
        u'service_institute',
        u'service_institute_images',
        u'sixty',
        u'socialwork_pubs',
        u'socialwork_student',
        u'sbhd_pubs',
        u'sociology',
        u'sociology_pubs',
        u'ssor_data',
        u'ssor_pubs',
        u'csbc_pubs',
        u'surgery_present',
        u'surgery_pubs',
        u'tedu_pubs',
        u'etd',
        u'urop',
        u'uresposters',
        u'brandcenter',
        u'vcubulletins',
        u'libraries',
        u'libraries_data',
        u'libraries_present',
        u'libraries_pubs',
        u'vcuhealth',
        u'vcuhealth_pubs',
        u'archives',
        u'davinci',
        u'davinci_student',
        u'vcoa',
        u'vcoa_pubs',
        u'wrld_pubs'
    ]
