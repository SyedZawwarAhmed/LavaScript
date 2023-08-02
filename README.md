<h1>LavaScript</h1>
<p>
  <b>LavaScript is a language inspired by JavaScript.</b>
</p>

<h3>Group Members:</h3>
<table>
  <tr>
    <th>Name</th>
    <th>Seat Number</th>
  </tr>
  <tr>
    <td>Sheikh Abdullah</td>
    <td>B20102146</td>
  </tr>
  <tr>
    <td>Syed Zawwar Ahmed</td>
    <td>B20102173</td>
  </tr>
  <tr>
    <td>Muhammad Annas Baig</td>
    <td>B20102078</td>
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
<p>Function can be decalared using <code>proc</code>. A function can accept 0 to n parameters separated by comma. <code>return</code> keyword can be used in the body to exit from function with or without a value.</p>

```
  proc isEven(a, b) {
    static rem = a % 2;
    if (rem == 0) {
      return "Number is even";
    } else {
      return "Number is odd";
    }
  }

  log isEven(23);
```
<h3>Data Structures</h3>

<h4>Arrays</h4>
<p>LavaScript supports the array data structure. Arrays can be defined by using brackets <code>[]</code> with the collection of values inside of the brackets separated by commas.</p>

```
dynamic myArray = [1, 3.8, "Hello"]
```

<h3>Object Oriented Programing (OOP)</h2>
<p>LavaScript also supports Object Oriented Programming. One can create classes of their own and then create instances namely objects of the classes created.</p>
<h4>Classes</h3>
<p>Classes can be created using <code>class</code> keyword.</p>

```
class Employee {
  
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

<h4>Objects</h3>
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