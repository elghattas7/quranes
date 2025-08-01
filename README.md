# El Noble Corán - Lector en línea 📖

Un sitio web moderno y responsive para la lectura del Noble Corán en español con una interfaz intuitiva de navegación.

## ✨ Características

- **Lectura fluida** : Navegación página por página con controles intuitivos
- **Interfaz responsive** : Compatible con móviles, tabletas y escritorio
- **Zoom adaptativo** : Ajuste del tamaño para una lectura cómoda
- **Navegación por teclado** : Atajos de teclado para navegación rápida
- **Modo pantalla completa** : Experiencia de lectura inmersiva
- **PWA** : Instalación posible como aplicación
- **Cache inteligente** : Lectura sin conexión después de la primera carga
- **SEO optimizado** : Optimizado para motores de búsqueda

## 🚀 Instalación

### Uso local (recomendado)

1. **Descargar** todos los archivos en una carpeta
2. **Verificar** que el archivo `quranES.pdf` esté presente
3. **Hacer doble clic** en `index.html` para abrir el sitio
4. **¡Disfrutar** de la lectura del Corán!

### Uso con servidor web (opcional)

Si prefieres usar un servidor web:

```bash
# Con Python 3
python3 server.py

# O servidor simple
python3 -m http.server 8001
```

Luego abrir http://localhost:8001 en tu navegador

### Despliegue en producción

1. **Subir** todos los archivos a tu servidor web
2. **Modificar** las URLs en `sitemap.xml` y `robots.txt`
3. **Agregar** los iconos PWA en la carpeta `images/`

## 📁 Estructura del proyecto

```
QuranES/
├── index.html          # Página principal (todo-en-uno)
├── quranES.pdf         # Archivo PDF del Corán
├── server.py           # Servidor Python (opcional)
├── manifest.json       # Manifest PWA
├── sitemap.xml         # Mapa del sitio
├── robots.txt          # Instrucciones para robots
├── sw.js               # Service Worker
└── README.md           # Documentación
```

## 🎮 Uso

### Navegación
- **Flechas izquierda/derecha** : Página anterior/siguiente
- **Flechas arriba/abajo** : Página anterior/siguiente
- **+/-** : Zoom adelante/atrás
- **F o F11** : Modo pantalla completa

### Interfaz
- **Botones de navegación** : Controles visuales
- **Campo de página** : Ir directamente a una página
- **Controles de zoom** : Ajustar el tamaño de visualización
- **Modo pantalla completa** : Lectura inmersiva

## 🔧 Personalización

### Colores
Modifica las variables CSS en `index.html` :

```css
:root {
    --primary-color: #2c5530;    /* Verde principal */
    --secondary-color: #d4af37;  /* Oro */
    --accent-color: #8b4513;     /* Marrón */
}
```

### Contenido
- Modifica los textos en `index.html`
- Ajusta las metadatos SEO
- Personaliza los mensajes de interfaz

## 📱 PWA (Progressive Web App)

El sitio puede instalarse como una aplicación:

1. **Chrome/Edge** : Hacer clic en el icono de instalación en la barra de direcciones
2. **Firefox** : Menú → "Instalar esta aplicación"
3. **Safari** : Compartir → "Agregar a pantalla de inicio"

## 🔍 SEO y Rendimiento

### Optimizaciones incluidas
- Metadatos completos (Open Graph, Twitter Cards)
- Estructura HTML semántica
- Schema.org markup
- Sitemap XML
- Service Worker para cache
- Imágenes optimizadas (por agregar)

### Palabras clave objetivo
- "corán"
- "quran español"
- "lectura corán en línea"
- "corán pdf"
- "noble corán"
- "traducción española corán"

## 🛠️ Desarrollo

### Tecnologías utilizadas
- **HTML5** : Estructura semántica
- **CSS3** : Diseño responsive con Grid y Flexbox
- **JavaScript ES6+** : Lógica de aplicación
- **Service Worker** : Cache y funcionalidades sin conexión

### Mejoras posibles
- [ ] Función de búsqueda en el texto
- [ ] Marcadores personalizados
- [ ] Modo oscuro/claro
- [ ] Audio (recitación)
- [ ] Traducciones múltiples
- [ ] Notas personales

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver el archivo LICENSE para más detalles.

## 🤝 Contribución

¡Las contribuciones son bienvenidas! No dudes en:
- Reportar errores
- Proponer mejoras
- Enviar pull requests

## 📞 Soporte

Para cualquier pregunta o problema:
- Abrir un issue en GitHub
- Contactar al equipo de desarrollo

---

**Que la paz y las bendiciones de Allah sean contigo** 🤲
