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


// Controllers are meant to group associated request handling logic within a single class


// Create a route for controller
Route::get('/text', 'UserController@text');


// Create a route for controller
Route::get('/new', 'UserController@show');
