@extends('layouts.app')
@section('content')
  <div class="container">
      <a href="/posts" class="btn btn-default">Go back</a>
      <h3>{{ $post->title }}</h3>
      <div>
          {{ $post->body }}
      </div>
      <hr>
      <small>Written on {{ $post->created_at }}</small>
  </div>
@endsection
