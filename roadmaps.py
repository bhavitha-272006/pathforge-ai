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
#  MASTER REGISTRY
# ─────────────────────────────────────────────
ROADMAP_REGISTRY = {
    "frontend":          FRONTEND,
    "backend":           BACKEND,
    "fullstack":         FULLSTACK,
    "full stack":        FULLSTACK,
    "ai engineer":       AI_ML,
    "machine learning":  AI_ML,
    "ml engineer":       AI_ML,
    "data scientist":    DATA_SCIENTIST,
    "data science":      DATA_SCIENTIST,
    "cyber security":    CYBER_SECURITY,
    "cybersecurity":     CYBER_SECURITY,
    "devops":            DEVOPS,
    "mobile":            MOBILE,
    "android":           MOBILE,
    "ios":               MOBILE,
    "blockchain":        BLOCKCHAIN,
    "game developer":    GAME_DEV,
    "game development":  GAME_DEV,
}