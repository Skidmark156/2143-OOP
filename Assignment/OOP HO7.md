Part A: Conceptual Questions

DRY (Don’t Repeat Yourself)

Definition:
DRY (Don’t Repeat Yourself) is a principle that aims to reduce code duplication by ensuring that each piece of knowledge or logic exists in a single place within a system. This improves maintainability and reduces errors.

Example of DRY Violation:
class User {
public:
    void printUserDetails() {
        cout << "Name: John Doe" << endl;
        cout << "Age: 30" << endl;
    }
    
    void printUserDetailsWithAddress() {
        cout << "Name: John Doe" << endl;
        cout << "Age: 30" << endl;
        cout << "Address: 123 Main St" << endl;
    }
};

Refactored to Follow DRY:
class User {
public:
    void printUserDetails(bool includeAddress = false) {
        cout << "Name: John Doe" << endl;
        cout << "Age: 30" << endl;
        if (includeAddress) {
            cout << "Address: 123 Main St" << endl;
        }
    }
};

KISS (Keep It Simple, Stupid)

Definition:
KISS emphasizes simplicity in design and coding. Code should be as simple as possible while meeting requirements, avoiding unnecessary complexity.

Why It’s Crucial:

Easier debugging and maintenance.

Improves readability and collaboration.

Reduces potential errors.

Drawback of Oversimplification:
If code is oversimplified, it might lack necessary structure, leading to difficulty in scaling or adding features in the future.

Introduction to SOLID (High-Level)

Single Responsibility Principle (SRP): A class should have only one reason to change, meaning it should have a single responsibility.

Open-Closed Principle (OCP): Software entities should be open for extension but closed for modification, allowing enhancements without altering existing code.
Why SOLID Matters in Large Codebases:
Applying SOLID ensures maintainability, flexibility, and scalability by reducing dependencies, making the system easier to modify and extend.

Part B: Minimal Examples or Scenarios

DRY Violation & Fix
Scenario:
Two functions perform similar tasks with slight differences.
Refactored Approach:
class Logger {
public:
    void logMessage(string message, bool isError = false) {
        if (isError) {
            cout << "[ERROR]: " << message << endl;
        } else {
            cout << "[INFO]: " << message << endl;
        }
    }
};

KISS Principle Example
Scenario:
A function calculates discounts with unnecessary complexity.
Before (Violating KISS):
double calculateDiscount(double price, string customerType) {
    if (customerType == "Regular") {
        return price * 0.05;
    } else if (customerType == "Premium") {
        return price * 0.10;
    } else if (customerType == "VIP") {
        return price * 0.20;
    } else {
        return 0;
    }
}

After (Following KISS):
map<string, double> discountRates = { {"Regular", 0.05}, {"Premium", 0.10}, {"VIP", 0.20} };

double calculateDiscount(double price, string customerType) {
    return price * discountRates[customerType];
}

SOLID Application
Scenario:
A Shape interface has two unrelated responsibilities.
Violating Interface Segregation Principle (ISP):
class Shape {
public:
    virtual void draw() = 0;
    virtual double computeArea() = 0;
};

Fix (Following ISP by Splitting Interfaces):
class Drawable {
public:
    virtual void draw() = 0;
};

class Measurable {
public:
    virtual double computeArea() = 0;
};

class Circle : public Drawable, public Measurable {
public:
    void draw() override {
        cout << "Drawing Circle" << endl;
    }
    double computeArea() override {
        return 3.14 * radius * radius;
    }
private:
    double radius;
};

Part C: Reflection & Short Discussion
Trade-Offs
Scenario Where Repetition is More Readable:
Sometimes, trying to abstract logic into reusable functions may make code harder to follow. For example, having two separate, 
clear functions for different behaviors in a small project might be more readable than creating a generalized function with multiple parameters.

Combining Principles
By adhering to DRY and KISS together, we ensure code is both reusable and simple. For example, defining a formatPrice() 
function prevents repetition while keeping logic simple, rather than embedding formatting in multiple places.

SOLID in Practice
Not all SOLID principles are needed in small projects. In an early-stage codebase, strict adherence might add unnecessary complexity. 
Instead, applying SOLID selectively ensures flexibility while maintaining simplicity.