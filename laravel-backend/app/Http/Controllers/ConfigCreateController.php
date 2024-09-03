<?php

namespace App\Http\Controllers;

use App\Models\SeoConfig;
use Illuminate\Support\Str;
use Illuminate\Http\Request;
use App\Services\ScriptRunner;
use App\Services\Envoy;

class ConfigCreateController extends Controller
{
    public function handle(Request $request)
    {
        $seoConfig = new SeoConfig;

        $seoConfig->meta_tag_title_min_length = $request->get('meta_tag_title_min_length');
        $seoConfig->meta_tag_title_max_length = $request->get('meta_tag_title_max_length');
        $seoConfig->meta_tag_description_min_length = $request->get('meta_tag_description_min_length');
        $seoConfig->meta_tag_description_max_length = $request->get('meta_tag_description_max_length');
        $seoConfig->max_page_size = $request->get('max_page_size');
        $seoConfig->min_page_word_count = $request->get('min_page_word_count');
        $seoConfig->max_h1_header_length = $request->get('max_h1_header_length');
        $seoConfig->max_h2_header_length = $request->get('max_h2_header_length');

        $seoConfig->save();

        return response()->json(['message' => 'SEO config saved successfully'], 201);
    }
}
