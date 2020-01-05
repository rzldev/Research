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


// Create a simple route
Route::get('/hello', function () {
    return '<h1>Hello World</h1>';
});


// Create a route with view
Route::get('/about', function () {
    return view('pages.about');
});


// Create a route with some specfifc key or parameter
Route::get('/users/{id}/{name}', function ($id, $name) {
    return '<h1>This is user '.$name.' with id '.$id.'</h1>';
});


// Create a route with controller inside
Route::get('/index', 'PagesController@index');


Route::get('/service', 'PagesController@service');
