from django.http import HttpResponse

def home(request):
    html_content = """
    <html>
        <head>
            <title>API de Pedidos</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #f4f4f4;
                }
                h1 {
                    color: #333;
                }
                p {
                    font-size: 1.2em;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                }
                li {
                    margin: 10px 0;
                }
                a {
                    text-decoration: none;
                    color: #007BFF;
                }
                a:hover {
                    text-decoration: underline;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    background: #fff;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Bienvenido a la API de Pedidos</h1>
                <p>Usa las siguientes rutas para interactuar con la API:</p>
                <ul>
                    <li><a href="/api/usuario/">/api/usuario/</a> - Interactuar con la API de usuarios</li>
                    <li><a href="/api/pedido/">/api/pedido/</a> - Interactuar con la API de pedidos</li>
                    <li><a href="/api/direccion-envio/">/api/direccion-envio/</a> - Interactuar con la API de direcciones de envío</li>
                </ul>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html_content)