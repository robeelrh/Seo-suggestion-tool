<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Suggestion;

class SuggestionGetAllController extends Controller
{
    public function handle(Request $request){
        $suggestions = Suggestion::get();
        if (empty($suggestions)) {
            return response()->json([
                'errors' => [
                    'Error' => 'No suggestion exist',
                ]
            ], 422);
        }
        return response()->json($suggestions);
    }
}
