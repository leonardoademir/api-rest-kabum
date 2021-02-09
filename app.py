from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Teste Kabum<br>Leonardo Ademir Tonezi dos Santos<br>POST -> URL + /kabum'

@app.route('/kabum', methods=['POST'])
def calculo_de_frete():
  data = request.get_json()
  output = []
  
  peso = data['peso']
  altura = data['dimensao']['altura']
  largura = data['dimensao']['largura']

  ninja = verificar_ninja(altura, largura)
  kabum = verificar_kabum(altura, largura)

  if peso > 0:
    if ninja:
      output.append({ 'nome': 'Entrega Ninja',
                      'valor_frete': (peso * 0.3) / 10,
                      'prazo_dias': 6
      })
      
    if kabum:
      output.append({ 'nome': 'Entrega Kabum',
                      'valor_frete': (peso * 0.2) / 10,
                      'prazo_dias': 4
      })
  else:
    output.append({ 'Erro': 'Peso invalido.'})
  

  return jsonify(output)

def verificar_ninja(altura, largura):
  ninja = False

  if(altura >= 10) and (altura <= 200) and (largura >= 10) and (largura <= 200):
    ninja = True

  return  ninja

def verificar_kabum(altura, largura):
  kabum = False

  if(altura >= 5) and (altura <= 140) and (largura >= 5) and (largura <= 140):
    kabum = True

  return  kabum

if __name__ == '__main__':
  app.run(debug=True)