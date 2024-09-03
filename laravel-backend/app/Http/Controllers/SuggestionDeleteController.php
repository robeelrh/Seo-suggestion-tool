<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Suggestion;

class SuggestionDeleteController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'suggestion_id' => 'required',
        ]);
        Suggestion::where("id",$request->get('suggestion_id'))->first()->delete();
        return response()->json(['message' => 'Suggestion deleted']);
    }
}
