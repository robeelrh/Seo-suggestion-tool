<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Str;
use App\Models\ScrapedUrls;


class ScrapedURLGetURLsByScrapedURLIDController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id' => 'required',
        ]);
        $data = ScrapedUrls::where('id', $request->get('scraped_url_id'))->get();
        if ($data) {
            return response()->json($data, 200);
        } else {
            return response()->json(['message' => 'No data found for the scraped_url_id'], 404);
        }
    }
}
