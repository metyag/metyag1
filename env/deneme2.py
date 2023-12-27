import yaml

# environment.yml dosyasını oku
with open('environment.yml', 'r') as file:
    env = yaml.safe_load(file)

# env.yaml dosyası için veriler
env_data = {
    'name': env.get('name', 'default_name'),
    'channels': env.get('channels', []),
    'dependencies': env.get('dependencies', [])
}

# env.yaml dosyasını oluştur ve verileri yaz
with open('env.yaml', 'w') as file:
    yaml.dump(env_data, file, default_flow_style=False)
