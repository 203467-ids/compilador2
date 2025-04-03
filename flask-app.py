from flask import Flask, render_template, request, jsonify
import os
import json
import tempfile
import subprocess
import uuid
import sys
from antlr4 import *
from compiler import Compiler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compile', methods=['POST'])
def compile_code():
    source_code = request.form.get('code', '')
    
    # Compilar el código
    compiler = Compiler()
    result = compiler.compile(source_code)
    
    return jsonify(result)

@app.route('/generate_antlr', methods=['GET'])
def generate_antlr():
    """Genera los archivos ANTLR a partir de la gramática."""
    try:
        grammar_path = os.path.join(os.path.dirname(__file__), 'SimpleLang.g4')
        
        # Verificar si el archivo de gramática existe
        if not os.path.exists(grammar_path):
            with open(grammar_path, 'w') as f:
                # Obtener la gramática desde el código del compilador
                # Este es solo un ejemplo, deberías extraer la gramática real
                from compiler import GRAMMAR
                f.write(GRAMMAR)
        
        # Ejecutar el generador ANTLR
        cmd = ['java', '-jar', 'antlr-4.9.3-complete.jar', '-Dlanguage=Python3', grammar_path]
        process = subprocess.run(cmd, capture_output=True, text=True)
        
        if process.returncode != 0:
            return jsonify({
                'success': False, 
                'error': process.stderr
            })
        
        return jsonify({
            'success': True,
            'message': 'Archivos ANTLR generados correctamente'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    # Asegurarse de que los archivos ANTLR estén generados
    # antes de iniciar el servidor
    app.run(debug=True)
