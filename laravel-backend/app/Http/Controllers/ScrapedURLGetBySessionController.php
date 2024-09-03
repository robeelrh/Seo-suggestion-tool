<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Str;
use App\Models\ScrapedUrls;


class ScrapedURLGetBySessionController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraper_id' => 'required',
        ]);
        $data = ScrapedUrls::where('scraper_id', $request->get('scraper_id'))->get();
        if ($data) {
            return response()->json($data, 200);
        } else {
            return response()->json(['message' => 'No data found for the scraper_id'], 404);
        }
    }
}
