<?php

namespace App\Http\Controllers;

use App\Models\Scraper;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;


class ScraperGetOneController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraper_id' => 'required',
        ]);
        $scraper = Scraper::where([
            ['id', '=', $request->get('scraper_id')]
        ])->get();

        if (empty($scraper)) {
            return response()->json([
                'errors' => [
                    'scraper' => 'The scraper does not exist',
                ]
            ], 422);
        }
        return response()->json($scraper);
    }
}
