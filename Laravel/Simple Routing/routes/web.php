<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

// Routing in Laravel allows you to route all your application requests to its appropriate controller.

// Create a new route page
Route::get('/new', function() {
    return view('new');
});


// Create another route page
Route::view('/about', 'about');


// Redirect page
Route::redirect('/old', '/new', 301);
// Code 301 is used for URL redirection


// Routing a page with a key
Route::get('key:{key}', function($key) {
    return $key;
});
