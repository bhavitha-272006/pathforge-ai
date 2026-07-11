# roadmaps.py
# 10 careers x 3 levels (beginner / intermediate / advanced)
# All roadmaps share the same dict structure so roadmap.html works for all.
#
# Structure of every roadmap:
# {
#   "goal": str,
#   "level": str,
#   "duration": str,
#   "hours_per_day": int,
#   "source": "manual",
#   "skills": [
#       {
#           "name": str,
#           "duration": str,          # e.g. "1 week"
#           "topics": [str, ...],
#           "tasks":  [str, ...],
#           "resources": [{"title": str, "url": str}, ...]
#       },
#       ...
#   ]
# }

# ─────────────────────────────────────────────
#  CAREER KEYS  (used for fuzzy matching)
# ─────────────────────────────────────────────
MANUAL_CAREERS = [
    "frontend",
    "backend",
    "fullstack",
    "full stack",
    "ai engineer",
    "machine learning",
    "data scientist",
    "cyber security",
    "devops",
    "mobile",
    "android",
    "ios",
    "blockchain",
    "game developer",
    "game development",
]


# ─────────────────────────────────────────────
#  1. FRONTEND DEVELOPER
# ─────────────────────────────────────────────
FRONTEND = {
    "beginner": {
        "goal": "Frontend Developer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "HTML Basics",
                "duration": "1 week",
                "topics": ["Tags & structure", "Forms", "Tables", "Semantic HTML"],
                "tasks": ["Build a personal profile page", "Create a registration form"],
                "resources": [
                    {"title": "MDN HTML Guide", "url": "https://developer.mozilla.org/en-US/docs/Learn/HTML"},
                    {"title": "W3Schools HTML", "url": "https://www.w3schools.com/html/"},
                ],
            },
            {
                "name": "CSS Fundamentals",
                "duration": "2 weeks",
                "topics": ["Selectors", "Box model", "Flexbox", "Colors & fonts"],
                "tasks": ["Style your profile page", "Build a responsive card layout"],
                "resources": [
                    {"title": "CSS Tricks", "url": "https://css-tricks.com/"},
                    {"title": "Flexbox Froggy", "url": "https://flexboxfroggy.com/"},
                ],
            },
            {
                "name": "JavaScript Basics",
                "duration": "3 weeks",
                "topics": ["Variables", "Functions", "DOM manipulation", "Events"],
                "tasks": ["Build a to-do list", "Create a simple calculator"],
                "resources": [
                    {"title": "JavaScript.info", "url": "https://javascript.info/"},
                    {"title": "Eloquent JavaScript (free)", "url": "https://eloquentjavascript.net/"},
                ],
            },
            {
                "name": "Responsive Design",
                "duration": "1 week",
                "topics": ["Media queries", "Mobile-first", "Viewport units"],
                "tasks": ["Make your portfolio fully responsive"],
                "resources": [
                    {"title": "Responsive Web Design - freeCodeCamp", "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/"},
                ],
            },
            {
                "name": "Git & GitHub",
                "duration": "1 week",
                "topics": ["Init, commit, push", "Branching", "GitHub Pages"],
                "tasks": ["Push your portfolio to GitHub", "Deploy using GitHub Pages"],
                "resources": [
                    {"title": "Git Handbook", "url": "https://guides.github.com/introduction/git-handbook/"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Frontend Developer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Advanced CSS & Animations",
                "duration": "1 week",
                "topics": ["CSS Grid", "Custom properties", "Keyframes", "Transitions"],
                "tasks": ["Build an animated landing page"],
                "resources": [
                    {"title": "CSS Grid Garden", "url": "https://cssgridgarden.com/"},
                    {"title": "Animista", "url": "https://animista.net/"},
                ],
            },
            {
                "name": "React.js",
                "duration": "5 weeks",
                "topics": ["Components", "Props & State", "Hooks", "React Router", "Context API"],
                "tasks": ["Build a weather app", "Create a multi-page React portfolio"],
                "resources": [
                    {"title": "React Official Docs", "url": "https://react.dev/"},
                    {"title": "Scrimba React Course", "url": "https://scrimba.com/learn/learnreact"},
                ],
            },
            {
                "name": "API Integration",
                "duration": "1 week",
                "topics": ["fetch / axios", "REST APIs", "JSON handling", "Async/Await"],
                "tasks": ["Build a movie search app using OMDB API"],
                "resources": [
                    {"title": "RapidAPI Learn", "url": "https://rapidapi.com/learn"},
                ],
            },
            {
                "name": "State Management",
                "duration": "2 weeks",
                "topics": ["Redux Toolkit", "Zustand", "Local vs global state"],
                "tasks": ["Add Redux to your weather app"],
                "resources": [
                    {"title": "Redux Toolkit Docs", "url": "https://redux-toolkit.js.org/"},
                ],
            },
            {
                "name": "Testing & Deployment",
                "duration": "1 week",
                "topics": ["Jest basics", "React Testing Library", "Netlify / Vercel deploy"],
                "tasks": ["Write unit tests", "Deploy React app to Vercel"],
                "resources": [
                    {"title": "Testing Library Docs", "url": "https://testing-library.com/docs/"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Frontend Developer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "TypeScript",
                "duration": "2 weeks",
                "topics": ["Types & interfaces", "Generics", "Strict mode", "TS with React"],
                "tasks": ["Convert a React project to TypeScript"],
                "resources": [
                    {"title": "TypeScript Handbook", "url": "https://www.typescriptlang.org/docs/handbook/"},
                ],
            },
            {
                "name": "Next.js",
                "duration": "4 weeks",
                "topics": ["SSR vs SSG", "App Router", "API routes", "Image optimization"],
                "tasks": ["Build a blog with Next.js and MDX"],
                "resources": [
                    {"title": "Next.js Learn", "url": "https://nextjs.org/learn"},
                ],
            },
            {
                "name": "Performance Optimization",
                "duration": "2 weeks",
                "topics": ["Lazy loading", "Code splitting", "Web Vitals", "Lighthouse audits"],
                "tasks": ["Achieve 90+ Lighthouse score on your app"],
                "resources": [
                    {"title": "Web.dev Performance", "url": "https://web.dev/performance/"},
                ],
            },
            {
                "name": "Micro-frontends & Design Systems",
                "duration": "3 weeks",
                "topics": ["Module federation", "Storybook", "Component tokens", "Monorepos"],
                "tasks": ["Build a Storybook component library"],
                "resources": [
                    {"title": "Storybook Docs", "url": "https://storybook.js.org/docs/"},
                ],
            },
            {
                "name": "System Design for Frontend",
                "duration": "2 weeks",
                "topics": ["Caching strategies", "CDN", "Frontend architecture patterns"],
                "tasks": ["Design a scalable e-commerce frontend architecture"],
                "resources": [
                    {"title": "Frontend System Design", "url": "https://frontendmastery.com/posts/frontend-system-design/"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  2. BACKEND DEVELOPER
# ─────────────────────────────────────────────
BACKEND = {
    "beginner": {
        "goal": "Backend Developer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Python Basics",
                "duration": "2 weeks",
                "topics": ["Data types", "Functions", "OOP", "File I/O"],
                "tasks": ["Write a CLI task manager", "Build a number guessing game"],
                "resources": [
                    {"title": "Python.org Tutorial", "url": "https://docs.python.org/3/tutorial/"},
                    {"title": "Automate the Boring Stuff (free)", "url": "https://automatetheboringstuff.com/"},
                ],
            },
            {
                "name": "Flask Framework",
                "duration": "2 weeks",
                "topics": ["Routes", "Templates", "Forms", "Flask-SQLAlchemy"],
                "tasks": ["Build a simple blog REST API"],
                "resources": [
                    {"title": "Flask Mega-Tutorial", "url": "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world"},
                ],
            },
            {
                "name": "SQL & Databases",
                "duration": "2 weeks",
                "topics": ["SELECT/INSERT/UPDATE/DELETE", "Joins", "SQLite", "PostgreSQL basics"],
                "tasks": ["Design a library management DB", "Connect Flask to SQLite"],
                "resources": [
                    {"title": "SQLZoo", "url": "https://sqlzoo.net/"},
                    {"title": "SQLite Tutorial", "url": "https://www.sqlitetutorial.net/"},
                ],
            },
            {
                "name": "REST API Design",
                "duration": "1 week",
                "topics": ["HTTP methods", "Status codes", "JSON", "Postman testing"],
                "tasks": ["Build a CRUD API for a bookstore"],
                "resources": [
                    {"title": "REST API Tutorial", "url": "https://restfulapi.net/"},
                ],
            },
            {
                "name": "Authentication Basics",
                "duration": "1 week",
                "topics": ["Sessions", "Flask-Login", "Password hashing"],
                "tasks": ["Add login/logout to your Flask app"],
                "resources": [
                    {"title": "Flask-Login Docs", "url": "https://flask-login.readthedocs.io/"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Backend Developer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Django Framework",
                "duration": "4 weeks",
                "topics": ["Models", "Views", "Templates", "Admin", "DRF"],
                "tasks": ["Build a full CRUD app with Django REST Framework"],
                "resources": [
                    {"title": "Django Docs", "url": "https://docs.djangoproject.com/"},
                    {"title": "DRF Tutorial", "url": "https://www.django-rest-framework.org/tutorial/"},
                ],
            },
            {
                "name": "PostgreSQL & ORM",
                "duration": "2 weeks",
                "topics": ["Advanced queries", "Indexes", "Migrations", "SQLAlchemy ORM"],
                "tasks": ["Optimize slow queries with EXPLAIN ANALYZE"],
                "resources": [
                    {"title": "PostgreSQL Tutorial", "url": "https://www.postgresqltutorial.com/"},
                ],
            },
            {
                "name": "JWT & OAuth",
                "duration": "1 week",
                "topics": ["JWT tokens", "Refresh tokens", "OAuth2 flow", "Google login"],
                "tasks": ["Implement JWT auth in your API"],
                "resources": [
                    {"title": "JWT.io", "url": "https://jwt.io/introduction/"},
                ],
            },
            {
                "name": "Caching & Redis",
                "duration": "2 weeks",
                "topics": ["Redis data structures", "Cache-aside pattern", "Rate limiting"],
                "tasks": ["Add Redis caching to your API endpoints"],
                "resources": [
                    {"title": "Redis University", "url": "https://university.redis.com/"},
                ],
            },
            {
                "name": "Testing & CI",
                "duration": "1 week",
                "topics": ["pytest", "Fixtures", "Mocking", "GitHub Actions"],
                "tasks": ["Write 80% test coverage for your API"],
                "resources": [
                    {"title": "pytest Docs", "url": "https://docs.pytest.org/"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Backend Developer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Microservices Architecture",
                "duration": "3 weeks",
                "topics": ["Service decomposition", "API Gateway", "Inter-service communication"],
                "tasks": ["Split a monolith into 3 microservices"],
                "resources": [
                    {"title": "Microservices.io", "url": "https://microservices.io/"},
                ],
            },
            {
                "name": "Message Queues",
                "duration": "2 weeks",
                "topics": ["RabbitMQ", "Celery", "Kafka basics", "Async task processing"],
                "tasks": ["Build an async email notification system with Celery"],
                "resources": [
                    {"title": "Celery Docs", "url": "https://docs.celeryq.dev/"},
                ],
            },
            {
                "name": "Docker & Kubernetes",
                "duration": "3 weeks",
                "topics": ["Dockerfiles", "Compose", "K8s Pods & Services", "Helm"],
                "tasks": ["Containerize your API and deploy to Kubernetes"],
                "resources": [
                    {"title": "Play with Docker", "url": "https://labs.play-with-docker.com/"},
                    {"title": "Kubernetes.io Learn", "url": "https://kubernetes.io/docs/tutorials/"},
                ],
            },
            {
                "name": "System Design",
                "duration": "4 weeks",
                "topics": ["Load balancing", "CAP theorem", "Sharding", "Design interviews"],
                "tasks": ["Design Twitter / URL shortener from scratch"],
                "resources": [
                    {"title": "System Design Primer", "url": "https://github.com/donnemartin/system-design-primer"},
                ],
            },
            {
                "name": "Observability",
                "duration": "1 week",
                "topics": ["Logging (structlog)", "Metrics (Prometheus)", "Tracing (OpenTelemetry)"],
                "tasks": ["Add structured logging and Prometheus metrics to your API"],
                "resources": [
                    {"title": "OpenTelemetry Docs", "url": "https://opentelemetry.io/docs/"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  3. AI / ML ENGINEER
# ─────────────────────────────────────────────
AI_ML = {
    "beginner": {
        "goal": "AI / ML Engineer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Python for Data",
                "duration": "2 weeks",
                "topics": ["NumPy", "Pandas", "Matplotlib", "Jupyter Notebooks"],
                "tasks": ["Analyze a CSV dataset", "Create 5 types of charts"],
                "resources": [
                    {"title": "Kaggle Python Course (free)", "url": "https://www.kaggle.com/learn/python"},
                    {"title": "Kaggle Pandas Course (free)", "url": "https://www.kaggle.com/learn/pandas"},
                ],
            },
            {
                "name": "Math Foundations",
                "duration": "2 weeks",
                "topics": ["Linear algebra basics", "Statistics", "Probability", "Derivatives"],
                "tasks": ["Implement linear regression from scratch using NumPy"],
                "resources": [
                    {"title": "3Blue1Brown Essence of Linear Algebra", "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab"},
                    {"title": "Khan Academy Statistics", "url": "https://www.khanacademy.org/math/statistics-probability"},
                ],
            },
            {
                "name": "ML with Scikit-learn",
                "duration": "3 weeks",
                "topics": ["Supervised learning", "Classification", "Regression", "Model evaluation"],
                "tasks": ["Build a spam classifier", "Predict house prices"],
                "resources": [
                    {"title": "Scikit-learn Tutorial", "url": "https://scikit-learn.org/stable/tutorial/"},
                    {"title": "Kaggle Intro to ML (free)", "url": "https://www.kaggle.com/learn/intro-to-machine-learning"},
                ],
            },
            {
                "name": "Data Preprocessing",
                "duration": "1 week",
                "topics": ["Missing values", "Encoding", "Scaling", "Train/test split"],
                "tasks": ["Clean a real-world messy dataset from Kaggle"],
                "resources": [
                    {"title": "Kaggle Data Cleaning (free)", "url": "https://www.kaggle.com/learn/data-cleaning"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "AI / ML Engineer",
        "level": "Intermediate",
        "duration": "5 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Deep Learning with TensorFlow/Keras",
                "duration": "4 weeks",
                "topics": ["Neural networks", "CNNs", "Activation functions", "Backpropagation"],
                "tasks": ["Build an image classifier (CIFAR-10)", "Recognize handwritten digits"],
                "resources": [
                    {"title": "TensorFlow Tutorials", "url": "https://www.tensorflow.org/tutorials"},
                    {"title": "Deep Learning Specialization (audit free)", "url": "https://www.coursera.org/specializations/deep-learning"},
                ],
            },
            {
                "name": "Natural Language Processing",
                "duration": "3 weeks",
                "topics": ["Tokenization", "Word embeddings", "RNNs", "HuggingFace basics"],
                "tasks": ["Sentiment analysis on movie reviews", "Text classification pipeline"],
                "resources": [
                    {"title": "HuggingFace NLP Course (free)", "url": "https://huggingface.co/learn/nlp-course"},
                ],
            },
            {
                "name": "PyTorch",
                "duration": "3 weeks",
                "topics": ["Tensors", "Autograd", "Custom datasets", "Training loops"],
                "tasks": ["Reimplement a Keras model in PyTorch"],
                "resources": [
                    {"title": "PyTorch Tutorials", "url": "https://pytorch.org/tutorials/"},
                ],
            },
            {
                "name": "Model Evaluation & Tuning",
                "duration": "2 weeks",
                "topics": ["Cross-validation", "Hyperparameter tuning", "Confusion matrix", "ROC-AUC"],
                "tasks": ["Tune a model with Optuna or GridSearchCV"],
                "resources": [
                    {"title": "Optuna Docs", "url": "https://optuna.readthedocs.io/"},
                ],
            },
            {
                "name": "ML Project End-to-End",
                "duration": "2 weeks",
                "topics": ["Problem framing", "EDA", "Feature engineering", "Deployment basics"],
                "tasks": ["Complete a Kaggle competition end-to-end"],
                "resources": [
                    {"title": "Kaggle Competitions", "url": "https://www.kaggle.com/competitions"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "AI / ML Engineer",
        "level": "Advanced",
        "duration": "6 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Transformers & LLMs",
                "duration": "4 weeks",
                "topics": ["Attention mechanism", "BERT/GPT architecture", "Fine-tuning", "PEFT/LoRA"],
                "tasks": ["Fine-tune a HuggingFace model on a custom dataset"],
                "resources": [
                    {"title": "HuggingFace Transformers", "url": "https://huggingface.co/docs/transformers"},
                    {"title": "Andrej Karpathy - Build GPT", "url": "https://www.youtube.com/watch?v=kCc8FmEb1nY"},
                ],
            },
            {
                "name": "MLOps",
                "duration": "3 weeks",
                "topics": ["MLflow", "DVC", "Model versioning", "CI/CD for ML"],
                "tasks": ["Track experiments with MLflow", "Version datasets with DVC"],
                "resources": [
                    {"title": "MLflow Docs", "url": "https://mlflow.org/docs/latest/index.html"},
                ],
            },
            {
                "name": "Model Deployment",
                "duration": "3 weeks",
                "topics": ["FastAPI serving", "ONNX", "TorchServe", "Gradio / Streamlit"],
                "tasks": ["Deploy a model as a REST API with FastAPI"],
                "resources": [
                    {"title": "FastAPI Docs", "url": "https://fastapi.tiangolo.com/"},
                    {"title": "Gradio Docs", "url": "https://www.gradio.app/docs/"},
                ],
            },
            {
                "name": "Reinforcement Learning",
                "duration": "3 weeks",
                "topics": ["MDPs", "Q-learning", "Policy gradient", "OpenAI Gym"],
                "tasks": ["Train an agent to play CartPole"],
                "resources": [
                    {"title": "Spinning Up in RL (OpenAI)", "url": "https://spinningup.openai.com/"},
                ],
            },
            {
                "name": "AI Research & Paper Reading",
                "duration": "3 weeks",
                "topics": ["Reading arxiv papers", "Reproducing results", "Writing reports"],
                "tasks": ["Reproduce one arxiv paper result", "Write a short research report"],
                "resources": [
                    {"title": "Papers With Code", "url": "https://paperswithcode.com/"},
                    {"title": "Arxiv CS.LG", "url": "https://arxiv.org/list/cs.LG/recent"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  4. DATA SCIENTIST
# ─────────────────────────────────────────────
DATA_SCIENTIST = {
    "beginner": {
        "goal": "Data Scientist",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Python & Data Tools",
                "duration": "2 weeks",
                "topics": ["Python basics", "Pandas", "NumPy", "Jupyter"],
                "tasks": ["Load and explore a real dataset", "Calculate summary statistics"],
                "resources": [
                    {"title": "Kaggle Python (free)", "url": "https://www.kaggle.com/learn/python"},
                ],
            },
            {
                "name": "Exploratory Data Analysis",
                "duration": "2 weeks",
                "topics": ["Distributions", "Correlation", "Seaborn / Matplotlib", "Outliers"],
                "tasks": ["Perform full EDA on the Titanic dataset"],
                "resources": [
                    {"title": "Kaggle EDA Guide", "url": "https://www.kaggle.com/learn/data-visualization"},
                ],
            },
            {
                "name": "Statistics for Data Science",
                "duration": "2 weeks",
                "topics": ["Hypothesis testing", "p-values", "Confidence intervals", "Distributions"],
                "tasks": ["Run an A/B test simulation", "Test a hypothesis on a dataset"],
                "resources": [
                    {"title": "StatQuest YouTube", "url": "https://www.youtube.com/c/joshstarmer"},
                ],
            },
            {
                "name": "Intro to Machine Learning",
                "duration": "2 weeks",
                "topics": ["Regression", "Classification", "Decision trees", "Model metrics"],
                "tasks": ["Predict sales using linear regression"],
                "resources": [
                    {"title": "Kaggle Intro to ML (free)", "url": "https://www.kaggle.com/learn/intro-to-machine-learning"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Data Scientist",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Feature Engineering",
                "duration": "2 weeks",
                "topics": ["Encoding", "Scaling", "Interaction features", "Dimensionality reduction (PCA)"],
                "tasks": ["Engineer features to improve model score by 5%"],
                "resources": [
                    {"title": "Kaggle Feature Engineering (free)", "url": "https://www.kaggle.com/learn/feature-engineering"},
                ],
            },
            {
                "name": "Advanced ML Algorithms",
                "duration": "3 weeks",
                "topics": ["XGBoost", "LightGBM", "Random Forests", "Stacking & ensembles"],
                "tasks": ["Win a Kaggle tabular competition using XGBoost"],
                "resources": [
                    {"title": "XGBoost Docs", "url": "https://xgboost.readthedocs.io/"},
                ],
            },
            {
                "name": "SQL for Data Science",
                "duration": "2 weeks",
                "topics": ["Window functions", "CTEs", "Aggregations", "BigQuery basics"],
                "tasks": ["Answer 10 business questions using SQL alone"],
                "resources": [
                    {"title": "Mode SQL Tutorial", "url": "https://mode.com/sql-tutorial/"},
                ],
            },
            {
                "name": "Data Storytelling",
                "duration": "2 weeks",
                "topics": ["Tableau / Power BI", "Storytelling with charts", "Executive dashboards"],
                "tasks": ["Build a 3-page dashboard in Tableau Public"],
                "resources": [
                    {"title": "Tableau Public", "url": "https://public.tableau.com/"},
                ],
            },
            {
                "name": "End-to-End Project",
                "duration": "3 weeks",
                "topics": ["Problem definition", "Data collection", "Modeling", "Presentation"],
                "tasks": ["Deliver a full data science project with slides and code"],
                "resources": [
                    {"title": "Kaggle Datasets", "url": "https://www.kaggle.com/datasets"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Data Scientist",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Bayesian Statistics",
                "duration": "3 weeks",
                "topics": ["Bayes theorem", "MCMC", "PyMC", "Posterior distributions"],
                "tasks": ["Build a Bayesian A/B test model"],
                "resources": [
                    {"title": "Probabilistic Programming & Bayesian Methods", "url": "https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers"},
                ],
            },
            {
                "name": "Time Series Analysis",
                "duration": "3 weeks",
                "topics": ["ARIMA", "Prophet", "Seasonal decomposition", "Forecasting"],
                "tasks": ["Forecast monthly sales for 12 months"],
                "resources": [
                    {"title": "Facebook Prophet Docs", "url": "https://facebook.github.io/prophet/"},
                ],
            },
            {
                "name": "Deep Learning for Tabular & NLP",
                "duration": "3 weeks",
                "topics": ["TabNet", "Text classification", "Embeddings for features"],
                "tasks": ["Apply NLP features to a tabular classification problem"],
                "resources": [
                    {"title": "fast.ai Course", "url": "https://course.fast.ai/"},
                ],
            },
            {
                "name": "Data Engineering Basics",
                "duration": "2 weeks",
                "topics": ["ETL pipelines", "Airflow", "Data lakes", "Spark intro"],
                "tasks": ["Build a simple ETL pipeline with Airflow"],
                "resources": [
                    {"title": "Apache Airflow Docs", "url": "https://airflow.apache.org/docs/"},
                ],
            },
            {
                "name": "Causal Inference",
                "duration": "2 weeks",
                "topics": ["RCTs", "Difference-in-differences", "DoWhy library", "CATE"],
                "tasks": ["Estimate causal effect of a marketing campaign"],
                "resources": [
                    {"title": "DoWhy Docs", "url": "https://py-why.github.io/dowhy/"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  5. CYBER SECURITY ENGINEER
# ─────────────────────────────────────────────
CYBER_SECURITY = {
    "beginner": {
        "goal": "Cyber Security Engineer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Networking Fundamentals",
                "duration": "2 weeks",
                "topics": ["OSI model", "TCP/IP", "DNS", "HTTP/HTTPS", "Firewalls"],
                "tasks": ["Use Wireshark to capture & analyze packets"],
                "resources": [
                    {"title": "Professor Messer CompTIA Network+", "url": "https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-training-course/"},
                ],
            },
            {
                "name": "Linux Basics",
                "duration": "2 weeks",
                "topics": ["File system", "Permissions", "Bash scripting", "Process management"],
                "tasks": ["Complete OverTheWire Bandit (levels 0-15)"],
                "resources": [
                    {"title": "OverTheWire Bandit", "url": "https://overthewire.org/wargames/bandit/"},
                    {"title": "Linux Journey", "url": "https://linuxjourney.com/"},
                ],
            },
            {
                "name": "Security Fundamentals",
                "duration": "2 weeks",
                "topics": ["CIA triad", "Cryptography basics", "Common vulnerabilities (OWASP Top 10)"],
                "tasks": ["Study and summarize the OWASP Top 10"],
                "resources": [
                    {"title": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/"},
                    {"title": "TryHackMe (free rooms)", "url": "https://tryhackme.com/"},
                ],
            },
            {
                "name": "Intro to Ethical Hacking",
                "duration": "2 weeks",
                "topics": ["Kali Linux setup", "Nmap scanning", "Basic exploitation concepts"],
                "tasks": ["Complete TryHackMe 'Pre-Security' learning path"],
                "resources": [
                    {"title": "TryHackMe Pre-Security", "url": "https://tryhackme.com/path/outline/presecurity"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Cyber Security Engineer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Web Application Security",
                "duration": "3 weeks",
                "topics": ["SQL injection", "XSS", "CSRF", "Burp Suite"],
                "tasks": ["Complete DVWA (Damn Vulnerable Web App) all modules"],
                "resources": [
                    {"title": "PortSwigger Web Security Academy (free)", "url": "https://portswigger.net/web-security"},
                ],
            },
            {
                "name": "Network Penetration Testing",
                "duration": "3 weeks",
                "topics": ["Metasploit", "Vulnerability scanning", "Exploitation", "Post-exploitation"],
                "tasks": ["Hack a Hack The Box starter machine"],
                "resources": [
                    {"title": "Hack The Box", "url": "https://www.hackthebox.com/"},
                    {"title": "TryHackMe Jr Penetration Tester", "url": "https://tryhackme.com/path/outline/jrpenetrationtester"},
                ],
            },
            {
                "name": "Cryptography & PKI",
                "duration": "2 weeks",
                "topics": ["Symmetric/asymmetric encryption", "TLS/SSL", "Certificates", "Hashing"],
                "tasks": ["Implement AES encryption in Python"],
                "resources": [
                    {"title": "Cryptohack (free)", "url": "https://cryptohack.org/"},
                ],
            },
            {
                "name": "SIEM & Log Analysis",
                "duration": "2 weeks",
                "topics": ["Splunk basics", "Log formats", "Threat detection rules", "Incident response"],
                "tasks": ["Analyze a PCAP file for indicators of compromise"],
                "resources": [
                    {"title": "Splunk Free Training", "url": "https://www.splunk.com/en_us/training/free-courses/splunk-fundamentals-1.html"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Cyber Security Engineer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Red Team Operations",
                "duration": "4 weeks",
                "topics": ["Advanced exploitation", "C2 frameworks (Cobalt Strike concepts)", "Pivoting", "Evasion"],
                "tasks": ["Complete a full TryHackMe Red Team path"],
                "resources": [
                    {"title": "TryHackMe Red Teaming", "url": "https://tryhackme.com/path/outline/redteaming"},
                ],
            },
            {
                "name": "Malware Analysis",
                "duration": "3 weeks",
                "topics": ["Static analysis", "Dynamic analysis", "IDA Pro basics", "Sandboxing"],
                "tasks": ["Analyze a real malware sample in a sandbox"],
                "resources": [
                    {"title": "ANY.RUN Sandbox", "url": "https://app.any.run/"},
                    {"title": "Malware Unicorn Workshops", "url": "https://malwareunicorn.org/"},
                ],
            },
            {
                "name": "Cloud Security",
                "duration": "3 weeks",
                "topics": ["AWS IAM", "S3 misconfigurations", "Cloud attack paths", "Prowler"],
                "tasks": ["Find vulnerabilities in a CloudGoat environment"],
                "resources": [
                    {"title": "CloudGoat by Rhino Security", "url": "https://github.com/RhinoSecurityLabs/cloudgoat"},
                ],
            },
            {
                "name": "Security Research & CVEs",
                "duration": "4 weeks",
                "topics": ["Vulnerability research", "0-day disclosure", "Bug bounty programs"],
                "tasks": ["Submit a valid bug bounty report on HackerOne"],
                "resources": [
                    {"title": "HackerOne", "url": "https://www.hackerone.com/"},
                    {"title": "Bugcrowd", "url": "https://www.bugcrowd.com/"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  6. DEVOPS ENGINEER
# ─────────────────────────────────────────────
DEVOPS = {
    "beginner": {
        "goal": "DevOps Engineer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Linux & Bash",
                "duration": "2 weeks",
                "topics": ["Shell commands", "Bash scripting", "Cron jobs", "SSH"],
                "tasks": ["Write a bash script to automate backups"],
                "resources": [
                    {"title": "Linux Command Line Book (free)", "url": "https://linuxcommand.org/tlcl.php"},
                ],
            },
            {
                "name": "Git & Version Control",
                "duration": "1 week",
                "topics": ["Branching strategies", "Pull requests", "Merge conflicts", "Git hooks"],
                "tasks": ["Implement GitFlow on a sample project"],
                "resources": [
                    {"title": "Atlassian Git Tutorials", "url": "https://www.atlassian.com/git/tutorials"},
                ],
            },
            {
                "name": "Docker Basics",
                "duration": "3 weeks",
                "topics": ["Images & containers", "Dockerfile", "Docker Compose", "Volumes & networking"],
                "tasks": ["Dockerize a Flask app with Compose (app + DB)"],
                "resources": [
                    {"title": "Play with Docker", "url": "https://labs.play-with-docker.com/"},
                    {"title": "Docker Docs Get Started", "url": "https://docs.docker.com/get-started/"},
                ],
            },
            {
                "name": "CI/CD Basics",
                "duration": "2 weeks",
                "topics": ["GitHub Actions", "Pipelines", "Build & test automation", "Artifacts"],
                "tasks": ["Set up a CI pipeline that runs tests on every push"],
                "resources": [
                    {"title": "GitHub Actions Docs", "url": "https://docs.github.com/en/actions"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "DevOps Engineer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Kubernetes",
                "duration": "4 weeks",
                "topics": ["Pods", "Deployments", "Services", "ConfigMaps", "Ingress"],
                "tasks": ["Deploy a multi-container app on Minikube"],
                "resources": [
                    {"title": "Kubernetes.io Interactive Tutorial", "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/"},
                    {"title": "KodeKloud (free tier)", "url": "https://kodekloud.com/"},
                ],
            },
            {
                "name": "Infrastructure as Code",
                "duration": "3 weeks",
                "topics": ["Terraform basics", "Ansible", "Modules", "State management"],
                "tasks": ["Provision an EC2 instance with Terraform"],
                "resources": [
                    {"title": "Terraform Learn", "url": "https://developer.hashicorp.com/terraform/tutorials"},
                ],
            },
            {
                "name": "Monitoring & Alerting",
                "duration": "2 weeks",
                "topics": ["Prometheus", "Grafana", "Alertmanager", "Dashboards"],
                "tasks": ["Set up a Prometheus + Grafana stack for your app"],
                "resources": [
                    {"title": "Grafana Labs Tutorials", "url": "https://grafana.com/tutorials/"},
                ],
            },
            {
                "name": "Cloud Platforms (AWS/GCP)",
                "duration": "3 weeks",
                "topics": ["EC2", "S3", "VPC", "IAM", "Lambda basics"],
                "tasks": ["Deploy a containerized app to AWS ECS"],
                "resources": [
                    {"title": "AWS Free Tier", "url": "https://aws.amazon.com/free/"},
                    {"title": "AWS Skill Builder", "url": "https://skillbuilder.aws/"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "DevOps Engineer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "GitOps & ArgoCD",
                "duration": "2 weeks",
                "topics": ["GitOps principles", "ArgoCD setup", "Flux", "Automated sync"],
                "tasks": ["Implement full GitOps workflow with ArgoCD"],
                "resources": [
                    {"title": "ArgoCD Docs", "url": "https://argo-cd.readthedocs.io/"},
                ],
            },
            {
                "name": "Service Mesh",
                "duration": "2 weeks",
                "topics": ["Istio / Linkerd", "mTLS", "Traffic management", "Observability"],
                "tasks": ["Deploy Istio on a Kubernetes cluster"],
                "resources": [
                    {"title": "Istio Docs", "url": "https://istio.io/latest/docs/"},
                ],
            },
            {
                "name": "Security in DevOps (DevSecOps)",
                "duration": "3 weeks",
                "topics": ["SAST/DAST", "Container scanning", "Secrets management (Vault)", "SBOM"],
                "tasks": ["Add Trivy scanning to your CI pipeline"],
                "resources": [
                    {"title": "HashiCorp Vault", "url": "https://developer.hashicorp.com/vault/tutorials"},
                ],
            },
            {
                "name": "SRE Practices",
                "duration": "3 weeks",
                "topics": ["SLOs/SLAs/SLIs", "Error budgets", "Chaos engineering", "Incident management"],
                "tasks": ["Run a chaos experiment with LitmusChaos"],
                "resources": [
                    {"title": "Google SRE Book (free)", "url": "https://sre.google/sre-book/table-of-contents/"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  7. FULL STACK DEVELOPER
# ─────────────────────────────────────────────
FULLSTACK = {
    "beginner": {
        "goal": "Full Stack Developer",
        "level": "Beginner",
        "duration": "4 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "HTML, CSS & JavaScript",
                "duration": "3 weeks",
                "topics": ["Semantic HTML", "Flexbox", "JS DOM", "ES6+"],
                "tasks": ["Build a responsive landing page"],
                "resources": [
                    {"title": "The Odin Project (free)", "url": "https://www.theodinproject.com/"},
                ],
            },
            {
                "name": "Python & Flask",
                "duration": "3 weeks",
                "topics": ["Routes", "Templates", "Forms", "SQLite"],
                "tasks": ["Build a simple blog with Flask"],
                "resources": [
                    {"title": "Flask Mega-Tutorial", "url": "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world"},
                ],
            },
            {
                "name": "Databases",
                "duration": "2 weeks",
                "topics": ["SQL basics", "SQLite", "SQLAlchemy ORM", "CRUD operations"],
                "tasks": ["Build a contact book with a database"],
                "resources": [
                    {"title": "SQLZoo", "url": "https://sqlzoo.net/"},
                ],
            },
            {
                "name": "First Full Stack Project",
                "duration": "2 weeks",
                "topics": ["Frontend + backend integration", "Forms to DB", "User sessions"],
                "tasks": ["Build a task manager app with login, CRUD, and a styled UI"],
                "resources": [
                    {"title": "Full Stack Python", "url": "https://www.fullstackpython.com/"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Full Stack Developer",
        "level": "Intermediate",
        "duration": "5 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "React.js",
                "duration": "4 weeks",
                "topics": ["Components", "Hooks", "React Router", "Context API"],
                "tasks": ["Build a React frontend that consumes your Flask API"],
                "resources": [
                    {"title": "React Official Docs", "url": "https://react.dev/"},
                ],
            },
            {
                "name": "REST API with Flask/Django",
                "duration": "3 weeks",
                "topics": ["Flask-RESTful", "Serialization", "JWT auth", "CORS"],
                "tasks": ["Build a fully authenticated REST API"],
                "resources": [
                    {"title": "Flask-RESTful Docs", "url": "https://flask-restful.readthedocs.io/"},
                ],
            },
            {
                "name": "PostgreSQL",
                "duration": "2 weeks",
                "topics": ["Advanced queries", "Indexes", "Relationships", "Migrations"],
                "tasks": ["Migrate your SQLite app to PostgreSQL"],
                "resources": [
                    {"title": "PostgreSQL Tutorial", "url": "https://www.postgresqltutorial.com/"},
                ],
            },
            {
                "name": "Deployment",
                "duration": "2 weeks",
                "topics": ["Heroku / Railway", "Render", "Environment variables", "Production config"],
                "tasks": ["Deploy your full stack app publicly"],
                "resources": [
                    {"title": "Railway.app", "url": "https://railway.app/"},
                    {"title": "Render Docs", "url": "https://render.com/docs"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Full Stack Developer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Next.js + TypeScript",
                "duration": "4 weeks",
                "topics": ["App Router", "Server components", "TypeScript", "tRPC"],
                "tasks": ["Build a SaaS app with Next.js App Router"],
                "resources": [
                    {"title": "Next.js Learn", "url": "https://nextjs.org/learn"},
                ],
            },
            {
                "name": "GraphQL",
                "duration": "2 weeks",
                "topics": ["Schema definition", "Resolvers", "Apollo Client", "Subscriptions"],
                "tasks": ["Replace your REST API with GraphQL"],
                "resources": [
                    {"title": "Apollo GraphQL Tutorial", "url": "https://www.apollographql.com/tutorials/"},
                ],
            },
            {
                "name": "Real-time Features",
                "duration": "2 weeks",
                "topics": ["WebSockets", "Socket.io", "SSE", "Live collaboration"],
                "tasks": ["Build a real-time chat feature"],
                "resources": [
                    {"title": "Socket.io Docs", "url": "https://socket.io/docs/v4/"},
                ],
            },
            {
                "name": "Full Stack Architecture",
                "duration": "3 weeks",
                "topics": ["Monorepo setup (Turborepo)", "Edge functions", "Caching layers", "Scalability"],
                "tasks": ["Design and implement a scalable multi-tenant SaaS"],
                "resources": [
                    {"title": "Turborepo Docs", "url": "https://turbo.build/repo/docs"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  8. MOBILE DEVELOPER (Android / iOS)
# ─────────────────────────────────────────────
MOBILE = {
    "beginner": {
        "goal": "Mobile Developer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Flutter & Dart Basics",
                "duration": "3 weeks",
                "topics": ["Dart syntax", "Widgets", "Layouts", "Hot reload"],
                "tasks": ["Build a counter app", "Build a BMI calculator"],
                "resources": [
                    {"title": "Flutter.dev Learn", "url": "https://flutter.dev/learn"},
                    {"title": "Dart.dev Tour", "url": "https://dart.dev/language"},
                ],
            },
            {
                "name": "Navigation & State",
                "duration": "2 weeks",
                "topics": ["Navigator 2.0", "Provider", "setState", "GetX basics"],
                "tasks": ["Build a multi-screen quiz app"],
                "resources": [
                    {"title": "Flutter Navigation", "url": "https://docs.flutter.dev/development/ui/navigation"},
                ],
            },
            {
                "name": "UI Components",
                "duration": "2 weeks",
                "topics": ["Material Design", "Custom widgets", "Animations", "Responsive layouts"],
                "tasks": ["Clone a popular app's UI (Spotify / Airbnb)"],
                "resources": [
                    {"title": "Flutter Widget Catalog", "url": "https://docs.flutter.dev/development/ui/widgets"},
                ],
            },
            {
                "name": "First App on Device",
                "duration": "1 week",
                "topics": ["Android emulator", "iOS Simulator", "Build & run", "App icons & splash"],
                "tasks": ["Run your quiz app on a real device or emulator"],
                "resources": [
                    {"title": "Flutter Install Guide", "url": "https://docs.flutter.dev/get-started/install"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Mobile Developer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Firebase Integration",
                "duration": "3 weeks",
                "topics": ["Authentication", "Firestore", "Storage", "Cloud Functions"],
                "tasks": ["Build a real-time chat app with Firebase"],
                "resources": [
                    {"title": "FlutterFire Docs", "url": "https://firebase.flutter.dev/docs/overview/"},
                ],
            },
            {
                "name": "REST API & Local Storage",
                "duration": "2 weeks",
                "topics": ["http package", "JSON parsing", "SharedPreferences", "SQLite (sqflite)"],
                "tasks": ["Build a news app that caches articles offline"],
                "resources": [
                    {"title": "pub.dev packages", "url": "https://pub.dev/"},
                ],
            },
            {
                "name": "Riverpod / Bloc",
                "duration": "3 weeks",
                "topics": ["State management patterns", "Riverpod providers", "BLoC pattern"],
                "tasks": ["Refactor your chat app to use Riverpod"],
                "resources": [
                    {"title": "Riverpod Docs", "url": "https://riverpod.dev/"},
                ],
            },
            {
                "name": "Publish to Stores",
                "duration": "1 week",
                "topics": ["Google Play Console", "App Store Connect", "Signing & versioning"],
                "tasks": ["Publish your app to Google Play (free)"],
                "resources": [
                    {"title": "Flutter Deployment Guide", "url": "https://docs.flutter.dev/deployment/android"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Mobile Developer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Native Integration",
                "duration": "2 weeks",
                "topics": ["Platform channels", "Method channels", "Native Kotlin/Swift modules"],
                "tasks": ["Build a Flutter plugin that uses a native camera API"],
                "resources": [
                    {"title": "Flutter Platform Channels", "url": "https://docs.flutter.dev/development/platform-integration/platform-channels"},
                ],
            },
            {
                "name": "Performance & Profiling",
                "duration": "2 weeks",
                "topics": ["Flutter DevTools", "Frame budget", "Jank reduction", "Image caching"],
                "tasks": ["Profile your app and reduce frame drops to 0"],
                "resources": [
                    {"title": "Flutter Performance Docs", "url": "https://docs.flutter.dev/perf"},
                ],
            },
            {
                "name": "On-device ML",
                "duration": "3 weeks",
                "topics": ["TensorFlow Lite", "ML Kit", "On-device inference", "Model conversion"],
                "tasks": ["Add real-time object detection to your app"],
                "resources": [
                    {"title": "TFLite Flutter", "url": "https://pub.dev/packages/tflite_flutter"},
                ],
            },
            {
                "name": "Monetization & Analytics",
                "duration": "2 weeks",
                "topics": ["In-app purchases", "AdMob", "Firebase Analytics", "A/B testing"],
                "tasks": ["Implement in-app purchases in a test app"],
                "resources": [
                    {"title": "in_app_purchase package", "url": "https://pub.dev/packages/in_app_purchase"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  9. BLOCKCHAIN DEVELOPER
# ─────────────────────────────────────────────
BLOCKCHAIN = {
    "beginner": {
        "goal": "Blockchain Developer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Blockchain Fundamentals",
                "duration": "1 week",
                "topics": ["What is blockchain", "Consensus mechanisms", "Wallets & keys", "Bitcoin vs Ethereum"],
                "tasks": ["Create a MetaMask wallet", "Make a testnet transaction"],
                "resources": [
                    {"title": "Ethereum.org Learn", "url": "https://ethereum.org/en/learn/"},
                    {"title": "CryptoZombies (free)", "url": "https://cryptozombies.io/"},
                ],
            },
            {
                "name": "Solidity Basics",
                "duration": "4 weeks",
                "topics": ["Data types", "Functions", "Modifiers", "Events", "Mappings"],
                "tasks": ["Write a simple storage contract", "Create an ERC-20 token"],
                "resources": [
                    {"title": "Solidity Docs", "url": "https://docs.soliditylang.org/"},
                    {"title": "CryptoZombies", "url": "https://cryptozombies.io/"},
                ],
            },
            {
                "name": "Hardhat Development",
                "duration": "2 weeks",
                "topics": ["Hardhat setup", "Compile & deploy", "Local blockchain", "Test scripts"],
                "tasks": ["Deploy your ERC-20 token to Sepolia testnet"],
                "resources": [
                    {"title": "Hardhat Docs", "url": "https://hardhat.org/docs"},
                ],
            },
            {
                "name": "Web3.js / Ethers.js",
                "duration": "1 week",
                "topics": ["Connect wallet", "Read contract data", "Send transactions"],
                "tasks": ["Build a simple dApp frontend that reads your contract"],
                "resources": [
                    {"title": "Ethers.js Docs", "url": "https://docs.ethers.org/"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Blockchain Developer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Smart Contract Patterns",
                "duration": "3 weeks",
                "topics": ["OpenZeppelin", "Proxy patterns", "Upgradeable contracts", "Access control"],
                "tasks": ["Build an upgradeable ERC-721 NFT contract"],
                "resources": [
                    {"title": "OpenZeppelin Docs", "url": "https://docs.openzeppelin.com/"},
                ],
            },
            {
                "name": "DeFi Protocols",
                "duration": "3 weeks",
                "topics": ["AMMs", "Liquidity pools", "Lending protocols", "Flash loans"],
                "tasks": ["Fork Uniswap V2 and deploy a local DEX"],
                "resources": [
                    {"title": "Uniswap V2 Docs", "url": "https://docs.uniswap.org/contracts/v2/overview"},
                ],
            },
            {
                "name": "Smart Contract Security",
                "duration": "2 weeks",
                "topics": ["Reentrancy", "Integer overflow", "Access control bugs", "Slither / MythX"],
                "tasks": ["Complete Ethernaut security challenges"],
                "resources": [
                    {"title": "Ethernaut", "url": "https://ethernaut.openzeppelin.com/"},
                ],
            },
            {
                "name": "Full dApp",
                "duration": "3 weeks",
                "topics": ["React + Wagmi", "IPFS for storage", "The Graph (indexing)", "Deployment"],
                "tasks": ["Build and deploy a full NFT marketplace dApp"],
                "resources": [
                    {"title": "Wagmi Docs", "url": "https://wagmi.sh/"},
                    {"title": "The Graph Docs", "url": "https://thegraph.com/docs/"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Blockchain Developer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Layer 2 & Scaling",
                "duration": "3 weeks",
                "topics": ["Optimistic rollups", "ZK-rollups", "Arbitrum", "Polygon zkEVM"],
                "tasks": ["Deploy a contract on Arbitrum Sepolia"],
                "resources": [
                    {"title": "L2BEAT", "url": "https://l2beat.com/"},
                    {"title": "Arbitrum Docs", "url": "https://docs.arbitrum.io/"},
                ],
            },
            {
                "name": "Zero-Knowledge Proofs",
                "duration": "4 weeks",
                "topics": ["ZK basics", "Circom / snarkjs", "Groth16", "ZK applications"],
                "tasks": ["Build a ZK proof that verifies age without revealing it"],
                "resources": [
                    {"title": "ZKP Learning Resources", "url": "https://zkproof.org/"},
                ],
            },
            {
                "name": "Protocol Design",
                "duration": "4 weeks",
                "topics": ["Tokenomics", "Governance", "DAO structures", "Incentive design"],
                "tasks": ["Design a governance DAO with voting and treasury"],
                "resources": [
                    {"title": "Compound Governance Docs", "url": "https://compound.finance/governance"},
                ],
            },
            {
                "name": "Audit & Bug Bounty",
                "duration": "3 weeks",
                "topics": ["Manual audit methodology", "Foundry fuzzing", "Code4rena contests"],
                "tasks": ["Participate in a Code4rena or Sherlock audit"],
                "resources": [
                    {"title": "Code4rena", "url": "https://code4rena.com/"},
                    {"title": "Foundry Docs", "url": "https://book.getfoundry.sh/"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  10. GAME DEVELOPER
# ─────────────────────────────────────────────
GAME_DEV = {
    "beginner": {
        "goal": "Game Developer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Godot Engine Basics",
                "duration": "2 weeks",
                "topics": ["Scenes & nodes", "GDScript", "2D sprites", "Input handling"],
                "tasks": ["Build Pong", "Build a simple platformer"],
                "resources": [
                    {"title": "Godot Docs", "url": "https://docs.godotengine.org/"},
                    {"title": "GDQuest Godot Tutorials", "url": "https://www.gdquest.com/tutorial/godot/"},
                ],
            },
            {
                "name": "Game Physics & Collision",
                "duration": "2 weeks",
                "topics": ["RigidBody2D", "KinematicBody", "CollisionShape", "Areas"],
                "tasks": ["Add gravity and collision to your platformer"],
                "resources": [
                    {"title": "Godot Physics Tutorial", "url": "https://docs.godotengine.org/en/stable/tutorials/physics/"},
                ],
            },
            {
                "name": "Tilemaps & Level Design",
                "duration": "2 weeks",
                "topics": ["TileMap node", "Autotile", "Level scenes", "Camera2D"],
                "tasks": ["Design 3 levels for your platformer"],
                "resources": [
                    {"title": "Godot TileMap Docs", "url": "https://docs.godotengine.org/en/stable/tutorials/2d/using_tilemaps.html"},
                ],
            },
            {
                "name": "Audio & Polish",
                "duration": "1 week",
                "topics": ["AudioStreamPlayer", "SFX", "Music loops", "Particles"],
                "tasks": ["Add sound effects, music, and particle effects"],
                "resources": [
                    {"title": "Freesound.org (free audio)", "url": "https://freesound.org/"},
                ],
            },
            {
                "name": "Export & Publish",
                "duration": "1 week",
                "topics": ["Export templates", "Web export (HTML5)", "itch.io publishing"],
                "tasks": ["Publish your game to itch.io"],
                "resources": [
                    {"title": "itch.io", "url": "https://itch.io/"},
                    {"title": "Godot Export Docs", "url": "https://docs.godotengine.org/en/stable/tutorials/export/"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Game Developer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "3D Game Development",
                "duration": "4 weeks",
                "topics": ["3D scenes", "MeshInstance3D", "CharacterBody3D", "3D camera", "Lighting"],
                "tasks": ["Build a basic 3D FPS prototype"],
                "resources": [
                    {"title": "Godot 3D Tutorial", "url": "https://docs.godotengine.org/en/stable/tutorials/3d/"},
                ],
            },
            {
                "name": "Game AI",
                "duration": "2 weeks",
                "topics": ["State machines", "Pathfinding (NavigationAgent)", "Enemy behaviour"],
                "tasks": ["Add a patrolling enemy that chases the player"],
                "resources": [
                    {"title": "Godot NavigationServer", "url": "https://docs.godotengine.org/en/stable/tutorials/navigation/"},
                ],
            },
            {
                "name": "Save & Load System",
                "duration": "1 week",
                "topics": ["JSON save files", "ConfigFile", "Encryption basics"],
                "tasks": ["Implement a full save/load system with multiple slots"],
                "resources": [
                    {"title": "Godot Save Games", "url": "https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html"},
                ],
            },
            {
                "name": "Shader Basics",
                "duration": "2 weeks",
                "topics": ["CanvasItem shaders", "GLSL basics", "Colour effects", "Outlines"],
                "tasks": ["Write a custom outline shader for your player character"],
                "resources": [
                    {"title": "Godot Shaders", "url": "https://docs.godotengine.org/en/stable/tutorials/shaders/"},
                    {"title": "The Book of Shaders", "url": "https://thebookofshaders.com/"},
                ],
            },
            {
                "name": "Game Jam Project",
                "duration": "3 weeks",
                "topics": ["Rapid prototyping", "Scope management", "Polish vs features"],
                "tasks": ["Enter a Ludum Dare or Global Game Jam and finish a game"],
                "resources": [
                    {"title": "Ludum Dare", "url": "https://ldjam.com/"},
                    {"title": "itch.io Game Jams", "url": "https://itch.io/jams"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Game Developer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Multiplayer Networking",
                "duration": "4 weeks",
                "topics": ["ENet / WebSocket", "RPC", "Client-side prediction", "Lag compensation"],
                "tasks": ["Build a 2-player online game with Godot Multiplayer API"],
                "resources": [
                    {"title": "Godot Multiplayer Docs", "url": "https://docs.godotengine.org/en/stable/tutorials/networking/"},
                ],
            },
            {
                "name": "Procedural Generation",
                "duration": "3 weeks",
                "topics": ["Noise functions", "Wave Function Collapse", "Dungeon generation"],
                "tasks": ["Generate an infinite procedural dungeon"],
                "resources": [
                    {"title": "Procedural Content Generation Book (free)", "url": "http://pcgbook.com/"},
                ],
            },
            {
                "name": "Advanced Rendering",
                "duration": "3 weeks",
                "topics": ["Custom post-processing", "PBR materials", "LOD systems", "GPU particles"],
                "tasks": ["Implement a full-screen post-process bloom + chromatic aberration"],
                "resources": [
                    {"title": "Godot Advanced Shaders", "url": "https://docs.godotengine.org/en/stable/tutorials/shaders/advanced_postprocessing.html"},
                ],
            },
            {
                "name": "Steam / Console Publishing",
                "duration": "3 weeks",
                "topics": ["Steam Greenlight replaced by Direct", "Achievements API", "GodotSteam plugin"],
                "tasks": ["Integrate Steamworks achievements into your game"],
                "resources": [
                    {"title": "GodotSteam", "url": "https://godotsteam.com/"},
                    {"title": "Steam Direct", "url": "https://partner.steamgames.com/"},
                ],
            },
        ],
    },
}

# ─────────────────────────────────────────────
#  11. DATA ANALYST
# ─────────────────────────────────────────────
DATA_ANALYST = {
    "beginner": {
        "goal": "Data Analyst",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Excel for Data Analysis",
                "duration": "2 weeks",
                "topics": ["Formulas & functions", "Pivot tables", "VLOOKUP", "Charts & graphs", "Conditional formatting"],
                "tasks": ["Analyze a sales dataset using pivot tables", "Create a monthly revenue dashboard in Excel"],
                "resources": [
                    {"title": "Excel for Beginners — freeCodeCamp YouTube", "url": "https://www.youtube.com/watch?v=Vl0H-qTclOg"},
                    {"title": "Excel Easy Tutorial", "url": "https://www.excel-easy.com/"},
                ],
            },
            {
                "name": "SQL Basics",
                "duration": "2 weeks",
                "topics": ["SELECT, WHERE, ORDER BY", "GROUP BY & aggregations", "JOINs", "Subqueries", "HAVING clause"],
                "tasks": ["Answer 10 business questions using SQL", "Analyze a retail database with JOINs"],
                "resources": [
                    {"title": "SQLZoo", "url": "https://sqlzoo.net/"},
                    {"title": "Mode SQL Tutorial", "url": "https://mode.com/sql-tutorial/"},
                ],
            },
            {
                "name": "Python for Data Analysis",
                "duration": "3 weeks",
                "topics": ["Pandas basics", "NumPy", "Data cleaning", "Merging datasets", "GroupBy operations"],
                "tasks": ["Load and clean a Kaggle CSV dataset", "Calculate summary statistics with Pandas"],
                "resources": [
                    {"title": "Kaggle Pandas Course (free)", "url": "https://www.kaggle.com/learn/pandas"},
                    {"title": "Kaggle Python Course (free)", "url": "https://www.kaggle.com/learn/python"},
                ],
            },
            {
                "name": "Data Visualization",
                "duration": "2 weeks",
                "topics": ["Matplotlib", "Seaborn", "Chart types", "Storytelling with data", "Color and design basics"],
                "tasks": ["Create 5 different chart types for one dataset", "Build a visual EDA report"],
                "resources": [
                    {"title": "Kaggle Data Visualization (free)", "url": "https://www.kaggle.com/learn/data-visualization"},
                    {"title": "Seaborn Tutorial", "url": "https://seaborn.pydata.org/tutorial.html"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Data Analyst",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Advanced SQL",
                "duration": "2 weeks",
                "topics": ["Window functions", "CTEs", "Stored procedures", "Query optimization", "BigQuery basics"],
                "tasks": ["Write window function queries for running totals", "Optimize a slow-running query"],
                "resources": [
                    {"title": "Advanced SQL for Data Scientists", "url": "https://mode.com/sql-tutorial/sql-window-functions/"},
                    {"title": "BigQuery Free Tier", "url": "https://cloud.google.com/bigquery/docs/sandbox"},
                ],
            },
            {
                "name": "Statistics for Analysis",
                "duration": "2 weeks",
                "topics": ["Descriptive statistics", "Hypothesis testing", "A/B testing", "Correlation vs causation", "Regression basics"],
                "tasks": ["Run an A/B test simulation in Python", "Test hypothesis on a real dataset"],
                "resources": [
                    {"title": "StatQuest with Josh Starmer", "url": "https://www.youtube.com/c/joshstarmer"},
                    {"title": "Khan Academy Statistics", "url": "https://www.khanacademy.org/math/statistics-probability"},
                ],
            },
            {
                "name": "Tableau / Power BI",
                "duration": "3 weeks",
                "topics": ["Connecting data sources", "Building dashboards", "Calculated fields", "Filters & parameters", "Publishing reports"],
                "tasks": ["Build a 3-page executive dashboard in Tableau Public", "Create an interactive sales report"],
                "resources": [
                    {"title": "Tableau Public (free)", "url": "https://public.tableau.com/"},
                    {"title": "Tableau Training Videos", "url": "https://www.tableau.com/learn/training"},
                ],
            },
            {
                "name": "Business Analytics",
                "duration": "2 weeks",
                "topics": ["KPIs and metrics", "Funnel analysis", "Cohort analysis", "Customer segmentation", "Presenting insights"],
                "tasks": ["Perform cohort analysis on an e-commerce dataset", "Present findings in a 5-slide deck"],
                "resources": [
                    {"title": "Google Analytics Academy (free)", "url": "https://analytics.google.com/analytics/academy/"},
                ],
            },
            {
                "name": "End-to-End Analysis Project",
                "duration": "3 weeks",
                "topics": ["Problem framing", "Data collection", "Cleaning & EDA", "Insights & recommendations", "Presentation"],
                "tasks": ["Complete a full business analytics case study", "Present findings to a mock stakeholder"],
                "resources": [
                    {"title": "Kaggle Datasets", "url": "https://www.kaggle.com/datasets"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Data Analyst",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Advanced Analytics with Python",
                "duration": "3 weeks",
                "topics": ["Pandas advanced (multi-index, reshape)", "Scipy for statistics", "Statsmodels", "Time series analysis", "Forecasting with Prophet"],
                "tasks": ["Build a sales forecasting model", "Perform time series decomposition"],
                "resources": [
                    {"title": "Facebook Prophet Docs", "url": "https://facebook.github.io/prophet/"},
                    {"title": "Statsmodels Tutorial", "url": "https://www.statsmodels.org/stable/gettingstarted.html"},
                ],
            },
            {
                "name": "Data Engineering for Analysts",
                "duration": "3 weeks",
                "topics": ["ETL pipelines", "Data warehousing concepts", "dbt (data build tool)", "Airflow basics", "Data modeling"],
                "tasks": ["Build a simple ETL pipeline", "Create a dbt model for a dataset"],
                "resources": [
                    {"title": "dbt Learn (free)", "url": "https://courses.getdbt.com/"},
                    {"title": "Modern Data Stack Guide", "url": "https://www.moderndatastack.xyz/"},
                ],
            },
            {
                "name": "Machine Learning for Analysts",
                "duration": "3 weeks",
                "topics": ["Regression models", "Classification", "Clustering for segmentation", "Feature importance", "Model interpretation"],
                "tasks": ["Build a customer churn prediction model", "Segment customers with K-Means clustering"],
                "resources": [
                    {"title": "Kaggle ML Course (free)", "url": "https://www.kaggle.com/learn/intro-to-machine-learning"},
                ],
            },
            {
                "name": "Advanced Visualization & Storytelling",
                "duration": "2 weeks",
                "topics": ["Plotly & Dash", "D3.js basics", "Executive storytelling", "Data journalism techniques"],
                "tasks": ["Build an interactive web dashboard with Plotly Dash", "Tell a data story in 3 charts"],
                "resources": [
                    {"title": "Plotly Dash Tutorial", "url": "https://dash.plotly.com/tutorial"},
                    {"title": "Storytelling with Data book summary", "url": "https://www.storytellingwithdata.com/"},
                ],
            },
            {
                "name": "Portfolio & Interview Prep",
                "duration": "2 weeks",
                "topics": ["Case study interviews", "SQL interview questions", "Portfolio presentation", "Business case walkthroughs"],
                "tasks": ["Solve 20 SQL interview questions", "Publish 2 analysis projects on GitHub/Kaggle"],
                "resources": [
                    {"title": "LeetCode SQL", "url": "https://leetcode.com/problemset/database/"},
                    {"title": "DataLemur SQL Interview Questions", "url": "https://datalemur.com/"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  12. CLOUD ENGINEER
# ─────────────────────────────────────────────
CLOUD_ENGINEER = {
    "beginner": {
        "goal": "Cloud Engineer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Cloud Fundamentals",
                "duration": "1 week",
                "topics": ["What is cloud computing", "IaaS vs PaaS vs SaaS", "Public vs private vs hybrid", "Major providers (AWS, GCP, Azure)", "Cloud pricing models"],
                "tasks": ["Create a free AWS account", "Explore the AWS console and identify 10 services"],
                "resources": [
                    {"title": "AWS Cloud Practitioner Essentials (free)", "url": "https://aws.amazon.com/training/digital/aws-cloud-practitioner-essentials/"},
                    {"title": "Google Cloud Skills Boost (free tier)", "url": "https://cloudskillsboost.google/"},
                ],
            },
            {
                "name": "Linux & Bash for Cloud",
                "duration": "2 weeks",
                "topics": ["Shell commands", "File permissions", "Bash scripting", "SSH", "Process management"],
                "tasks": ["Write a bash script to automate file backups", "Connect to an EC2 instance via SSH"],
                "resources": [
                    {"title": "Linux Command Line Book (free)", "url": "https://linuxcommand.org/tlcl.php"},
                    {"title": "OverTheWire Bandit (Linux practice)", "url": "https://overthewire.org/wargames/bandit/"},
                ],
            },
            {
                "name": "AWS Core Services",
                "duration": "3 weeks",
                "topics": ["EC2 (virtual machines)", "S3 (object storage)", "VPC (networking)", "IAM (identity & access)", "RDS (databases)"],
                "tasks": ["Launch an EC2 instance and host a webpage", "Upload files to S3 and set permissions"],
                "resources": [
                    {"title": "AWS Free Tier", "url": "https://aws.amazon.com/free/"},
                    {"title": "AWS Skill Builder (free courses)", "url": "https://skillbuilder.aws/"},
                ],
            },
            {
                "name": "Networking Basics",
                "duration": "2 weeks",
                "topics": ["TCP/IP", "DNS", "HTTP/HTTPS", "Load balancers", "CDN concepts"],
                "tasks": ["Set up a custom VPC with public and private subnets", "Configure a security group"],
                "resources": [
                    {"title": "AWS Networking Fundamentals", "url": "https://aws.amazon.com/getting-started/projects/build-wordpress-website/"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Cloud Engineer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Infrastructure as Code (Terraform)",
                "duration": "3 weeks",
                "topics": ["Terraform basics", "Providers & resources", "State management", "Modules", "Workspaces"],
                "tasks": ["Provision an EC2 + RDS setup with Terraform", "Use Terraform modules for reusability"],
                "resources": [
                    {"title": "Terraform Learn", "url": "https://developer.hashicorp.com/terraform/tutorials"},
                ],
            },
            {
                "name": "Containers & Docker",
                "duration": "2 weeks",
                "topics": ["Docker images & containers", "Dockerfile", "Docker Compose", "Amazon ECR", "ECS basics"],
                "tasks": ["Containerize a Flask app", "Push image to ECR and run on ECS"],
                "resources": [
                    {"title": "Docker Get Started", "url": "https://docs.docker.com/get-started/"},
                    {"title": "Play with Docker (free)", "url": "https://labs.play-with-docker.com/"},
                ],
            },
            {
                "name": "Kubernetes on Cloud",
                "duration": "3 weeks",
                "topics": ["Pods, Deployments, Services", "Amazon EKS / Google GKE", "Helm charts", "ConfigMaps & Secrets", "Auto-scaling"],
                "tasks": ["Deploy a multi-container app on EKS", "Set up horizontal pod autoscaling"],
                "resources": [
                    {"title": "Kubernetes.io Tutorials", "url": "https://kubernetes.io/docs/tutorials/"},
                    {"title": "KodeKloud (free tier)", "url": "https://kodekloud.com/"},
                ],
            },
            {
                "name": "CI/CD in the Cloud",
                "duration": "2 weeks",
                "topics": ["AWS CodePipeline", "GitHub Actions with AWS", "Blue/green deployments", "Infrastructure pipelines"],
                "tasks": ["Build a full CI/CD pipeline from GitHub to AWS ECS"],
                "resources": [
                    {"title": "GitHub Actions Docs", "url": "https://docs.github.com/en/actions"},
                    {"title": "AWS CodePipeline Tutorial", "url": "https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials.html"},
                ],
            },
            {
                "name": "Cloud Security",
                "duration": "2 weeks",
                "topics": ["IAM best practices", "Security groups & NACLs", "AWS WAF", "Secrets Manager", "Compliance basics"],
                "tasks": ["Audit an AWS account for security issues using Prowler"],
                "resources": [
                    {"title": "AWS Security Best Practices", "url": "https://docs.aws.amazon.com/security/"},
                    {"title": "Prowler (free AWS security tool)", "url": "https://github.com/prowler-cloud/prowler"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Cloud Engineer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Multi-Cloud Architecture",
                "duration": "3 weeks",
                "topics": ["AWS vs GCP vs Azure comparison", "Multi-cloud strategy", "Cloud-agnostic tools", "Disaster recovery", "Cost optimization"],
                "tasks": ["Design a multi-cloud architecture for high availability"],
                "resources": [
                    {"title": "Cloud Architecture Center (Google)", "url": "https://cloud.google.com/architecture"},
                    {"title": "AWS Well-Architected Framework", "url": "https://aws.amazon.com/architecture/well-architected/"},
                ],
            },
            {
                "name": "Serverless Architecture",
                "duration": "2 weeks",
                "topics": ["AWS Lambda", "API Gateway", "Event-driven architecture", "Step Functions", "Serverless Framework"],
                "tasks": ["Build a serverless API with Lambda + API Gateway + DynamoDB"],
                "resources": [
                    {"title": "Serverless Framework Docs", "url": "https://www.serverless.com/framework/docs"},
                    {"title": "AWS Lambda Docs", "url": "https://docs.aws.amazon.com/lambda/"},
                ],
            },
            {
                "name": "Site Reliability Engineering (SRE)",
                "duration": "3 weeks",
                "topics": ["SLOs, SLAs, SLIs", "Error budgets", "Observability (Prometheus, Grafana)", "Chaos engineering", "On-call practices"],
                "tasks": ["Set up Prometheus + Grafana monitoring stack", "Run a chaos experiment with LitmusChaos"],
                "resources": [
                    {"title": "Google SRE Book (free)", "url": "https://sre.google/sre-book/table-of-contents/"},
                    {"title": "Grafana Labs Tutorials", "url": "https://grafana.com/tutorials/"},
                ],
            },
            {
                "name": "Cloud Certifications Prep",
                "duration": "4 weeks",
                "topics": ["AWS Solutions Architect Associate", "Practice exams", "Architecture scenarios", "Cost estimation"],
                "tasks": ["Score 80%+ on 3 AWS SAA practice exams", "Design a full architecture for an e-commerce platform"],
                "resources": [
                    {"title": "AWS Exam Readiness (free)", "url": "https://aws.amazon.com/training/digital/aws-exam-readiness/"},
                    {"title": "ExamTopics AWS Practice Questions", "url": "https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-associate/"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  13. AR/VR DEVELOPER
# ─────────────────────────────────────────────
AR_VR = {
    "beginner": {
        "goal": "AR/VR Developer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "3D Fundamentals",
                "duration": "1 week",
                "topics": ["3D coordinate systems", "Meshes & polygons", "Textures & materials", "Lighting basics", "Camera concepts"],
                "tasks": ["Explore a 3D scene in Blender", "Create a simple 3D object with textures"],
                "resources": [
                    {"title": "Blender Beginner Tutorial (free)", "url": "https://www.youtube.com/watch?v=nIoXOplUvAw"},
                    {"title": "Blender.org (free software)", "url": "https://www.blender.org/"},
                ],
            },
            {
                "name": "Unity Basics",
                "duration": "3 weeks",
                "topics": ["Unity Editor overview", "GameObjects & components", "C# scripting basics", "Physics & colliders", "Scenes & prefabs"],
                "tasks": ["Build a simple 3D game (collect coins)", "Create a basic VR scene in Unity"],
                "resources": [
                    {"title": "Unity Learn (free)", "url": "https://learn.unity.com/"},
                    {"title": "Unity Essentials Pathway", "url": "https://learn.unity.com/pathway/unity-essentials"},
                ],
            },
            {
                "name": "AR Basics with AR Foundation",
                "duration": "2 weeks",
                "topics": ["AR concepts", "Plane detection", "Image tracking", "AR Foundation setup", "ARCore / ARKit"],
                "tasks": ["Build an AR app that places a 3D object on a flat surface", "Create a simple AR business card"],
                "resources": [
                    {"title": "Unity AR Foundation Docs", "url": "https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@latest"},
                    {"title": "Google ARCore Intro", "url": "https://developers.google.com/ar/develop"},
                ],
            },
            {
                "name": "VR Basics with XR Toolkit",
                "duration": "2 weeks",
                "topics": ["VR interaction design", "XR Interaction Toolkit", "Controllers & raycasting", "Teleportation", "VR comfort guidelines"],
                "tasks": ["Build a basic VR environment with interactable objects", "Implement VR locomotion"],
                "resources": [
                    {"title": "Unity XR Toolkit Docs", "url": "https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@latest"},
                    {"title": "Meta Quest Developer Hub", "url": "https://developer.oculus.com/"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "AR/VR Developer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Advanced Unity & C#",
                "duration": "3 weeks",
                "topics": ["Object-oriented design in Unity", "Scriptable Objects", "Unity Events", "Coroutines", "Optimization techniques"],
                "tasks": ["Build a complete VR game with a score system", "Implement an inventory system"],
                "resources": [
                    {"title": "Unity Advanced Programming", "url": "https://learn.unity.com/pathway/junior-programmer"},
                ],
            },
            {
                "name": "3D Modeling for XR",
                "duration": "2 weeks",
                "topics": ["Low-poly modeling", "UV unwrapping", "PBR materials", "GLTF/GLB format", "Polygon budgets for VR"],
                "tasks": ["Create a low-poly environment optimized for VR", "Export and import model into Unity"],
                "resources": [
                    {"title": "Blender Guru Donut Tutorial", "url": "https://www.youtube.com/watch?v=nIoXOplUvAw"},
                    {"title": "Sketchfab (3D model library)", "url": "https://sketchfab.com/"},
                ],
            },
            {
                "name": "Spatial Audio & Haptics",
                "duration": "1 week",
                "topics": ["3D spatial audio", "Oculus Audio SDK", "Haptic feedback basics", "Audio design for immersion"],
                "tasks": ["Implement 3D spatial audio in a VR scene"],
                "resources": [
                    {"title": "Meta Spatial Audio SDK", "url": "https://developer.oculus.com/documentation/unity/audio-ovrsource/"},
                ],
            },
            {
                "name": "WebXR Development",
                "duration": "2 weeks",
                "topics": ["WebXR API", "Three.js for 3D", "A-Frame framework", "Browser-based AR/VR", "Progressive Web XR"],
                "tasks": ["Build a WebXR experience accessible from any browser", "Create an A-Frame VR scene"],
                "resources": [
                    {"title": "A-Frame (free framework)", "url": "https://aframe.io/"},
                    {"title": "WebXR Device API", "url": "https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API"},
                ],
            },
            {
                "name": "XR Portfolio Project",
                "duration": "4 weeks",
                "topics": ["Full XR application design", "User testing", "Performance profiling", "App Store submission"],
                "tasks": ["Build and publish a complete AR or VR app", "Get feedback from 5 real users"],
                "resources": [
                    {"title": "Meta Quest App Lab", "url": "https://developer.oculus.com/blog/introducing-app-lab-a-new-way-to-distribute-oculus-quest-apps/"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "AR/VR Developer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Hand Tracking & Body Tracking",
                "duration": "2 weeks",
                "topics": ["Meta Hand Tracking SDK", "Gesture recognition", "Full body avatars", "Face tracking", "Eye tracking"],
                "tasks": ["Build a hand-tracking VR interface without controllers"],
                "resources": [
                    {"title": "Meta Hand Tracking Docs", "url": "https://developer.oculus.com/documentation/unity/unity-handtracking/"},
                ],
            },
            {
                "name": "AI in XR",
                "duration": "3 weeks",
                "topics": ["AI NPCs in VR", "Computer vision for AR", "Object detection (YOLO) in AR", "Generative AI for XR content"],
                "tasks": ["Build an AR app that detects real-world objects using ML Kit"],
                "resources": [
                    {"title": "Google ML Kit (free)", "url": "https://developers.google.com/ml-kit"},
                    {"title": "Unity Sentis (AI in Unity)", "url": "https://docs.unity3d.com/Packages/com.unity.sentis@latest"},
                ],
            },
            {
                "name": "Multiplayer XR",
                "duration": "3 weeks",
                "topics": ["Photon PUN2", "Shared AR spaces", "Avatar synchronization", "Latency management", "Voice chat in VR"],
                "tasks": ["Build a multiplayer VR meeting room"],
                "resources": [
                    {"title": "Photon PUN2 Docs", "url": "https://doc.photonengine.com/pun/current/getting-started/pun-intro"},
                ],
            },
            {
                "name": "Unreal Engine for XR",
                "duration": "4 weeks",
                "topics": ["Unreal Engine basics", "Blueprints", "VR template", "Nanite & Lumen for XR", "Pixel streaming"],
                "tasks": ["Port a Unity VR project concept to Unreal Engine"],
                "resources": [
                    {"title": "Unreal Engine Online Learning (free)", "url": "https://www.unrealengine.com/en-US/onlinelearning-courses"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  14. UI/UX DESIGNER
# ─────────────────────────────────────────────
UI_UX = {
    "beginner": {
        "goal": "UI/UX Designer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Design Fundamentals",
                "duration": "1 week",
                "topics": ["Color theory", "Typography basics", "Visual hierarchy", "Grid systems", "White space"],
                "tasks": ["Analyze the design of 5 popular apps", "Create a mood board for a mobile app"],
                "resources": [
                    {"title": "Google UX Design Certificate (audit free)", "url": "https://www.coursera.org/professional-certificates/google-ux-design"},
                    {"title": "Laws of UX", "url": "https://lawsofux.com/"},
                ],
            },
            {
                "name": "Figma Basics",
                "duration": "2 weeks",
                "topics": ["Figma interface", "Frames & layers", "Components & variants", "Auto layout", "Prototyping basics"],
                "tasks": ["Design a mobile login screen in Figma", "Create a simple clickable prototype"],
                "resources": [
                    {"title": "Figma Learn (free)", "url": "https://help.figma.com/hc/en-us/categories/360002051613"},
                    {"title": "Figma Tutorials YouTube", "url": "https://www.youtube.com/@Figma"},
                ],
            },
            {
                "name": "UX Research Basics",
                "duration": "2 weeks",
                "topics": ["User interviews", "Surveys", "Personas", "User journey mapping", "Empathy maps"],
                "tasks": ["Create a user persona for a food delivery app", "Map the user journey for online shopping"],
                "resources": [
                    {"title": "Nielsen Norman Group Articles (free)", "url": "https://www.nngroup.com/articles/"},
                    {"title": "UX Collective (free articles)", "url": "https://uxdesign.cc/"},
                ],
            },
            {
                "name": "Wireframing & Prototyping",
                "duration": "2 weeks",
                "topics": ["Low-fidelity wireframes", "High-fidelity mockups", "Interactive prototypes", "Usability testing", "Design handoff"],
                "tasks": ["Wireframe a complete e-commerce app (5 screens)", "Test prototype with 3 real users"],
                "resources": [
                    {"title": "Figma Prototyping Guide", "url": "https://help.figma.com/hc/en-us/articles/360040314193"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "UI/UX Designer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Design Systems",
                "duration": "2 weeks",
                "topics": ["Component libraries", "Design tokens", "Style guides", "Atomic design", "Figma variables"],
                "tasks": ["Build a complete design system for a SaaS product", "Document all components with usage guidelines"],
                "resources": [
                    {"title": "Material Design 3 (Google)", "url": "https://m3.material.io/"},
                    {"title": "Apple Human Interface Guidelines", "url": "https://developer.apple.com/design/human-interface-guidelines/"},
                ],
            },
            {
                "name": "Advanced UX Research",
                "duration": "2 weeks",
                "topics": ["A/B testing", "Card sorting", "Tree testing", "Eye tracking concepts", "Quantitative UX metrics"],
                "tasks": ["Conduct a usability test and write a report", "Run an A/B test on two button designs"],
                "resources": [
                    {"title": "Maze (free usability testing)", "url": "https://maze.co/"},
                    {"title": "UXtweak (free research tool)", "url": "https://www.uxtweak.com/"},
                ],
            },
            {
                "name": "Interaction Design",
                "duration": "2 weeks",
                "topics": ["Micro-interactions", "Motion design", "Figma animations", "Principle of least surprise", "Feedback & affordance"],
                "tasks": ["Design 5 micro-interactions for a mobile app", "Create an animated onboarding flow"],
                "resources": [
                    {"title": "Figma Smart Animate Tutorial", "url": "https://help.figma.com/hc/en-us/articles/360039818874"},
                    {"title": "UI Movement (inspiration)", "url": "https://uimovement.com/"},
                ],
            },
            {
                "name": "UX Writing",
                "duration": "1 week",
                "topics": ["Microcopy", "Error messages", "CTA writing", "Onboarding copy", "Tone & voice"],
                "tasks": ["Rewrite 10 confusing error messages", "Write onboarding copy for a productivity app"],
                "resources": [
                    {"title": "UX Writing Hub (free)", "url": "https://uxwritinghub.com/"},
                ],
            },
            {
                "name": "Portfolio & Case Studies",
                "duration": "3 weeks",
                "topics": ["UX case study structure", "Problem → Process → Solution", "Behance / Dribbble portfolio", "Portfolio website"],
                "tasks": ["Write a complete case study for your best project", "Publish portfolio on Behance or personal site"],
                "resources": [
                    {"title": "Behance (free portfolio)", "url": "https://www.behance.net/"},
                    {"title": "Dribbble", "url": "https://dribbble.com/"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "UI/UX Designer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Strategic UX & Product Thinking",
                "duration": "3 weeks",
                "topics": ["Jobs-to-be-done framework", "OKRs for UX", "Design strategy", "Business impact of UX", "Stakeholder management"],
                "tasks": ["Define OKRs for a UX project", "Present a design strategy to a mock executive team"],
                "resources": [
                    {"title": "Lean UX (book summary)", "url": "https://www.nngroup.com/articles/lean-ux/"},
                ],
            },
            {
                "name": "Accessibility & Inclusive Design",
                "duration": "2 weeks",
                "topics": ["WCAG 2.1 guidelines", "Screen reader design", "Color contrast", "Motor accessibility", "Cognitive accessibility"],
                "tasks": ["Audit an existing app for accessibility issues", "Redesign 3 screens to meet WCAG AA standard"],
                "resources": [
                    {"title": "WebAIM (free accessibility tool)", "url": "https://webaim.org/"},
                    {"title": "WCAG 2.1 Guidelines", "url": "https://www.w3.org/WAI/WCAG21/quickref/"},
                ],
            },
            {
                "name": "Design Leadership",
                "duration": "2 weeks",
                "topics": ["Design critique facilitation", "Mentoring junior designers", "Design sprints", "Cross-functional collaboration", "Design documentation"],
                "tasks": ["Facilitate a design sprint for a real problem", "Write a design brief and share with a team"],
                "resources": [
                    {"title": "Design Sprint Kit (Google)", "url": "https://designsprintkit.withgoogle.com/"},
                ],
            },
            {
                "name": "Emerging UX (AI, Voice, XR)",
                "duration": "3 weeks",
                "topics": ["AI-powered design tools", "Voice UI design", "Conversational UX", "AR/VR UX principles", "Zero UI"],
                "tasks": ["Design a voice interface for a smart home app", "Prototype an AR shopping experience"],
                "resources": [
                    {"title": "Designing Voice Interfaces (Nielsen Norman)", "url": "https://www.nngroup.com/articles/voice-interfaces/"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  15. EMBEDDED SYSTEMS ENGINEER
# ─────────────────────────────────────────────
EMBEDDED = {
    "beginner": {
        "goal": "Embedded Systems Engineer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Electronics Fundamentals",
                "duration": "1 week",
                "topics": ["Voltage, current, resistance", "Ohm's law", "Basic circuits", "Breadboarding", "Common components (resistors, capacitors, LEDs)"],
                "tasks": ["Build a simple LED blinking circuit on a breadboard", "Calculate resistor values for an LED circuit"],
                "resources": [
                    {"title": "All About Circuits (free)", "url": "https://www.allaboutcircuits.com/"},
                    {"title": "Electronics Tutorials", "url": "https://www.electronics-tutorials.ws/"},
                ],
            },
            {
                "name": "Arduino Programming",
                "duration": "3 weeks",
                "topics": ["Arduino IDE setup", "Digital I/O", "Analog I/O", "PWM", "Serial communication", "Sensors & actuators"],
                "tasks": ["Build a temperature monitor with DHT11 sensor", "Control an LED brightness with a potentiometer"],
                "resources": [
                    {"title": "Arduino Official Tutorials", "url": "https://docs.arduino.cc/built-in-examples/"},
                    {"title": "Arduino Project Hub", "url": "https://create.arduino.cc/projecthub"},
                ],
            },
            {
                "name": "C Programming for Embedded",
                "duration": "3 weeks",
                "topics": ["Pointers", "Bit manipulation", "Structs", "Memory management", "Volatile keyword", "Interrupt basics"],
                "tasks": ["Write a C program to toggle GPIO using bit manipulation", "Implement a simple state machine in C"],
                "resources": [
                    {"title": "Embedded C Programming (free)", "url": "https://www.learn-c.org/"},
                    {"title": "Barr Group Embedded C Coding Standard", "url": "https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard"},
                ],
            },
            {
                "name": "Microcontroller Basics",
                "duration": "1 week",
                "topics": ["MCU architecture", "GPIO", "Timers", "UART/I2C/SPI", "STM32 vs ESP32 vs Arduino"],
                "tasks": ["Set up ESP32 development environment", "Blink an LED on ESP32 using ESP-IDF"],
                "resources": [
                    {"title": "ESP32 Getting Started", "url": "https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/"},
                    {"title": "Random Nerd Tutorials (ESP32)", "url": "https://randomnerdtutorials.com/esp32/"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "Embedded Systems Engineer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "RTOS (Real-Time Operating Systems)",
                "duration": "3 weeks",
                "topics": ["FreeRTOS basics", "Tasks & scheduling", "Queues & semaphores", "Mutexes", "Interrupt handling in RTOS"],
                "tasks": ["Implement a producer-consumer system with FreeRTOS queues", "Create a multi-task LED control system"],
                "resources": [
                    {"title": "FreeRTOS Official Docs", "url": "https://www.freertos.org/Documentation/RTOS_book.html"},
                    {"title": "Mastering FreeRTOS (free PDF)", "url": "https://www.freertos.org/Documentation/Mastering-the-FreeRTOS-Real-Time-Kernel.v1.1.0.pdf"},
                ],
            },
            {
                "name": "Communication Protocols",
                "duration": "2 weeks",
                "topics": ["UART deep dive", "SPI master/slave", "I2C addressing", "CAN bus basics", "Modbus"],
                "tasks": ["Communicate between two STM32 boards via SPI", "Read sensor data over I2C"],
                "resources": [
                    {"title": "Serial Protocols Explained (DigiKey)", "url": "https://www.digikey.com/en/blog/uart-i2c-spi-serial-peripheral-interfaces"},
                ],
            },
            {
                "name": "STM32 Development",
                "duration": "3 weeks",
                "topics": ["STM32CubeIDE", "HAL library", "GPIO, Timer, ADC", "DMA", "Bootloader basics"],
                "tasks": ["Build a data logger with STM32 that saves to SD card", "Implement DMA-based ADC sampling"],
                "resources": [
                    {"title": "STM32 Getting Started (ST Micro)", "url": "https://www.st.com/en/development-tools/stm32cubeide.html"},
                    {"title": "ControllersTech STM32 Tutorials", "url": "https://controllerstech.com/stm32-tutorials/"},
                ],
            },
            {
                "name": "IoT Connectivity",
                "duration": "2 weeks",
                "topics": ["WiFi with ESP32", "MQTT protocol", "AWS IoT Core", "HTTP REST from MCU", "OTA updates"],
                "tasks": ["Send sensor data to AWS IoT Core via MQTT", "Implement OTA firmware update on ESP32"],
                "resources": [
                    {"title": "AWS IoT Core Docs", "url": "https://docs.aws.amazon.com/iot/"},
                    {"title": "MQTT Essentials (HiveMQ)", "url": "https://www.hivemq.com/mqtt-essentials/"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "Embedded Systems Engineer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Linux Embedded Systems",
                "duration": "4 weeks",
                "topics": ["Yocto Project", "Buildroot", "Device tree", "Kernel modules", "Linux drivers"],
                "tasks": ["Build a custom Linux image with Buildroot for Raspberry Pi", "Write a simple Linux kernel module"],
                "resources": [
                    {"title": "Buildroot Docs", "url": "https://buildroot.org/docs.html"},
                    {"title": "Linux Device Drivers (free book)", "url": "https://lwn.net/Kernel/LDD3/"},
                ],
            },
            {
                "name": "DSP & Signal Processing",
                "duration": "3 weeks",
                "topics": ["FFT basics", "Digital filters (FIR/IIR)", "ADC/DAC theory", "CMSIS-DSP library", "Audio processing"],
                "tasks": ["Implement a low-pass FIR filter on STM32", "Perform FFT on ADC samples"],
                "resources": [
                    {"title": "CMSIS-DSP Library Docs", "url": "https://arm-software.github.io/CMSIS_6/latest/DSP/index.html"},
                    {"title": "DSP Guide (free book)", "url": "https://www.dspguide.com/"},
                ],
            },
            {
                "name": "Functional Safety",
                "duration": "2 weeks",
                "topics": ["IEC 61508 / ISO 26262 basics", "MISRA C coding standard", "Safety integrity levels", "Fault tolerance", "Hardware watchdogs"],
                "tasks": ["Apply MISRA C rules to existing code using a linter", "Design a watchdog timer system"],
                "resources": [
                    {"title": "MISRA C Guidelines", "url": "https://www.misra.org.uk/"},
                    {"title": "Automotive Functional Safety Intro", "url": "https://www.renesas.com/us/en/document/whp/introduction-automotive-functional-safety"},
                ],
            },
            {
                "name": "Edge AI on Microcontrollers",
                "duration": "3 weeks",
                "topics": ["TensorFlow Lite for Microcontrollers", "Model quantization", "Edge Impulse", "Neural network on MCU", "Keyword spotting"],
                "tasks": ["Deploy a keyword spotting model on Arduino Nano 33 BLE", "Train and deploy a gesture classifier"],
                "resources": [
                    {"title": "Edge Impulse (free)", "url": "https://www.edgeimpulse.com/"},
                    {"title": "TensorFlow Lite Micro Docs", "url": "https://www.tensorflow.org/lite/microcontrollers"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  16. QA/TESTING ENGINEER
# ─────────────────────────────────────────────
QA_ENGINEER = {
    "beginner": {
        "goal": "QA/Testing Engineer",
        "level": "Beginner",
        "duration": "3 months",
        "hours_per_day": 2,
        "source": "manual",
        "skills": [
            {
                "name": "Software Testing Fundamentals",
                "duration": "1 week",
                "topics": ["Types of testing (unit, integration, system, acceptance)", "Black box vs white box", "Test case design", "Bug life cycle", "Test plan basics"],
                "tasks": ["Write 20 test cases for a login page", "Document a bug report for a real app"],
                "resources": [
                    {"title": "ISTQB Foundation Level Syllabus (free)", "url": "https://www.istqb.org/certifications/certified-tester-foundation-level"},
                    {"title": "Software Testing Help", "url": "https://www.softwaretestinghelp.com/"},
                ],
            },
            {
                "name": "Manual Testing",
                "duration": "2 weeks",
                "topics": ["Functional testing", "Regression testing", "Exploratory testing", "Boundary value analysis", "Equivalence partitioning"],
                "tasks": ["Manually test a real website and document 10 bugs", "Write a test plan for a mobile app"],
                "resources": [
                    {"title": "Guru99 Manual Testing Tutorial", "url": "https://www.guru99.com/manual-testing.html"},
                ],
            },
            {
                "name": "API Testing with Postman",
                "duration": "2 weeks",
                "topics": ["HTTP methods (GET, POST, PUT, DELETE)", "Request/response structure", "Postman collections", "Assertions in Postman", "Environment variables"],
                "tasks": ["Test a public REST API with 15 test cases", "Write automated assertions in Postman"],
                "resources": [
                    {"title": "Postman Learning Center (free)", "url": "https://learning.postman.com/"},
                    {"title": "ReqRes API for practice", "url": "https://reqres.in/"},
                ],
            },
            {
                "name": "SQL for Testers",
                "duration": "2 weeks",
                "topics": ["SELECT queries", "WHERE clauses", "JOINs for validation", "Verifying database changes", "Data integrity testing"],
                "tasks": ["Validate database state after 10 API calls", "Write SQL queries to verify test data"],
                "resources": [
                    {"title": "SQLZoo (free practice)", "url": "https://sqlzoo.net/"},
                ],
            },
        ],
    },
    "intermediate": {
        "goal": "QA/Testing Engineer",
        "level": "Intermediate",
        "duration": "4 months",
        "hours_per_day": 3,
        "source": "manual",
        "skills": [
            {
                "name": "Selenium WebDriver",
                "duration": "3 weeks",
                "topics": ["Selenium setup with Python", "Locators (XPath, CSS)", "Page Object Model", "Waits (explicit/implicit)", "Cross-browser testing"],
                "tasks": ["Automate login and search on a real website", "Implement Page Object Model for an e-commerce site"],
                "resources": [
                    {"title": "Selenium Python Docs", "url": "https://selenium-python.readthedocs.io/"},
                    {"title": "Selenium Official Docs", "url": "https://www.selenium.dev/documentation/"},
                ],
            },
            {
                "name": "Pytest Framework",
                "duration": "2 weeks",
                "topics": ["Pytest basics", "Fixtures", "Parametrize", "Markers", "Conftest.py", "HTML reports"],
                "tasks": ["Write a full test suite for a Flask API using pytest", "Generate HTML test reports"],
                "resources": [
                    {"title": "Pytest Official Docs", "url": "https://docs.pytest.org/en/stable/"},
                ],
            },
            {
                "name": "Performance Testing",
                "duration": "2 weeks",
                "topics": ["Load testing concepts", "JMeter basics", "Locust (Python)", "Response time analysis", "Bottleneck identification"],
                "tasks": ["Load test a web app with 100 concurrent users using Locust", "Identify performance bottleneck"],
                "resources": [
                    {"title": "Locust.io (free, Python-based)", "url": "https://locust.io/"},
                    {"title": "JMeter User Manual", "url": "https://jmeter.apache.org/usermanual/"},
                ],
            },
            {
                "name": "CI/CD for QA",
                "duration": "2 weeks",
                "topics": ["GitHub Actions for test automation", "Jenkins basics", "Test reporting in CI", "Fail fast strategy", "Quality gates"],
                "tasks": ["Set up GitHub Actions to run Selenium tests on every PR", "Configure quality gates"],
                "resources": [
                    {"title": "GitHub Actions Docs", "url": "https://docs.github.com/en/actions"},
                ],
            },
            {
                "name": "Mobile Testing",
                "duration": "3 weeks",
                "topics": ["Appium setup", "Mobile locators", "Android emulator", "iOS Simulator", "Mobile-specific testing (gestures, orientation)"],
                "tasks": ["Automate login flow on an Android app with Appium", "Test for different screen sizes"],
                "resources": [
                    {"title": "Appium Docs", "url": "https://appium.io/docs/en/latest/"},
                ],
            },
        ],
    },
    "advanced": {
        "goal": "QA/Testing Engineer",
        "level": "Advanced",
        "duration": "5 months",
        "hours_per_day": 4,
        "source": "manual",
        "skills": [
            {
                "name": "Test Architecture & Strategy",
                "duration": "2 weeks",
                "topics": ["Test pyramid", "Testing microservices", "Contract testing (Pact)", "Shift-left testing", "Test coverage metrics"],
                "tasks": ["Design a complete test strategy for a microservices application", "Implement contract testing"],
                "resources": [
                    {"title": "Pact Contract Testing (free)", "url": "https://docs.pact.io/"},
                    {"title": "Test Pyramid by Martin Fowler", "url": "https://martinfowler.com/articles/practical-test-pyramid.html"},
                ],
            },
            {
                "name": "Security Testing",
                "duration": "3 weeks",
                "topics": ["OWASP Top 10 testing", "SQL injection testing", "XSS testing", "CSRF testing", "ZAP proxy"],
                "tasks": ["Test a vulnerable web app (DVWA) for all OWASP Top 10", "Write a security test report"],
                "resources": [
                    {"title": "OWASP ZAP (free)", "url": "https://www.zaproxy.org/"},
                    {"title": "DVWA (Damn Vulnerable Web App)", "url": "https://dvwa.co.uk/"},
                ],
            },
            {
                "name": "AI in Testing",
                "duration": "2 weeks",
                "topics": ["AI-powered test generation", "Visual testing with AI", "Self-healing tests", "Test data generation with AI", "Testim / Mabl tools"],
                "tasks": ["Use AI to generate test cases for an untested module", "Implement visual regression testing"],
                "resources": [
                    {"title": "Applitools Visual AI Testing (free tier)", "url": "https://applitools.com/"},
                    {"title": "Testim (AI testing tool)", "url": "https://www.testim.io/"},
                ],
            },
            {
                "name": "QA Leadership",
                "duration": "2 weeks",
                "topics": ["Building a QA team", "Metrics (defect density, test coverage)", "QA process improvement", "Risk-based testing", "Stakeholder reporting"],
                "tasks": ["Create a QA metrics dashboard", "Write a quality improvement plan for a project"],
                "resources": [
                    {"title": "QA Lead Skills Guide", "url": "https://www.ministryoftesting.com/"},
                ],
            },
            {
                "name": "Advanced Automation Frameworks",
                "duration": "3 weeks",
                "topics": ["Playwright (modern web testing)", "Cypress advanced", "BDD with Behave/Cucumber", "Test data management", "Parallel execution"],
                "tasks": ["Migrate a Selenium suite to Playwright", "Implement BDD test scenarios with Behave"],
                "resources": [
                    {"title": "Playwright Docs (free)", "url": "https://playwright.dev/python/docs/intro"},
                    {"title": "Cypress Docs", "url": "https://docs.cypress.io/"},
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  MASTER REGISTRY — 16 careers total
# ─────────────────────────────────────────────
ROADMAP_REGISTRY = {
    # ── Original 10 careers ──
    "frontend":              FRONTEND,
    "backend":               BACKEND,
    "fullstack":             FULLSTACK,
    "full stack":            FULLSTACK,
    "ai engineer":           AI_ML,
    "machine learning":      AI_ML,
    "ml engineer":           AI_ML,
    "data scientist":        DATA_SCIENTIST,
    "data science":          DATA_SCIENTIST,
    "cyber security":        CYBER_SECURITY,
    "cybersecurity":         CYBER_SECURITY,
    "devops":                DEVOPS,
    "mobile":                MOBILE,
    "android":               MOBILE,
    "ios":                   MOBILE,
    "blockchain":            BLOCKCHAIN,
    "game developer":        GAME_DEV,
    "game development":      GAME_DEV,
    "data analyst":          DATA_ANALYST,
    "cloud engineer":        CLOUD_ENGINEER,
    "cloud computing":       CLOUD_ENGINEER,
    "ar/vr developer":       AR_VR,
    "ar vr developer":       AR_VR,
    "arvr":                  AR_VR,
    "augmented reality":     AR_VR,
    "virtual reality":       AR_VR,
    "ui/ux designer":        UI_UX,
    "ui ux designer":        UI_UX,
    "ux designer":           UI_UX,
    "ui designer":           UI_UX,
    "embedded systems":      EMBEDDED,
    "embedded engineer":     EMBEDDED,
    "iot engineer":          EMBEDDED,
    "qa engineer":           QA_ENGINEER,
    "qa testing":            QA_ENGINEER,
    "software tester":       QA_ENGINEER,
    "testing engineer":      QA_ENGINEER,
}