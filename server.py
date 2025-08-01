#!/usr/bin/env python3
"""
Servidor HTTP simple con soporte CORS para el lector del Corán en español
"""

import http.server
import socketserver
import os
import mimetypes
from urllib.parse import urlparse

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar encabezados CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()
    
    def do_OPTIONS(self):
        # Manejar solicitudes OPTIONS para CORS
        self.send_response(200)
        self.end_headers()
    
    def guess_type(self, path):
        # Asegurar el tipo MIME correcto para PDFs
        mimetype, encoding = mimetypes.guess_type(path)
        if path.endswith('.pdf'):
            mimetype = 'application/pdf'
        elif path.endswith('.js'):
            mimetype = 'application/javascript'
        elif path.endswith('.css'):
            mimetype = 'text/css'
        elif path.endswith('.html'):
            mimetype = 'text/html'
        return mimetype, encoding
    
    def log_message(self, format, *args):
        # Log personalizado
        print(f"[{self.date_time_string()}] {format % args}")

def run_server(port=8001):
    # Cambiar al directorio del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print(f"🚀 Iniciando servidor del Corán en español en el puerto {port}")
    print(f"📁 Directorio: {os.getcwd()}")
    print(f"🌐 URL: http://localhost:{port}")
    print(f"📖 PDF: {os.path.exists('quranES.pdf')}")
    
    with socketserver.TCPServer(("", port), CORSHTTPRequestHandler) as httpd:
        print(f"✅ Servidor iniciado con éxito")
        print("Presiona Ctrl+C para detener")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Deteniendo servidor")

if __name__ == "__main__":
    run_server()
