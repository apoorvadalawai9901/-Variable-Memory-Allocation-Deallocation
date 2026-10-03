
# JavaScript, Node.js, Python, and Java: Variables, Memory, and Runtime

This guide compares JavaScript, Node.js, Python, and Java with an emphasis on variables, object references, memory lifetime, garbage collection, and concurrency.

> **First distinction:** JavaScript is a language. Node.js is a runtime that executes JavaScript outside a browser. Node.js commonly uses Google's V8 engine, but it also provides APIs and runtime components such as the event loop and libuv. JavaScript in a browser and JavaScript in Node.js share core language semantics, but their available APIs and host environments differ.

## 1. Declaring variables

| Environment | Typical declaration | What the declaration means |
| --- | --- | --- |
| JavaScript / Node.js | `let`, `const`, `var` | Declares a binding. `let` and `const` are block-scoped; `var` is function-scoped. `const` prevents rebinding, not mutation of an object it refers to. |
| Python | Assignment, such as `count = 3` | Binds a name to an object. A name does not have a permanent declared type. Python also has type annotations, but they are not normally enforced by the runtime. |
| Java | `int count = 3;` or `String name = "Ada";` | Declares a variable with a compile-time type. Local variables generally need to be initialized before they are read. |

```javascript
let count = 3;
const settings = { theme: "light" };
settings.theme = "dark"; // allowed: the object can change
// settings = {};        // TypeError: the const binding cannot be reassigned
```

```python
count = 3
count = "three"  # valid: this name can be rebound to an object of another type
```

```java
int count = 3;
// count = "three"; // compile-time type error
```

**What to notice:** Java ties `count` to the type `int`. Python and JavaScript let the same name be assigned a value of another type later.

## 2. Static and dynamic typing

Java is statically typed: the compiler checks declared types and many type errors before the program runs. JavaScript and Python are dynamically typed: values have types at runtime, and a name or variable can refer to values of different types over time.

“Static” does not mean every error is caught at compile time, and “dynamic” does not mean there is no type checking. Java checks types at runtime in some cases, such as casts and array stores. JavaScript and Python perform many operations with runtime type rules and can raise errors when those rules are violated. Optional tools such as TypeScript and Python type checkers can add earlier feedback without changing the basic runtime model.

```python
value = 5
value = "five"  # allowed; the name now refers to a string
```

```java
int value = 5;
// value = "five"; // rejected by the compiler
```

**Result:** Python accepts both assignments. Java rejects the second because a `String` cannot be assigned to an `int` variable.

## 3. Primitive values, objects, and references

- **JavaScript:** Primitive values include numbers, strings, booleans, `null`, `undefined`, bigints, and symbols. Objects include arrays, functions, and ordinary object values. Primitives behave as values; object variables provide access to object identity.
- **Python:** Everything manipulated by a program is an object, including integers, strings, functions, and lists. Names are bound to objects.
- **Java:** Variables can hold primitive values such as `int` and `boolean`, or references to objects such as `String`, arrays, and class instances. A reference is not the object itself.

The implementation's physical layout is runtime-dependent. These categories describe language behavior; they do not guarantee a particular stack or heap location.

```javascript
let number = 7;
let profile = { name: "Mina" };
```

`number` holds a primitive value. `profile` gives access to an object. If another variable is assigned `profile`, both variables can access the same object. Python names and Java object variables have the same sharing effect when they refer to a mutable object, though their type systems differ.

## 4. Assignment: binding, references, and copying

Assignment usually does not make a deep copy of an object. In Python and JavaScript, assigning an object-bearing variable to another variable makes both variables refer to the same object. Java copies the reference value when assigning an object variable, so both references can likewise designate the same object.

```javascript
const first = { score: 10 };
const second = first;
second.score = 20;
console.log(first.score); // 20
```

```python
first = [1, 2]
second = first
second.append(3)
print(first)  # [1, 2, 3]
```

```java
int[] first = {1, 2};
int[] second = first;
second[0] = 9;
System.out.println(first[0]); // 9
```

To copy, use an operation designed for the required depth: for example, JavaScript's spread syntax makes a shallow copy of an array or plain object, Python's `list.copy()` makes a shallow list copy, and Java array `clone()` makes a shallow array copy. Nested objects remain shared in a shallow copy. A deep copy requires recursively copying the nested data, subject to the types involved.

**Read the examples this way:** changing a property or array element through `second` changes what `first` observes, because there is one shared object. Reassigning `second` to a new object would not change `first`.

## 5. Mutable and immutable values

