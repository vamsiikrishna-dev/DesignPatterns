# Adding Behavior Dynamically: The Decorator Design Pattern in File Processing

The Decorator pattern is a structural design pattern that allows you to add new functionality to objects dynamically without altering their structure. Today, we'll explore a practical implementation that demonstrates how to enhance file operations with encryption and compression capabilities using a flexible, composable approach.

## The Problem: Flexible File Processing Requirements

Imagine you're building a file management system where different files need different processing:

- Some files need to be **encrypted** for security
- Some files need to be **compressed** to save space
- Some files need **both encryption and compression**
- Some files need **neither** (just basic storage)

Without proper design, you might end up with:

- Multiple classes for every combination (FileRepository, EncryptedFileRepository, CompressedFileRepository, EncryptedCompressedFileRepository)
- Exponential growth of classes as you add more features
- Code duplication across similar classes
- Difficulty in combining features dynamically

## The Solution: Decorator Pattern

The Decorator pattern allows you to wrap objects with additional behavior layers, creating a flexible composition system where you can mix and match features as needed.

## Implementation Breakdown

### 1. Component Interface: IFileRepository

First, we define the common interface that all file handlers must implement:

```python
# IFileRepository.py
from abc import ABC, abstractmethod

class IFileRepository(ABC):
    @abstractmethod
    def write_file(self, file_name, data):
        pass

    @abstractmethod
    def read_file(self, file_name, data):
        pass
```

This interface ensures that all components (both base and decorators) provide consistent file operations.

### 2. Concrete Component: FileRepository

The base implementation provides core file operations:

```python
# FileRepository.py
from .IFileRepository import IFileRepository

class FileRepository(IFileRepository):
    def write_file(self, file_name, data):
        print(f"[FileRepository] written into file {file_name} with data {data}")

    def read_file(self, file_name):
        return f"Hello World"
```

This is the foundation component that handles basic file operations without any additional processing.

### 3. Concrete Decorators

#### FileEncrypter Decorator
```python
# FileEncrypter.py
from .FileRepository import IFileRepository

class FileEncrypter(IFileRepository):
    def __init__(self, wrapee: IFileRepository):
        self.repo: IFileRepository = wrapee

    def _encrypt_AES(self, data):
        data = "# " + data + " #"
        return data
    
    def _decrypt_AES(self, data):
        data = data[1:-1]
        return data

    def write_file(self, file_name, data):
        data = self._encrypt_AES(data)
        print(f"[FileEncrypter] Encrypted data {data}")
        self.repo.write_file(file_name, data)

    def read_file(self, file_name):
        data = self.repo.read_file(file_name)
        data = self._decrypt_AES(data)
        return f"{file_name} file_contents {data}"
```

#### FileCompressor Decorator
```python
# FileCompressor.py
from .FileRepository import IFileRepository

class FileCompressor(IFileRepository):
    def __init__(self, wrapee: IFileRepository):
        self.repo: IFileRepository = wrapee

    def _compress_base64(self, data):
        return f"$${data}$$"
    
    def _parse_base64(self, data):  
        return data[2:-2]

    def write_file(self, file_name, data):
        data1 = data
        data = self._compress_base64(data)
        print(f"[FileCompressor] {data1} compressed to {data}")
        self.repo.write_file(file_name, data)

    def read_file(self, file_name):
        data = self.repo.read_file(file_name)
        data = self._parse_base64(data)
        return f"data parsing is done. data::{data}"
```

### Key Design Elements

**Composition over Inheritance**: Decorators contain a reference to another component rather than inheriting from concrete classes.

**Interface Consistency**: All decorators implement the same interface as the base component.

**Transparent Wrapping**: Clients can use decorated objects exactly like the original objects.

**Recursive Composition**: Decorators can wrap other decorators, creating chains of behavior.

### 4. Client Usage: Flexible Composition

Here's how the decorators can be composed dynamically:

```python
# Client.py
from Utils import IFileRepository, FileRepository, FileCompressor, FileEncrypter

if __name__ == '__main__':
    # Basic file operations
    file_handler: IFileRepository = FileRepository()
    file_handler.write_file("sample.txt", "Hello World")
    
    # Add encryption
    file_handler = FileEncrypter(file_handler)
    file_handler.write_file("sample.txt", "Hello World")
    
    # Add both encryption and compression
    file_handler = FileCompressor(file_handler)
    file_handler.write_file("sample.txt", "Hello World")
```

## Composition Flexibility

The beauty of this pattern lies in its flexibility. You can create different combinations easily:

### Different Processing Pipelines
```python
# Just compression
compressed_handler = FileCompressor(FileRepository())

# Just encryption  
encrypted_handler = FileEncrypter(FileRepository())

# Compression then encryption
comp_then_encrypt = FileEncrypter(FileCompressor(FileRepository()))

# Encryption then compression
encrypt_then_comp = FileCompressor(FileEncrypter(FileRepository()))

# Multiple layers of the same decorator
double_encrypted = FileEncrypter(FileEncrypter(FileRepository()))
```

