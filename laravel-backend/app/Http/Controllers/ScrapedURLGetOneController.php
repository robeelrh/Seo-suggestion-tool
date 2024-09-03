<?php

namespace App\Http\Controllers;

use App\Models\ScrapedUrls;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;


class ScrapedURLGetOneController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id' => 'required',
        ]);
        $scraped_url = ScrapedUrls::where([
            ['id', '=', $request->get('scraped_url_id')]
        ])->get();

        if (empty($scraped_url)) {
            return response()->json([
                'errors' => [
                    'scraped' => 'The scraped_url_id does not exist',
                ]
            ], 422);
        }
        return response()->json($scraped_url);
    }
}