- **JavaScript:** Primitive values, including strings and numbers, are immutable. Arrays and ordinary objects are mutable. `const` does not make an array or object immutable.
- **Python:** Integers, floats, booleans, strings, and tuples are immutable (a tuple may still contain references to mutable objects). Lists, dictionaries, and sets are mutable.
- **Java:** Primitive values are assigned as values. `String` and wrapper objects such as `Integer` are immutable; arrays and most collection implementations are mutable. A `final` reference cannot be reassigned, but the referenced object may still be mutable.

```python
text = "cat"
text = text + "s"  # creates/binds a new string; it does not alter the old string

items = ["cat"]
items.append("cats")  # mutates the existing list
```

Mutability determines whether an operation changes an existing object or produces another value. It is a separate question from whether a variable can be reassigned.

**Result:** after the string example, `text` refers to the new string `"cats"`; strings are not edited in place. After `append`, `items` is still the same list, now containing two entries.

## 6. Stack and heap: useful model, not a language guarantee

The **call stack** tracks active function or method calls: return locations, parameters, and execution state. The **heap** is commonly used for dynamically managed objects whose lifetimes are not tied to one call. These are helpful conceptual categories, but actual layouts are decided by each runtime, compiler, and optimization.

The shortcut “variables are on the stack and objects are on the heap” is unreliable. A local variable may contain a primitive, a reference, or a value optimized by the runtime. Actual placement is an implementation detail, so do not infer it from a source-level variable declaration.

```python
def make_list():
	values = [10, 20]
	return values

result = make_list()
```

When the function returns, its call has finished, but the list is still usable through `result`. This example demonstrates lifetime and reachability without assuming a particular physical address or memory region.

Reason about observable behavior and object reachability first; use runtime-specific profiling tools when actual memory placement matters.

## 7. What happens during a function or method call?

A call transfers control to a function or method. The runtime records enough state to return to the caller and supplies arguments. The called code may create local bindings and objects, call other functions, and produce a return value. When the call completes, its call frame is no longer active; objects created during it can remain alive if they are still reachable elsewhere.

```python
def make_greeting(name):
    message = "Hello, " + name
    return message

greeting = make_greeting("Ada")
```

The call receives `"Ada"`, builds a greeting, and returns it. `message` is local to the call; `greeting` in the caller receives the returned result. A function's local scope ending does not itself imply that every object created there is immediately destroyed.

## 8. Functions as values

JavaScript and Python treat functions as first-class values: functions can be assigned to variables, passed as arguments, and returned from other functions. Node.js uses those same JavaScript language features.

Java has methods associated with classes or objects, rather than freely declared top-level functions in the same sense. Java supports behavior as a value through lambdas and method references, usually targeting a functional interface such as `Runnable` or `Function<T, R>`.

```javascript
function double(value) { return value * 2; }
const apply = double;
console.log(apply(4)); // 8
```

```python
def double(value):
	return value * 2

apply = double
print(apply(4))  # 8
```

In both examples, the function itself is stored in `apply` and then called through that name. In Java, the comparable value is commonly a lambda assigned to a functional-interface variable.

## 9. Argument passing: what “pass by value” means

In **JavaScript, Python, and Java**, arguments are passed by value. The meaning of the copied value differs by argument:

- For a primitive or immutable value, the function receives the value (or a binding to an immutable object in Python). Reassigning a parameter does not reassign the caller's variable.
- For a mutable object, the value passed is an object reference. The function can use that reference to mutate the shared object, but assigning a different object to the parameter does not replace the caller's reference.

This is sometimes informally called “pass by object sharing” in Python. It is not pass-by-reference: the callee cannot rebind the caller's variable.

```python
def change(values):
    values.append(3)  # mutates the list shared with the caller
    values = [99]     # rebinds only this local parameter

numbers = [1, 2]
change(numbers)
print(numbers)  # [1, 2, 3]
```

**Result:** the caller sees the appended `3`, because both parameter and caller refer to the same list. The caller does not see `[99]`, because assigning to the parameter changes only the local parameter. JavaScript and Java behave the same way for mutable arrays/objects.

To make a replacement visible to the caller, return it and assign the return value:

```python
def with_extra_item(values):
	return values + [3]

numbers = [1, 2]
numbers = with_extra_item(numbers)
```

## 10. Closures and captured variables

A closure is a function together with access to variables from its surrounding lexical scope. The runtime preserves the needed captured state for as long as the closure can be called, even if the original function has returned.

```javascript
function makeCounter() {
	let count = 0;
	return () => ++count;
}

const next = makeCounter();
console.log(next()); // 1
console.log(next()); // 2
```

Python nested functions can refer to enclosing names; `nonlocal` allows rebinding an enclosing function's local name. Java lambdas can capture local variables that are final or effectively final. A captured object may still be mutable even though the local reference must not be reassigned. Captured state stays alive because the closure retains access to it.

