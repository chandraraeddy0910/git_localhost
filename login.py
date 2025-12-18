from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Login (Single Page)</title>

  <!-- Bootstrap CSS (CDN) -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

  <style>
    body { background: #f6f7fb; }
    .login-card {
      max-width: 420px;
      margin: 10vh auto;
      border: 0;
      border-radius: 16px;
      box-shadow: 0 10px 30px rgba(0,0,0,.08);
    }
    .brand {
      font-weight: 700;
      letter-spacing: .3px;
    }
    .subtle { color: #6c757d; }
  </style>
</head>
<body>

  <div class="container">
    <div class="card login-card">
      <div class="card-body p-4 p-md-5">
        <div class="mb-3 text-center">
          <div class="brand h3 mb-1">Git Practice Login</div>
          <div class="subtle">Single page • Flask + Bootstrap</div>
        </div>

        {% if message %}
          <div class="alert alert-{{ category }} py-2" role="alert">
            {{ message }}
          </div>
        {% endif %}

        <form method="POST" action="/login" class="needs-validation" novalidate>
          <div class="mb-3">
            <label class="form-label">Username</label>
            <input name="username" class="form-control" placeholder="e.g. admin" required />
            <div class="invalid-feedback">Please enter a username.</div>
          </div>

          <div class="mb-3">
            <label class="form-label">Password</label>
            <input name="password" type="password" class="form-control" placeholder="e.g. password123" required />
            <div class="invalid-feedback">Please enter a password.</div>
          </div>

          <div class="d-flex justify-content-between align-items-center mb-3">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="1" id="remember" name="remember">
              <label class="form-check-label" for="remember">Remember me</label>
            </div>
            <a class="small text-decoration-none" href="#" onclick="alert('Demo only 🙂'); return false;">
              Forgot password?
            </a>
          </div>

          <button class="btn btn-primary w-100" type="submit">Login</button>

          <hr class="my-4" />

          <button class="btn btn-outline-dark w-100" type="button"
                  onclick="alert('Demo only 🙂');">
            Continue with GitHub
          </button>
        </form>

        <p class="small text-center subtle mt-3 mb-0">
          Tip: demo login is <b>admin</b> / <b>password123</b>
        </p>
      </div>
    </div>
  </div>

  <!-- Bootstrap JS (optional) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

  <!-- Client-side validation -->
  <script>
    (() => {
      const forms = document.querySelectorAll('.needs-validation');
      Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
          if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    })();
  </script>
</body>
</html>
"""

@app.get("/")
def home():
  return render_template_string(PAGE, message=None, category="info")

@app.post("/login")
def login():
  username = (request.form.get("username") or "").strip()
  password = request.form.get("password") or ""

  # Demo credentials (for practice only)
  if username == "admin" and password == "password123":
    return render_template_string(PAGE, message=f"Welcome, {username}! ✅", category="success")

  return render_template_string(PAGE, message="Invalid username or password. ❌", category="danger")

if __name__ == "__main__":
  app.run(debug=True)
