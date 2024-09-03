<?php

namespace App\Http\Controllers;

use App\Models\SeoConfig;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;


class ConfigGetController extends Controller
{
    public function handle(Request $request)
    {
        $this->validate($request, [
            'seo_config_id' => 'required',
        ]);
        $seo_config = SeoConfig::where([
            ['id', '=', $request->get('seo_config_id')]
        ])->first();

        if (empty($seo_config)) {
            return response()->json([
                'errors' => [
                    'scraped' => 'The seo_config_id does not exist',
                ]
            ], 422);
        }
        return response()->json($seo_config);
    }
}