```python
def make_counter():
	count = 0

	def next_count():
		nonlocal count
		count += 1
		return count

	return next_count

next_count = make_counter()
print(next_count())  # 1
print(next_count())  # 2
```

The outer call has returned, but the returned inner function still needs `count`, so that value remains available between calls. Java's capture rule differs: a lambda may capture a local variable only when it is final or effectively final.

## 11. Garbage collection and object lifetime

Garbage collection automates reclamation of memory occupied by objects that the program can no longer use. In tracing collectors, an object is generally eligible when it is no longer reachable from roots such as active stack frames, static fields, or runtime handles. Eligibility does not promise immediate collection.

`del` in Python removes a name or container entry; it does not mean “free this memory now.” JavaScript has no general `delete` operation for freeing objects: `delete object.property` removes a property. In all these managed environments, dropping one reference does not reclaim an object if another reference still reaches it. Even after collection, the runtime may retain reclaimed memory for reuse instead of returning it immediately to the operating system.

```python
first = [1, 2]
second = first
del first
print(second)  # [1, 2]; the list is still reachable
```

Deleting `first` removes only that name. The list remains alive because `second` still refers to it. If the last reference is removed, the object may become eligible for cleanup, but the exact cleanup time is not promised.

## 12. Garbage collection by runtime

- **JavaScript in V8, including typical Node.js deployments:** V8 uses tracing garbage collection, with strategies tuned for different object ages and allocation patterns. The exact collector and behavior can change between V8 versions.
- **CPython:** Primarily uses reference counting, plus a cyclic garbage collector to find certain unreachable reference cycles. Other Python implementations may use different strategies.
- **Java on the JVM:** Uses tracing garbage collectors. The JVM offers different collectors with different latency and throughput trade-offs; the selected collector depends on configuration and runtime version.

Garbage collection is an implementation detail with observable performance consequences, not a language-level schedule that applications should rely on for timely resource cleanup. Close files, sockets, and database connections explicitly, using constructs such as Python context managers or Java try-with-resources.

## 13. Memory leaks in garbage-collected programs

A garbage collector cannot reclaim an object that remains reachable, even if the application no longer finds it useful. Common causes include:

- unbounded or incorrectly sized caches;
- references retained in global variables or long-lived collections;
- event listeners, callbacks, or timers that are never removed;
- closures that keep large object graphs alive;
- queues that receive work faster than it is consumed.

These are often called memory leaks because memory use keeps growing, although the objects are technically still reachable. Diagnose them with heap snapshots, allocation profiles, and runtime-specific monitoring.

```python
saved_requests = []

def handle_request(request):
	saved_requests.append(request)  # grows forever if entries are never removed
```

Even after each request finishes, every saved request remains reachable through `saved_requests`. A garbage collector cannot know that the application no longer needs those entries; the program must remove or limit them.

## 14. Language and runtime comparison

| Language or environment | Runtime and notable responsibilities |
| --- | --- |
| JavaScript in a browser | A JavaScript engine (often V8, SpiderMonkey, or JavaScriptCore) plus browser-provided APIs such as the DOM and browser event loop. |
| Node.js | JavaScript engine (commonly V8), Node.js APIs, and libuv for event-loop and asynchronous I/O support, alongside operating-system facilities. |
| Python | A language with multiple implementations. CPython is the most widely used implementation and includes its own object model, memory manager, and interpreter. |
| Java | Java bytecode executed by a Java Virtual Machine (JVM), which provides class loading, runtime services, memory management, and often JIT compilation. |

Node.js is not a separate language from JavaScript, and “Python runtime” does not always mean CPython. Runtime details matter when discussing garbage collection, performance, I/O, and available APIs.

## 15. Compilation, interpretation, and JIT compilation

“Compiled versus interpreted” is not a clean either/or distinction. Implementations can combine parsing, bytecode, interpretation, and just-in-time (JIT) compilation.

- **JavaScript / V8:** V8 parses and executes JavaScript and may compile frequently used code to optimized machine code, with de-optimization when assumptions stop holding.
- **CPython:** Typically compiles source to Python bytecode, then evaluates that bytecode in its virtual machine. This does not mean CPython behaves exactly like a native-code compiler; other Python implementations may differ.
- **Java:** The Java compiler typically translates source into bytecode. The JVM interprets and/or JIT-compiles bytecode at runtime, depending on the implementation and workload.

The useful question is which implementation and execution path are in use, not simply whether a language is “compiled” or “interpreted.”

## 16. Event loops, asynchronous I/O, and threads

An **event loop** schedules callbacks or tasks, often allowing one thread to coordinate many I/O operations while those operations wait. **Threads** allow multiple execution flows; they can be useful for concurrency and, depending on the runtime and workload, parallel execution.

