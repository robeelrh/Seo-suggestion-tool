<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Suggestion;

class SuggestionUpdateController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'suggestion_id' => 'required',

        ]);
        $suggestion = Suggestion::where('id',$request->get('suggestion_id'))->first();
        $suggestion->test_name =$request->get('test_name');
        $suggestion->description =$request->get('description');
        $suggestion->update();
        return response()->json($suggestion);
    }
}
