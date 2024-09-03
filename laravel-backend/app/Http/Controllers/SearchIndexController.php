<?php

namespace App\Http\Controllers;

use App\Models\SearchIndex;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;


class SearchIndexController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'api_key' => 'required',
            'query'=>'required',
            'website_url'=>'required',
            'language'=>'required',
            'country'=>'required',
            "pageLimter"=>'required',
            "keywords"=>'required',
            "timer"=>'required'
        ]);

            $baseUrl = "https://www.googleapis.com/customsearch/v1";
            $cx = "1490ad8b2fb61469f";
        
            $params = [
                'key' => $request->get('api_key'),
                'cx' => $cx,
                'q' => $request->get('query'),
                'hl' => $request->get('language'),
                'gl' => $request->get('country'),
            ];
        
            $url = $baseUrl . '?' . http_build_query($params);
            
            $response = file_get_contents($url);
            $results = json_decode($response, true)['items'] ?? [];
            $index=0;
            $search_index = new SearchIndex();
            $search_index->query = $request->get('query');
            $search_index->url = $request->get('website_url');
            $search_index->language = $request->get('language');
            $search_index->country = $request->get('country');
            $search_index->page_limiter = $request->get('page_limiter');
            $search_index->keywords = $request->get('keywords');
            $search_index->timer = $request->get('timer');

            foreach ($results as $i => $result) {
                if (strpos($result['link'], $request->get('website_url')) !== false) {
                    $index= $i + 1;
                    $search_index->index = $index;
                    $search_index->save();
                    return response()->json($search_index, 201);
                }
            }
            $search_index->index = 0;
            $search_index->save();
            return response()->json(['message' => 'Website is not ranked till given page'], 201);
        }
                
    
}
