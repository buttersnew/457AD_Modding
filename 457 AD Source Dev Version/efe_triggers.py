from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *

from module_constants import *

from compiler import *

efe_triggers = [

(0, 0, 0, [(call_script, "script_cf_start_siege_debug_trigger"),], [(call_script, "script_cf_efe_start_siege_debug"),]),
(0, 0, 0, [(call_script, "script_cf_start_normal_debug_trigger"),], [(call_script, "script_cf_update_lord_party_texts"),]),
(0, 0, 0, [(call_script, "script_cf_start_normal_debug_trigger")], [(call_script, "script_cf_kill_parties_debug"),]),
(1, 0, 0, [], [(call_script, "script_cf_update_sieged_center_texts"),]),
]