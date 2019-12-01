<?php

// Set the namespace
namespace App\Http\Controllers;

// Set the extended controller for class
use App\Http\Controllers\Controller;

// Create a class
class UserController extends Controller {

  //Create a function 1
  public function text () {
    return 'Simple Controller';
  }

  //Create a function 2
  public function show () {
    return view('new');
  }
}
