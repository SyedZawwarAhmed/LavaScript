<h1>LavaScript</h1>
<p>
  <b>LavaScript is a language inspired by JavaScript.</b>
</p>

<h3>Group Members:</h3>
<table>
  <tr>
    <td>Sheikh Abdullah</td>
  </tr>
  <tr>
    <td>Syed Zawwar Ahmed</td>
  </tr>
  <tr>
    <td>Muhammad Annas Baig</td>
  </tr>
</table>

<br>
<h2>Language Specification</h2>

<h3>Variables</h3>
<p>Variables can be declared using <code>dynamic</code> and <code>static</code>.
dynamic variables are changeable while static variable is unchangeable like <code>const</code>.</p>

```
  dynamic a = 10;
  static b = "two";
  a = false;
  a = a + 3;
```

<h3>Operators</h3>
<p>LavaScript has 2 types of operators.</p>
  <h4>Mathematical Operators:</h4>
  <code> +, -, *, /, ^, %</code>
  <h4>Logical Operators:</h4>
  <code> ==, !=, >, <, >=, <=, &&, ||</code>

<h3>Data Types</h3>
<p>We have 3 datatypes in LavaScript. Namely: string, number and boolean.</p>

```
  dynamic a = 10;
  dynamic b = 2 - 3;
  dynamic c = "Sheikh Abdullah";
  static d = true;
  dynamic e = false && true;
```

<h3>Built-ins</h3>
<p>Use <code>log</code> to print anything to console.</p>

```
  log "Hello World";
  static foo = "I'm a Ubitian";
  log foo;
```

<h3>Conditionals</h3>
<p>LavaScript supports if-else construct, <code>if</code> block will execute if condition is <code>true</code>, <code>else</code> block will execute if the above conditions is <code>false</code>. if-else blocks can be nested.

```
  dynamic = 10;
  if (a < 20) {
    log "a is less than 20";
  } else {
    if (a > 20) {
      log "a is greater than 20";
    } else {
      log "a is equals to 20";
    }
  }
```

<h3>Loops</h3>
<p>Statements inside <code>until</code> blocks are executed as long as a specified condition evaluates to true. If the condition becomes <code>false</code>, statement within the loop stops executing and control passes to the statement following the loop. Use <code>exit</code> to break the loop and <code className="language-cpp">skip</code> to continue within loop.</p>

```
  dynamic i = 0;
  until (i < 10) {
    log "Let's study Automata";
    if (i == 5) {
      exit;
    } else {
      skip;
    }
    i = i + 1;
  }
```

<h3>Functions</h3>
<p>Function can be decalared using <code>proc</code>. A function can accept 0 to n parameters separated by comma. <code>return</code> keyword can be used in the body to exit from function with or without a value. You can optionally specify the return type of a function</p>

```
  proc isEven(a, b): string {
    static rem = a % 2;
    if (rem == 0) {
      return "Number is even";
    } else {
      return "Number is odd";
    }
  }

  log isEven(23);
```

<h3>Comments</h3>
<p>While code is for computer to understand, the comments are for humans. LavaScript supports two types of comments i.e single-line comment, starts with <code>?</code> and multi-line comment, wrapped by <code>@...@</code>.</p>

```
? This is a variable
static f = 4;

@
  This function is used to calculate age
  from date of birth.
@
proc calcAge(dob) {
  ...
}
```

<h3>Data Structures</h3>

<h4>Arrays</h4>
<p>LavaScript supports the array data structure. Arrays can be defined by using brackets <code>[]</code> with the collection of values inside of the brackets separated by commas. Arrays can be multi-dimensional as well.</p>

```
dynamic myArray = [1, 3.8, "Hello"];

dynamic multiArray = [
  [
    ['a', 'b', 'c'],
    ['A', 'B', 'C']
  ],
  [1, 2, 3]
];
```

<h3>Object Oriented Programing (OOP)</h2>
<p>LavaScript also supports Object Oriented Programming. One can create classes of their own and then create instances namely objects of the classes created.</p>
<h4>Classes</h3>
<p>Classes can be created using <code>class</code> keyword.</p>

```
class Employee {
  ...
}
```

<p>Public attributes can be added by writing their identifier in the class definition. Private attributes can also be added by writing a <code>#</code> followed by their identifier in the class definition.</p>

