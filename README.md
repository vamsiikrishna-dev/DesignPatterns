# Design Patterns in Python 🐍

A comprehensive collection of design pattern implementations in Python with practical examples and detailed explanations.

## 📋 Overview

This repository demonstrates classic design patterns through real-world examples, making them easy to understand and apply in your own projects. Each pattern includes:

- Clean, well-documented Python code
- Practical use cases
- Detailed blog posts explaining the concepts
- Working examples you can run immediately

## 🎯 Patterns Implemented

### Creational Patterns

#### 🏭 [Abstract Factory Pattern](./AbstractFactory/)
Build cross-platform GUI components with families of related objects.
```python
gui_factory = MacFactory() if os == OSType.Mac else WindowsFactory()
button = gui_factory.create_button()
button.render()  # Renders platform-specific button
```

#### 🔨 [Builder Pattern](./Builder/)
Construct complex HTTP requests with a fluent interface.
```python
request = builder \
    .with_url("http://localhost:8000/users") \
    .with_method("GET") \
    .with_param("id", 2) \
    .build()
```

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Design-Patterns
```

2. Run any example:
```bash
cd AbstractFactory
python Client.py
```

3. Read the detailed explanations in the blog posts included with each pattern.

## 📚 What You'll Learn

- **When to use** each design pattern
- **Real-world applications** beyond textbook examples
- **Best practices** for implementing patterns in Python
- **Trade-offs** and considerations for each approach

## 🎓 Perfect For

- **Students** learning design patterns
- **Developers** looking for practical implementations
- **Interview preparation** with working code examples
- **Architecture decisions** in real projects

## 📖 Detailed Documentation

Each pattern folder contains:
- `Client.py` - Working example demonstrating usage
- Detailed blog post explaining the pattern
- Clean, production-ready implementations
- Comments explaining key design decisions

## 🤝 Contributing

Feel free to:
- Add new design patterns
- Improve existing implementations
- Fix bugs or typos
- Suggest better examples

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **Star this repo** if you find it helpful for learning design patterns!