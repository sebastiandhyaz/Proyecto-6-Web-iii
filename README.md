<p align="center">
  <img src="https://img.icons8.com/ios-filled/100/000000/library.png" width="100" alt="Logo Biblioteca"/>
</p>

<h1 align="center">📚 Sistema de Préstamos de Biblioteca 📚</h1>
<p align="center">
  <b>Gestión moderna y sencilla de tu biblioteca con Django</b>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python"/>
  <img src="https://img.shields.io/badge/Django-Framework-green?logo=django"/>
  <img src="https://img.shields.io/badge/Virtualenv-Activated-purple?logo=virtualenv"/>
</p>

---

<div align="center">
  
✨ <b>Características Principales</b> ✨

<table align="center">
  <tr>
    <td>📖 <b>Gestión de Libros:</b><br>Alta, edición y eliminación de libros disponibles.</td>
    <td>🧑‍💼 <b>Gestión de Socios:</b><br>Registro y administración de usuarios.</td>
  </tr>
  <tr>
    <td>🔄 <b>Préstamos:</b><br>Solicitud, renovación y devolución de libros.</td>
    <td>⏰ <b>Fechas de Devolución:</b><br>Límite de entrega para cada préstamo.</td>
  </tr>
  <tr>
    <td>📜 <b>Historial de Préstamos:</b><br>Consulta de préstamos por usuario.</td>
    <td>⚠️ <b>Multas:</b><br>Cálculo automático de penalizaciones por retraso en la devolución.</td>
  </tr>
</table>

</div>

---

## 🚀 Instalación Rápida

### Método 1: Instalación Automática (Recomendado)

1. **Clona el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd Proyecto-6-Web-iii
   ```

2. **Ejecuta el script de configuración**
   ```bash
   ./setup.sh
   ```

3. **¡Inicia el servidor!**
   ```bash
   ./run_server.sh
   ```

### Método 2: Instalación Manual

1. **Clona el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd Proyecto-6-Web-iii/Proyecto
   ```

2. **Activa el entorno virtual existente**
   ```bash
   source env/bin/activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r Proyecto/requirements.txt
   ```

4. **Navega al proyecto Django**
   ```bash
   cd Proyecto
   ```

5. **Aplica las migraciones**
   ```bash
   python manage.py migrate
   ```

6. **(Opcional) Crea un superusuario**
   ```bash
   python manage.py createsuperuser
   ```

7. **¡Ejecuta el servidor!**
   ```bash
   python manage.py runserver
   ```

8. **Accede desde tu navegador**
   
   <p align="center"><b>http://127.0.0.1:8000/</b></p>

---

## 🗂️ Estructura de las Tablas

| Tabla     | Descripción                                                  |
|-----------|-------------------------------------------------------------|
| **Libro**   | Datos del libro: título, autor, ISBN, etc.                  |
| **Socio**   | Información personal de los socios.                         |
| **Préstamo**| Registro de cada préstamo, fechas y estado.                 |
| **Multa**   | Penalizaciones por retrasos en la devolución de libros.     |

---

## 🔧 Solución de Problemas

### Error: "Couldn't import Django"
Si obtienes el error `ModuleNotFoundError: No module named 'django'`:

1. **Solución rápida**: Ejecuta `./setup.sh`
2. **Solución manual**: 
   ```bash
   cd Proyecto
   source env/bin/activate
   pip install -r Proyecto/requirements.txt
   ```

### Error: "runserver" no funciona
- Asegúrate de haber activado el entorno virtual: `source Proyecto/env/bin/activate`
- Verifica que estés en el directorio correcto: `cd Proyecto/Proyecto`
- Instala las dependencias si no están instaladas: `pip install -r requirements.txt`

### Scripts Disponibles
- `./setup.sh` - Configura el entorno e instala dependencias
- `./run_server.sh` - Inicia el servidor de desarrollo automáticamente

## 💡 Notas Importantes

- Puedes personalizar las reglas de multas y los períodos de préstamo en la configuración.
- El sistema es extensible y adaptable a las necesidades de tu biblioteca.
- Interfaz amigable, moderna y muy fácil de usar.

---

<p align="center">
  <b>¡Listo para gestionar tu biblioteca de manera eficiente y elegante! ✨</b>
</p>
