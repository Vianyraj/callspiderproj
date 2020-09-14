import json
import requests
r= requests.get('https://formulae.brew.sh/api/formula.json')

packages_json= r.json()
package_name= packages_json[0]['name']
package_desc= packages_json[0]['desc']
package_json= r.json()
print(package_name, package_desc)
packages_str = json.dumps(package_json, indent=2)
package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]

print(package_name, package_desc, installs_30, installs_90)