- **Node.js:** Commonly runs JavaScript callbacks on an event loop. Asynchronous I/O is coordinated through Node.js and libuv; some work is handled by the operating system or a worker pool. CPU-heavy JavaScript on the main thread can delay other callbacks.
- **Python `asyncio`:** Provides cooperative asynchronous tasks, especially useful for I/O-bound work. A task generally yields at `await`; ordinary CPU-heavy Python code blocks that event loop. Threads and processes are also available. CPython's GIL affects parallel execution of Python bytecode in common builds, but does not prevent concurrency during many I/O operations, and Python implementations/configurations can differ.
- **Java:** Provides threads and higher-level concurrency APIs. Threads can perform I/O concurrently and can execute CPU work in parallel, subject to available cores and synchronization costs.

For many independent network waits, asynchronous I/O can be efficient. For CPU-bound work, consider parallelism, worker threads, processes, or native code appropriate to the runtime. “Async” and “parallel” are not synonyms.

## 17. A request's path through an application

A typical server-side request can be pictured as:

1. The operating system and server runtime receive network data.
2. The runtime dispatches the request to a handler or callback.
3. The handler creates local bindings and may allocate request, query, or result objects.
4. The application performs work, such as querying a database or calling another API. It may await asynchronous I/O or use a thread, depending on the platform and design.
5. The handler builds a result and the server serializes it into a response.
6. Once the request completes, request-scoped references can be dropped. Shared caches or other retained references may keep some objects alive.

The language does not prescribe one universal request architecture. Framework, server, runtime, and database-driver choices affect the details.

## 18. Comparing performance responsibly

There is no useful universal answer to “which language is fastest?” Performance depends on the workload and implementation: CPU-heavy computation, I/O waits, allocation rate, garbage-collection pauses, data structures, libraries, deployment configuration, and concurrency model all matter.

Benchmark representative end-to-end work, include warm-up where relevant, measure latency and throughput, and monitor memory as well as CPU. Prefer profiling before rewriting: the bottleneck may be a database query or network wait rather than the language runtime.

## 19. Variable lifetime, object reachability, and collection

These are related but distinct concepts:

1. **Scope** determines where a name can be used in source code.
2. **Binding lifetime** describes how long that name or variable is maintained by the language/runtime.
3. **Object reachability** determines whether the program can still get to an object through active references.
4. **Collection and memory reuse** are runtime decisions that happen after an object becomes eligible; their timing and effect on process memory are not guaranteed by scope ending.

For example, a function-local name can go out of scope while a returned object remains reachable. Conversely, removing one name does not make an object collectible if a global list still refers to it.

```python
def create_data():
	temporary_name = {"status": "ready"}
	return temporary_name

data = create_data()  # the local name is gone; the dictionary remains reachable as data
```

**Keep the terms separate:** scope answers “where can I use this name?” Reachability answers “can the program still get to this object?” Garbage collection acts on unreachable objects, not simply on names that have left scope.

## 20. What happens in `result = a + b`?

The exact steps depend on the types of `a` and `b`, the language's operator rules, and runtime optimizations. In broad terms, the runtime resolves the names, evaluates the operands, applies addition semantics, then binds or assigns the result.

### Python

```python
result = a + b
```

Python looks up `a` and `b`, evaluates them, and applies the addition operation defined for their types. For integers this produces an integer sum; for strings it produces concatenation. Custom classes can define behavior for `+` using special methods. The name `result` is then bound to the resulting object. Exact allocation and reuse are implementation details.

```python
a = 2
b = 3
result = a + b  # result is 5
```

### JavaScript / Node.js

```javascript
const result = a + b;
```

JavaScript evaluates `a` and `b` and applies the `+` operator's rules. Depending on the operand types, it can perform numeric addition or string concatenation, including type coercion. The resulting value is bound to the block-scoped `const` name `result`, which cannot be reassigned. If the result is an object, the binding provides access to that object; `const` does not freeze it.

```javascript
const a = 2;
const b = 3;
const result = a + b; // result is 5
```

### Java

```java
int result = a + b;
```

Assuming `a` and `b` are compatible numeric values, Java resolves their statically known types and applies the corresponding addition operation. The result is assigned to the `int` local variable. The compiler checks type compatibility, while integer overflow for `int` wraps according to Java's defined integer arithmetic. If the operands are `String` values, `+` performs string concatenation instead and the result type is `String`.

```java
int a = 2;
int b = 3;
int result = a + b; // result is 5
```

**Compare the result:** all three examples produce `5`. The difference is how each language determines the types and meaning of `+`: Java checks compatible types before execution, while Python and JavaScript apply runtime rules. The source line does not reveal identical machine instructions or memory behavior.