### Runtime Configuration
```python
def create_file_handler(needs_encryption=False, needs_compression=False):
    handler = FileRepository()
    
    if needs_encryption:
        handler = FileEncrypter(handler)
    
    if needs_compression:
        handler = FileCompressor(handler)
    
    return handler

# Configure based on requirements
secure_handler = create_file_handler(needs_encryption=True, needs_compression=True)
basic_handler = create_file_handler()
```

## Execution Flow Analysis

When you call `file_handler.write_file("sample.txt", "Hello World")` with both decorators:

1. **FileCompressor** receives the call
   - Compresses "Hello World" to "$$Hello World$$"
   - Calls the wrapped component (FileEncrypter)

2. **FileEncrypter** receives the compressed data
   - Encrypts "$$Hello World$$" to "# $$Hello World$$ #"
   - Calls the wrapped component (FileRepository)

3. **FileRepository** receives the processed data
   - Writes "# $$Hello World$$ #" to the file

The data flows through the decorator chain, with each decorator adding its processing layer.

## Advantages of This Implementation

### 1. **Dynamic Behavior Addition**
You can add or remove functionality at runtime without changing existing code:
```python
# Start with basic functionality
handler = FileRepository()

# Add encryption when needed
if user.requires_encryption():
    handler = FileEncrypter(handler)

# Add compression based on file size
if file_size > COMPRESSION_THRESHOLD:
    handler = FileCompressor(handler)
```

### 2. **Single Responsibility Principle**
Each decorator has one clear responsibility:
- FileEncrypter: Handles encryption/decryption
- FileCompressor: Handles compression/decompression
- FileRepository: Handles basic file operations

### 3. **Open/Closed Principle**
The system is open for extension (new decorators) but closed for modification (existing classes don't change).

### 4. **Flexible Combinations**
You can create any combination of behaviors without creating new classes for each combination.

## When to Use the Decorator Pattern

The Decorator pattern is ideal when:

- **Dynamic Behavior**: You need to add responsibilities to objects dynamically
- **Multiple Combinations**: You have several optional features that can be combined
- **Avoiding Class Explosion**: Creating subclasses for every combination would be impractical
- **Runtime Configuration**: Behavior needs to be configurable at runtime

## Real-World Applications

Beyond file processing, the Decorator pattern is commonly used for:

- **Web Middleware**: Adding authentication, logging, caching to HTTP requests
- **Stream Processing**: Adding buffering, encryption, compression to data streams
- **UI Components**: Adding borders, scrollbars, shadows to visual elements
- **Coffee Shop Example**: Adding milk, sugar, whipped cream to coffee orders
- **Logging Systems**: Adding timestamps, formatting, filtering to log messages

## Decorator vs. Other Patterns

### Decorator vs. Adapter
- **Decorator**: Adds new behavior while keeping the same interface
- **Adapter**: Changes the interface to make incompatible classes work together

### Decorator vs. Composite
- **Decorator**: Adds behavior to individual objects
- **Composite**: Treats groups of objects as single objects

### Decorator vs. Strategy
- **Decorator**: Adds layers of behavior
- **Strategy**: Chooses between different algorithms

## Best Practices

1. **Keep Decorators Lightweight**: Each decorator should add one specific behavior
2. **Maintain Interface Consistency**: All decorators should implement the same interface
3. **Consider Order**: The order of decoration matters for the final behavior
4. **Handle Edge Cases**: Consider what happens with null or invalid wrapped objects
5. **Document Behavior**: Clearly document how decorators interact with each other

## Extending the Implementation

You could enhance this implementation with additional decorators:

```python
class FileValidator(IFileRepository):
    def __init__(self, wrapee: IFileRepository):
        self.repo = wrapee
    
    def write_file(self, file_name, data):
        if not self._validate_data(data):
            raise ValueError("Invalid data format")
        self.repo.write_file(file_name, data)
    
    def _validate_data(self, data):
        return len(data) > 0 and isinstance(data, str)

class FileLogger(IFileRepository):
    def __init__(self, wrapee: IFileRepository):
        self.repo = wrapee
    
    def write_file(self, file_name, data):
        print(f"[FileLogger] Writing to {file_name}")
        self.repo.write_file(file_name, data)
        print(f"[FileLogger] Write completed")
```

## Conclusion

The Decorator pattern provides an elegant solution for adding behavior to objects dynamically without altering their structure. Our file processing example demonstrates how this pattern can create flexible, composable systems where features can be mixed and matched as needed.

By using composition instead of inheritance, we achieve better flexibility and avoid the class explosion problem that would occur with traditional inheritance-based approaches. The pattern promotes clean code organization, single responsibility, and makes it easy to add new features without modifying existing code.

Whether you're building file processing systems, web middleware, or any application that needs flexible behavior composition, the Decorator pattern is a powerful tool for creating maintainable, extensible software architectures.

The beauty of this pattern lies in its ability to transform simple objects into sophisticated, feature-rich components through elegant composition, making complex functionality feel natural and intuitive.