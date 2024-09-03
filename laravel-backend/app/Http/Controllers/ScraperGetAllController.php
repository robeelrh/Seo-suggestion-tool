<?php

namespace App\Http\Controllers;

use App\Models\Scraper;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;


class ScraperGetAllController extends Controller
{
    public function handle()
    {   
        
        $website = Scraper::get();
        if (empty($website)) {
            return response()->json([
                'errors' => [
                    'website' => 'The website does not exist',
                ]
            ], 422);
        }
        return response()->json($website);
    }
}
