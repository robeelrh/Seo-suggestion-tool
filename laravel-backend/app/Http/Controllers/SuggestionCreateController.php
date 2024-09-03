<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Suggestion;

class SuggestionCreateController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'test_name' => 'required',
            'description' => 'required'
        ]);
        $suggestion = new Suggestion;   
        $suggestion->test_name = $request->get('test_name');
        $suggestion->description = $request->get('description');
        $suggestion->save();
        
        return response()->json(['suggestion' => $suggestion], 201);
    }
}
