# Coffee Vending Machine — Design Document

## Table of Contents
1. [Overview](#overview)
2. [Design Patterns Used](#design-patterns-used)
3. [System Architecture](#system-architecture)
4. [Module Breakdown](#module-breakdown)
   - [Enums](#enums)
   - [Machine (Coffee Models)](#machine-coffee-models)
   - [Factory](#factory)
   - [State](#state)
   - [Client](#client)
5. [Class Diagram](#class-diagram)
6. [State Machine Diagram](#state-machine-diagram)
7. [Interaction Flow](#interaction-flow)
8. [Design Decisions](#design-decisions)
9. [Extensibility](#extensibility)

---

## Overview

The **Coffee Vending Machine** is a simulation of a real-world coffee dispenser, built as a Low-Level Design (LLD) exercise. The system models the full lifecycle of a coffee purchase: selecting a coffee type, inserting money, dispensing the coffee, and handling cancellations or refunds.

The implementation combines two classical Gang-of-Four (GoF) design patterns:
- **State Pattern** — to manage the vending machine's internal lifecycle states.
- **Factory Pattern** — to abstract and encapsulate the creation of different coffee objects.

---

## Design Patterns Used

| Pattern   | Where Applied               | Purpose                                                                 |
|-----------|-----------------------------|-------------------------------------------------------------------------|
| **State** | `state/states.py`           | Manages transitions between `ReadyState`, `PaymentState`, `DispenseCoffeeState`, and `OutOfIngredientState`. |
| **Factory** | `factory/coffee_factory.py` | Decouples coffee object creation from the client; creates `Espresso`, `Latte`, or `Cappuccino` based on `CoffeeType` enum. |
| **Template Method** | `machine/coffee.py` | `Coffee.prepare()` defines the skeleton brewing algorithm (`_grind_beans → _brew → _pour_into_cup`); subclasses inherit the flow. |

---

## System Architecture

```
CoffeeVendingMachine/
│
├── client.py                        # Entry point / driver code
│
├── enums/
│   ├── coffee_type.py               # CoffeeType enum (ESPRESSO, LATTE, CAPPACCINO)
│   └── ingredient.py                # Ingredient enum (COFFEE_BEANS, MILK, SUGAR, WATER, CARAMEL_SYRUP)
│
├── machine/
│   ├── coffee.py                    # Abstract Coffee base + Espresso, Latte, Cappaccino concrete classes
│   └── coffee_vending_machine.py    # CoffeeVendingMachine context — delegates actions to current state
│
├── factory/
│   └── coffee_factory.py            # CoffeeFactory — static factory method to instantiate coffee objects
│
└── state/
    └── states.py                    # VendingMachineState (abstract) + 4 concrete state classes
```

---

## Module Breakdown

### Enums

#### `CoffeeType` (`enums/coffee_type.py`)
Defines the supported coffee variants.

| Member       | Value         |
|--------------|---------------|
| `ESPRESSO`   | `"Espresso"`  |
| `LATTE`      | `"LATTE"`     |
| `CAPPACCINO` | `"CAPPACCINO"`|

#### `Ingredient` (`enums/ingredient.py`)
Defines the ingredients used in coffee recipes.

| Member           | Value              |
|------------------|--------------------|
| `COFFEE_BEANS`   | `"COFFEE_BEANS"`   |
| `MILK`           | `"MILK"`           |
| `SUGAR`          | `"SUGAR"`          |
| `WATER`          | `"WATER"`          |
| `CARAMEL_SYRUP`  | `"CARAMEL_SYRUP"`  |

---

### Machine (Coffee Models)

#### `Coffee` (`machine/coffee.py`) — Abstract Base Class

Defines the interface and shared brewing logic for all coffee types.

| Member              | Type       | Description                                                      |
|---------------------|------------|------------------------------------------------------------------|
| `coffee_type`       | `str`      | Coffee name/label                                                |
| `get_coffee_type()` | method     | Returns the coffee type string                                   |
| `prepare()`         | method     | **Template method** — orchestrates grind → brew → pour steps     |
| `_grind_beans()`    | method     | Step 1: Grinds coffee beans (shared implementation)              |
| `_brew()`           | method     | Step 2: Brews with hot water (shared implementation)             |
| `_pour_into_cup()`  | method     | Step 3: Pours into cup (shared implementation)                   |
| `get_price()`       | abstract   | Returns price in rupees                                          |
| `get_recipe()`      | abstract   | Returns `Dict[Ingredient, int]` ingredient quantities            |

#### Concrete Coffee Classes

| Class        | Price (₹) | Recipe                                               |
|--------------|-----------|------------------------------------------------------|
| `Espresso`   | 200       | Coffee Beans: 7g, Water: 30ml                        |
| `Latte`      | 220       | Coffee Beans: 7g, Water: 30ml, Milk: 100ml           |
| `Cappaccino` | 250       | Coffee Beans: 7g, Water: 30ml, Milk: 150ml           |

---

#### `CoffeeVendingMachine` (`machine/coffee_vending_machine.py`) — Context Class

The central **context** object in the State pattern. It holds the current state and delegates every user action to the active state object.

| Attribute / Method          | Description                                                          |
|-----------------------------|----------------------------------------------------------------------|
| `_state`                    | Current `VendingMachineState` instance (starts as `ReadyState`)      |
| `coffee`                    | Currently selected `Coffee` object                                   |
| `money_inserted`            | Total money inserted so far (in rupees)                              |
| `set_state(state)`          | Transitions the machine to a new state                               |
| `select_coffee(coffee)`     | Delegates to `_state.select_coffee()`                                |
| `insert_money(money)`       | Delegates to `_state.insert_money()`                                 |
| `prepare_coffee(coffee)`    | Delegates to `_state.dispense_coffee()`                              |
| `cancel()`                  | Delegates to `_state.cancel()`                                       |
| `refund(refund_amount)`     | Prints a refund message; called internally by states                 |

---

### Factory

#### `CoffeeFactory` (`factory/coffee_factory.py`)

A **static factory** that maps `CoffeeType` enum values to concrete `Coffee` instances.

```python
CoffeeFactory.create_coffee(CoffeeType.ESPRESSO)  # → Espresso()
CoffeeFactory.create_coffee(CoffeeType.LATTE)      # → Latte()
CoffeeFactory.create_coffee(CoffeeType.CAPPACCINO) # → Cappaccino()
```

Raises `Exception("Unknown coffee")` for unrecognized types.

---

### State

#### `VendingMachineState` (`state/states.py`) — Abstract Base

Defines the interface all states must implement:

| Abstract Method                          | Description                              |
|------------------------------------------|------------------------------------------|
| `select_coffee(machine, coffee)`         | Handle coffee selection in this state    |
| `insert_money(machine, money)`           | Handle money insertion in this state     |
| `dispense_coffee(machine, coffee)`       | Handle coffee dispensing in this state   |
| `cancel(machine)`                        | Handle cancellation in this state        |

#### Concrete States

| State                    | Behaviour Summary                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| **`ReadyState`**         | Initial state. Accepts coffee selection → transitions to `PaymentState`. Rejects money/dispense.       |
| **`PaymentState`**       | Accepts money increments. Transitions to `DispenseCoffeeState` once inserted ≥ coffee price. Supports cancel + refund. |
| **`DispenseCoffeeState`**| Calls `coffee.prepare()`, calculates and refunds change. Transitions back to `ReadyState` after dispense or cancel. |
| **`OutOfIngredientState`**| All actions blocked with "out of ingredients" message except cancel, which refunds and resets to `ReadyState`. |

---

## Class Diagram

```
                        ┌─────────────────────────────┐
                        │      CoffeeVendingMachine    │
                        │─────────────────────────────│
                        │ - _state: VendingMachineState│
                        │ - coffee: Coffee             │
                        │ - money_inserted: int        │
                        │─────────────────────────────│
                        │ + select_coffee(coffee)      │
                        │ + insert_money(money)        │
                        │ + prepare_coffee(coffee)     │
                        │ + cancel()                   │
                        │ + refund(amount)             │
                        └──────────────┬──────────────┘
                                       │ delegates to
                                       ▼
                        ┌─────────────────────────────┐
                        │    <<abstract>>              │
                        │    VendingMachineState       │
                        │─────────────────────────────│
                        │ + select_coffee()            │
                        │ + insert_money()             │
                        │ + dispense_coffee()          │
                        │ + cancel()                   │
                        └─┬──────┬──────┬─────────────┘
                          │      │      │
           ┌──────────────┘      │      └────────────────────┐
           ▼                     ▼                            ▼
  ┌────────────────┐   ┌──────────────────┐   ┌───────────────────────┐
  │  ReadyState    │   │  PaymentState    │   │ DispenseCoffeeState   │
  └────────────────┘   └──────────────────┘   └───────────────────────┘
                                                    
  ┌──────────────────────────┐
  │  OutOfIngredientState    │
  └──────────────────────────┘

                        ┌───────────────┐
                        │  <<abstract>> │
                        │    Coffee     │
                        │───────────────│
                        │ + prepare()   │
                        │ + get_price() │
                        │ + get_recipe()│
                        └──────┬────────┘
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
       ┌──────────┐     ┌──────────┐     ┌────────────┐
       │ Espresso │     │  Latte   │     │ Cappaccino │
       └──────────┘     └──────────┘     └────────────┘

                        ┌─────────────────┐
                        │  CoffeeFactory  │
                        │─────────────────│
                        │ + create_coffee │
                        │   (CoffeeType)  │
                        └─────────────────┘
```

---

## State Machine Diagram

```
                    ┌────────────────────────────────────────────────────────────┐
                    │                                                            │
    [start]         │  select_coffee()          insert_money()                  │
       │            │  ─────────────►           (money >= price)                │
       ▼            │                           ────────────────►               │
  ┌──────────┐      │  ┌──────────────────┐     ┌──────────────────┐  dispense_coffee()  ┌────────────────────────┐
  │  Ready   │ ─────┼─►│  PaymentState    │─────►│ DispenseCoffee  │──────────────────►  │  [dispense + refund]   │
  │  State   │      │  └──────────────────┘     │    State        │                      │   → back to Ready      │
  └──────────┘      │          │                └─────────────────┘                      └────────────────────────┘
       ▲            │     cancel()                      │ cancel()
       │            │  ──────────────────               │
       └────────────┴──── refund + reset ◄──────────────┘

  OutOfIngredientState: any action → "out of ingredients"; cancel → refund + ReadyState
```

---

## Interaction Flow

The following sequence describes a **successful coffee purchase** (as shown in `client.py`):

```
Client                   CoffeeFactory         CoffeeVendingMachine        State
  │                           │                        │                     │
  │── create_coffee(ESPRESSO) ►│                        │                     │
  │◄─ Espresso() ─────────────│                        │                     │
  │                                                     │                     │
  │── machine = CoffeeVendingMachine() ────────────────►│ init _state=ReadyState
  │                                                     │                     │
  │── select_coffee(espresso) ─────────────────────────►│                     │
  │                                                     │── select_coffee() ──►│ [ReadyState]
  │                                                     │                     │ sets coffee, transitions → PaymentState
  │                                                     │                     │
  │── insert_money(150) ────────────────────────────────►│                     │
  │                                                     │── insert_money() ───►│ [PaymentState]
  │                                                     │                     │ total=150, price=200 → stay in PaymentState
  │                                                     │                     │
  │── insert_money(250) ────────────────────────────────►│                     │
  │                                                     │── insert_money() ───►│ [PaymentState]
  │                                                     │                     │ total=400 >= 200 → transition → DispenseCoffeeState
  │                                                     │                     │
  │── prepare_coffee(espresso) ────────────────────────►│                     │
  │                                                     │── dispense_coffee() ►│ [DispenseCoffeeState]
  │                                                     │                     │ coffee.prepare() → grind, brew, pour
  │                                                     │                     │ refund(400 - 200 = 200 rupees)
```

---

## Design Decisions

### 1. State Pattern for Machine Lifecycle
Instead of using `if/elif` chains inside `CoffeeVendingMachine` to handle state-dependent logic, the **State Pattern** cleanly separates each phase into its own class. Adding a new state (e.g., `MaintenanceState`) only requires creating a new class and adding transition logic — the machine context remains unchanged.

### 2. Factory Pattern for Coffee Creation
Using `CoffeeFactory.create_coffee(CoffeeType)` ensures the client never directly instantiates coffee objects. This makes it easy to swap implementations, add new coffee types, or introduce caching without changing the calling code.

### 3. Template Method in `Coffee.prepare()`
The brewing sequence (`_grind_beans → _brew → _pour_into_cup`) is fixed in the abstract base class. Concrete subclasses inherit this flow while only being required to define `get_price()` and `get_recipe()`. This enforces a consistent brewing experience across all types.

### 4. Separation of Concerns
| Concern                    | Handled By                          |
|----------------------------|-------------------------------------|
| Coffee type identity       | `CoffeeType` enum                   |
| Ingredient definitions     | `Ingredient` enum                   |
| Coffee object creation     | `CoffeeFactory`                     |
| Coffee brewing behaviour   | `Coffee` subclasses                 |
| Machine lifecycle/state    | `VendingMachineState` subclasses    |
| Machine orchestration      | `CoffeeVendingMachine`              |

---

## Extensibility

| Scenario                          | What to Add / Change                                                                 |
|-----------------------------------|--------------------------------------------------------------------------------------|
| Add a new coffee type             | Add entry to `CoffeeType` enum, create a new `Coffee` subclass, add a case in `CoffeeFactory` |
| Add a new ingredient              | Add entry to `Ingredient` enum, use it in a coffee's `get_recipe()`                  |
| Add a new machine state           | Create a class extending `VendingMachineState`, add transition logic in relevant states |
| Add ingredient inventory tracking| Inject an `InventoryManager` into `CoffeeVendingMachine`; `DispenseCoffeeState` checks stock before dispensing and transitions to `OutOfIngredientState` if empty |
| Support multiple currency         | Abstract the payment system into a `PaymentProvider` interface                       |
| Persist machine state             | Serialize `CoffeeVendingMachine` state via a repository layer                        |
