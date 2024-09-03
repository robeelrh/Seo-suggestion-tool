<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use DB;


class SeoGetImagesTestData extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'scraped_url_id' => 'required',
        ]);

        $result = [];
        
        $data = \DB::table('seo_test_img_tags_size_dims')->where('scraped_url_id', $request->get('scraped_url_id'))->get();
        
        if ($data->count() > 0) {
            $result = $data;
        } else {
            $result = ['message' => 'No data found for the scraper_id'];
        }
        
        return response()->json($result, 200);
    }
}
