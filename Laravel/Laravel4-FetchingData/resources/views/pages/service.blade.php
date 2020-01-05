@extends('layouts.app')
@section('content')
<div class="content">
    <div class="title m-b-md">
        {{ $title }}
    </div>
    
    {{-- Print Services --}}
    <ul class="list-group">
      @foreach($services as $service)
        <li class="list-group-item">{{ $service }}</li>
      @endforeach
    </ul>
</div>
@endsection
