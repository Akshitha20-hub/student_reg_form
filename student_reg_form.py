import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Student Registration Form',
      theme: ThemeData(primarySwatch: Colors.teal),
      home: StudentForm(),
    );
  }
}

class StudentForm extends StatefulWidget {
  @override
  _StudentFormState createState() => _StudentFormState();
}

class _StudentFormState extends State<StudentForm> {
  final _formKey = GlobalKey<FormState>();
  String _studentName = '';
  String _rollNumber = '';
  String _selectedDepartment = 'CSE';
  bool _isHosteller = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Student Registration Form')),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Form(
          key: _formKey,
          child: ListView(
            children: [
              const SizedBox(height: 10),
              TextFormField(
                decoration: const InputDecoration(
                  labelText: 'Student Name',
                  border: OutlineInputBorder(),
                ),
                validator: (value) =>
                    value!.isEmpty ? 'Please enter student name' : null,
                onSaved: (value) => _studentName = value!,
              ),
              const SizedBox(height: 20),
              TextFormField(
                decoration: const InputDecoration(
                  labelText: 'Roll Number',
                  border: OutlineInputBorder(),
                ),
                validator: (value) =>
                    value!.isEmpty ? 'Please enter roll number' : null,
                onSaved: (value) => _rollNumber = value!,
              ),
              const SizedBox(height: 20),
              Row(
                children: [
                  const Text(
                    'Department:',
                    style: TextStyle(fontSize: 16),
                  ),
                  const SizedBox(width: 20),
                  DropdownButton<String>(
                    value: _selectedDepartment,
                    items: <String>['CSE', 'ECE', 'EEE', 'IT', 'MECH']
                        .map<DropdownMenuItem<String>>((String value) {
                      return DropdownMenuItem<String>(
                        value: value,
                        child: Text(value),
                      );
                    }).toList(),
                    onChanged: (value) {
                      setState(() {
                        _selectedDepartment = value!;
                      });
                    },
                  ),
                ],
              ),
              const SizedBox(height: 20),
              Row(
                children: [
                  Checkbox(
                    value: _isHosteller,
                    onChanged: (value) {
                      setState(() {
                        _isHosteller = value!;
                      });
                    },
                  ),
                  const Text('Hosteller'),
                ],
              ),
              const SizedBox(height: 30),
              ElevatedButton(
                style: ElevatedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 15),
                  backgroundColor: Colors.teal,
                ),
                onPressed: () {
                  if (_formKey.currentState!.validate()) {
                    _formKey.currentState!.save();
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                        content: Text('Form Submitted Successfully!'),
                        backgroundColor: Colors.green,
                      ),
                    );
                    print('--- STUDENT DETAILS ---');
                    print('Name: $_studentName');
                    print('Roll No: $_rollNumber');
                    print('Department: $_selectedDepartment');
                    print('Hosteller: $_isHosteller');
                  }
                },
                child: const Text(
                  'SUBMIT',
                  style: TextStyle(color: Colors.white, fontSize: 18),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }