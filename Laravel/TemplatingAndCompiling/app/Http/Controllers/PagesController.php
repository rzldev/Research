<?php

// namespace defines the file path
namespace App\Http\Controllers;

// calling Request library
use Illuminate\Http\Request;

class PagesController extends Controller
{

    // Passing parameter to page 1
    public function index() {
      $title = 'Index Page';

      return view('pages.index', compact('title'));
    }

    // Passing parameter to page 2
    public function about() {
      $title = 'About Page';

      return view('pages.about')->with('title', $title);
    }

    // Passing parameter to page 3
    public function service() {
      $data = array(
        'title' => 'Service Page',
        'services' => [
          'Android Development',
          'Web Development',
          'Data Science'
          ]
    );

      return view('pages.service')->with($data);
    }

}
