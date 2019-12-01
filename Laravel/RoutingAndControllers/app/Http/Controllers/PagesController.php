<?php

// namespace defines the file path
namespace App\Http\Controllers;

// calling Request library
use Illuminate\Http\Request;

class PagesController extends Controller
{
    // Create a function for index page
    public function index() {
      return view('pages.index');
    }

    // Create a function for about page
    public function about() {
      return view('pages.about');
    }

    // Create a function for service page
    public function service() {
      return view('pages.service');
    }
}
