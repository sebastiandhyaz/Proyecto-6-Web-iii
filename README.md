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
    <td>⚠️ <b>Multas (opcional):</b><br>Cálculo automático de penalizaciones por retraso.</td>
  </tr>
</table>

</div>

---

## 🚀 Instalación Rápida

1. **Clona el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-proyecto>
   ```

2. **Crea y activa el entorno virtual**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Instala dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica migraciones**
   ```bash
   python manage.py migrate
   ```

5. **(Opcional) Crea un superusuario**
   ```bash
   python manage.py createsuperuser
   ```

6. **¡Ejecuta el servidor!**
   ```bash
   python manage.py runserver
   ```

7. **Accede en tu navegador**
   
   <p align="center"><b>http://127.0.0.1:8000/</b></p>

---

## 🗂️ Estructura de las Tablas

| Tabla     | Descripción                                                  |
|-----------|-------------------------------------------------------------|
| **Libro**   | Datos del libro: título, autor, ISBN, etc.                  |
| **Socio**   | Información personal de los socios.                         |
| **Préstamo**| Registro de cada préstamo, fechas y estado.                 |
| **Multa**   | (Opcional) Penalizaciones por retrasos en devoluciones.     |

---

## 💡 Notas Importantes

- Puedes personalizar reglas de multas y periodos de préstamo en la configuración.
- El sistema es extensible y adaptable a las necesidades de tu biblioteca.
- Interfaz amigable, moderna y muy fácil de usar.

---

<p align="center">
  <b>¡Listo para gestionar tu biblioteca de manera eficiente y elegante! ✨</b>
</p>
