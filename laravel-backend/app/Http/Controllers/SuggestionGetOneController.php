<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Suggestion;

class SuggestionGetOneController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'test_name' => 'required',
        ]);
        $suggestion = Suggestion::where([
            ['test_name', '=', $request->get('test_name')]
        ])->get();

        if (empty($suggestion)) {
            return response()->json([
                'errors' => [
                    'suggestion' => 'The suggestion does not exist',
                ]
            ], 422);
        }
        return response()->json($suggestion);
    }
}
