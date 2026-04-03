import json
import os
import re

class FullSystemValidator:
    def __init__(self, netlist_path, rules_path):
        self.netlist_data = self._load_json(netlist_path)
        self.rules_data = self._load_json(rules_path)
        self.pin_to_net_map = {}
        self.locked_mcu_pins = {}  
        self.results = []
        self.total_numerator = 0
        self.total_denominator = 0
        self._initialize_pin_map()

    def _load_json(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _initialize_pin_map(self):
        netlist = self.netlist_data.get("System_Netlist", [])
        for net in netlist:
            net_id = net.get("net_id")
            for conn in net.get("Connections", []):
                key = (str(conn["ComponentID"]).strip(), str(conn["PinName"]).strip())
                if key not in self.pin_to_net_map:
                    self.pin_to_net_map[key] = set()
                self.pin_to_net_map[key].add(net_id)

    def _get_mcu_pin_in_net(self, mcu_id, target_nets):
        for (cid, pname), nets in self.pin_to_net_map.items():
            if cid == mcu_id and not nets.isdisjoint(target_nets):
                return pname, nets
        return None, None

    def run_verification(self):
        for rule in self.rules_data.get("Routing_Rules", []):
            rule_name = rule.get("RuleName", "Unnamed")
            rule_type = rule.get("Type")
            log, matched, required = [], 0, 0

            if rule_type in ["Bus_Pairing", "Resource_Allocation"]:
                mcu_id = rule.get("MCU")
                mcu_groups = self.rules_data["MCU_Function_Groups"].get(mcu_id, {})
                pattern = rule.get("Target_Group_Pattern")
                candidates = [g for g in mcu_groups.keys() if re.match(pattern or "", g)]
                
                best_match, best_log, best_locked = 0, [], {}

                for g_name in candidates:
                    curr_match, curr_total, curr_log, curr_locked = 0, 0, [], {}
                    group_pins = [str(p["PinName"]).strip() for p in mcu_groups[g_name]]
                    
                    for slave in rule.get("Slaves", []):
                        iface_pins = self.rules_data["Component_Interfaces"].get(slave["ComponentID"], {}).get(slave["Interface"], [])
                        for p_req in iface_pins:
                            curr_total += 1
                            comp_key = (slave["ComponentID"], str(p_req["PinName"]).strip())
                            nets = self.pin_to_net_map.get(comp_key)
                            
                            if nets:
                                mcu_pin, mcu_nets = self._get_mcu_pin_in_net(mcu_id, nets)
                                if mcu_pin in group_pins:
                                    lock_key = (mcu_id, mcu_pin)
                                    if lock_key not in self.locked_mcu_pins or not self.locked_mcu_pins[lock_key].isdisjoint(mcu_nets):
                                        curr_match += 1
                                        curr_log.append(f"SUCCESS: {comp_key[0]}[{comp_key[1]}] <-> {mcu_id}[{mcu_pin}]")
                                        curr_locked[lock_key] = mcu_nets
                                    else:
                                        curr_log.append(f"LOCK CONFLICT: {mcu_id}[{mcu_pin}] used by different Net.")
                    
                    if curr_match > best_match:
                        best_match, best_log, best_locked = curr_match, curr_log, curr_locked
                    required = max(required, curr_total)
                
                matched = best_match
                log = best_log
                self.locked_mcu_pins.update(best_locked)

            elif rule_type == "Direct_Link":
                nodes = rule.get("Nodes", [])
                required = len(nodes)
                node_net_sets = [self.pin_to_net_map.get((n["ComponentID"], str(n["PinName"]).strip()), set()) for n in nodes]
                common = set.intersection(*node_net_sets) if node_net_sets else set()
                if common:
                    matched = required
                    log.append(f"LINK VERIFIED: Share Net(s) {list(common)}")
                else:
                    log.append("LINK FAILED: No common Net.")

            self.total_numerator += matched
            self.total_denominator += required
            status = "PASS" if matched == required and required > 0 else ("PARTIAL" if matched > 0 else "FAIL")
            self.results.append({"rule": rule_name, "status": status, "score": f"{matched}/{required}", "details": log})

    def generate_report(self, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        coverage = (self.total_numerator / self.total_denominator * 100) if self.total_denominator > 0 else 0
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"=== Full System Connectivity Verification Report ===\n")
            f.write(f"Total Pins/Links Verified: {self.total_numerator}/{self.total_denominator} ({coverage:.2f}%)\n")
            f.write("-" * 65 + "\n\n")
            for res in self.results:
                f.write(f"[{res['status']}] {res['rule']} ({res['score']})\n")
                for line in res['details']: f.write(f"  * {line}\n")
                f.write("\n")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    NETLIST = os.path.join(BASE_DIR, "..", "Result", "deepseek-v3", "system_step4.json")
    RULES = os.path.join(BASE_DIR, "static_check.json") 
    OUTPUT = os.path.join(BASE_DIR, "rules_report.txt")

    if os.path.exists(NETLIST) and os.path.exists(RULES):
        validator = FullSystemValidator(NETLIST, RULES)
        validator.run_verification()
        validator.generate_report(OUTPUT)