```
class Employee {
  name;
  #SSN;
}
```

<p>In the above code block, the Employee class has two attributes, <code>name</code> is a public attribute, <code>SSN</code> is a private attribute.</p>

<p>A constructor is a function which is called at the time of creation of an object of the class. The constructor method can be added by using the <code>constructor</code> keyword.</p>

```
class Employee {
  name;
  #SSN;

  constructor(name, SSN) {
    this.name = name;
    this.SSN = SSN;
  }
}
```

<p>The <code>this</code> keyword refers to the current instace of the class.</p>

<p>Furthermore, simple methods can also be introduced by defining a function in the class definition with the <code>method</code> keyword. Again, class methods can also be made private by adding a # before the identifier.</p>

```
class Employee {
  name;
  #SSN;
  #salary;

  constructor(name, SSN, salary) {
    this.name = name;
    this.SSN = SSN;
    this.salary = salary;
  }

  method #fire() {
    log "Good bye! You've been promoted to a customer.";
  }

  method evalutate(performance) {
    if (performance == 'good') {
      this.salary = this.salary + 10000;
    } else {
      this.fire();
    }
  }
}
```

<p>In this example, <code>evaluate</code> is a public method while <code>fire</code> is a private method. Note that private methods can only be called inside of a class.</p>

<h4>Objects</h4>
<p>Objects are instances of any LavaScript class. They can be created by using the <code>init</code> keyword followed by the name of the class, and passing the respective arguements as the parameters of the class constructor.</p>

```
dynamic employee1 = init Employee("Sheikh Abdullah", 123456789, 250000);
```

<p>In the above line of code,  an instance of the class Employee is created and then assigned to a dynamic variable employee 1.</p>

The object attributes and methods can be accessed using the <code>dot(.)</code> operator.

```
log employee1.name;
```

This line of code will dislay the name of the <code>employee1</code> object in the terminal, in this case "Sheikh Abdullah".

```
employee1.evaluate("good");
```

This will call the <code>evaluate</code> method of the <code>Employee</code> class for this object.

<h4>Inheritance</h4>
<p>In LavaScript, it is possible to inherit attributes and methods from one class to another.
To inherit from a class, use the <code>extends</code> keyword.</p>

```
class SoftwareEngineer extends Employee {
  level;

  constructor(level, name, SSN) {
    this.level = level;
    super(name, SSN, this.level * 75000);
  }
}

static emp = init SoftwareEngineer(3, "Sheikh Abdullah", 123456789, 74000);
log emp.name; // prints: Sheikh Abdullah
```

<p>The <code>super</code> keyword is a reference variable which is used to refer immediate parent class object.</p>
<p>If you don't want a class to be extended, you can mark it with <code>sealed</code> keyword.</p>

```
sealed class Employee {
  ...
}
```

<h4>Interfaces</h4>
<p>Interface is a blueprint of a class. It is used to achieve abstraction in LavaScript.
In interfaces you can only define the method headers. The body will be described by the class that implements it. </p>

```
interface IShape {
    method GetArea(): number;
}

class Rectangle implements IShape {
    #length;
    #breadth;

    method GetArea(): number {
      return this.length * this.breadth;
    }
}
```

<p>Multi-Inheritance is supported in LavaScript through the use of interfaces.</p>

```
interface IShape {
    method GetArea(): number;
}

interface IColor {
    method GetColor(): string;
}

class Rectangle implements IShape, IColor {
    #length;
    #breadth;
    #color;

    method GetArea(): number {
      return this.length * this.breadth;
    }

    method GetColor(): string {
      return this.color;
    }
}
```

<h2>Classification of Keywords</h2>
<p>The keywords can be classified as follows:</p>
<ul>
<li><b>Initializers</b></li>
<ul>
<li>static</li>
<li>dynamic</li>
</ul>
<li><b>Special Identifiers</b></li>
<ul>
<li>log</li>
</ul>
<li><b>init</b></li>
<li><b>if</b></li>
<li><b>else</b></li>
<li><b>until</b></li>
<li><b>proc</b></li>
<li><b>return</b></li>
<li><b>class</b></li>
<li><b>method</b></li>
<li><b>this</b></li>
<li><b>interface</b></li>
<li><b>extends</b></li>
<li><b>implements</b></li>
<li><b>super</b></li>
<li><b>sealed</b></li>
</ul>
